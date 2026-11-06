import argparse
from pathlib import Path

from mke.pipeline import process_and_export


def main():
    """Command-line interface for Media Knowledge Extractor."""

    parser = argparse.ArgumentParser(
        description="Media Knowledge Extractor"
    )

    parser.add_argument(
        "input",
        help="Path to the audio or video file"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output path without extension"
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    output_path = (
        Path(args.output)
        if args.output
        else Path("outputs") / input_path.stem
    )

    print(f"Processing: {input_path}")

    process_and_export(str(input_path), str(output_path))

    print(f"Completed! Files saved to: {output_path.parent}")


if __name__ == "__main__":
    main()