"""HTTP API client for smartcardfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install smartcardfyi[api]``

Usage::

    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        results = api.search("emv")
        card = api.card("emv-contact")
        comparison = api.compare("java-card", "multos")
"""

from __future__ import annotations

from typing import Any

import httpx


class SmartCardFYI:
    """API client for the smartcardfyi.com REST API.

    Provides access to 12 endpoints covering smart card types, chip platforms,
    standards, manufacturers, applications, form factors, certifications,
    glossary terms, search, comparison, and random discovery.

    Args:
        base_url: API base URL. Defaults to ``https://smartcardfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://smartcardfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def card(self, slug: str) -> dict[str, Any]:
        """Get smart card type detail with specs, standards, and applications.

        Args:
            slug: Card type URL slug (e.g. ``"emv-contact"``, ``"sim-card"``, ``"piv-card"``).
        """
        return self._get(f"/api/card/{slug}/")

    def platform(self, slug: str) -> dict[str, Any]:
        """Get chip platform detail with supported card types and features.

        Args:
            slug: Platform URL slug (e.g. ``"java-card"``, ``"multos"``, ``"basiccard"``).
        """
        return self._get(f"/api/platform/{slug}/")

    def standard(self, slug: str) -> dict[str, Any]:
        """Get smart card standard detail with linked card types.

        Args:
            slug: Standard URL slug (e.g. ``"iso-7816"``, ``"emv-4-3"``, ``"globalplatform-2-3"``).
        """
        return self._get(f"/api/standard/{slug}/")

    def manufacturer(self, slug: str) -> dict[str, Any]:
        """Get manufacturer detail with product lines and chip platforms.

        Args:
            slug: Manufacturer URL slug (e.g. ``"nxp"``, ``"infineon"``, ``"idemia"``).
        """
        return self._get(f"/api/manufacturer/{slug}/")

    def application(self, slug: str) -> dict[str, Any]:
        """Get application detail with associated card types and standards.

        Args:
            slug: Application URL slug (e.g. ``"payment"``, ``"identity"``, ``"transit"``).
        """
        return self._get(f"/api/application/{slug}/")

    def form_factor(self, slug: str) -> dict[str, Any]:
        """Get form factor detail with dimensions and associated card types.

        Args:
            slug: Form factor URL slug (e.g. ``"id-1"``, ``"mini-sim"``, ``"nano-sim"``).
        """
        return self._get(f"/api/form-factor/{slug}/")

    def certification(self, slug: str) -> dict[str, Any]:
        """Get certification detail with requirements and certified products.

        Args:
            slug: Certification URL slug (e.g. ``"common-criteria"``, ``"fips-140"``).
        """
        return self._get(f"/api/certification/{slug}/")

    def glossary_term(self, slug: str) -> dict[str, Any]:
        """Get glossary term definition for tooltips and reference.

        Args:
            slug: Term URL slug (e.g. ``"apdu"``, ``"atr"``, ``"secure-element"``).
        """
        return self._get(f"/api/term/{slug}/")

    def search(self, query: str) -> dict[str, Any]:
        """Search across card types, platforms, standards, and glossary terms.

        Args:
            query: Search term (minimum 2 characters).
        """
        return self._get("/api/search/", q=query)

    def compare(self, slug_a: str, slug_b: str) -> dict[str, Any]:
        """Compare two smart card types side by side.

        Args:
            slug_a: First card type slug (e.g. ``"emv-contact"``).
            slug_b: Second card type slug (e.g. ``"emv-contactless"``).
        """
        return self._get("/api/compare/", a=slug_a, b=slug_b)

    def random(self) -> dict[str, Any]:
        """Get a random smart card type with full detail."""
        return self._get("/api/random/")

    def openapi(self) -> dict[str, Any]:
        """Get the OpenAPI 3.1.0 specification."""
        return self._get("/api/openapi.json")

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> SmartCardFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
