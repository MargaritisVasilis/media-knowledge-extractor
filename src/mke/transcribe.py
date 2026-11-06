from faster_whisper import WhisperModel


def transcribe_audio(audio_path: str) -> list[dict]:
    """Transcribe audio and return timestamped segments."""

    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language=None
    )

    results = []

    for segment in segments:
        results.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return results