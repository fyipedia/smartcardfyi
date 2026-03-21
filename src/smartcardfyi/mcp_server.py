"""MCP server for smartcardfyi — AI assistant tools for smartcardfyi.com.

Run: uvx --from "smartcardfyi[mcp]" python -m smartcardfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SmartCardFYI")


@mcp.tool()
def list_card_types(limit: int = 20, offset: int = 0) -> str:
    """List card_types from smartcardfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.list_card_types(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No card_types found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_card_type(slug: str) -> str:
    """Get detailed information about a specific card_type.

    Args:
        slug: URL slug identifier for the card_type.
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.get_card_type(slug)
        return str(data)


@mcp.tool()
def list_applications(limit: int = 20, offset: int = 0) -> str:
    """List applications from smartcardfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.list_applications(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No applications found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_smartcard(query: str) -> str:
    """Search smartcardfyi.com for smart card types, EMV applications, and certifications.

    Args:
        query: Search query string.
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
