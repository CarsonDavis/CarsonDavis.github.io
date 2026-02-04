# Writing Posts with the Image System

## Uploading Images

Upload originals (any format) to the post's `original/` folder in S3:

```bash
aws s3 sync ./my-photos/ s3://made-by-carson-images/my-new-post/original/
```

The Lambda will automatically generate:
- `s3://made-by-carson-images/my-new-post/webp/{stem}.webp` — full-size WebP
- `s3://made-by-carson-images/my-new-post/lqip/{stem}.webp` — 16px thumbnail

Wait a few seconds for processing, then verify:

```bash
aws s3 ls s3://made-by-carson-images/my-new-post/webp/
aws s3 ls s3://made-by-carson-images/my-new-post/lqip/
```

## Image Tag Format

Every image in a post uses this HTML tag:

```html
<img src="lqip/photo.webp" data-full="webp/photo.webp" alt="A useful description"
     style="aspect-ratio: 4000 / 3000;" class="lqip" loading="lazy">
```

The post's `media_subpath` frontmatter prepends the S3 URL automatically, so `src` and `data-full` are relative to the post's image folder.

### What Each Attribute Does

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `src` | `lqip/photo.webp` | Points to the ~300-byte thumbnail. Loads instantly. |
| `data-full` | `webp/photo.webp` | The full-size image URL. JS reads this when the image enters the viewport. |
| `alt` | Description text | Accessibility. Screen readers, broken images, SEO. |
| `style="aspect-ratio: W / H;"` | Original pixel dimensions | Reserves layout space before any image loads. Prevents CLS. |
| `class="lqip"` | — | Applies blur CSS and registers the image with the IntersectionObserver. |
| `loading="lazy"` | — | Native browser lazy loading as a fallback if JS is disabled. |

## Getting Aspect Ratios

You need the original image's width and height for the `aspect-ratio` style. Options:

**From the command line:**

```bash
# Using Pillow (via uv)
uv run python -c "from PIL import Image; i=Image.open('photo.jpg'); print(f'{i.width} / {i.height}')"

# Using macOS sips
sips -g pixelWidth -g pixelHeight photo.jpg

# Using ImageMagick
identify -format '%w / %h' photo.jpg
```

**From S3 (if you only have the WebP):**

```bash
# Download and check
aws s3 cp s3://made-by-carson-images/my-post/webp/photo.webp /tmp/photo.webp
uv run python -c "from PIL import Image; i=Image.open('/tmp/photo.webp'); print(f'{i.width} / {i.height}')"
```

The values don't need to be the exact original dimensions — they just need the correct ratio. `4000 / 3000` is the same as `400 / 300` or `4 / 3`.

## How the Blur Transition Works

1. Page loads → browser fetches each `src` (the tiny LQIP thumbnail, ~300 bytes)
2. CSS `filter: blur(10px)` and `scale(1.05)` make the thumbnail look like a blurred preview
3. As the user scrolls, `lqip-loader.js` detects images approaching the viewport (200px margin)
4. JS creates a hidden `Image()` object to preload the full-size image from `data-full`
5. Once loaded, JS swaps `src` to the full image and adds class `lqip-loaded`
6. CSS transitions blur to 0 and scale to 1 over 0.3 seconds

If the LQIP doesn't exist yet (Lambda hasn't processed it), the `onerror` handler falls back to loading the full image directly. The page still works — you just don't get the blur effect.

## Common Patterns

### Single Image

```html
<img src="lqip/sunset.webp" data-full="webp/sunset.webp" alt="Sunset over the lake"
     style="aspect-ratio: 4000 / 2667;" class="lqip" loading="lazy">
```

### Grid Layout

Wrap images in a div with your grid CSS. Each image gets its own LQIP tag:

```html
<div class="image-grid">
  <img src="lqip/photo1.webp" data-full="webp/photo1.webp" alt="Photo 1"
       style="aspect-ratio: 3000 / 2000;" class="lqip" loading="lazy">
  <img src="lqip/photo2.webp" data-full="webp/photo2.webp" alt="Photo 2"
       style="aspect-ratio: 3000 / 2000;" class="lqip" loading="lazy">
  <img src="lqip/photo3.webp" data-full="webp/photo3.webp" alt="Photo 3"
       style="aspect-ratio: 3000 / 2000;" class="lqip" loading="lazy">
</div>
```

### Markdown Fallback

If you don't need the blur transition (quick draft, non-critical image):

```markdown
![Description](webp/photo.webp)
```

This still works — it just loads the full image immediately without LQIP. The `media_subpath` resolves the URL the same way.

## Fallback Behavior

| Scenario | What happens |
|----------|-------------|
| LQIP exists, full image exists | Normal blur-to-sharp transition |
| LQIP doesn't exist yet | `onerror` fires, full image loads directly (no blur) |
| Full image doesn't exist | Broken image icon (same as any missing image) |
| JavaScript disabled | `loading="lazy"` provides native lazy loading; LQIP thumbnail displays permanently |
| Very old browser (no IntersectionObserver) | LQIP thumbnail displays, no swap occurs |
