"""
Image processor Lambda handlers.

Two functions triggered by S3 ObjectCreated events:

1. image_compressor - Triggered by uploads to */original/*
   Converts images to WebP via cwebp, writes to */webp/*

2. lqip_generator - Triggered by uploads to */webp/*
   Generates 16px thumbnails, writes to */lqip/*

The chain works automatically:
  original/ → compressor → webp/ → lqip_generator → lqip/

For migrating old posts, move existing WebPs directly to webp/
and the LQIP generator will fire automatically.
"""

import logging
import os
import subprocess
import tempfile
from io import BytesIO
from pathlib import PurePosixPath
from urllib.parse import unquote_plus

import boto3
from PIL import Image, ImageOps

logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3_BUCKET = os.environ.get("S3_BUCKET", "made-by-carson-images")
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp"}
LQIP_WIDTH = 16
LQIP_QUALITY = 20
CACHE_CONTROL = "max-age=31536000"  # 1 year

s3 = boto3.client("s3")


# =============================================================================
# Image Compressor - converts originals to WebP
# =============================================================================

def compressor_handler(event, context):
    """Process uploads to /original/ - convert to WebP."""
    for record in event.get("Records", []):
        raw_key = record["s3"]["object"]["key"]
        key = unquote_plus(raw_key)

        logger.info("Compressor received: %s", key)

        # Guard: only process files in /original/ paths
        if "/original/" not in key:
            logger.info("Skipping %s — not in /original/", key)
            continue

        # Guard: only process supported image formats
        ext = PurePosixPath(key).suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            logger.info("Skipping %s — unsupported extension %s", key, ext)
            continue

        compress_image(key)

    return {"statusCode": 200}


def convert_with_cwebp(source_path, dest_path):
    """Convert an image to WebP using cwebp, matching convert_to_webp.py flags."""
    result = subprocess.run(
        [
            "cwebp",
            "-q", "60",
            "-metadata", "icc",
            "-mt",
            "-exact",
            "-m", "6",
            source_path,
            "-o", dest_path,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"cwebp failed: {result.stderr}")


def apply_exif_rotation(source_path, dest_path):
    """Apply EXIF orientation and save back, preserving ICC profile."""
    with Image.open(source_path) as img:
        transposed = ImageOps.exif_transpose(img)
        if transposed is not img:
            icc_profile = img.info.get("icc_profile")
            save_kwargs = {"format": "WEBP", "quality": 95}
            if icc_profile:
                save_kwargs["icc_profile"] = icc_profile
            transposed.save(dest_path, **save_kwargs)


def compress_image(key):
    """Download, convert to WebP, and upload."""
    path = PurePosixPath(key)
    stem = path.stem
    ext = path.suffix.lower()

    # Parse folder structure: {folder}/original/{filename}
    parts = key.split("/original/")
    folder = parts[0]

    webp_key = f"{folder}/webp/{stem}.webp"

    logger.info("Source: %s", key)
    logger.info("WebP output: %s", webp_key)

    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, f"source{ext}")
        webp_path = os.path.join(tmpdir, f"{stem}.webp")

        # Download source image
        s3.download_file(S3_BUCKET, key, source_path)

        if ext == ".webp":
            # WebP source: copy as-is to avoid double-lossy compression
            logger.info("WebP source — copying as-is")
            webp_path = source_path
        else:
            # Convert with cwebp
            convert_with_cwebp(source_path, webp_path)
            apply_exif_rotation(webp_path, webp_path)
            logger.info("WebP encoded: %d bytes", os.path.getsize(webp_path))

        # Upload to webp/
        s3.upload_file(
            webp_path,
            S3_BUCKET,
            webp_key,
            ExtraArgs={
                "ContentType": "image/webp",
                "CacheControl": CACHE_CONTROL,
            },
        )

    logger.info("Compressor done: %s", key)


# =============================================================================
# LQIP Generator - creates thumbnails from WebPs
# =============================================================================

def lqip_handler(event, context):
    """Process uploads to /webp/ - generate LQIP thumbnails."""
    for record in event.get("Records", []):
        raw_key = record["s3"]["object"]["key"]
        key = unquote_plus(raw_key)

        logger.info("LQIP generator received: %s", key)

        # Guard: only process files in /webp/ paths
        if "/webp/" not in key:
            logger.info("Skipping %s — not in /webp/", key)
            continue

        # Guard: only process WebP files
        ext = PurePosixPath(key).suffix.lower()
        if ext != ".webp":
            logger.info("Skipping %s — not a WebP file", key)
            continue

        generate_lqip(key)

    return {"statusCode": 200}


def generate_lqip(key):
    """Download WebP, generate thumbnail, upload to lqip/."""
    path = PurePosixPath(key)
    stem = path.stem

    # Parse folder structure: {folder}/webp/{filename}
    parts = key.split("/webp/")
    folder = parts[0]

    lqip_key = f"{folder}/lqip/{stem}.webp"

    logger.info("Source: %s", key)
    logger.info("LQIP output: %s", lqip_key)

    # Download WebP
    response = s3.get_object(Bucket=S3_BUCKET, Key=key)
    image_bytes = response["Body"].read()

    # Generate thumbnail
    with Image.open(BytesIO(image_bytes)) as img:
        img = ImageOps.exif_transpose(img)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        ratio = img.height / img.width
        lqip_height = max(1, int(LQIP_WIDTH * ratio))
        lqip_img = img.resize((LQIP_WIDTH, lqip_height), Image.LANCZOS)

        lqip_buffer = BytesIO()
        lqip_img.save(lqip_buffer, format="WEBP", quality=LQIP_QUALITY)
        lqip_bytes = lqip_buffer.getvalue()

    logger.info("LQIP generated: %d bytes (%dx%d)", len(lqip_bytes), LQIP_WIDTH, lqip_height)

    # Upload to lqip/
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=lqip_key,
        Body=lqip_bytes,
        ContentType="image/webp",
        CacheControl=CACHE_CONTROL,
    )

    logger.info("LQIP generator done: %s", key)
