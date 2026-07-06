# Topological Mapping for AOPs

This directory contains organized artifacts for topological mapping of Adverse Outcome Pathways.

## Directory Structure

- **data/**: Analysis results and network data files
- **scripts/**: Python scripts for creating and analyzing topological maps
- **visualizations/**: Generated pathway visualizations
- **documentation/**: Guides and reference materials
- **examples/**: Sample pathways and templates

## Quick Start

1. **View the guide**: `documentation/guide.md`
2. **Run an example**: `python scripts/example_map.py`
3. **View results**: Check `visualizations/` and `data/` directories

## Key Files

- `scripts/example_map.py`: Example topological mapping script
- `documentation/guide.md`: Comprehensive topological mapping guide
- `data/liver_toxicity_analysis.json`: Analysis results from example
- `visualizations/liver_toxicity.png`: Generated pathway visualization

## Usage

```bash
# Run the example script
python scripts/example_map.py

# View the generated visualization
open visualizations/liver_toxicity.png

# Examine the analysis results
cat data/liver_toxicity_analysis.json
```

## Extending

To add your own AOP analysis:

1. Create a new script in `scripts/`
2. Save data files in `data/`
3. Store visualizations in `visualizations/`
4. Document your approach in `documentation/`
