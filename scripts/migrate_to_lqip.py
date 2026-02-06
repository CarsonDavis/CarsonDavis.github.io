#!/usr/bin/env python3
"""
LQIP Migration Script - Transform existing image references to use LQIP pattern.

This script transforms:
1. HTML images: <img src="photo.jpg" ...> -> <img src="lqip/photo.webp" data-full="webp/photo.webp" class="lqip" loading="lazy" ...>
2. Markdown images: ![alt](photo.jpg) -> <img src="lqip/photo.webp" data-full="webp/photo.webp" alt="alt" class="lqip" loading="lazy">

All image extensions are converted to .webp in the output paths, since the
Lambda pipeline produces WebPs regardless of the source format.

Usage:
    uv run scripts/migrate_to_lqip.py --dry-run _posts/2025-02-15-film_camera_photos.md
    uv run scripts/migrate_to_lqip.py _posts/2025-02-15-film_camera_photos.md
    uv run scripts/migrate_to_lqip.py --all
    uv run scripts/migrate_to_lqip.py --all --dry-run
"""

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


POSTS_DIR = Path(__file__).parent.parent / "_posts"
BACKUP_DIR = Path(__file__).parent.parent / "_posts_backup"

# Image file extensions to process
IMAGE_EXTENSIONS = (".webp", ".jpg", ".jpeg", ".png", ".tiff", ".tif")


def has_media_subpath(content: str) -> bool:
    """Check if a post has a media_subpath in its frontmatter."""
    return bool(re.search(r"^media_subpath:\s*/.+", content, re.MULTILINE))


def is_already_migrated(tag: str) -> bool:
    """Check if an image tag is already migrated (has data-full attribute)."""
    return "data-full=" in tag


def is_external_url(src: str) -> bool:
    """Check if a source is an external URL."""
    return src.startswith(("http://", "https://", "//"))


def is_lqip_path(src: str) -> bool:
    """Check if the source already points to an LQIP."""
    return src.startswith("lqip/") or "/lqip/" in src


def to_webp_stem(filename: str) -> str:
    """Convert any image filename to its .webp equivalent stem.

    'photo.jpg' -> 'photo.webp'
    'photo.webp' -> 'photo.webp'
    """
    return Path(filename).stem + ".webp"


def migrate_html_image(match: re.Match) -> str:
    """
    Migrate an HTML image tag to LQIP format.

    Input: <img src="photo.jpg" alt="desc">
    Output: <img src="lqip/photo.webp" data-full="webp/photo.webp" alt="desc" class="lqip" loading="lazy">
    """
    full_tag = match.group(0)

    # Skip if already migrated
    if is_already_migrated(full_tag):
        return full_tag

    # Extract src
    src_match = re.search(r'src="([^"]+)"', full_tag)
    if not src_match:
        return full_tag

    src = src_match.group(1)

    # Skip external URLs and non-image files
    if is_external_url(src):
        return full_tag

    if not src.lower().endswith(IMAGE_EXTENSIONS):
        return full_tag

    # Skip if already an LQIP path
    if is_lqip_path(src):
        return full_tag

    # Build new paths — always .webp regardless of source extension
    webp_name = to_webp_stem(src)
    lqip_src = f"lqip/{webp_name}"
    full_src = f"webp/{webp_name}"

    # Replace src with lqip src and add data-full
    new_tag = full_tag
    new_tag = re.sub(r'src="[^"]+"', f'src="{lqip_src}" data-full="{full_src}"', new_tag)

    # Add class="lqip" - handle existing class attribute
    if 'class="' in new_tag:
        new_tag = re.sub(r'class="([^"]*)"', r'class="\1 lqip"', new_tag)
    else:
        # Add class before the closing >
        new_tag = re.sub(r"(/?>)$", r' class="lqip"\1', new_tag)

    # Add loading="lazy" if not present
    if 'loading="' not in new_tag:
        new_tag = re.sub(r"(/?>)$", r' loading="lazy"\1', new_tag)

    return new_tag


def migrate_markdown_image(match: re.Match) -> str:
    """
    Migrate a Markdown image to HTML with LQIP format.

    Input: ![alt text](photo.jpg)
    Output: <img src="lqip/photo.webp" data-full="webp/photo.webp" alt="alt text" class="lqip" loading="lazy">
    """
    full_match = match.group(0)
    alt_text = match.group(1)
    src = match.group(2)

    # Skip external URLs
    if is_external_url(src):
        return full_match

    if not src.lower().endswith(IMAGE_EXTENSIONS):
        return full_match

    # Skip if already an LQIP path
    if is_lqip_path(src):
        return full_match

    # Build new paths — always .webp regardless of source extension
    webp_name = to_webp_stem(src)
    lqip_src = f"lqip/{webp_name}"
    full_src = f"webp/{webp_name}"

    # Escape alt text for HTML attribute
    alt_escaped = alt_text.replace('"', "&quot;")

    return f'<img src="{lqip_src}" data-full="{full_src}" alt="{alt_escaped}" class="lqip" loading="lazy">'


