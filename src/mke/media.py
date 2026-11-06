from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".mp3", ".wav", ".m4a", ".flac",
    ".mp4", ".mov", ".mkv", ".avi"
}


def is_supported_media(file_path: str) -> bool:
    """Check whether a file has a supported media extension."""
    return Path(file_path).suffix.lower() in SUPPORTED_EXTENSIONS
