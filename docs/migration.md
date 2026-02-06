# Migration Guide

This doc covers migrating old posts to the new image system. New posts use the Lambda pipeline automatically — this is only for posts that predate it.

## What's Changing

| Before | After |
|--------|-------|
| Convert images locally with `cwebp` | Upload originals to S3 `original/`, Lambda converts automatically |
| WebPs in folder root | WebPs in `webp/` subfolder |
| No placeholders | LQIP thumbnails in `lqip/` subfolder |
| `<img src="photo.webp">` | `<img src="lqip/photo.webp" data-full="webp/photo.webp" class="lqip" loading="lazy">` |

## New Posts vs Old Posts

**New posts** — upload raw images to `original/`, Lambda chain handles everything:
```
original/photo.jpg  →  Compressor  →  webp/photo.webp  →  LQIP Generator  →  lqip/photo.webp
```

**Old posts** — images exist at the folder root in various formats (WebP, JPG, PNG, or a mix). Each format migrates differently:
```
photo.webp  →  move to webp/photo.webp     →  LQIP Generator  →  lqip/photo.webp
photo.jpg   →  move to original/photo.jpg  →  Compressor       →  webp/photo.webp  →  LQIP Generator  →  lqip/photo.webp
```

Root-level WebPs go directly to `webp/` (they've already been through `cwebp`, no re-compression). Non-WebP files go to `original/` so the Compressor can convert them.

## Migrating an Old Post

### Step 1: Check for conflicts

Before moving anything, check for filename stem collisions — any files (at root or in `original/`) that would produce the same `webp/{stem}.webp`. If they collide, the Compressor Lambda would overwrite the migrated WebP.

```bash
uv run scripts/check_migration_conflicts.py film-camera-photos
```

If conflicts are found, rename or remove the conflicting files before proceeding.

### Step 2: Move images to their correct subfolders

```bash
# List what's at the root
aws s3 ls s3://made-by-carson-images/film-camera-photos/ --profile personal

# Move WebPs to webp/ (already compressed, triggers LQIP generator)
aws s3 mv s3://made-by-carson-images/film-camera-photos/ \
         s3://made-by-carson-images/film-camera-photos/webp/ \
         --recursive --exclude "*" --include "*.webp" --profile personal

# Move non-WebPs to original/ (triggers Compressor → LQIP chain)
aws s3 mv s3://made-by-carson-images/film-camera-photos/ \
         s3://made-by-carson-images/film-camera-photos/original/ \
         --recursive --exclude "*" --include "*.jpg" --include "*.jpeg" \
         --include "*.png" --include "*.tiff" --include "*.tif" --profile personal
```

WebPs moved to `webp/` trigger the LQIP Generator. Non-WebPs moved to `original/` trigger the Compressor, which writes to `webp/`, which then triggers the LQIP Generator.

### Step 3: Verify LQIPs were created

```bash
aws s3 ls s3://made-by-carson-images/film-camera-photos/lqip/ --profile personal
```

### Step 4: Update the markdown

Run the migration script on the post:

```bash
# Preview changes
uv run scripts/migrate_to_lqip.py --dry-run _posts/2025-02-15-film_camera_photos.md

# Apply changes (creates backup in _posts_backup/)
uv run scripts/migrate_to_lqip.py _posts/2025-02-15-film_camera_photos.md
```

The script:
- Converts `<img src="photo.jpg">` to `<img src="lqip/photo.webp" data-full="webp/photo.webp" class="lqip" loading="lazy">`
- Converts `![alt](photo.jpg)` to the same HTML format
- Changes any image extension (`.jpg`, `.png`, etc.) to `.webp` in the output paths
- Skips external URLs and already-migrated images
- Only processes posts with `media_subpath` in frontmatter

### Step 5: Verify locally

```bash
bundle exec jekyll serve
```

Open the post and verify:
- Blurred previews appear immediately
- Full images load as you scroll
- Blur-to-sharp transition works

## Batch Migration

To migrate multiple posts at once:

```bash
# Check all folders for conflicts first
uv run scripts/check_migration_conflicts.py --all

# Move images for multiple folders
for folder in film-camera-photos kitchen-knives plane-collection; do
  aws s3 mv s3://made-by-carson-images/$folder/ \
           s3://made-by-carson-images/$folder/webp/ \
           --recursive --exclude "*" --include "*.webp" --profile personal
  aws s3 mv s3://made-by-carson-images/$folder/ \
           s3://made-by-carson-images/$folder/original/ \
           --recursive --exclude "*" --include "*.jpg" --include "*.jpeg" \
           --include "*.png" --include "*.tiff" --include "*.tif" --profile personal
done

# Wait for LQIP generation, then migrate all posts
uv run scripts/migrate_to_lqip.py --dry-run --all
uv run scripts/migrate_to_lqip.py --all
```

## Cleanup

After migrating posts:

```bash
# Delete backups once verified
rm -rf _posts_backup/
```
