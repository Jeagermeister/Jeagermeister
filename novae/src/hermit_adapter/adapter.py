"""Hermit adapter contract and MVP stub implementation."""

from src.commands import ParsedCommand


class HermitAdapter:
    """Stub transport for forwarding parsed commands to Hermit in future phases."""

    def send(self, command: ParsedCommand) -> str:
        """Send command to Hermit transport (stubbed for MVP)."""
        return f"[hermit-stub] received command='{command.name}' raw='{command.raw_text}'"
