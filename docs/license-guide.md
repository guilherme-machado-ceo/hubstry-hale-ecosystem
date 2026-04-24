# License Compatibility Guide

> Comprehensive guide explaining the licensing constraints across all papers
> in the Hubstry HALE Ecosystem and what can be derived versus cited.

---

## âš–ï¸ License Overview

The Hubstry HALE Ecosystem references four academic papers with **two different
Creative Commons licenses**. Understanding these differences is critical for
compliance.

---

## ðŸ“œ The Two Licenses

### CC BY-NC-ND 4.0 (Creative Commons Attribution-NonCommercial-NoDerivatives)

**Applied to**: Paper 1 â€” HALE Working Paper v3.0
**DOI**: [10.5281/zenodo.18901934](https://doi.org/10.5281/zenodo.18901934)

#### What you CAN do:
- âœ… **Share** â€” copy and redistribute the material in any medium or format
- âœ… **Adapt** â€” remix, transform, and build upon the material (for personal use only)

#### What you MUST do:
- ðŸ“Œ **Attribution** â€” give appropriate credit, provide a link to the license, and indicate if changes were made
- ðŸ“Œ **No additional restrictions** â€” not apply legal terms that restrict others from doing anything the license permits

#### What you CANNOT do:
- âŒ **NonCommercial (NC)** â€” not use the material for commercial purposes
- âŒ **NoDerivatives (ND)** â€” not distribute modified versions of the material

#### Practical Implications for This Ecosystem:
| Action | Allowed? | Notes |
|--------|----------|-------|
| Cite the paper in documentation | âœ… Yes | Must include full citation |
| Reference concepts in README | âœ… Yes | Must attribute the source |
| Implement algorithms from the paper | âš ï¸ Risky | Original algorithms cannot be derived; implement independently |
| Copy code snippets from the paper | âŒ No | No derivatives allowed |
| Use in a commercial product | âŒ No | Non-commercial only |
| Translate the paper | âŒ No | Translation is a derivative |
| Create a summary of the paper | âš ï¸ Gray area | Brief citations are OK; extended summaries may be derivatives |

---

### CC BY 4.0 (Creative Commons Attribution)

**Applied to**: Papers 2, 3, and 4
- Paper 2: [10.5281/zenodo.18776462](https://doi.org/10.5281/zenodo.18776462)
- Paper 3: [10.5281/zenodo.18776401](https://doi.org/10.5281/zenodo.18776401)
- Paper 4: [10.5281/zenodo.19056387](https://doi.org/10.5281/zenodo.19056387)

#### What you CAN do:
- âœ… **Share** â€” copy and redistribute the material in any medium or format
- âœ… **Adapt** â€” remix, transform, and build upon the material for any purpose, including commercially

#### What you MUST do:
- ðŸ“Œ **Attribution** â€” give appropriate credit, provide a link to the license, and indicate if changes were made

#### What you CANNOT do:
- âŒ No additional legal restrictions beyond CC BY 4.0

#### Practical Implications for This Ecosystem:
| Action | Allowed? | Notes |
|--------|----------|-------|
| Implement algorithms in code | âœ… Yes | Must attribute the paper |
| Create derivative software | âœ… Yes | Must attribute the paper |
| Use in commercial products | âœ… Yes | Must attribute the paper |
| Modify and redistribute | âœ… Yes | Must indicate changes and attribute |
| Copy code snippets | âœ… Yes | With attribution |

---

## ðŸ”€ License Compatibility Matrix

### Can Paper A content be combined with Paper B content?

| | Paper 1 (BY-NC-ND) | Paper 2 (BY) | Paper 3 (BY) | Paper 4 (BY) |
|---|---|---|---|---|
| **Paper 1 (BY-NC-ND)** | ðŸ”´ Same | ðŸŸ¡ Limited | ðŸŸ¡ Limited | ðŸŸ¡ Limited |
| **Paper 2 (BY)** | ðŸŸ¡ Limited | ðŸŸ¢ Full | ðŸŸ¢ Full | ðŸŸ¢ Full |
| **Paper 3 (BY)** | ðŸŸ¡ Limited | ðŸŸ¢ Full | ðŸŸ¢ Full | ðŸŸ¢ Full |
| **Paper 4 (BY)** | ðŸŸ¡ Limited | ðŸŸ¢ Full | ðŸŸ¢ Full | ðŸŸ¢ Full |

**Legend**:
- ðŸŸ¢ **Full**: Both sides allow full adaptation and commercial use
- ðŸŸ¡ **Limited**: Paper 1 cannot be modified; can only be cited alongside BY content
- ðŸ”´ **Same**: Same license, same constraints

---

## ðŸ—ï¸ Repository License Strategy

### Per-Repository License Compliance

#### iot-protocol-hubstry
| Paper | License | How It Is Used | Compliance |
|-------|---------|----------------|------------|
| Paper 1 (HALE v3.0) | CC BY-NC-ND 4.0 | Cited in docs as theoretical basis | âœ… Compliant |
| Paper 4 (HPG 1.0) | CC BY 4.0 | Algorithms adapted into code | âœ… Compliant |

**Strategy**: Paper 1 concepts are cited only. All implementable code derives from
Paper 4 (CC BY 4.0). No code is derived from Paper 1.

#### hubstry-security
| Paper | License | How It Is Used | Compliance |
|-------|---------|----------------|------------|
| Paper 2 (pi*sqrt+Q) | CC BY 4.0 | Quantum-safe algorithms adapted | âœ… Compliant |
| Paper 4 (HPG 1.0) | CC BY 4.0 | Grid security overlay adapted | âœ… Compliant |

**Strategy**: All implementations derive from Papers 2 and 4, both CC BY 4.0.
Full adaptation is permitted with attribution.

#### qualia-hub-ecosystem
| Paper | License | How It Is Used | Compliance |
|-------|---------|----------------|------------|
| Paper 2 (pi*sqrt+Q) | CC BY 4.0 | Mathematical framework adapted | âœ… Compliant |
| Paper 3 (pi*sqrt Hex) | CC BY 4.0 | Hexa-relational algebra adapted | âœ… Compliant |

**Strategy**: All implementations derive from Papers 2 and 3, both CC BY 4.0.
Full adaptation is permitted with attribution.

---

## ðŸ“ Proper Attribution Format

### For CC BY 4.0 Papers (Papers 2, 3, 4):

When adapting code or algorithms from these papers, include:

```
Based on: [Paper Title]
Author: [Author Name]
DOI: [DOI]
License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
Original source: [URL]
```

### For CC BY-NC-ND 4.0 Paper (Paper 1):

When citing Paper 1 concepts:

```
The theoretical framework is inspired by:
[Paper Title]
Author: [Author Name]
DOI: 10.5281/zenodo.18901934
License: CC BY-NC-ND 4.0 (https://creativecommons.org/licenses/by-nc-nd/4.0/)
Note: This work is independently developed and not derived from the referenced paper.
```

---

## âš ï¸ Common Pitfalls to Avoid

1. **Copying algorithms from Paper 1 into code** â€” This violates the NoDerivatives clause.
   Instead, cite the paper as inspiration and implement independently.

2. **Using Paper 1 content in commercial products** â€” This violates the NonCommercial clause.
   Paper 1 can only be referenced in non-commercial contexts.

3. **Failing to attribute Papers 2-4** â€” CC BY 4.0 requires attribution for any use.
   Always include DOI and license reference.

4. **Assuming all papers have the same license** â€” Paper 1 has significantly more
   restrictive terms than Papers 2-4.

5. **Creating modified translations of Paper 1** â€” Translations are considered
   derivatives and are not allowed under CC BY-NC-ND 4.0.

---

## ðŸ”„ License Upgrade Path

If the author of Paper 1 (HALE v3.0) chooses to relicense under CC BY 4.0 in
a future version, the ecosystem would gain:

- âœ… Ability to directly adapt HALE algorithms into code
- âœ… Commercial use of Paper 1 content
- âœ… Full integration parity across all 4 papers

Until such a change occurs, Paper 1 remains **reference-only** across the ecosystem.

---

## ðŸ“š References

- [Creative Commons BY-NC-ND 4.0 Full Text](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)
- [Creative Commons BY 4.0 Full Text](https://creativecommons.org/licenses/by/4.0/legalcode)
- [CC License Compatibility Chart](https://creativecommons.org/compatibility/)
- [Zenodo DOI Registration](https://zenodo.org/)