import subprocess
from pathlib import Path


def extract_audio(input_path: str, output_path: str) -> None:
    """Extract audio from media as mono 16 kHz WAV."""

    source = Path(input_path)
    destination = Path(output_path)

    if not source.is_file():
        raise FileNotFoundError(f"File not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-v", "error",
        "-i", str(source),
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-c:a", "pcm_s16le",
        "-y",
        str(destination),
    ]

    subprocess.run(command, check=True)