"""MCP server for smartcardfyi — smart card tools for AI assistants.

Requires the ``mcp`` extra: ``pip install smartcardfyi[mcp]``

Run as a standalone server::

    python -m smartcardfyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "smartcardfyi": {
                "command": "python",
                "args": ["-m", "smartcardfyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("smartcardfyi")


@mcp.tool()
def smartcard_search(query: str) -> str:
    """Search for smart card types, chip platforms, standards, and terminology on SmartCardFYI.

    Search across smart card formats (EMV, SIM, PIV, CAC, FIDO2), chip platforms
    (Java Card, MULTOS, JCOP, BasicCard), standards (ISO 7816, GlobalPlatform),
    and glossary terms.

    Args:
        query: Search term (e.g. "emv", "java card", "sim", "apdu").
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        results = api.search(query)

    items = results.get("results", [])
    if not items:
        return f"No results found for '{query}'."

    lines = [
        f"## Smart Card Search: {query}",
        "",
        f"Found {len(items)} result(s):",
        "",
        "| Type | Name | Slug |",
        "|------|------|------|",
    ]

    for item in items:
        t, n, s = item.get("type", ""), item.get("name", ""), item.get("slug", "")
        lines.append(f"| {t} | {n} | {s} |")

    return "\n".join(lines)


@mcp.tool()
def smartcard_lookup(slug: str) -> str:
    """Look up a specific smart card type by slug.

    Returns full specifications including interface, platform, form factor,
    memory size, crypto support, certifications, and related standards.

    Args:
        slug: Card type slug (e.g. "emv-contact", "sim-card", "piv-card", "java-card").
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.card(slug)

    lines = [
        f"## {data.get('name', slug)}",
        "",
        data.get("description", ""),
        "",
        f"- **Category**: {data.get('category', 'N/A')}",
        f"- **Interface**: {data.get('interface', 'N/A')}",
        f"- **Platform**: {data.get('platform', 'N/A')}",
        f"- **Form Factor**: {data.get('form_factor', 'N/A')}",
        f"- **Memory Size**: {data.get('memory_size', 'N/A')}",
        f"- **Crypto Support**: {data.get('crypto_support', 'N/A')}",
    ]

    standards = data.get("standards", [])
    if standards:
        lines.append("")
        lines.append("### Standards")
        for st in standards:
            lines.append(f"- {st.get('name', '')} ({st.get('issuing_body', '')})")

    return "\n".join(lines)


@mcp.tool()
def smartcard_compare(slug_a: str, slug_b: str) -> str:
    """Compare two smart card types side by side.

    Args:
        slug_a: First card type slug (e.g. "emv-contact").
        slug_b: Second card type slug (e.g. "emv-contactless").
    """
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.compare(slug_a, slug_b)

    a = data.get("a", {})
    b = data.get("b", {})

    lines = [
        f"## {a.get('name', slug_a)} vs {b.get('name', slug_b)}",
        "",
        "| Property | " + a.get("name", slug_a) + " | " + b.get("name", slug_b) + " |",
        "|----------|"
        + "-" * len(a.get("name", slug_a))
        + "--|"
        + "-" * len(b.get("name", slug_b))
        + "--|",
    ]

    fields = [
        ("Category", "category"),
        ("Interface", "interface"),
        ("Platform", "platform"),
        ("Form Factor", "form_factor"),
        ("Memory Size", "memory_size"),
        ("Multi-app", "is_multi_app"),
    ]
    for label, key in fields:
        lines.append(f"| {label} | {a.get(key, '-')} | {b.get(key, '-')} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
