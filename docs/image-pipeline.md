# Image Processing & LQIP System

## Problem

The site is image-heavy. Many posts have 100+ images, all hosted on S3 at full resolution. Without intervention:

1. The browser requests every visible image at full size simultaneously
2. Images pop in one at a time as they download, causing layout shift (high CLS)
3. Images below the fold load immediately even though the user hasn't scrolled to them
4. On slow connections, the page feels broken — empty boxes everywhere

The old workflow was also manual: convert to WebP locally with `cwebp`, upload, hope you remembered the right flags.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         S3 Bucket                               │
│              made-by-carson-images.s3.amazonaws.com             │
├─────────────────────────────────────────────────────────────────┤
│  /film-camera-photos/                                           │
│  ├── original/              ← YOU upload here (new posts)       │
│  │   ├── photo1.jpg                                             │
│  │   └── photo2.png                                             │
│  ├── webp/                  ← Compressor generates, or you      │
│  │   ├── photo1.webp           move existing WebPs here         │
│  │   └── photo2.webp                                            │
│  └── lqip/                  ← LQIP Generator creates            │
│      ├── photo1.webp        (~300 bytes, 16px wide)             │
│      └── photo2.webp                                            │
└─────────────────────────────────────────────────────────────────┘
          │
          │ S3 ObjectCreated events
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                 Lambda: Image Compressor                        │
├─────────────────────────────────────────────────────────────────┤
│  Trigger: s3:ObjectCreated:* (filtered in handler to */original/*)│
│                                                                 │
│  1. Download from S3                                            │
│  2. Convert to WebP via cwebp (quality 60, ICC preserved)       │
│  3. Apply EXIF rotation                                         │
│  4. Upload to /{folder}/webp/                                   │
│                                                                 │
│  If source is already .webp: copy as-is (no re-encoding)        │
└─────────────────────────────────────────────────────────────────┘
          │
          │ Output triggers next Lambda
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                 Lambda: LQIP Generator                          │
├─────────────────────────────────────────────────────────────────┤
│  Trigger: s3:ObjectCreated:* (filtered in handler to */webp/*)   │
│                                                                 │
│  1. Download WebP from S3                                       │
│  2. Generate 16px thumbnail (Pillow, quality 20)                │
│  3. Upload to /{folder}/lqip/                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Frontend (Browser)                           │
├─────────────────────────────────────────────────────────────────┤
│  Chirpy's built-in LQIP system (post.min.js):                   │
│  1. Build: refactor-content.html converts lqip= to data-lqip   │
│  2. LQIP thumbnail shown as blurred placeholder                 │
│  3. Chirpy JS lazy-loads full image as user scrolls              │
│  4. Blur removed with smooth transition on load                  │
└─────────────────────────────────────────────────────────────────┘
```

## S3 Folder Structure

Each post gets a top-level folder in the bucket. Within it:

| Path | Contents | Who creates it |
|------|----------|----------------|
| `{folder}/original/` | Source files (JPG, PNG, TIFF, WebP) | You, via `upload_images.py` |
| `{folder}/webp/` | Full-size WebP conversions | Lambda |
| `{folder}/lqip/` | 16px thumbnails (~200–500 bytes) | Lambda |

Originals are never deleted. They serve as the archival source of truth.

## How the Lambdas Process Images

Two Lambda functions run as container images (Dockerfile based on `public.ecr.aws/lambda/python:3.12`) with `cwebp` installed.

### Image Compressor

Triggered when files are created in `/original/`. Processing steps:

1. **URL-decode the object key** — S3 events URL-encode filenames, so `photo (1).jpg` arrives as `photo+%281%29.jpg`. The handler uses `unquote_plus()` to decode.
2. **Guard: skip if not in `/original/`** — prevents processing other paths.
3. **Guard: skip unsupported extensions** — only `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.webp` are processed.
4. **Download** — fetch the source image from S3 to Lambda's `/tmp`.
5. **Convert to WebP via `cwebp`** — same flags as the local `convert_to_webp.py` script. WebP sources are copied as-is.
6. **Apply EXIF rotation** — camera rotation tags are applied via Pillow so the image displays correctly.
7. **Upload to `/webp/`** — written to S3 with 1-year cache headers.

### LQIP Generator

Triggered when files are created in `/webp/`. Processing steps:

1. **URL-decode the object key**
2. **Guard: skip if not in `/webp/`** — prevents processing other paths.
3. **Guard: skip if not `.webp`** — only WebP files are processed.
4. **Download** — fetch the WebP from S3.
5. **Generate 16px thumbnail** — via Pillow (see spec below).
6. **Upload to `/lqip/`** — written to S3 with 1-year cache headers.

The chain works automatically: upload to `original/` triggers the Compressor, which writes to `webp/`, which triggers the LQIP Generator, which writes to `lqip/`.

## Supported Input Formats

| Extension | Handling |
|-----------|----------|
| `.jpg`, `.jpeg` | Convert to WebP quality 60, preserve ICC profile, apply EXIF rotation |
| `.png` | Convert to WebP quality 60 |
| `.tiff`, `.tif` | Convert to WebP quality 60, preserve ICC profile |
| `.webp` | Copy as-is to `webp/` folder (no re-encoding), generate LQIP only |

## WebP Conversion Spec

The Lambda uses `cwebp` with the same flags as the local `convert_to_webp.py` script. EXIF rotation handling differs (Lambda uses Pillow's `exif_transpose`).

```
cwebp -q 60 -metadata icc -mt -exact -m 6 input.jpg -o output.webp
```

| Flag | Value | Purpose |
|------|-------|---------|
| `-q` | 60 | Quality level |
| `-m` | 6 | Best compression method (slowest encode, smallest file) |
| `-metadata` | `icc` | Preserve ICC color profile |
| `-mt` | — | Multi-threaded encoding |
| `-exact` | — | Preserve exact RGB color values |

## LQIP Thumbnail Spec

| Setting | Value |
|---------|-------|
| Width | 16 pixels |
| Height | Proportional (preserves aspect ratio) |
| Format | WebP |
| Quality | 20 |
| Resampling | Lanczos |
| Typical size | 200–500 bytes |

## How the Frontend Loads Images

Chirpy's built-in LQIP system handles everything. No custom JS or CSS is needed.

### Build time (`refactor-content.html`)

Chirpy's include transforms the `lqip` attribute at build time:
- `<img src="webp/X.webp" lqip="lqip/X.webp">` becomes `<img data-src="webp/X.webp" data-lqip="lqip/X.webp">`
- The image is wrapped in `<a class="blur">` (not `shimmer`, because `data-lqip` is present)

### Runtime (`post.min.js`)

Chirpy's JS handles the lazy load and transition:
- Detects images with `data-src` approaching the viewport
- Loads the full image in the background
- Swaps `data-src` to `src` and removes the blur class on load

### HTML tag format

```html
<img src="webp/photo.webp" lqip="lqip/photo.webp" alt="description">
```

No `class`, `loading`, or `data-*` attributes needed — Chirpy adds them at build time.

## Day-to-Day Workflow

```bash
# 1. Upload originals to S3 (handles deduplication, collision renaming, and WebP polling)
uv run scripts/upload_images.py ./my-photos/ my-new-post

# 2. Lambda automatically creates:
#    s3://made-by-carson-images/my-new-post/webp/photo1.webp
#    s3://made-by-carson-images/my-new-post/lqip/photo1.webp

# 3. Write your post with media_subpath: /my-new-post/
#    and reference images with the LQIP tag format
```

That's it. No local conversion, no manual thumbnail generation.

## Edge Cases

| Case | Handling |
|------|----------|
| Filename with spaces: `70820002 (1).jpg` | `unquote_plus()` decodes URL-encoded keys from S3 events |
| Filename with plus/parens: `arst0064+(2).webp` | Same URL decoding |
| WebP uploaded to `original/` | Copied as-is to `webp/` folder (no re-encoding), LQIP still generated |
| PNG with transparency (RGBA) | LQIP generator converts to RGB for thumbnail; compressor passes to `cwebp` as-is |
| Large TIFF (50+ MB) | Compressor has 1024 MB memory + 1024 MB storage; the resulting WebP is much smaller, handled by LQIP generator's 512 MB limits |
| EXIF orientation tag | Applied via `ImageOps.exif_transpose()` before encoding |
| Compressor output triggers LQIP Generator | By design — `webp/` trigger fires the LQIP Generator |
| LQIP output doesn't trigger anything | `/lqip/` doesn't match either trigger path |
| Lambda fails after retries | Message goes to SQS dead letter queue (14-day retention) |
| Full image preload fails | Chirpy's JS handles the error; LQIP placeholder remains visible |
