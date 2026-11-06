from pathlib import Path
from tempfile import TemporaryDirectory

from mke.audio import extract_audio
from mke.media import is_supported_media
from mke.transcription import transcribe


def process_media(file_path: str) -> list[dict]:
    """Extract audio and transcribe a media file."""

    source = Path(file_path)

    if not source.is_file():
        raise FileNotFoundError(f"File not found: {source}")

    if not is_supported_media(file_path):
        raise ValueError(f"Unsupported media format: {source.suffix}")

    with TemporaryDirectory() as temp_dir:
        audio_path = Path(temp_dir) / "audio.wav"

        extract_audio(str(source), str(audio_path))

        segments = transcribe(str(audio_path))

    return segments

from mke.export import export_transcript


def process_and_export(file_path: str, output_path: str) -> None:
    """Process media and save the transcription."""

    segments = process_media(file_path)

    export_transcript(segments, output_path)