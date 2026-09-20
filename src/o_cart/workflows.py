"""Ormus workflow specs that compose CARTO agent-skills operations.

Keep these as data, not as a copy of CARTO Workflows proprietary components.
Agents should load the matching `skills/carto-*` playbook for execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from o_cart.geo import GeoLayer


@dataclass
class WorkflowStep:
    skill: str
    intent: str
    inputs: dict[str, str] = field(default_factory=dict)


@dataclass
class WorkflowSpec:
    name: str
    purpose: str
    layers: list[GeoLayer] = field(default_factory=list)
    steps: list[WorkflowStep] = field(default_factory=list)

    def add_step(self, skill: str, intent: str, **inputs: str) -> "WorkflowSpec":
        self.steps.append(WorkflowStep(skill=skill, intent=intent, inputs=inputs))
        return self


def ormus_spatial_pipeline(
    name: str,
    layers: Iterable[GeoLayer],
    *,
    enrich: bool = True,
    hotspots: bool = False,
    route: bool = False,
) -> WorkflowSpec:
    """Build a default Ormus geospatial DAG that routes through CARTO skills."""
    spec = WorkflowSpec(
        name=name,
        purpose="Ormus geospatial intelligence pipeline",
        layers=list(layers),
    )
    spec.add_step("carto-basics", "ensure auth and profile")
    spec.add_step("carto-explore-datawarehouse", "discover sources")
    spec.add_step("carto-query-datawarehouse", "validate geometries")
    if enrich:
        spec.add_step("carto-spatial-enrichment", "enrich with observatory features")
    if hotspots:
        spec.add_step("carto-hotspot-analysis", "score spatial clusters")
    if route:
        spec.add_step("carto-routing-od-analysis", "compute OD / isolines")
    spec.add_step("carto-create-workflow", "persist the DAG in CARTO Workflows")
    return spec
