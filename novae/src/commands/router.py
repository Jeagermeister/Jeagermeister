"""Command parsing and routing for MVP scaffolding."""

from dataclasses import dataclass


@dataclass
class ParsedCommand:
    """Minimal command representation for routing in MVP stage."""

    name: str
    raw_text: str


class CommandRouter:
    """Converts text into a command and chooses next action."""

    def parse(self, transcript: str) -> ParsedCommand:
        cleaned = transcript.strip().lower()
        if not cleaned:
            cleaned = "noop"
        return ParsedCommand(name=cleaned.split()[0], raw_text=transcript)
