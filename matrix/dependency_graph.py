#!/usr/bin/env python3
"""
Dependency Graph Generator for Hubstry HALE Ecosystem

Generates a text-based dependency graph showing relationships between
academic papers and implementation repositories. No external dependencies
required - uses only Python standard library.

Usage:
    python dependency_graph.py [--format ascii|dot|json] [--output FILE]

Author: guilherme-machado-ceo
License: CC BY 4.0
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class License(Enum):
    CC_BY_NC_ND_40 = "CC BY-NC-ND 4.0"
    CC_BY_40 = "CC BY 4.0"


class IntegrationType(Enum):
    REFERENCE_ONLY = "Reference Only"
    FULL_ADAPTATION = "Full Adaptation"


@dataclass
class Paper:
    """Represents an academic paper in the ecosystem."""
    id: str
    title: str
    short_name: str
    doi: str
    license: License
    zenodo_url: str

    @property
    def is_adaptable(self) -> bool:
        return self.license == License.CC_BY_40


@dataclass
class Repository:
    """Represents an implementation repository."""
    name: str
    url: str
    description: str


@dataclass
class Dependency:
    """Represents a paper-to-repo dependency."""
    paper_id: str
    repo_name: str
    integration_type: IntegrationType
    description: str


@dataclass
class InterRepoDependency:
    """Represents a repo-to-repo communication."""
    source: str
    target: str
    protocol: str
    description: str


class EcosystemGraph:
    """Graph representation of the HALE Ecosystem."""

    def __init__(self) -> None:
        self.papers: dict[str, Paper] = {}
        self.repos: dict[str, Repository] = {}
        self.dependencies: list[Dependency] = []
        self.inter_repo_deps: list[InterRepoDependency] = []

    def add_paper(self, paper: Paper) -> None:
        self.papers[paper.id] = paper

    def add_repo(self, repo: Repository) -> None:
        self.repos[repo.name] = repo

    def add_dependency(self, dep: Dependency) -> None:
        self.dependencies.append(dep)

    def add_inter_repo_dep(self, dep: InterRepoDependency) -> None:
        self.inter_repo_deps.append(dep)

    def get_papers_for_repo(self, repo_name: str) -> list[Dependency]:
        return [d for d in self.dependencies if d.repo_name == repo_name]

    def get_repos_for_paper(self, paper_id: str) -> list[Dependency]:
        return [d for d in self.dependencies if d.paper_id == paper_id]


def build_ecosystem() -> EcosystemGraph:
    """Build the complete HALE Ecosystem graph."""
    graph = EcosystemGraph()

    # --- Papers ---
    graph.add_paper(Paper(
        id="P1",
        title="HALE Working Paper v3.0",
        short_name="HALE v3.0",
        doi="10.5281/zenodo.18901934",
        license=License.CC_BY_NC_ND_40,
        zenodo_url="https://doi.org/10.5281/zenodo.18901934",
    ))
    graph.add_paper(Paper(
        id="P2",
        title="pi*sqrt(f(A)) + Quantum Computation",
        short_name="pi*sqrt+Q",
        doi="10.5281/zenodo.18776462",
        license=License.CC_BY_40,
        zenodo_url="https://doi.org/10.5281/zenodo.18776462",
    ))
    graph.add_paper(Paper(
        id="P3",
        title="pi*sqrt(f(A)) Hexa-Relational Algebra",
        short_name="pi*sqrt Hex",
        doi="10.5281/zenodo.18776401",
        license=License.CC_BY_40,
        zenodo_url="https://doi.org/10.5281/zenodo.18776401",
    ))
    graph.add_paper(Paper(
        id="P4",
        title="HPG 1.0 Harmonic Protocol Grid",
        short_name="HPG 1.0",
        doi="10.5281/zenodo.19056387",
        license=License.CC_BY_40,
        zenodo_url="https://doi.org/10.5281/zenodo.19056387",
    ))

    # --- Repositories ---
    graph.add_repo(Repository(
        name="iot-protocol-hubstry",
        url="https://github.com/guilherme-machado-ceo/iot-protocol-hubstry",
        description="IoT Harmonic Protocol implementation with post-quantum security",
    ))
    graph.add_repo(Repository(
        name="hubstry-security",
        url="https://github.com/guilherme-machado-ceo/hubstry-security",
        description="Cybersecurity framework with harmonic signal layer",
    ))
    graph.add_repo(Repository(
        name="qualia-hub-ecosystem",
        url="https://github.com/guilherme-machado-ceo/qualia-hub-ecosystem",
        description="Qualia processing with hexa-relational algebra",
    ))

    # --- Paper -> Repo Dependencies ---
    graph.add_dependency(Dependency(
        paper_id="P1",
        repo_name="iot-protocol-hubstry",
        integration_type=IntegrationType.REFERENCE_ONLY,
        description="HALE theoretical framework cited as basis for IoT addressing",
    ))
    graph.add_dependency(Dependency(
        paper_id="P1",
        repo_name="hale-ecosystem",
        integration_type=IntegrationType.REFERENCE_ONLY,
        description="HALE v3.0 as conceptual foundation for meta-framework",
    ))
    graph.add_dependency(Dependency(
        paper_id="P2",
        repo_name="hubstry-security",
        integration_type=IntegrationType.FULL_ADAPTATION,
        description="Quantum-safe primitives adapted into security framework",
    ))
    graph.add_dependency(Dependency(
        paper_id="P2",
        repo_name="qualia-hub-ecosystem",
        integration_type=IntegrationType.FULL_ADAPTATION,
        description="pi*sqrt(f(A)) mathematical framework adapted for qualia processing",
    ))
    graph.add_dependency(Dependency(
        paper_id="P3",
        repo_name="qualia-hub-ecosystem",
        integration_type=IntegrationType.FULL_ADAPTATION,
        description="Hexa-relational algebra for knowledge representation engine",
    ))
    graph.add_dependency(Dependency(
        paper_id="P4",
        repo_name="iot-protocol-hubstry",
        integration_type=IntegrationType.FULL_ADAPTATION,
        description="HPG grid topology and routing adapted for IoT protocol",
    ))
    graph.add_dependency(Dependency(
        paper_id="P4",
        repo_name="hubstry-security",
        integration_type=IntegrationType.FULL_ADAPTATION,
        description="HPG security overlay adapted for cybersecurity framework",
    ))

    # --- Inter-Repo Dependencies ---
    graph.add_inter_repo_dep(InterRepoDependency(
        source="iot-protocol-hubstry",
        target="hubstry-security",
        protocol="HSL (Harmonic Signal Layer)",
        description="Encrypted telemetry exchange via harmonic signal layer",
    ))
    graph.add_inter_repo_dep(InterRepoDependency(
        source="hubstry-security",
        target="qualia-hub-ecosystem",
        protocol="Qualia API",
        description="Anomaly classification via qualia analysis",
    ))
    graph.add_inter_repo_dep(InterRepoDependency(
        source="qualia-hub-ecosystem",
        target="iot-protocol-hubstry",
        protocol="Data Pipeline",
        description="Semantic data feed for IoT protocol enrichment",
    ))

    return graph


def render_ascii(graph: EcosystemGraph) -> str:
    """Render the dependency graph as ASCII art."""
    lines: list[str] = []

    lines.append("")
    lines.append("=" * 72)
    lines.append("  HUBSTRY HALE ECOSYSTEM - DEPENDENCY GRAPH")
    lines.append("=" * 72)
    lines.append("")

    # --- Papers section ---
    lines.append("  ACADEMIC PAPERS")
    lines.append("  " + "-" * 68)
    for pid, paper in graph.papers.items():
        adapts = "ADAPTABLE" if paper.is_adaptable else "REFERENCE ONLY"
        lines.append(f"")
        lines.append(f"  [{pid}] {paper.short_name}")
        lines.append(f"       Title  : {paper.title}")
        lines.append(f"       DOI    : {paper.doi}")
        lines.append(f"       License: {paper.license.value}")
        lines.append(f"       Status : {adapts}")

    # --- Repositories section ---
    lines.append("")
    lines.append("")
    lines.append("  REPOSITORIES")
    lines.append("  " + "-" * 68)
    for rname, repo in graph.repos.items():
        deps = graph.get_papers_for_repo(rname)
        dep_str = ", ".join(f"{d.paper_id}({d.integration_type.value})" for d in deps)
        lines.append(f"")
        lines.append(f"  [{rname}]")
        lines.append(f"       URL  : {repo.url}")
        lines.append(f"       Desc : {repo.description}")
        lines.append(f"       Papers: {dep_str}")

    # --- Dependency Matrix ---
    lines.append("")
    lines.append("")
    lines.append("  DEPENDENCY MATRIX")
    lines.append("  " + "-" * 68)

    header = f"  {'Paper':<16} {'License':<18} {'Integration':<16} {'Repo':<28}"
    lines.append(header)
    lines.append("  " + "-" * 66)

    for dep in graph.dependencies:
        paper = graph.papers[dep.paper_id]
        marker = "  " if dep.integration_type == IntegrationType.FULL_ADAPTATION else ".."
        line = f"{marker}{paper.short_name:<14} {paper.license.value:<18} "
        line += f"{dep.integration_type.value:<16} {dep.repo_name:<28}"
        lines.append(line)

    # --- Inter-Repo Communication ---
    lines.append("")
    lines.append("")
    lines.append("  INTER-REPOSITORY COMMUNICATION")
    lines.append("  " + "-" * 68)

    for irepo in graph.inter_repo_deps:
        arrow = "->"
        lines.append(f"  {irepo.source:<28} {arrow} {irepo.target:<28}")
        lines.append(f"    Protocol: {irepo.protocol}")
        lines.append(f"    Purpose : {irepo.description}")
        lines.append("")

    # --- ASCII Graph ---
    lines.append("")
    lines.append("  VISUAL GRAPH")
    lines.append("  " + "-" * 68)
    lines.append("")
    lines.append("                  +-----------------------------+")
    lines.append("                  | hubstry-hale-ecosystem     |")
    lines.append("                  | (Meta-Framework)            |")
    lines.append("                  +-----------------------------+")
    lines.append("                   /    |      |      \\")
    lines.append("                  /     |      |       \\")
    lines.append("  [P1:BY-NC-ND] .  [P2:BY] [P3:BY] [P4:BY]")
    lines.append("     (ref only)      |  \\   /  |      /  \\")
    lines.append("                     |   \\ /   |     /    \\")
    lines.append("                     v    v    v    v      v")
    lines.append("              +-----------+  +----------+  +--------+")
    lines.append("              | hubstry-  |  | qualia-  |  | iot-   |")
    lines.append("              | security  |  | hub-     |  | proto- |")
    lines.append("              +-----------+  | ecosystem|  | col-   |")
    lines.append("                   |        +----------+  | hubstry|")
    lines.append("          HSL <-->|<--> Qualia API        +--------+")
    lines.append("                   |         ^                     |")
    lines.append("                   |         |                     |")
    lines.append("                   +---------+---------- HPG <-----+")
    lines.append("")
    lines.append("  Legend:")
    lines.append("    [P#:LICENSE] = Paper with its Creative Commons license")
    lines.append("    =========>    = Full adaptation (CC BY 4.0)")
    lines.append("    ..........>  = Reference only (CC BY-NC-ND 4.0)")
    lines.append("    <------>     = Bidirectional communication protocol")
    lines.append("")
    lines.append("=" * 72)

    return "\n".join(lines)


def render_dot(graph: EcosystemGraph) -> str:
    """Render the dependency graph in Graphviz DOT format."""
    lines: list[str] = []

    lines.append("digraph hale_ecosystem {")
    lines.append('  rankdir=TB;')
    lines.append('  compound=true;')
    lines.append('  fontname="Helvetica";')
    lines.append('  fontsize=12;')
    lines.append("")

    # --- Meta-framework cluster ---
    lines.append("  subgraph cluster_meta {")
    lines.append('    label="hubstry-hale-ecosystem (Meta-Framework)";')
    lines.append('    style=filled;')
    lines.append('    fillcolor="#e8f5e9";')
    lines.append('    color="#2e7d32";')
    lines.append('    pencolor=3;')
    lines.append('    meta [label="Paper Mapping\\nLicense Guide\\nArchitecture Docs";')
    lines.append('           shape=box, style=filled, fillcolor="#c8e6c9"];')
    lines.append("  }")
    lines.append("")

    # --- Paper nodes ---
    lines.append("  subgraph cluster_papers {")
    lines.append('    label="Academic Papers";')
    lines.append('    style=filled;')
    lines.append('    fillcolor="#fff9c4";')
    lines.append('    color="#f9a825";')

    for pid, paper in graph.papers.items():
        color = "#ffcdd2" if not paper.is_adaptable else "#bbdefb"
        border = "#c62828" if not paper.is_adaptable else "#1565c0"
        lines.append(f'    {pid} [label="{paper.short_name}\\n{paper.license.value}";')
        lines.append(f'          shape=note, style=filled, fillcolor="{color}",')
        lines.append(f'          color="{border}", fontcolor="#212121"];')

    lines.append("  }")
    lines.append("")

    # --- Repo nodes ---
    lines.append("  subgraph cluster_repos {")
    lines.append('    label="Implementation Repositories";')
    lines.append('    style=filled;')
    lines.append('    fillcolor="#fff3e0";')
    lines.append('    color="#e65100";')

    for rname, repo in graph.repos.items():
        safe = rname.replace("-", "_")
        lines.append(f'    {safe} [label="{rname}\\n{repo.description}";')
        lines.append(f'           shape=component, style=filled, fillcolor="#ffe0b2",')
        lines.append(f'           color="#e65100", fontcolor="#212121"];')

    lines.append("  }")
    lines.append("")

    # --- Paper to Repo edges ---
    for dep in graph.dependencies:
        paper = graph.papers[dep.paper_id]
        safe_repo = dep.repo_name.replace("-", "_")
        if dep.integration_type == IntegrationType.FULL_ADAPTATION:
            style = 'style=bold, color="#1565c0", label="adapt"'
        else:
            style = 'style=dashed, color="#c62828", label="cite"'
        lines.append(f'  {dep.paper_id} -> {safe_repo} [{style}];')

    lines.append("")

    # --- Inter-repo edges ---
    for irepo in graph.inter_repo_deps:
        src = irepo.source.replace("-", "_")
        tgt = irepo.target.replace("-", "_")
        lines.append(f'  {src} -> {tgt} [label="{irepo.protocol}", style=bold, color="#424242"];')

    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def render_json(graph: EcosystemGraph) -> str:
    """Render the dependency graph as JSON."""
    data = {
        "ecosystem": "hubstry-hale-ecosystem",
        "meta_framework": {
            "repository": "https://github.com/guilherme-machado-ceo/hubstry-hale-ecosystem",
            "license": "CC BY 4.0",
        },
        "papers": [
            {
                "id": p.id,
                "title": p.title,
                "short_name": p.short_name,
                "doi": p.doi,
                "license": p.license.value,
                "url": p.zenodo_url,
                "is_adaptable": p.is_adaptable,
            }
            for p in graph.papers.values()
        ],
        "repositories": [
            {
                "name": r.name,
                "url": r.url,
                "description": r.description,
                "linked_papers": [
                    {
                        "paper_id": d.paper_id,
                        "integration_type": d.integration_type.value,
                        "description": d.description,
                    }
                    for d in graph.get_papers_for_repo(r.name)
                ],
            }
            for r in graph.repos.values()
        ],
        "inter_repo_communication": [
            {
                "source": ir.source,
                "target": ir.target,
                "protocol": ir.protocol,
                "description": ir.description,
            }
            for ir in graph.inter_repo_deps
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate dependency graph for the Hubstry HALE Ecosystem"
    )
    parser.add_argument(
        "--format",
        choices=["ascii", "dot", "json"],
        default="ascii",
        help="Output format (default: ascii)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    graph = build_ecosystem()

    if args.format == "ascii":
        content = render_ascii(graph)
    elif args.format == "dot":
        content = render_dot(graph)
    elif args.format == "json":
        content = render_json(graph)
    else:
        print(f"Unknown format: {args.format}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Graph written to: {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()