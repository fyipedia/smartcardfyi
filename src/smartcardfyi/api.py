"""HTTP API client for smartcardfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install smartcardfyi[api]``

Usage::

    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        items = api.list_applications()
        detail = api.get_application("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class SmartCardFYI:
    """API client for the smartcardfyi.com REST API.

    Provides typed access to all smartcardfyi.com endpoints including
    list, detail, and search operations.

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

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_applications(self, **params: Any) -> dict[str, Any]:
        """List all applications."""
        return self._get("/api/v1/applications/", **params)

    def get_application(self, slug: str) -> dict[str, Any]:
        """Get application by slug."""
        return self._get(f"/api/v1/applications/" + slug + "/")

    def list_card_types(self, **params: Any) -> dict[str, Any]:
        """List all card types."""
        return self._get("/api/v1/card-types/", **params)

    def get_card_type(self, slug: str) -> dict[str, Any]:
        """Get card type by slug."""
        return self._get(f"/api/v1/card-types/" + slug + "/")

    def list_categories(self, **params: Any) -> dict[str, Any]:
        """List all categories."""
        return self._get("/api/v1/categories/", **params)

    def get_category(self, slug: str) -> dict[str, Any]:
        """Get category by slug."""
        return self._get(f"/api/v1/categories/" + slug + "/")

    def list_certifications(self, **params: Any) -> dict[str, Any]:
        """List all certifications."""
        return self._get("/api/v1/certifications/", **params)

    def get_certification(self, slug: str) -> dict[str, Any]:
        """Get certification by slug."""
        return self._get(f"/api/v1/certifications/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_form_factors(self, **params: Any) -> dict[str, Any]:
        """List all form factors."""
        return self._get("/api/v1/form-factors/", **params)

    def get_form_factor(self, slug: str) -> dict[str, Any]:
        """Get form factor by slug."""
        return self._get(f"/api/v1/form-factors/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_manufacturers(self, **params: Any) -> dict[str, Any]:
        """List all manufacturers."""
        return self._get("/api/v1/manufacturers/", **params)

    def get_manufacturer(self, slug: str) -> dict[str, Any]:
        """Get manufacturer by slug."""
        return self._get(f"/api/v1/manufacturers/" + slug + "/")

    def list_personalization(self, **params: Any) -> dict[str, Any]:
        """List all personalization."""
        return self._get("/api/v1/personalization/", **params)

    def get_personalization(self, slug: str) -> dict[str, Any]:
        """Get personalization by slug."""
        return self._get(f"/api/v1/personalization/" + slug + "/")

    def list_platforms(self, **params: Any) -> dict[str, Any]:
        """List all platforms."""
        return self._get("/api/v1/platforms/", **params)

    def get_platform(self, slug: str) -> dict[str, Any]:
        """Get platform by slug."""
        return self._get(f"/api/v1/platforms/" + slug + "/")

    def list_standards(self, **params: Any) -> dict[str, Any]:
        """List all standards."""
        return self._get("/api/v1/standards/", **params)

    def get_standard(self, slug: str) -> dict[str, Any]:
        """Get standard by slug."""
        return self._get(f"/api/v1/standards/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> SmartCardFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
