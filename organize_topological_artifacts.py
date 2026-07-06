#!/usr/bin/env python3
"""
Organize Topological Mapping Artifacts

This script organizes all topological mapping files and artifacts into a structured
directory hierarchy for better management and documentation.
"""

import os
import shutil
import json
from pathlib import Path

def organize_artifacts():
    """Organize topological mapping artifacts into structured directories."""
    
    # Define the target directory structure
    base_dir = Path("topological_mapping")
    
    # Create directory structure
    directories = {
        "data": base_dir / "data",
        "scripts": base_dir / "scripts",
        "visualizations": base_dir / "visualizations",
        "documentation": base_dir / "documentation",
        "examples": base_dir / "examples"
    }
    
    # Create directories
    for dir_path in directories.values():
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Organize existing files
    files_to_organize = {
        "topological_mapping_for_AOPs.md": directories["documentation"] / "guide.md",
        "example_topological_map.py": directories["scripts"] / "example_map.py",
        "aop_analysis.json": directories["data"] / "liver_toxicity_analysis.json",
        "liver_toxicity_aop.png": directories["visualizations"] / "liver_toxicity.png"
    }
    
    # Move files
    for src, dst in files_to_organize.items():
        if Path(src).exists():
            shutil.move(src, dst)
            print(f"Moved {src} -> {dst}")
    
    # Create README for the topological mapping directory
    readme_content = """# Topological Mapping for AOPs

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
"""
    
    with open(base_dir / "README.md", "w") as f:
        f.write(readme_content)
    
    print(f"\nCreated README at {base_dir / 'README.md'}")
    
    # Create a summary of the organized files
    print("\n" + "="*60)
    print("ORGANIZATION SUMMARY")
    print("="*60)
    
    for dir_name, dir_path in directories.items():
        print(f"\n{dir_name.upper()}:")
        print(f"  Location: {dir_path}")
        
        # List contents
        contents = list(dir_path.glob("*"))
        if contents:
            print(f"  Contents ({len(contents)} items):")
            for item in contents:
                if item.is_file():
                    size = item.stat().st_size
                    print(f"    - {item.name} ({size} bytes)")
                else:
                    print(f"    - {item.name}/ (directory)")
        else:
            print("  (empty)")
    
    print("\n" + "="*60)
    print("ORGANIZATION COMPLETE")
    print("="*60)
    print(f"\nAll topological mapping artifacts are now organized in: {base_dir}")

def create_index_file():
    """Create an index file for quick reference."""
    
    index_content = """# Topological Mapping Index

## Quick Access

### Documentation
- [Main Guide](topological_mapping/documentation/guide.md)

### Scripts
- [Example Map](topological_mapping/scripts/example_map.py)

### Data
- [Liver Toxicity Analysis](topological_mapping/data/liver_toxicity_analysis.json)

### Visualizations
- [Liver Toxicity Pathway](topological_mapping/visualizations/liver_toxicity.png)

## Analysis Summary

### Liver Toxicity AOP
- **Nodes**: 7 (1 MIE, 5 KEs, 1 AO)
- **Edges**: 7
- **Critical Nodes**: KE1 (Oxidative Stress), KE4 (Inflammation), KE5 (Cell Death)
- **Pathways**: 2 distinct pathways from MIE to AO
- **Shortest Path**: MIE → KE1 → KE3 → KE4 → KE5 → AO

### Centrality Measures
- **Highest Degree**: KE1, KE4 (0.500)
- **Highest Betweenness**: KE4 (0.267)
- **Highest Closeness**: KE4 (0.381)

## How to Use

```bash
# Navigate to the topological mapping directory
cd topological_mapping

# Run the example
python scripts/example_map.py

# View the visualization
open visualizations/liver_toxicity.png

# Examine the data
cat data/liver_toxicity_analysis.json
```

## Next Steps

1. **Create your own AOP**: Copy the example script and modify for your pathway
2. **Analyze results**: Use the centrality measures to identify critical nodes
3. **Visualize**: Generate custom visualizations for your pathway
4. **Document**: Add your findings to the documentation directory
"""
    
    with open("topological_mapping_index.md", "w") as f:
        f.write(index_content)
    
    print(f"\nCreated index file: topological_mapping_index.md")

if __name__ == "__main__":
    print("Organizing topological mapping artifacts...")
    organize_artifacts()
    create_index_file()
    print("\nDone!")