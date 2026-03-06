"""Tests for smartcardfyi API client."""

from __future__ import annotations

from smartcardfyi.api import SmartCardFYI


def test_client_init() -> None:
    client = SmartCardFYI()
    assert client._client.base_url == "https://smartcardfyi.com"
    client.close()


def test_client_custom_base_url() -> None:
    client = SmartCardFYI(base_url="https://test.example.com")
    assert client._client.base_url == "https://test.example.com"
    client.close()


def test_client_context_manager() -> None:
    with SmartCardFYI() as api:
        assert api._client.base_url == "https://smartcardfyi.com"


def test_version() -> None:
    from smartcardfyi import __version__

    assert __version__ == "0.1.0"
