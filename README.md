# Lightroom Preset Automation — Commercial Pipeline

> Python-based automation system for generating, packaging, and distributing commercial Adobe Lightroom Classic presets.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/license-proprietary-red.svg)](#license)
[![Presets: 49](https://img.shields.io/badge/presets-49-green.svg)](#collection-overview)

## Project Overview

This project demonstrates an **automation-first approach** to digital product creation — using Python to generate commercially packaged Adobe Lightroom Classic preset files (`.xmp`) from structured recipe definitions. The system eliminates manual preset creation, ensures metadata consistency, and produces distribution-ready ZIP packages.

**This is a commercial product.** The preset recipes (slider values, color grading, and tonal adjustments) are proprietary and not included in this repository. This repo showcases the **architecture, automation pipeline, and engineering approach** behind the product.

### Key Capabilities

- **Template-driven XMP generation** — Structured recipe data → valid Adobe XMP metadata files
- **Proper UUID generation** — Each preset receives a unique identifier per Adobe spec
- **Internal group tagging** — Lightroom Classic organizes by XMP metadata, not disk folders
- **Automated commercial packaging** — ZIP archives with READMEs for each sales tier
- **Universal camera compatibility** — AUTO lens correction, no manufacturer lock-in
- **Trademark-safe naming** — Descriptive names replacing branded film stock references

## Architecture

```
┌─────────────────────────────────────────────────┐
│              Recipe Definitions                   │
│  (Proprietary — not in repo)                     │
│  Structured dicts: name, group, settings, desc   │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│              XMP Template Engine                  │
│  • UUID generation (Adobe format)                │
│  • Namespace-compliant XML structure             │
│  • Color/Monochrome support flags                │
│  • Copyright and metadata embedding              │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│           Package Builder Pipeline               │
│  • 4 commercial packages (tiered pricing)        │
│  • Folder organization matching LrC groups       │
│  • README generation per package                 │
│  • ZIP archive creation for distribution         │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│         Distribution-Ready Output                │
│  Package_1_Film_Masters/          (11 presets)   │
│  Package_2_Workflow_Toolkit/      (27 presets)   │
│  Package_3_Creative_Styles/       (11 presets)   │
│  Package_4_Complete_Collection/   (49 presets)   │
│  + ZIP archives for each package                 │
└─────────────────────────────────────────────────┘
```

## Collection Overview

### 49 Professional Presets across 9 Categories

| Category | Count | Purpose |
|----------|-------|---------|
| Foundation | 3 | Universal lens correction (AUTO) |
| White Balance | 6 | Color temperature corrections |
| Exposure Recovery | 5 | Problem-solving for difficult exposures |
| Lighting Fixes | 4 | Situation-specific enhancements |
| Film Simulations | 4 | Classic color film emulations |
| Professional Styles | 11 | 2025-2026 trending creative looks |
| B&W Film Simulations | 7 | Monochrome film stock aesthetics |
| Sharpening | 6 | Output sharpening by use case |
| Noise Reduction | 3 | High-ISO cleanup tiers |

### Commercial Packages

| Package | Presets | Price | Target Market |
|---------|---------|-------|---------------|
| Film Masters Collection | 11 | $39-49 | Film photography enthusiasts |
| Professional Workflow Toolkit | 27 | $29-39 | Working professionals, event photographers |
| Modern Creative Styles | 11 | $39-49 | Wedding/portrait photographers, influencers |
| Complete Master Collection | 49 | $89-97 | All-in-one (30-40% savings) |

## Technical Details

### XMP File Format

Each preset is a valid Adobe XMP (Extensible Metadata Platform) file containing:

- **Namespace declarations** — `adobe:ns:meta/`, `camera-raw-settings/1.0/`
- **Preset metadata** — UUID, name, group, description, copyright
- **Compatibility flags** — Color/Monochrome support, HDR/SDR, Scene/Output referred
- **Processing parameters** — Exposure, tone, color, HSL adjustments, grain, sharpening

### Key Technical Decisions

| Decision | Rationale |
|----------|-----------|
| AUTO lens correction | Universal compatibility across all camera brands |
| Internal group tags | LrC ignores disk folders; uses XMP `<crs:Group>` for organization |
| No camera restrictions | `CameraModelRestriction=""` ensures any camera body works |
| ProcessVersion 15.4 | Current Adobe Camera Raw processing engine |
| Trademark-safe names | Descriptive alternatives to branded film stock names |

### Workflow Order

The preset collection follows a deliberate application order to prevent parameter conflicts:

```
1. Foundation (lens correction)
2. White Balance (color temperature)
3. Exposure Recovery (if needed)
4. Lighting Fixes (situation-specific)
5. Creative Style OR Film Simulation
6. Sharpening (output preparation)
7. Noise Reduction (if high ISO)
```

## Usage

```bash
# Generate all 4 packages
python generate_presets.py

# Generate specific package
python generate_presets.py --package 1    # Film Masters only

# Generate with ZIP archives for distribution
python generate_presets.py --zip

# Custom output directory
python generate_presets.py --output ./dist --zip
```

### Requirements

- Python 3.8+
- No external dependencies (stdlib only: `uuid`, `shutil`, `argparse`, `pathlib`)

## Project Structure

```
lightroom-preset-automation/
├── README.md                    # This file
├── generate_presets.py          # Main generator (recipes redacted)
├── docs/
│   ├── ARCHITECTURE.md          # Detailed technical design
│   ├── PRESET_GUIDE.md          # Collection overview and workflow
│   └── MARKETING_BRIEF.md       # Go-to-market summary
├── examples/
│   └── sample_output.xmp        # Example XMP structure (no recipes)
└── .github/
    └── FUNDING.yml              # Sponsorship links
```

## Engineering Highlights

This project demonstrates several transferable engineering patterns:

- **Template-driven code generation** — Applicable to infrastructure-as-code, config management, MLOps
- **Structured data → file output pipeline** — Similar patterns in CI/CD, deployment automation
- **Metadata engineering** — XML namespace compliance, UUID generation, schema validation
- **Commercial packaging automation** — Multi-tier product bundling, distribution-ready artifacts
- **Systematic debugging** — Resolved Adobe-specific metadata parsing behaviors through methodical investigation
- **Market-driven development** — Research-informed feature selection and competitive positioning

## About

Built by **[John Pritchard](https://github.com/jhpritch-dev)** — AI Infrastructure Engineer and photographer based in Gainesville, FL.

- 🌐 [theusefuldigital.com](https://theusefuldigital.com)
- 📸 Canon R5 / R7 shooter
- 🔧 Python, Docker, Ollama, self-hosted AI infrastructure

## License

**Proprietary** — The preset recipes, slider values, and commercial packaging are proprietary intellectual property of The Useful Digital. This repository is shared for portfolio demonstration purposes. The automation architecture and XMP template engine may be referenced for educational purposes.

© 2026 The Useful Digital. All rights reserved.
