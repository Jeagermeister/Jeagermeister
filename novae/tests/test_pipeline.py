from src.main import run_once
from src.commands import CommandRouter


def test_run_once_returns_stubbed_adapter_response() -> None:
    result = run_once()
    assert "hermit-stub" in result
    assert "status" in result


def test_router_defaults_to_noop_on_empty_input() -> None:
    parsed = CommandRouter().parse("   ")
    assert parsed.name == "noop"