def migrate_content(content: str) -> tuple[str, int]:
    """
    Migrate all image references in content to LQIP format.

    Returns:
        Tuple of (migrated_content, number_of_changes)
    """
    changes = 0

    # Track original content to count changes
    original = content

    # Migrate HTML images: <img src="..." ...>
    # This regex matches <img tags with various attributes
    html_img_pattern = re.compile(r"<img\s+[^>]*src=\"[^\"]+\"[^>]*/?>", re.IGNORECASE)

    def count_html_migration(m):
        nonlocal changes
        result = migrate_html_image(m)
        if result != m.group(0):
            changes += 1
        return result

    content = html_img_pattern.sub(count_html_migration, content)

    # Migrate Markdown images: ![alt](src)
    # Must come after HTML migration to avoid double-processing
    markdown_img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    def count_md_migration(m):
        nonlocal changes
        result = migrate_markdown_image(m)
        if result != m.group(0):
            changes += 1
        return result

    content = markdown_img_pattern.sub(count_md_migration, content)

    return content, changes


def process_file(
    file_path: Path, dry_run: bool = False, backup: bool = True
) -> dict:
    """
    Process a single markdown file.

    Args:
        file_path: Path to the markdown file
        dry_run: If True, only report changes without writing
        backup: If True, create backup before modifying

    Returns:
        Dict with stats: {file: str, changes: int, skipped: bool, reason: str}
    """
    stats = {"file": str(file_path.name), "changes": 0, "skipped": False, "reason": ""}

    # Read file
    content = file_path.read_text(encoding="utf-8")

    # Check if file has media_subpath
    if not has_media_subpath(content):
        stats["skipped"] = True
        stats["reason"] = "No media_subpath"
        return stats

    # Migrate content
    new_content, changes = migrate_content(content)
    stats["changes"] = changes

    if changes == 0:
        stats["skipped"] = True
        stats["reason"] = "No images to migrate"
        return stats

    if dry_run:
        print(f"\n{file_path.name}: {changes} image(s) would be migrated")
        # Show a sample of changes
        show_diff_sample(content, new_content)
        return stats

    # Create backup
    if backup:
        BACKUP_DIR.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"{file_path.stem}_{timestamp}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)

    # Write migrated content
    file_path.write_text(new_content, encoding="utf-8")
    print(f"{file_path.name}: Migrated {changes} image(s)")

    return stats


def show_diff_sample(original: str, modified: str, max_samples: int = 3):
    """Show a sample of changes for dry-run mode."""
    orig_lines = original.splitlines()
    mod_lines = modified.splitlines()

    samples_shown = 0
    for i, (orig, mod) in enumerate(zip(orig_lines, mod_lines)):
        if orig != mod and samples_shown < max_samples:
            print(f"  Line {i + 1}:")
            # Truncate long lines for display
            orig_display = orig[:100] + "..." if len(orig) > 100 else orig
            mod_display = mod[:100] + "..." if len(mod) > 100 else mod
            print(f"    - {orig_display}")
            print(f"    + {mod_display}")
            samples_shown += 1

    if samples_shown == 0:
        print("  (No line-by-line differences to show)")


def main():
    parser = argparse.ArgumentParser(
        description="Migrate image references to LQIP format"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        help="Specific markdown file to process",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all posts in _posts directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip creating backup files",
    )
    args = parser.parse_args()

    if not args.file and not args.all:
        parser.error("Either specify a file or use --all")

    if args.file and args.all:
        parser.error("Cannot specify both a file and --all")

    # Get files to process
    if args.all:
        files = sorted(POSTS_DIR.glob("*.md"))
    else:
        if not args.file.exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
        files = [args.file]

    if args.dry_run:
        print("[DRY RUN MODE - No files will be modified]\n")

    # Process files
    total_stats = {"processed": 0, "migrated": 0, "skipped": 0, "total_changes": 0}

    for file_path in files:
        stats = process_file(
            file_path, dry_run=args.dry_run, backup=not args.no_backup
        )
        total_stats["processed"] += 1

        if stats["skipped"]:
            total_stats["skipped"] += 1
            if not args.all:  # Only show skip reason for single file
                print(f"{stats['file']}: Skipped - {stats['reason']}")
        else:
            total_stats["migrated"] += 1
            total_stats["total_changes"] += stats["changes"]

    # Print summary
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  Files processed: {total_stats['processed']}")
    print(f"  Files migrated: {total_stats['migrated']}")
    print(f"  Files skipped: {total_stats['skipped']}")
    print(f"  Total images migrated: {total_stats['total_changes']}")

    if args.dry_run and total_stats["total_changes"] > 0:
        print("\nRun without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
