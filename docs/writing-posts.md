# Writing Posts with the Image System

## Making a New Post

Create a new file in `_posts/` with the naming convention `YYYY-MM-DD-post_name.md`. Use this frontmatter template:

```yaml
---
title: Post Title
date: 2025-01-01
categories: [category1, category2]
tags: []
description: Brief description of the post.
media_subpath: /post-name/
image: cover_image.webp
published: False
---
```

Set `published: False` while drafting. The `media_subpath` should match the S3 folder name (see below).

If the post uses image grids, include the standard grid CSS block:

```html
<style>
    .grid-2x2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
        column-gap: 20px;
        justify-items: center;
    }
    .grid-3x2 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: auto auto;
        column-gap: 20px;
        justify-items: center;
    }
    .grid-container {
        justify-items: center;
    }
    .grid-container > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
    }
    .grid-container .image-div {
        justify-content: flex-end;
    }
    .grid-container img {
        width: auto;
        max-width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
        margin-bottom: 5px;
    }
    .grid-container .caption {
        display: block;
        text-align: center;
        font-style: normal;
        font-size: 80%;
        padding: 0;
        color: #6d6c6c;
    }
</style>
```

## Uploading Images

The S3 folder for a post is based on the post filename — the slug portion with hyphens instead of underscores:

| Post filename | S3 folder |
|---------------|-----------|
| `2025-02-15-film_camera_photos.md` | `film-camera-photos` |
| `2024-02-14-kitchen_knives.md` | `kitchen-knives` |

Use the upload script to send a folder of images to S3:

```bash
# Preview what will be uploaded
uv run scripts/upload_images.py ./my-photos/ film-camera-photos --dry-run

# Upload, wait for Lambda processing, and open preview in browser
uv run scripts/upload_images.py ./my-photos/ film-camera-photos
```

The script:
1. Scans the local folder for image files
2. Checks for filename stem collisions against what's already in S3 — renames automatically (e.g. `sunset_2.jpg`) to avoid overwriting
3. Uploads to `original/`, which triggers the Lambda chain
4. Polls `webp/` until all WebPs are generated
5. Opens a browser preview showing all the images with their filenames

## Image Tag Format

Every image in a post uses this HTML tag:

```html
<img src="webp/photo.webp" lqip="lqip/photo.webp" alt="A useful description">
```

The post's `media_subpath` frontmatter prepends the S3 URL automatically, so `src` and `lqip` are relative to the post's image folder.

### What Each Attribute Does

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `src` | `webp/photo.webp` | Points to the full-size image. Chirpy converts this to `data-src` for lazy loading. |
| `lqip` | `lqip/photo.webp` | The ~300-byte thumbnail. Chirpy converts this to `data-lqip` and uses it as a blur placeholder. |
| `alt` | Description text | Accessibility. Screen readers, broken images, SEO. |

Chirpy's `refactor-content.html` include processes these attributes at build time, wrapping the image in `<a class="blur">` with `data-src` and `data-lqip` attributes. The theme's `post.min.js` handles the lazy load and blur-to-sharp transition automatically.

## How the Blur Transition Works

1. Page loads — Chirpy's `refactor-content.html` transforms `<img src="X" lqip="Y">` into a lazy-loading structure with `data-src` and `data-lqip`
2. The LQIP thumbnail is shown as a blurred placeholder
3. As the user scrolls, Chirpy's JS detects images approaching the viewport
4. The full image loads in the background
5. Once loaded, the blur is removed with a smooth transition

## Common Patterns

### Single Image

```html
<img src="webp/sunset.webp" lqip="lqip/sunset.webp" alt="Sunset over the lake">
```

### Grid Layout

```html
<div class="grid-container grid-2x2">
    <div class="image-div">
        <img src="webp/photo1.webp" lqip="lqip/photo1.webp" alt="Photo 1">
    </div>
    <div class="image-div">
        <img src="webp/photo2.webp" lqip="lqip/photo2.webp" alt="Photo 2">
    </div>
    <div class="caption">Caption 1</div>
    <div class="caption">Caption 2</div>
</div>
```

Use `grid-2x2` for two columns, `grid-3x2` for three.

### Markdown Fallback

If you don't need the blur transition (quick draft, non-critical image):

```markdown
![Description](webp/photo.webp)
```

This loads the full image immediately without LQIP. The `media_subpath` resolves the URL the same way.

## Links

Internal link to another post:
```
[Phone Meter Repair]({% link _posts/2018-06-24-phone_meter.md %})
```

Link to a specific header:
```
[nipping press]({% link _posts/2023-08-26-bookbinding_equipment.md %}#nipping-press)
```

## Image Metadata

View geographic location data:
```bash
exiftool -GPSPosition image.jpg
```

Get coordinates in Google Maps format:
```bash
exiftool -c "%.6f" -GPSPosition image.jpg
```

Install with:
```bash
brew install exiftool
```

## Fallback Behavior

| Scenario | What happens |
|----------|-------------|
| LQIP exists, full image exists | Normal blur-to-sharp transition via Chirpy's built-in JS |
| Full image doesn't exist | Broken image icon (same as any missing image) |
| JavaScript disabled | Images don't load (Chirpy requires JS for `data-src` swap) |
| No `lqip` attribute | Chirpy uses shimmer animation placeholder instead of blur |
