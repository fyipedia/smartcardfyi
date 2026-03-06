"""Command-line interface for smartcardfyi.

Requires the ``cli`` extra: ``pip install smartcardfyi[cli]``

Usage::

    smartcardfyi search "emv"
    smartcardfyi card emv-contact
    smartcardfyi compare java-card multos
    smartcardfyi random
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="smartcardfyi",
    help="Smart card encyclopedia — card types, chip platforms, and specs from SmartCardFYI.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'emv', 'java card', 'sim')"),
) -> None:
    """Search across card types, platforms, standards, and glossary."""
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        results = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name")
    table.add_column("Slug")

    items = results.get("results", [])
    if not items:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    for item in items:
        table.add_row(item.get("type", ""), item.get("name", ""), item.get("slug", ""))

    console.print(table)


@app.command()
def card(
    slug: str = typer.Argument(help="Card type slug (e.g. 'emv-contact', 'sim-card')"),
) -> None:
    """Look up a smart card type with full specifications."""
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.card(slug)

    console.print(f"\n[bold]{data.get('name', slug)}[/bold]")
    if data.get("description"):
        console.print(f"  {data['description'][:200]}")
    console.print()

    table = Table(title="Specifications")
    table.add_column("Property", style="cyan")
    table.add_column("Value")

    specs = [
        ("Category", data.get("category")),
        ("Interface", data.get("interface")),
        ("Platform", data.get("platform")),
        ("Form Factor", data.get("form_factor")),
        ("Memory Size", data.get("memory_size")),
        ("Crypto Support", data.get("crypto_support")),
        ("Multi-app", data.get("is_multi_app")),
        ("Certification", data.get("certification")),
    ]
    for label, value in specs:
        if value is not None:
            table.add_row(label, str(value))

    console.print(table)


@app.command()
def compare(
    slug_a: str = typer.Argument(help="First card type slug"),
    slug_b: str = typer.Argument(help="Second card type slug"),
) -> None:
    """Compare two smart card types side by side."""
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.compare(slug_a, slug_b)

    a = data.get("a", {})
    b = data.get("b", {})

    table = Table(title=f"{a.get('name', slug_a)} vs {b.get('name', slug_b)}")
    table.add_column("Property", style="cyan")
    table.add_column(a.get("name", slug_a), style="green")
    table.add_column(b.get("name", slug_b), style="yellow")

    fields = [
        ("Category", "category"),
        ("Interface", "interface"),
        ("Platform", "platform"),
        ("Form Factor", "form_factor"),
        ("Memory Size", "memory_size"),
        ("Multi-app", "is_multi_app"),
    ]
    for label, key in fields:
        table.add_row(label, str(a.get(key, "-")), str(b.get(key, "-")))

    console.print(table)


@app.command()
def random() -> None:
    """Discover a random smart card type."""
    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        data = api.random()

    console.print(f"\n[bold]{data.get('name', 'Unknown')}[/bold]")
    if data.get("description"):
        console.print(f"  {data['description'][:200]}")
    console.print(f"  Interface: {data.get('interface', 'N/A')}")
    console.print(f"  Platform: {data.get('platform', 'N/A')}")
    console.print(f"  Category: {data.get('category', 'N/A')}")
    console.print()


if __name__ == "__main__":
    app()
