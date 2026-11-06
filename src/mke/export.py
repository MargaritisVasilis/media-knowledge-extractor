import json
from pathlib import Path


def export_transcript(segments: list[dict], output_path: str) -> None:
    """Save transcription as TXT and JSON files."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Save plain text
    text = "\n".join(segment["text"] for segment in segments)

    txt_path = path.with_suffix(".txt")
    txt_path.write_text(text, encoding="utf-8")

    # Save structured transcription
    json_path = path.with_suffix(".json")
    json_path.write_text(
        json.dumps(segments, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )