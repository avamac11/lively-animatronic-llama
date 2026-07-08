# Topological Mapping for AOPs

This directory contains organized artifacts for topological mapping of Adverse Outcome Pathways.

## Directory Structure

- **data/**: Analysis results and network data files
  - `liver_toxicity_analysis.json`: Analysis results for chemical-induced liver toxicity pathway
  - `carcinogenesis_analysis.json`: Analysis results for chemical-induced carcinogenesis pathway
- **scripts/**: Python scripts for creating and analyzing topological maps
  - `example_map.py`: Generates the liver toxicity AOP map
  - `carcinogenesis_map.py`: Generates the carcinogenesis AOP map
- **visualizations/**: Generated pathway visualizations
  - `liver_toxicity.png`: Visualization of chemical-induced liver toxicity pathway
  - `carcinogenesis.png`: Visualization of chemical-induced carcinogenesis pathway
- **documentation/**: Guides and reference materials
  - `guide.md`: Comprehensive guide to creating topological maps
  - `interpretation_guide.md`: Guide to interpreting topological map analysis
- **examples/**: Sample pathways and templates

## Quick Start

1. **View the guide**: `documentation/guide.md`
2. **Run an example**: 
   - For liver toxicity: `python scripts/example_map.py`
   - For carcinogenesis: `python scripts/carcinogenesis_map.py`
3. **View results**: Check `visualizations/` and `data/` directories

## Key Files

- `scripts/example_map.py`: Example topological mapping script
- `data/liver_toxicity_analysis.json`: Analysis results from example
- `visualizations/liver_toxicity.png`: Generated pathway visualization
- `scripts/carcinogenesis_map.py`: Example topological mapping script
- `data/carcinogenesis_analysis.json`: Analysis results from example
- `visualizations/carcinogenesis.png`: Generated pathway visualization
- `documentation/guide.md`: Comprehensive topological mapping guide
- `documentation/interpretation_guide.md`: Guide to interpreting topological map analysis

## Usage

```bash
# Run the example scripts
python scripts/example_map.py
python scripts/carcinogenesis_map.py

# View the generated visualizations
open visualizations/liver_toxicity.png
open visualizations/carcinogenesis.png

# Examine the analysis results
cat data/liver_toxicity_analysis.json
cat data/carcinogenesis_analysis.json
```

## Extending

To add your own AOP analysis:

1. Create a new script in `scripts/`
2. Save data files in `data/`
3. Store visualizations in `visualizations/`
4. Document your approach in `documentation/`

## Example Pathways

The repository includes example scripts that demonstrate the use of topological mapping to visualize and analyze complex biological pathways, identify critical nodes, and understand pathway connectivity.
