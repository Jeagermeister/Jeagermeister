"""Speech-to-text abstractions for MVP scaffolding."""

from src.audio import AudioChunk


class SpeechToTextEngine:
    """Stub STT provider returning deterministic text for MVP wiring."""

    def transcribe(self, chunk: AudioChunk) -> str:
        """Translate captured audio into command text (stub behavior)."""
        _ = chunk
        return "status"
