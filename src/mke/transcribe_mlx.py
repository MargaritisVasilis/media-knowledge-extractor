import mlx_whisper


def transcribe_audio_mlx(audio_path: str) -> list[dict]:
    """Transcribe audio using MLX Whisper on Apple Silicon."""

    result = mlx_whisper.transcribe(
        audio_path,
        path_or_hf_repo="mlx-community/whisper-medium-mlx",
        language=None
    )

    segments = []

    for segment in result["segments"]:
        segments.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip()
        })

    return segments