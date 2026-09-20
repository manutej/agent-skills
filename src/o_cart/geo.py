"""Lightweight layer descriptors for Ormus geospatial pipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class GeoLayer:
    """A named spatial layer that an Ormus workflow can bind to a warehouse source."""

    name: str
    source: str
    geom_column: str = "geom"
    properties: dict[str, Any] = field(default_factory=dict)

    def as_carto_source(self) -> dict[str, str]:
        """Shape expected by CARTO-style named sources."""
        return {
            "name": self.name,
            "source": self.source,
            "geom_column": self.geom_column,
        }
