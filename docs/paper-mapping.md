# Paper Mapping - Detailed Contribution Matrix

> Detailed mapping of which paper contributes what to which repository,
> including algorithm inventory and license constraints per paper.

---

## ðŸ“‹ Paper-to-Repository Contribution Matrix

### Paper 1: HALE Working Paper v3.0

- **DOI**: [10.5281/zenodo.18901934](https://doi.org/10.5281/zenodo.18901934)
- **License**: CC BY-NC-ND 4.0 (No Derivatives)
- **Integration Type**: Reference Only

| Contribution | Target Repo | Constraint |
|-------------|-------------|------------|
| Harmonic Addressing concept | iot-protocol-hubstry | Cite only, no code derivation |
| Labeling Equation framework | hale-ecosystem (this repo) | Cite only, conceptual reference |
| IoT signal processing theory | iot-protocol-hubstry | Referenced in documentation only |
| HALE notation system | All repos | Used in documentation with citation |

**Algorithm Inventory (Paper 1)**:
| Algorithm | Description | Adaptable? |
|-----------|-------------|------------|
| HALE-SIG | Harmonic signal generation | âŒ No - reference only |
| HALE-ADDR | Address resolution via harmonics | âŒ No - reference only |
| HALE-LBL | Label assignment protocol | âŒ No - reference only |
| HALE-RES | Resource mapping | âŒ No - reference only |

---

### Paper 2: pi*sqrt(f(A)) + Quantum Computation

- **DOI**: [10.5281/zenodo.18776462](https://doi.org/10.5281/zenodo.18776462)
- **License**: CC BY 4.0 (Full Adaptation Allowed)
- **Integration Type**: Full Adaptation

| Contribution | Target Repo | Constraint |
|-------------|-------------|------------|
| pi*sqrt(f(A)) formulation | qualia-hub-ecosystem | Adapt with attribution |
| Quantum computation mapping | hubstry-security | Adapt with attribution |
| Functional analysis framework | qualia-hub-ecosystem | Adapt with attribution |
| Quantum-safe primitives | hubstry-security | Adapt with attribution |

**Algorithm Inventory (Paper 2)**:
| Algorithm | Description | Adaptable? |
|-----------|-------------|------------|
| PI-SQRT-CORE | Core pi*sqrt evaluation engine | âœ… Yes |
| QUANT-MAP | Quantum computation state mapping | âœ… Yes |
| FUNC-ANALYSIS | Functional analysis solver | âœ… Yes |
| QUANT-SAFE-KEY | Post-quantum key generation | âœ… Yes |
| HARMONIC-STATE | Harmonic quantum state representation | âœ… Yes |

---

### Paper 3: pi*sqrt(f(A)) Hexa-Relational Algebra

- **DOI**: [10.5281/zenodo.18776401](https://doi.org/10.5281/zenodo.18776401)
- **License**: CC BY 4.0 (Full Adaptation Allowed)
- **Integration Type**: Full Adaptation

| Contribution | Target Repo | Constraint |
|-------------|-------------|------------|
| Six-dimensional relational model | qualia-hub-ecosystem | Adapt with attribution |
| Hexa-relational operators | qualia-hub-ecosystem | Adapt with attribution |
| Qualia knowledge representation | qualia-hub-ecosystem | Adapt with attribution |
| Multi-dimensional data mapping | qualia-hub-ecosystem | Adapt with attribution |

**Algorithm Inventory (Paper 3)**:
| Algorithm | Description | Adaptable? |
|-----------|-------------|------------|
| HEX-REL-JOIN | Six-way relational join operation | âœ… Yes |
| HEX-PROJ | Hexa-dimensional projection | âœ… Yes |
| QUALIA-MAP | Qualia space mapping function | âœ… Yes |
| DIM-REDUCE | Dimensionality reduction (6D to 3D) | âœ… Yes |
| SEMANTIC-BIND | Semantic binding in qualia space | âœ… Yes |

---

### Paper 4: HPG 1.0 Harmonic Protocol Grid

- **DOI**: [10.5281/zenodo.19056387](https://doi.org/10.5281/zenodo.19056387)
- **License**: CC BY 4.0 (Full Adaptation Allowed)
- **Integration Type**: Full Adaptation

| Contribution | Target Repo | Constraint |
|-------------|-------------|------------|
| Grid-based protocol architecture | iot-protocol-hubstry | Adapt with attribution |
| Harmonic communication protocol | hubstry-security | Adapt with attribution |
| Protocol grid topology | iot-protocol-hubstry | Adapt with attribution |
| Inter-node harmonic routing | iot-protocol-hubstry | Adapt with attribution |
| Security overlay for grid | hubstry-security | Adapt with attribution |

**Algorithm Inventory (Paper 4)**:
| Algorithm | Description | Adaptable? |
|-----------|-------------|------------|
| HPG-GRID-INIT | Grid initialization and topology | âœ… Yes |
| HPG-HARMONIC-ROUTE | Harmonic-aware routing algorithm | âœ… Yes |
| HPG-SEC-OVERLAY | Security overlay protocol | âœ… Yes |
| HPG-NODE-REG | Node registration in grid | âœ… Yes |
| HPG-DISCOVERY | Service discovery via harmonics | âœ… Yes |
| HPG-FAILOVER | Grid failover mechanism | âœ… Yes |

---

## ðŸ“Š Cross-Repository Dependency Summary

```mermaid
graph LR
    subgraph Papers
        P1["P1: HALE v3.0<br/>(CC BY-NC-ND)"]
        P2["P2: pi*sqrt+Q<br/>(CC BY)"]
        P3["P3: pi*sqrt Hex<br/>(CC BY)"]
        P4["P4: HPG 1.0<br/>(CC BY)"]
    end

    subgraph Repos
        R1["iot-protocol"]
        R2["hubstry-security"]
        R3["qualia-hub"]
    end

    P1 -.->|"cite"| R1
    P1 -.->|"cite"| R3

    P2 ====>"adapt"| R2
    P2 ====>"adapt"| R3

    P3 ====>"adapt"| R3

    P4 ====>"adapt"| R1
    P4 ====>"adapt"| R2

    style P1 fill:#ffcdd2,stroke:#c62828
    style P2 fill:#bbdefb,stroke:#1565c0
    style P3 fill:#bbdefb,stroke:#1565c0
    style P4 fill:#bbdefb,stroke:#1565c0
```

---

## ðŸ”‘ License Constraints Summary

| Paper | Derivative Code Allowed | Commercial Use | Must Cite | Can Modify |
|-------|------------------------|----------------|-----------|------------|
| Paper 1 (HALE v3.0) | âŒ No | âŒ No (NC) | âœ… Yes | âŒ No (ND) |
| Paper 2 (pi*sqrt+Q) | âœ… Yes | âœ… Yes | âœ… Yes | âœ… Yes |
| Paper 3 (pi*sqrt Hex) | âœ… Yes | âœ… Yes | âœ… Yes | âœ… Yes |
| Paper 4 (HPG 1.0) | âœ… Yes | âœ… Yes | âœ… Yes | âœ… Yes |

> **Critical**: Any implementation derived from Paper 1 must be independently
> developed and only cite Paper 1 as inspiration. No code, algorithm, or
> mathematical formulation from Paper 1 may be directly reproduced or adapted.