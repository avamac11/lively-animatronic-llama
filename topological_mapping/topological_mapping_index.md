# Topological Mapping Index

## Quick Access

### Documentation
- [Main Guide](topological_mapping/documentation/guide.md)

### Scripts
- [Example Map](topological_mapping/scripts/example_map.py)

### Data


### Visualizations


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

## Example how to Use

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
