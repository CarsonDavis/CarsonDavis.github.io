#!/usr/bin/env python3
"""
Pre-flight check for LQIP migration.

Every image file — whether at the root level or in original/ — ultimately
produces a webp/{stem}.webp. This script flags any stem that would be
claimed by more than one source file (e.g. photo.jpg and photo.png both
producing webp/photo.webp).

Usage:
    uv run scripts/check_migration_conflicts.py film-camera-photos
    uv run scripts/check_migration_conflicts.py --all
"""

import argparse
import json
import subprocess
import sys
from pathlib import PurePosixPath


BUCKET = "made-by-carson-images"
PROFILE = "personal"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp"}


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


def get_top_level_folders() -> list[str]:
    """Get all top-level folders in the bucket."""
    result = subprocess.run(
        [
            "aws", "s3api", "list-objects-v2",
            "--bucket", BUCKET,
            "--delimiter", "/",
            "--query", "CommonPrefixes[].Prefix",
            "--output", "json",
            "--profile", PROFILE,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error listing bucket: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    parsed = json.loads(result.stdout)
    if not parsed:
        return []
    return [p.strip("/") for p in parsed]


def check_folder(folder: str) -> list[str]:
    """
    Check a single folder for stem collisions.

    Collects every image file at the root and in original/ that would
    produce a webp/{stem}.webp, then flags any stem with multiple sources.

    Returns a list of conflict descriptions (empty if clean).
    """
    keys = list_s3_keys(f"{folder}/")

    # stem -> list of source paths (relative to folder)
    sources_by_stem: dict[str, list[str]] = {}

    for key in keys:
        relative = key[len(folder) + 1:]
        path = PurePosixPath(relative)

        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        # Root-level files (would be moved to webp/ or original/)
        if "/" not in relative:
            sources_by_stem.setdefault(path.stem, []).append(relative)

        # Files in original/ (Compressor produces webp/{stem}.webp)
        elif relative.startswith("original/"):
            name = relative[len("original/"):]
            if "/" not in name:
                sources_by_stem.setdefault(PurePosixPath(name).stem, []).append(relative)

    conflicts = []
    for stem in sorted(sources_by_stem):
        files = sources_by_stem[stem]
        if len(files) > 1:
            file_list = "\n".join(f"    {f}" for f in files)
            conflicts.append(
                f"  stem '{stem}' -> webp/{stem}.webp\n{file_list}"
            )

    return conflicts


def main():
    parser = argparse.ArgumentParser(
        description="Check for stem collisions before LQIP migration"
    )
    parser.add_argument(
        "folder",
        nargs="?",
        help="S3 folder to check (e.g. film-camera-photos)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check all folders in the bucket",
    )
    args = parser.parse_args()

    if not args.folder and not args.all:
        parser.error("Either specify a folder or use --all")

    if args.folder and args.all:
        parser.error("Cannot specify both a folder and --all")

    if args.all:
        folders = get_top_level_folders()
        if not folders:
            print("No folders found in bucket.")
            return
    else:
        folders = [args.folder]

    total_conflicts = 0

    for folder in folders:
        conflicts = check_folder(folder)
        if conflicts:
            print(f"\n{folder}: {len(conflicts)} conflict(s)")
            for c in conflicts:
                print(c)
            total_conflicts += len(conflicts)

    if total_conflicts:
        print(f"\nFound {total_conflicts} conflict(s). Resolve before migrating.")
        sys.exit(1)
    else:
        print(f"\nNo conflicts found across {len(folders)} folder(s). Safe to migrate.")


if __name__ == "__main__":
    main()
