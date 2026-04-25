# Hubstry HALE Ecosystem

> **Meta-Framework** | Ecossistema Integrado de Pesquisa e Desenvolvimento
>
> Central hub that unifies 4 academic papers and cross-links 3 specialized
> repositories under the Hubstry Harmonic framework.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI: Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.18901934.svg)](https://doi.org/10.5281/zenodo.18901934)

---
## Incrementos / Latest Implementations

| Módulo | Arquivo | Descrição |
|--------|---------|-----------|
| **HALE Pipeline** | hale_core/hale_equation.py | Pipeline: f0 - H - h - ψ - c - M - g |
| **Funções ψ1-ψ4** | hale_core/psi_functions.py | 4 funções de endereçamento selecionáveis |
| **Omnigrid 2D** | hpg_core/omnigrid.py | Grade O_N = H_N × {-1,+1} com Euler |
| **HPM 1.0** | hpg_core/hpm_config.py | 12 canais harmônicos (f0=16.384 kHz) |
| **Sinal s(t) + FFT** | hpg_core/signal_processing.py | Sinal composto + decodificação FFT |
| **Verificação Espectral** | hpg_core/spectral_verification.py | Integridade de razões racionais |
| **HSL Auth** | security/hsl_auth.py | H-Challenge/Response 3 etapas (~200B) |
| **Detecção de Intrusão** | security/intrusion_detection.py | Desvio de fase Δφ > ε |
| **Rotação LFSR** | security/key_rotation.py | Rotação de chaves via LFSR |
| **π-Radical Operator** | pi_radical/pi_radical.py | Operador π-radical — 6 relações ρ₁-ρ₆ |
| **Lattice 64 Perfis** | pi_radical/lattice_profiles.py | Lattice de 64 perfis harmônicos |
| **W Matrix Fixed-Point** | pi_radical/w_matrix.py | Matriz W — ponto fixo espectral |
| **Bound ρ₃ Quântico** | pi_radical/quantum_bound.py | Limite quântico ρ₃ |
| **HALE Demo** | demo/hale_demo.py | Demonstração interativa HALE |


## ðŸŒ VisÃ£o Geral / Overview

### PortuguÃªs

O **Hubstry HALE Ecosystem** Ã© o repositÃ³rio meta-framework que serve como hub central
de referÃªncia para todas as 4 publicaÃ§Ãµes acadÃªmicas e integra os 3 repositÃ³rios
especializados do ecossistema Hubstry. Este repositÃ³rio mapeia as contribuiÃ§Ãµes
de cada paper, estabelece a arquitetura de integraÃ§Ã£o e garante a conformidade
licenciosa entre os componentes.

### English

The **Hubstry HALE Ecosystem** is the meta-framework repository serving as the central
reference hub for all 4 academic publications and integrating the 3 specialized
repositories of the Hubstry ecosystem. This repository maps each paper contribution,
establishes the integration architecture, and ensures license compliance across components.

---

## ðŸ“„ Paper Mapping / Mapeamento de PublicaÃ§Ãµes

| Paper | DOI | License | Repo(s) | Integration Type |
|-------|-----|---------|---------|-----------------|
| HALE v3.0 Working Paper | [10.5281/zenodo.18901934](https://doi.org/10.5281/zenodo.18901934) | CC BY-NC-ND 4.0 | iot-protocol-hubstry, hale-ecosystem | Reference only |
| pi*sqrt+Q Quantum Computation | [10.5281/zenodo.18776462](https://doi.org/10.5281/zenodo.18776462) | CC BY 4.0 | qualia-hub-ecosystem, hubstry-security | Full adaptation |
| pi*sqrt Hexa-Relational Algebra | [10.5281/zenodo.18776401](https://doi.org/10.5281/zenodo.18776401) | CC BY 4.0 | qualia-hub-ecosystem | Full adaptation |
| HPG 1.0 Harmonic Protocol Grid | [10.5281/zenodo.19056387](https://doi.org/10.5281/zenodo.19056387) | CC BY 4.0 | iot-protocol-hubstry, hubstry-security | Full adaptation |

---

## ðŸ”— Cross-Linked Repositories / RepositÃ³rios Vinculados

| Repository | Description | Primary Papers |
|------------|-------------|----------------|
| [iot-protocol-hubstry](https://github.com/guilherme-machado-ceo/iot-protocol-hubstry) | IoT Harmonic Protocol implementation with post-quantum security | HALE v3.0, HPG 1.0 |
| [hubstry-security](https://github.com/guilherme-machado-ceo/hubstry-security) | Cybersecurity framework with harmonic signal layer | pi*sqrt+Q, HPG 1.0 |
| [qualia-hub-ecosystem](https://github.com/guilherme-machado-ceo/qualia-hub-ecosystem) | Qualia processing with hexa-relational algebra | pi*sqrt+Q, pi*sqrt Hex |

---

## ðŸ“œ License Compatibility Matrix

| Paper | License | Commercial Use | Modification | Distribution | Derivatives |
|-------|---------|----------------|--------------|--------------|-------------|
| HALE v3.0 | **CC BY-NC-ND 4.0** | âŒ Non-commercial only | âŒ No derivatives | âœ… With attribution | âŒ No derivatives allowed |
| pi*sqrt+Q | **CC BY 4.0** | âœ… Yes | âœ… Yes | âœ… With attribution | âœ… With same license |
| pi*sqrt Hex | **CC BY 4.0** | âœ… Yes | âœ… Yes | âœ… With attribution | âœ… With same license |
| HPG 1.0 | **CC BY 4.0** | âœ… Yes | âœ… Yes | âœ… With attribution | âœ… With same license |

> **Note**: Paper 1 (HALE v3.0) uses CC BY-NC-ND 4.0, meaning its content can only be
> **cited and referenced** â€” never modified or used as a basis for derivative works.
> Papers 2-4 use CC BY 4.0, allowing full adaptation and derivative works with attribution.

---

## ðŸ—ï¸ Ecosystem Architecture / Arquitetura do Ecossistema

```mermaid
graph TB
    subgraph MetaFramework ["hubstry-hale-ecosystem (This Repo)"]
        A[README.md<br/>Paper Mapping & Cross-links]
        B[docs/<br/>Architecture & Licensing]
        C[references/<br/>Bibliography]
        D[matrix/<br/>Dependency Graph]
    end

    subgraph Papers ["Academic Papers (Zenodo)"]
        P1[Paper 1: HALE v3.0<br/>CC BY-NC-ND 4.0]
        P2[Paper 2: pi*sqrt+Q<br/>CC BY 4.0]
        P3[Paper 3: pi*sqrt Hex<br/>CC BY 4.0]
        P4[Paper 4: HPG 1.0<br/>CC BY 4.0]
    end

    subgraph Repos ["Implementation Repositories"]
        R1[iot-protocol-hubstry<br/>IoT Harmonic Protocol]
        R2[hubstry-security<br/>Cybersecurity Framework]
        R3[qualia-hub-ecosystem<br/>Qualia Processing]
    end

    A --> P1
    A --> P2
    A --> P3
    A --> P4

    P1 -.->|Reference Only| R1
    P1 -.->|Reference Only| MetaFramework

    P2 -->|Full Adaptation| R2
    P2 -->|Full Adaptation| R3

    P3 -->|Full Adaptation| R3

    P4 -->|Full Adaptation| R1
    P4 -->|Full Adaptation| R2

    R1 <-->|HSL Protocol| R2
    R2 <-->|Qualia Layer| R3
    R3 <-->|Data Flow| R1

    style MetaFramework fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style P1 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style P2 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style P3 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style P4 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style R1 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style R2 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style R3 fill:#fff3e0,stroke:#e65100,stroke-width:2px
```

---

## ðŸ“‚ Repository Structure / Estrutura do RepositÃ³rio

```
hubstry-hale-ecosystem/
â”œâ”€â”€ README.md                          # This file - bilingual overview
â”œâ”€â”€ LICENSE                            # CC BY 4.0
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ paper-mapping.md               # Detailed paper-to-repo mapping
â”‚   â”œâ”€â”€ ecosystem-architecture.md      # Full architecture with diagrams
â”‚   â””â”€â”€ license-guide.md               # License compatibility guide
â”œâ”€â”€ references/
â”‚   â””â”€â”€ bibliography.bib               # BibTeX entries for all 4 DOIs
â””â”€â”€ matrix/
    â””â”€â”€ dependency_graph.py            # Dependency graph generator
```

---

## ðŸ§® Mathematical Foundations / Fundamentos MatemÃ¡ticos

The ecosystem is grounded in the **HALE (Harmonic Addressing & Labeling Equation)**
framework and its extensions:

- **HALE Core**: Harmonic signal processing for IoT addressing and labeling
- **pi*sqrt(f(A))**: Mathematical framework combining pi with square root of
  functional analysis applied to quantum computation
- **Hexa-Relational Algebra**: Six-dimensional relational algebra for qualia
  processing and knowledge representation
- **HPG (Harmonic Protocol Grid)**: Grid-based protocol architecture for
  harmonic communication in IoT networks

---

## ðŸ¤ ContribuiÃ§Ã£o / Contributing

This is an academic meta-framework repository. Contributions should follow
the license constraints of the referenced papers:

1. **Paper 1 (HALE v3.0)**: Can only be cited/referenced â€” no derivative works
2. **Papers 2-4**: Derivative works allowed with proper attribution under CC BY 4.0

See [docs/license-guide.md](docs/license-guide.md) for full details.

---

## ðŸ“– Citation / CitaÃ§Ã£o

When referencing this ecosystem, please cite all relevant papers:

```bibtex
@misc{hale-ecosystem-2025,
  author    = {Machado, Guilherme},
  title     = {{Hubstry HALE Ecosystem: Meta-Framework}},
  year      = {2025},
  publisher = {GitHub},
  url       = {https://github.com/guilherme-machado-ceo/hubstry-hale-ecosystem}
}
```

---

## ðŸ“‹ Badges

<p align="center">
  <img src="https://img.shields.io/badge/Papers-4-blue" alt="4 Papers"/>
  <img src="https://img.shields.io/badge/Repositories-3-orange" alt="3 Repos"/>
  <img src="https://img.shields.io/badge/License-CC%20BY%204.0-green" alt="CC BY 4.0"/>
  <img src="https://img.shields.io/badge/Status-Meta--Framework-purple" alt="Meta-Framework"/>
</p>

---

<p align="center">
  <strong>Hubstry HALE Ecosystem</strong><br/>
  <em>Harmonic Architecture for Linked Ecosystems</em><br/>
  <a href="https://github.com/guilherme-machado-ceo">guilherme-machado-ceo</a> | 2025
</p>