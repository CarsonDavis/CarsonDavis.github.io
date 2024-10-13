import os
import sys
import subprocess
from typing import NoReturn


def convert_images_to_webp(source_folder: str) -> None:
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"The folder {source_folder} does not exist.")
        return

    # Create a new folder inside the source folder for the WebP files
    destination_folder: str = os.path.join(source_folder, "webp_images")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(
            (".jpeg", ".jpg")
        ):  # Add more extensions if needed
            source_path: str = os.path.join(source_folder, filename)
            destination_path: str = os.path.join(
                destination_folder, f"{os.path.splitext(filename)[0]}.webp"
            )

            # Run the cwebp command
            subprocess.run(["cwebp", "-q", "70", source_path, "-o", destination_path])

            print(f"Converted {filename} to {destination_path}")


def main() -> NoReturn:
    if len(sys.argv) != 2:
        print("Usage: python convert_to_webp.py <folder_path>")
        sys.exit(1)

    folder_path: str = sys.argv[1]
    convert_images_to_webp(folder_path)


if __name__ == "__main__":
    main()
