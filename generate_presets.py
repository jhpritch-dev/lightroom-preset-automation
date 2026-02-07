#!/usr/bin/env python3
"""
Lightroom Classic Preset Generator - Commercial Edition v3.0
============================================================
Generates 49 professional XMP preset files across 4 commercial packages.

NOTE: Recipe values (slider settings) have been redacted from this public
repository. This file demonstrates the generation architecture and XMP
template engine. The commercial product is available at theusefuldigital.com.

Author: The Useful Digital (theusefuldigital.com)
"""

import os
import sys
import uuid
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

VERSION = "3.0"
AUTHOR = "The Useful Digital"
COPYRIGHT = "© 2026 The Useful Digital - theusefuldigital.com"
BASE_OUTPUT = "Preset_Output"

# =============================================================================
# XMP TEMPLATE — Adobe Lightroom Classic compatible
# =============================================================================

XMP_TEMPLATE = """<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
   crs:PresetType="Normal"
   crs:Cluster=""
   crs:UUID="{uuid}"
   crs:SupportsAmount2="False"
   crs:SupportsAmount="False"
   crs:SupportsColor="{supports_color}"
   crs:SupportsMonochrome="{supports_mono}"
   crs:SupportsHighDynamicRange="True"
   crs:SupportsNormalDynamicRange="True"
   crs:SupportsSceneReferred="True"
   crs:SupportsOutputReferred="True"
   crs:RequiresRGBTables="False"
   crs:ShowInPresets="True"
   crs:ShowInQuickActions="False"
   crs:CameraModelRestriction=""
   crs:Copyright="{copyright}"
   crs:ContactInfo=""
   crs:Version="18.0"
   crs:ProcessVersion="15.4"
   crs:HasSettings="True"
   crs:CropConstrainToWarp="0"
{settings}>
   <crs:Name>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{name}</rdf:li>
    </rdf:Alt>
   </crs:Name>
   <crs:ShortName>
    <rdf:Alt>
     <rdf:li xml:lang="x-default"/>
    </rdf:Alt>
   </crs:ShortName>
   <crs:SortName>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{sort_name}</rdf:li>
    </rdf:Alt>
   </crs:SortName>
   <crs:Group>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{group}</rdf:li>
    </rdf:Alt>
   </crs:Group>
   <crs:Description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{description}</rdf:li>
    </rdf:Alt>
   </crs:Description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# =============================================================================
# CORE ENGINE
# =============================================================================

preset_counter = 0

def generate_uuid() -> str:
    """Generate UUID in Adobe's format."""
    return uuid.uuid4().hex.upper()

def create_xmp_settings(params: Dict) -> str:
    """Convert parameter dictionary to XMP attribute string."""
    lines = []
    for key, value in params.items():
        if value is not None:
            lines.append(f'   crs:{key}="{value}"')
    return '\n'.join(lines)

def save_preset(name: str, group: str, settings: Dict, description: str = "",
                folder: str = "output", sort_prefix: str = "") -> bool:
    """Save a single preset as an XMP file."""
    global preset_counter
    try:
        Path(folder).mkdir(parents=True, exist_ok=True)
        is_bw = settings.get("ConvertToGrayscale") == "True"
        supports_color = "False" if is_bw else "True"
        supports_mono = "True"
        sort_name = f"{sort_prefix}{name}" if sort_prefix else name

        xmp_content = XMP_TEMPLATE.format(
            uuid=generate_uuid(), name=name, group=group,
            settings=create_xmp_settings(settings), description=description,
            supports_color=supports_color, supports_mono=supports_mono,
            copyright=COPYRIGHT, sort_name=sort_name,
        )

        safe_name = (name.replace(' ', '_').replace('/', '-')
                        .replace('&', 'and').replace('+', 'plus')
                        .replace('#', 'num'))
        filepath = os.path.join(folder, f"{safe_name}.xmp")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(xmp_content)
        preset_counter += 1
        return True
    except Exception as e:
        print(f"  ✗ ERROR creating '{name}': {e}")
        return False

# =============================================================================
# RECIPE DEFINITIONS — REDACTED
# =============================================================================
#
# The full generator contains 49 preset recipes organized into 9 categories:
#
#   00_FOUNDATION (3)           — Universal AUTO lens correction
#   01_WHITE_BALANCE (6)        — Color temperature corrections
#   02_EXPOSURE_RECOVERY (5)    — Under/overexposure recovery
#   03_LIGHTING_FIXES (4)       — Situation-specific enhancements
#   04_FILM_SIMULATIONS (4)     — Color film emulations (trademark-safe)
#   05_PROFESSIONAL_STYLES (11) — 2025-2026 trending creative looks
#   06_BW_FILM_SIMULATIONS (7)  — Monochrome film aesthetics
#   07_SHARPENING (6)           — Output sharpening by use case
#   08_NOISE_REDUCTION (3)      — ISO-tiered noise cleanup
#
# Each recipe is a Python dictionary with CRS parameter keys and values.
# Example structure (values redacted):
#
#   {
#       "name": "Creamy Moody - Warm",
#       "desc": "#1 wedding trend 2025-2026",
#       "settings": {
#           "Exposure2012": "[REDACTED]",
#           "Contrast2012": "[REDACTED]",
#           "Highlights2012": "[REDACTED]",
#           "SaturationAdjustmentGreen": "[REDACTED]",
#           "ColorGradeMidtoneHue": "[REDACTED]",
#           "ColorGradeMidtoneSat": "[REDACTED]",
#           # ... additional parameters
#       }
#   }
#
# The commercial version is available at theusefuldigital.com
# =============================================================================

def main():
    print("=" * 60)
    print("  Lightroom Preset Generator v3.0 — Architecture Demo")
    print("  Recipe values redacted in this public version.")
    print("  Commercial product: theusefuldigital.com")
    print("=" * 60)
    print()
    print("This file demonstrates the XMP generation architecture.")
    print("See docs/ARCHITECTURE.md for full technical details.")

if __name__ == "__main__":
    main()
