import platform


def transcribe(audio_path: str) -> list[dict]:
    """Automatically select the transcription engine."""

    is_apple_silicon = (
        platform.system() == "Darwin"
        and platform.machine() == "arm64"
    )

    if is_apple_silicon:
        from mke.transcribe_mlx import transcribe_audio_mlx
        return transcribe_audio_mlx(audio_path)

    from mke.transcribe import transcribe_audio
    return transcribe_audio(audio_path)