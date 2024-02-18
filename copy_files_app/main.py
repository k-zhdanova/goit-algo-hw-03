import os
import shutil
from pathlib import Path
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Copy files to destination directory and sort them by extension."
    )
    parser.add_argument("source", type=Path, help="Source directory path")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Destination directory path. Default is 'dist'",
    )
    return parser.parse_args()


def recursive_copy(source: Path, destination: Path):
    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} not found")

    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in source.iterdir():
        if item.is_dir():
            recursive_copy(item, destination)
        else:
            extension = item.suffix
            extension_dir = destination / extension
            if not extension_dir.exists():
                extension_dir.mkdir()

            shutil.copy(item, extension_dir)


def main():
    try:
        args = parse_args()
        source = args.source
        destination = args.destination

        recursive_copy(source, destination)
        print(f"Files were successfully copied from {source} to {destination}.")

    except KeyboardInterrupt:
        print("Program was interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
