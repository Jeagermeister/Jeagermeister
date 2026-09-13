"""Audio capture abstractions for MVP scaffolding."""

from dataclasses import dataclass


@dataclass
class AudioChunk:
    """Represents a captured unit of audio data for the MVP flow."""

    data: bytes
    sample_rate_hz: int = 16_000


class AudioCapture:
    """Stub microphone capture provider for first-pass pipeline testing."""

    def capture_once(self) -> AudioChunk:
        """Return a placeholder audio chunk until real capture is integrated."""
        return AudioChunk(data=b"mvp-audio-placeholder")
