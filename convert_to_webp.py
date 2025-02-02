import os
import sys
import subprocess
from typing import NoReturn, Dict, Optional
from PIL import Image


def get_image_orientation(image_path: str) -> int:
    """Get the EXIF orientation of an image."""
    try:
        with Image.open(image_path) as img:
            exif = img._getexif()
            if exif is None:
                return 1
            return exif.get(274, 1)  # 274 is the EXIF tag for orientation
    except Exception:
        return 1


def create_output_directory(source_folder: str, base_name: str = "webp_images") -> str:
    """Create a unique output directory for WebP files."""
    destination_folder: str = os.path.join(source_folder, base_name)

    counter = 1
    while os.path.exists(destination_folder):
        destination_folder = os.path.join(source_folder, f"{base_name}_{counter}")
        counter += 1

    os.makedirs(destination_folder)
    print(f"Creating output folder: {destination_folder}")
    return destination_folder


def get_rotation_degrees(orientation: int) -> int:
    """Convert EXIF orientation to rotation degrees."""
    rotation_map: Dict[int, int] = {
        2: 0,  # Mirrored
        3: 180,  # 180 degrees
        4: 0,  # Mirrored and rotated 180 degrees
        5: 0,  # Mirrored and rotated 270 degrees
        6: -90,  # 90 degrees
        7: 0,  # Mirrored and rotated 90 degrees
        8: 90,  # 270 degrees
    }
    return rotation_map.get(orientation, 0)


def convert_to_webp(source_path: str, destination_path: str) -> None:
    """Convert a single image to WebP format."""
    subprocess.run(
        [
            "cwebp",
            "-q",
            "70",
            "-metadata",
            "icc",  # Preserve ICC profile
            "-mt",  # Enable multi-threading
            "-exact",  # Preserve color values
            "-m",
            "6",  # Best compression method
            source_path,
            "-o",
            destination_path,
        ]
    )


def apply_rotation(image_path: str, orientation: int) -> None:
    """Apply rotation to an image if needed."""
    if orientation <= 1:
        return

    rotation_degrees = get_rotation_degrees(orientation)

    if rotation_degrees == 0:
        return

    with Image.open(image_path) as img:
        # Preserve the ICC profile before rotation
        icc_profile = img.info.get("icc_profile")

        rotated = img.rotate(rotation_degrees, expand=True)
        # Save with the preserved ICC profile
        rotated.save(
            image_path,
            "WEBP",
            quality=70,
            icc_profile=icc_profile,
        )


def process_image(source_path: str, destination_path: str) -> None:
    """Process a single image: convert to WebP and handle rotation."""
    orientation = get_image_orientation(source_path)
    convert_to_webp(source_path, destination_path)
    apply_rotation(destination_path, orientation)
    print(f"Converted {os.path.basename(source_path)} to {destination_path}")


def convert_images_to_webp(source_folder: str) -> None:
    """Convert all JPEG images in a folder to WebP format."""
    if not os.path.exists(source_folder):
        print(f"The folder {source_folder} does not exist.")
        return

    destination_folder = create_output_directory(source_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpeg", ".jpg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, f"{os.path.splitext(filename)[0]}.webp"
            )
            process_image(source_path, destination_path)


def main() -> NoReturn:
    if len(sys.argv) != 2:
        print("Usage: python convert_to_webp.py <folder_path>")
        sys.exit(1)

    folder_path: str = sys.argv[1]
    convert_images_to_webp(folder_path)


if __name__ == "__main__":
    main()
