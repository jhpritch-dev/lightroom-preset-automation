# Architecture — Lightroom Preset Generator

## System Design

### Overview

The generator follows a **three-stage pipeline** pattern:

1. **Recipe Definition** — Structured Python dictionaries define each preset's parameters
2. **Template Rendering** — The XMP engine interpolates recipes into valid Adobe XML
3. **Package Assembly** — Presets are grouped, documented, and archived for distribution

### Why Automation?

Manual preset creation in Lightroom Classic involves 15-30 minutes per preset of slider adjustment, naming, grouping, and export. For a 49-preset collection, that's **12-25 hours** of repetitive work with high error potential.

The automated approach:
- Generates all 49 presets in **under 2 seconds**
- Eliminates human error in slider values and metadata
- Enables rapid iteration — recipe change → regenerate → test
- Produces consistent, validated output every run

### XMP Template Engine

The core engine transforms a settings dictionary into a valid Adobe XMP file:

```python
# Recipe format (values redacted)
{
    "name": "Preset Name",
    "desc": "Human-readable description",
    "settings": {
        "Exposure2012": "...",
        "Contrast2012": "...",
        "Highlights2012": "...",
        # ... additional CRS parameters
    }
}
```

Key implementation details:

- **UUID Generation** — `uuid.uuid4().hex.upper()` produces Adobe-compatible identifiers
- **Namespace Compliance** — All parameters use the `crs:` (Camera Raw Settings) namespace
- **Support Flags** — B&W presets automatically set `SupportsColor="False"`
- **Sort Names** — Category prefix enables deterministic ordering in LrC UI
- **Copyright Embedding** — Embedded in each XMP file for IP protection

### Adobe Lightroom Classic Integration

A critical discovery during development: **LrC ignores disk folder structure entirely.** Preset organization is determined by the `<crs:Group>` XML element inside each XMP file. This means:

- Folder names on disk are irrelevant to LrC's UI
- Group names must be consistent across all presets in a category
- Renaming folders after generation has no effect on LrC organization

### Package Builder

Each commercial package is a function that composes category generators:

```
Package 1 (Film Masters):     color_film + bw_film
Package 2 (Workflow Toolkit):  foundation + wb + exposure + lighting + sharpening + noise
Package 3 (Creative Styles):   professional_styles
Package 4 (Complete Bundle):   ALL categories
```

The builder handles:
- Directory creation and cleanup
- README generation with installation instructions
- ZIP archive creation for platform upload
- Preset count validation against expected totals

### File Naming

Filenames are sanitized for cross-platform compatibility:
- Spaces → underscores
- Slashes → hyphens
- Ampersands → "and"
- Plus signs → "plus"
- Hash symbols → "num"

## Debugging History

### The Group Naming Problem

**Symptom:** Presets appeared duplicated or missing in Lightroom Classic.

**Root Cause:** Group names in XMP metadata didn't match between presets. LrC treated `"00 - Foundation"` and `"00_FOUNDATION"` as different groups, creating duplicates.

**Fix:** Standardized all group names to match the folder convention (`00_FOUNDATION`, `01_WHITE_BALANCE`, etc.) since LrC uses the internal group tag, not the folder name.

### The B&W Visibility Issue

**Symptom:** B&W film simulation presets didn't appear in LrC.

**Root Cause:** B&W presets had `SupportsColor="True"` and `SupportsMonochrome="True"`, which caused filtering issues in some LrC views.

**Fix:** B&W presets now set `SupportsColor="False"` when `ConvertToGrayscale="True"` is present.

### Camera-Specific → Universal

**Original:** Included Canon R5 and R7 specific base presets with manufacturer lens profiles.

**Problem:** Limited market to Canon users only (~25% of target market).

**Solution:** Removed camera-specific presets, switched to `LensProfileSetup="Auto"` and `EnableLensCorrections="2"` for universal compatibility. Reduced from 51 to 49 presets while expanding addressable market.

## Dependencies

- **Python 3.8+** (stdlib only)
- No pip packages required
- No build tools or compilation
- Runs on any OS with Python installed
