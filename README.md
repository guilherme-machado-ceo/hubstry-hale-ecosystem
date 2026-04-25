# Hubstry HALE Ecosystem
Meta-Framework | Ecossistema Integrado de Pesquisa e Desenvolvimento

Central hub that unifies 4 academic papers and cross-links 3 specialized repositories under the Hubstry Harmonic framework.

**License:** CC BY 4.0 | **DOI:** [Zenodo](https://zenodo.org)

---

## Visão Geral / Overview

**Português**
O Hubstry HALE Ecosystem é o repositório meta-framework que serve como hub central de referência para todas as 4 publicações acadêmicas e integra os 3 repositórios especializados do ecossistema Hubstry. Este repositório mapeia as contribuições de cada paper, estabelece a arquitetura de integração e garante a conformidade licenciosa entre os componentes.

**English**
The Hubstry HALE Ecosystem is the meta-framework repository serving as the central reference hub for all 4 academic publications and integrating the 3 specialized repositories of the Hubstry ecosystem. This repository maps each paper contribution, establishes the integration architecture, and ensures license compliance across components.

## Incrementos / Latest Implementations

| Módulo | Arquivo | Descrição |
|--------|---------|-----------|
| **HALE Pipeline** | hale_core/hale_equation.py | Pipeline: f0 - H - h - psi - c - M - g |
| **Funções psi1-psi4** | hale_core/psi_functions.py | 4 funções de endereçamento selecionáveis |
| **Omnigrid 2D** | hpg_core/omnigrid.py | Grade O_N = H_N x {-1,+1} com Euler |
| **HPM 1.0** | hpg_core/hpm_config.py | 12 canais harmônicos (f0=16.384 kHz) |
| **Sinal s(t) + FFT** | hpg_core/signal_processing.py | Sinal composto + decodificação FFT |
| **Verificação Espectral** | hpg_core/spectral_verification.py | Integridade de razões racionais |
| **HSL Auth** | security/hsl_auth.py | H-Challenge/Response 3 etapas (~200B) |
| **Detecção de Intrusão** | security/intrusion_detection.py | Desvio de fase delta_phi > epsilon |
| **Rotação LFSR** | security/key_rotation.py | Rotação de chaves via LFSR |
| **pi-Radical Operator** | pi_radical/pi_radical.py | Operador pi-radical - 6 relações rho |
| **Lattice 64 Perfis** | pi_radical/lattice_profiles.py | Lattice de 64 perfis harmônicos |
| **W Matrix Fixed-Point** | pi_radical/w_matrix.py | Matriz W - ponto fixo espectral |
| **Bound rho3 Quântico** | pi_radical/quantum_bound.py | Limite quântico rho3 |
| **HALE Demo** | demo/hale_demo.py | Demonstração interativa HALE |

## Paper Mapping / Mapeamento de Publicações

| Paper | DOI | License | Repo(s) | Integration Type |
|-------|-----|---------|---------|-----------------|
| HALE v3.0 Working Paper | 10.5281/zenodo.18901934 | CC BY-NC-ND 4.0 | iot-protocol-hubstry, hale-ecosystem | Reference only |
| pi*sqrt+Q Quantum Computation | 10.5281/zenodo.18776462 | CC BY 4.0 | qualia-hub-ecosystem, hubstry-security | Full adaptation |
| pi*sqrt Hexa-Relational Algebra | 10.5281/zenodo.18776401 | CC BY 4.0 | qualia-hub-ecosystem | Full adaptation |
| HPG 1.0 Harmonic Protocol Grid | 10.5281/zenodo.19056387 | CC BY 4.0 | iot-protocol-hubstry, hubstry-security | Full adaptation |

## Cross-Linked Repositories / Repositórios Vinculados

| Repository | Description | Primary Papers |
|-----------|-------------|---------------|
| iot-protocol-hubstry | IoT Harmonic Protocol implementation with post-quantum security | HALE v3.0, HPG 1.0 |
| hubstry-security | Cybersecurity framework with harmonic signal layer | pi*sqrt+Q, HPG 1.0 |
| qualia-hub-ecosystem | Qualia processing with hexa-relational algebra | pi*sqrt+Q, pi*sqrt Hex |

## License Compatibility Matrix

| Paper | License | Commercial Use | Modification | Distribution | Derivatives |
|-------|---------|---------------|-------------|-------------|------------|
| HALE v3.0 | CC BY-NC-ND 4.0 | Non-commercial only | No derivatives | With attribution | No derivatives allowed |
| pi*sqrt+Q | CC BY 4.0 | Yes | Yes | With attribution | With same license |
| pi*sqrt Hex | CC BY 4.0 | Yes | Yes | With attribution | With same license |
| HPG 1.0 | CC BY 4.0 | Yes | Yes | With attribution | With same license |

> **Note:** Paper 1 (HALE v3.0) uses CC BY-NC-ND 4.0, meaning its content can only be cited and referenced -- never modified or used as a basis for derivative works. Papers 2-4 use CC BY 4.0, allowing full adaptation and derivative works with attribution.

## Ecosystem Architecture / Arquitetura do Ecossistema

### Repository Structure / Estrutura do Repositório


## Mathematical Foundations / Fundamentos Matemáticos

- **HALE Core:** Harmonic signal processing for IoT addressing and labeling
- **pi*sqrt(f(A)):** Mathematical framework combining pi with square root of functional analysis applied to quantum computation
- **Hexa-Relational Algebra:** Six-dimensional relational algebra for qualia processing and knowledge representation
- **HPG (Harmonic Protocol Grid):** Grid-based protocol architecture for harmonic communication in IoT networks

## Contribuição / Contributing

- Paper 1 (HALE v3.0): Can only be cited/referenced -- no derivative works
- Papers 2-4: Derivative works allowed with proper attribution under CC BY 4.0

## Citation / Citação

```bibtex
@misc{hale-ecosystem-2025,
  author    = {Machado, Guilherme},
  title     = {{Hubstry HALE Ecosystem: Meta-Framework}},
  year      = {2025},
  publisher = {GitHub},
  url       = {https://github.com/guilherme-machado-ceo/hubstry-hale-ecosystem}
}
```
