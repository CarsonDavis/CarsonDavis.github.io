#!/usr/bin/env python3
"""
Upload images to S3 for a post.

Takes a local folder of images, deduplicates stems against what's already
in S3 (and within the batch itself), uploads to original/, waits for the
Lambda to produce WebPs, then opens a preview in the browser.

Usage:
    uv run scripts/upload_images.py ./my-photos/ film-camera-photos
    uv run scripts/upload_images.py ./my-photos/ film-camera-photos --dry-run
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
import webbrowser
from pathlib import Path, PurePosixPath

BUCKET = "made-by-carson-images"
PROFILE = "personal"
CDN_URL = "https://made-by-carson-images.s3.amazonaws.com"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp"}
POLL_INTERVAL = 3
POLL_TIMEOUT = 180


def list_s3_keys(prefix: str) -> list[str]:
    """List all object keys under a prefix."""
    result = subprocess.run(
        [
            "aws", "s3api", "list-objects-v2",
            "--bucket", BUCKET,
            "--prefix", prefix,
            "--query", "Contents[].Key",
            "--output", "json",
            "--profile", PROFILE,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error listing {prefix}: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    parsed = json.loads(result.stdout)
    if not parsed:
        return []
    return parsed


def get_existing_stems(folder: str) -> set[str]:
    """Get all stems already in original/ and webp/ for a folder."""
    stems = set()
    for subfolder in ("original", "webp"):
        keys = list_s3_keys(f"{folder}/{subfolder}/")
        for key in keys:
            stems.add(PurePosixPath(key).stem)
    return stems


def sanitize_filename(name: str) -> str:
    """Sanitize a filename stem for use in URLs and markdown.

    - Replaces spaces with underscores
    - Strips parentheses
    - Collapses multiple underscores
    - Strips leading/trailing underscores
    """
    name = name.replace(" ", "_")
    name = re.sub(r"[()]", "", name)
    name = re.sub(r"_+", "_", name)
    name = name.strip("_")
    return name


def deduplicate_stem(stem: str, taken: set[str]) -> str:
    """Return a unique stem by appending _2, _3, etc. if needed."""
    if stem not in taken:
        return stem
    n = 2
    while f"{stem}_{n}" in taken:
        n += 1
    return f"{stem}_{n}"


def build_upload_plan(local_dir: Path, folder: str) -> list[tuple[Path, str]]:
    """
    Build a list of (local_path, s3_key) pairs with deduplicated stems.

    Returns the plan sorted by original filename.
    """
    local_files = sorted(
        f for f in local_dir.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
    )

    if not local_files:
        print(f"No image files found in {local_dir}")
        sys.exit(1)

    existing_stems = get_existing_stems(folder)
    taken = set(existing_stems)
    plan = []
    renames = []

    for local_path in local_files:
        original_stem = local_path.stem
        stem = sanitize_filename(original_stem)
        stem = deduplicate_stem(stem, taken)
        taken.add(stem)

        s3_key = f"{folder}/original/{stem}{local_path.suffix}"
        plan.append((local_path, s3_key))

        if stem != original_stem:
            renames.append((local_path.name, f"{stem}{local_path.suffix}"))

    if renames:
        print("Renames to avoid collisions:")
        for old, new in renames:
            print(f"  {old} -> {new}")
        print()

    return plan


def upload_files(plan: list[tuple[Path, str]]) -> None:
    """Upload all files in the plan to S3."""
    for i, (local_path, s3_key) in enumerate(plan, 1):
        print(f"  [{i}/{len(plan)}] {local_path.name} -> s3://{BUCKET}/{s3_key}")
        result = subprocess.run(
            [
                "aws", "s3", "cp",
                str(local_path),
                f"s3://{BUCKET}/{s3_key}",
                "--profile", PROFILE,
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)


def wait_for_webps(folder: str, expected_stems: set[str]) -> bool:
    """Poll webp/ until all expected stems appear or timeout."""
    print(f"\nWaiting for {len(expected_stems)} WebP(s)...", end="", flush=True)
    start = time.time()

    while time.time() - start < POLL_TIMEOUT:
        keys = list_s3_keys(f"{folder}/webp/")
        found = {PurePosixPath(k).stem for k in keys}
        remaining = expected_stems - found

        if not remaining:
            print(f" done ({int(time.time() - start)}s)")
            return True

        print(".", end="", flush=True)
        time.sleep(POLL_INTERVAL)

    print(f"\nTimed out after {POLL_TIMEOUT}s. Missing: {', '.join(sorted(remaining))}")
    return False


def open_preview(folder: str, stems: set[str]) -> None:
    """Generate a local HTML preview and open it in the browser."""
    sorted_stems = sorted(stems)

    img_tags = []
    for stem in sorted_stems:
        url = f"{CDN_URL}/{folder}/webp/{stem}.webp"
        img_tags.append(
            f'    <div style="margin:10px;display:inline-block;text-align:center">\n'
            f'      <img src="{url}" style="max-width:400px;max-height:400px">\n'
            f'      <div style="font-family:monospace;font-size:14px;margin-top:4px">{stem}.webp</div>\n'
            f'    </div>'
        )

    html = (
        "<!DOCTYPE html>\n<html><head><title>Upload Preview</title></head>\n"
        "<body style=\"background:#1a1a1a;color:#ccc;padding:20px\">\n"
        f"  <h2 style=\"font-family:sans-serif\">{folder} — {len(sorted_stems)} images</h2>\n"
        f"  <div style=\"display:flex;flex-wrap:wrap\">\n"
        + "\n".join(img_tags) + "\n"
        "  </div>\n"
        "</body></html>\n"
    )

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        preview_path = f.name

    webbrowser.open(f"file://{preview_path}")
    print(f"Preview opened: {preview_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Upload images to S3 with deduplication and preview"
    )
    parser.add_argument(
        "local_dir",
        type=Path,
        help="Local folder containing images",
    )
    parser.add_argument(
        "folder",
        help="S3 folder name (e.g. film-camera-photos)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show upload plan without uploading",
    )
    parser.add_argument(
        "--no-preview",
        action="store_true",
        help="Skip opening browser preview",
    )
    args = parser.parse_args()

    if not args.local_dir.is_dir():
        print(f"Error: {args.local_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Build upload plan
    print(f"Scanning {args.local_dir} -> {args.folder}/original/\n")
    plan = build_upload_plan(args.local_dir, args.folder)

    print(f"Upload plan ({len(plan)} file(s)):")
    for local_path, s3_key in plan:
        print(f"  {local_path.name} -> {s3_key}")

    if args.dry_run:
        print("\n[DRY RUN — nothing uploaded]")
        return

    # Upload
    print(f"\nUploading {len(plan)} file(s):")
    upload_files(plan)

    # Wait for Lambda processing
    expected_stems = {PurePosixPath(s3_key).stem for _, s3_key in plan}
    wait_for_webps(args.folder, expected_stems)

    # Preview
    if not args.no_preview:
        open_preview(args.folder, expected_stems)


if __name__ == "__main__":
    main()
