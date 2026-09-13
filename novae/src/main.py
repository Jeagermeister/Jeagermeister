"""NOVAE MVP entrypoint wiring audio, STT, parsing, and Hermit adapter stubs."""

import logging

from src.audio import AudioCapture
from src.commands import CommandRouter
from src.hermit_adapter import HermitAdapter
from src.stt import SpeechToTextEngine


def run_once() -> str:
    """Run a single MVP pipeline iteration and return adapter output."""
    capture = AudioCapture()
    stt = SpeechToTextEngine()
    router = CommandRouter()
    hermit = HermitAdapter()

    chunk = capture.capture_once()
    transcript = stt.transcribe(chunk)
    command = router.parse(transcript)
    return hermit.send(command)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    result = run_once()
    logging.info("NOVAE MVP pipeline result: %s", result)


if __name__ == "__main__":
    main()
