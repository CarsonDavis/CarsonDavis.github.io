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
│              made-by-carson-images.s3.amazonaws.com              │
├─────────────────────────────────────────────────────────────────┤
│  /film-camera-photos/                                           │
│  ├── original/              ← YOU upload here                   │
│  │   ├── photo1.jpg                                             │
│  │   └── photo2.png                                             │
│  ├── webp/                  ← Lambda generates (full-size)      │
│  │   ├── photo1.webp                                            │
│  │   └── photo2.webp                                            │
│  └── lqip/                  ← Lambda generates (thumbnails)     │
│      ├── photo1.webp        (~300 bytes, 16px wide)             │
│      └── photo2.webp                                            │
└─────────────────────────────────────────────────────────────────┘
          │
          │ S3 ObjectCreated event
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                       AWS Lambda                                │
├─────────────────────────────────────────────────────────────────┤
│  Trigger: any file created in the S3 bucket                     │
│  Guard:   only processes files in */original/* paths            │
│                                                                 │
│  For each uploaded image:                                       │
│  1. Download from S3                                            │
│  2. Apply EXIF rotation, convert to RGB                         │
│  3. Generate full-size WebP (quality 60) → /{folder}/webp/      │
│  4. Generate 16px LQIP (quality 20) → /{folder}/lqip/          │
│  5. Upload both back to S3                                      │
│                                                                 │
│  If source is already .webp: copy as-is (no re-encoding)        │
│  Originals stay in /original/ for archival                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Frontend (Browser)                           │
├─────────────────────────────────────────────────────────────────┤
│  lqip-loader.js loaded on all pages:                            │
│  1. Images start with LQIP src (tiny, instant load)             │
│  2. CSS blur(10px) hides pixelation                             │
│  3. IntersectionObserver triggers when image nears viewport     │
│  4. Full image loads in background, then crossfades in          │
└─────────────────────────────────────────────────────────────────┘
```

## S3 Folder Structure

Each post gets a top-level folder in the bucket. Within it:

| Path | Contents | Who creates it |
|------|----------|----------------|
| `{folder}/original/` | Source files (JPG, PNG, TIFF, WebP) | You, via `aws s3 sync` |
| `{folder}/webp/` | Full-size WebP conversions | Lambda |
| `{folder}/lqip/` | 16px thumbnails (~200–500 bytes) | Lambda |

Originals are never deleted. They serve as the archival source of truth.

## How the Lambda Processes Images

When an image lands in `original/`, the S3 event triggers the Lambda. Processing steps:

1. **URL-decode the object key** — S3 events URL-encode filenames, so `photo (1).jpg` arrives as `photo+%281%29.jpg`. The handler uses `unquote_plus()` to decode.
2. **Guard: skip if not in `/original/`** — prevents infinite loops from the Lambda's own output.
3. **Guard: skip unsupported extensions** — only `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.webp` are processed.
4. **Parse paths** — extract the folder name and stem filename from the key.
5. **Download** — fetch the source image from S3 to Lambda's `/tmp`.
6. **Open with Pillow** — load into memory.
7. **Apply EXIF orientation** — camera rotation tags are applied so the image displays correctly.
8. **Convert color mode** — RGBA/P (PNG transparency) converted to RGB.
9. **Generate full-size WebP** — see spec below. WebP sources are copied as-is.
10. **Generate LQIP thumbnail** — see spec below.
11. **Upload both** — written back to S3 with 1-year cache headers.

## Supported Input Formats

| Extension | Handling |
|-----------|----------|
| `.jpg`, `.jpeg` | Convert to WebP quality 60, preserve ICC profile, apply EXIF rotation |
| `.png` | Convert RGBA→RGB, then to WebP quality 60 |
| `.tiff`, `.tif` | Convert to WebP quality 60, preserve ICC profile |
| `.webp` | Copy as-is to `webp/` folder (no re-encoding), generate LQIP only |

## WebP Conversion Spec

| Setting | Value | Notes |
|---------|-------|-------|
| Quality | 60 | Matches the old `cwebp -q 60` |
| Method | 6 | Best compression (slowest encode, smallest file) |
| ICC profile | Preserved | `icc_profile=img.info.get("icc_profile")` |

The old local workflow used `cwebp` with `-exact` (preserve exact color values). Pillow doesn't have an equivalent, but the difference is negligible for web delivery. Outputs won't be byte-identical to `cwebp` but are visually equivalent.

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

Three pieces work together:

### 1. CSS (in `_includes/head.html`)

```css
img.lqip {
  filter: blur(10px);
  transform: scale(1.05);
  transition: filter 0.3s ease, transform 0.3s ease;
}
img.lqip.lqip-loaded {
  filter: blur(0);
  transform: scale(1);
}
```

The `scale(1.05)` hides blur edge artifacts. When loaded, both blur and scale animate to their final values.

### 2. JavaScript (`assets/js/lqip-loader.js`)

An IIFE that:
- Creates an `IntersectionObserver` with `rootMargin: "200px"` (starts loading 200px before the image scrolls into view)
- For each `.lqip` image entering the margin, creates a hidden `Image()` to preload the full-size URL from `data-full`
- On successful load, swaps `src` to the full image and adds `lqip-loaded` class (triggers CSS transition)
- On error (LQIP doesn't exist yet), still swaps to full image — graceful degradation
- Unobserves each image after triggering to avoid duplicate work

### 3. HTML tag format

```html
<img src="lqip/photo.webp" data-full="webp/photo.webp" alt="description"
     style="aspect-ratio: 4000 / 3000;" class="lqip" loading="lazy">
```

The `aspect-ratio` style reserves space in the layout before anything loads, preventing CLS.

## Day-to-Day Workflow

```bash
# 1. Upload originals to S3
aws s3 sync ./my-photos/ s3://made-by-carson-images/my-new-post/original/

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
| PNG with transparency (RGBA) | Converted to RGB before WebP encoding |
| Large TIFF (50+ MB) | 1024 MB memory + 1024 MB ephemeral storage + 120s timeout handle this |
| EXIF orientation tag | Applied via `ImageOps.exif_transpose()` before encoding |
| Lambda output triggers another S3 event | `/original/` guard prevents processing — `webp/` and `lqip/` paths never contain `/original/` |
| Lambda fails after retries | Message goes to SQS dead letter queue (14-day retention) |
| LQIP doesn't exist yet when page loads | `onerror` handler in JS falls back to loading the full image directly |
