# AOP Constructor Integration with Topological Mapping

This document demonstrates how the aop-constructor agent integrates the admet-mie, aop-expert, and topological-mapping-aop agents to create comprehensive AOP analyses.

## Integration Workflow

### 1. Input Analysis Phase
The process begins with molecule input and initial analysis:

```python
# User provides a molecule (e.g., aspirin)
molecule = "CC(=O)OC1=CC=CC=C1C(=O)O"

# aop-constructor accepts the molecule and initiates the workflow
aop_constructor.analyze_molecule(molecule)
```

### 2. ADMET and MIE Analysis Phase
The admet-mie agent analyzes the molecule's properties:

```python
# admet-mie analyzes ADMET properties
admet_results = admet_mie.analyze_admet(molecule)

# admet-mie identifies potential molecular initiating events
mies = admet_mie.identify_mies(admet_results)

# Results returned to aop-constructor:
# - ADMET profile (absorption, distribution, metabolism, excretion, toxicity)
# - Potential MIEs with confidence scores
# - Molecular descriptors and properties
```

### 3. AOP Construction Phase
The aop-expert agent builds the AOP based on MIEs:

```python
# aop-expert constructs AOP from MIEs
aop_data = aop_expert.construct_aop(mies)

# Results returned to aop-constructor:
# - Complete AOP with key events (KEs)
# - Relationships between events
# - Confidence levels for each connection
# - Biological context and references
```

### 4. Topological Analysis Phase
The topological-mapping-aop agent analyzes the AOP network:

```python
# topological-mapping-aop creates topological map
topological_map = topological_mapping.create_topological_map(aop_data)

# Analyze critical pathways
critical_paths = topological_mapping.analyze_critical_paths(topological_map)

# Find intervention points
intervention_points = topological_mapping.find_intervention_points(topological_map)

# Calculate network metrics
metrics = topological_mapping.calculate_network_metrics(topological_map)

# Visualize the network
visualization = topological_mapping.visualize_map(topological_map)

# Results returned to aop-constructor:
# - Network visualization
# - Critical pathways ranked by importance
# - Optimal intervention points with scores
# - Network metrics (centrality, connectivity, etc.)
# - Robustness analysis
```

### 5. Integration and Output Phase
The aop-constructor combines all results:

```python
# aop-constructor integrates all analyses
final_analysis = aop_constructor.integrate_results(
    molecule_info=molecule_data,
    admet_results=admet_results,
    aop_structure=aop_data,
    topological_analysis=topological_results
)

# Final output includes:
# 1. Molecule information and properties
# 2. ADMET profile and toxicity assessment
# 3. Complete AOP with key events and relationships
# 4. Topological map visualization
# 5. Critical pathways analysis
# 6. Intervention points with biological significance
# 7. Network metrics and robustness assessment
# 8. Confidence levels for each component
```

## Complete Example: Aspirin AOP Analysis

```python
# Step 1: Initialize the aop-constructor with molecule
aop_constructor = AOPConstructor()
molecule = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
result = aop_constructor.analyze_molecule(molecule)

# Step 2: ADMET and MIE analysis (handled internally by admet-mie)
admet_results = result.admet_analysis
print(f"ADMET Profile: {admet_results.profile}")
print(f"Potential MIEs: {admet_results.molecular_initiating_events}")

# Step 3: AOP construction (handled internally by aop-expert)
aop_structure = result.aop_structure
print(f"AOP Key Events: {[ke.name for ke in aop_structure.key_events]}")

# Step 4: Topological analysis (handled internally by topological-mapping-aop)
topological_analysis = result.topological_analysis
print(f"Critical Paths: {topological_analysis.critical_paths[:3]}")
print(f"Top Intervention Points: {topological_analysis.intervention_points[:3]}")

# Step 5: View the integrated results
print("=== COMPLETE AOP ANALYSIS ===")
print(f"Molecule: {result.molecule_info.name}")
print(f"Adverse Outcome: {result.aop_structure.adverse_outcome}")
print(f"Most Critical Path: {topological_analysis.critical_paths[0]}")
print(f"Best Intervention Point: {topological_analysis.intervention_points[0]}")

# Save visualization
result.topological_analysis.visualization.save("aspirin_aop_network.png")
```

## Integration Benefits

### 1. Enhanced Pathway Understanding
- Topological mapping provides visual representation of complex AOP networks
- Identifies key nodes and critical pathways that might be overlooked in linear analysis
- Reveals network structure and connectivity patterns

### 2. Improved Intervention Strategy
- Network analysis identifies optimal intervention points based on centrality metrics
- Critical path analysis shows which pathways have the greatest impact on adverse outcomes
- Robustness analysis helps identify resilient intervention targets

### 3. Quality Validation
- Topological analysis validates biological plausibility of constructed AOPs
- Network metrics help identify inconsistencies or gaps in pathway structure
- Connectivity analysis ensures logical flow from MIE to adverse outcome

### 4. Comprehensive Output
- Integrated visualization combines biological knowledge with network analysis
- Multi-dimensional analysis (biological + topological) provides deeper insights
- Confidence scores incorporate both biological evidence and network properties

## Advanced Integration Example

```python
# Analyze temporal dynamics of AOP
time_series_data = load_temporal_data("aspirin_timeline.csv")
temporal_results = topological_mapping.analyze_temporal_dynamics(
    topological_map,
    time_series_data
)

# Assess network robustness
robustness_metrics = topological_mapping.find_robustness_metrics(topological_map)

# Compare with alternative pathways
alternative_aop = aop_expert.get_alternative_aop(mies[0])
alternative_map = topological_mapping.create_topological_map(alternative_aop)
similarity = topological_mapping.compare_networks(topological_map, alternative_map)

# Integrated output
print(f"Temporal Evolution: {temporal_results.summary}")
print(f"Network Resilience: {robustness_metrics.resilience_score:.2f}")
print(f"Alternative Pathway Similarity: {similarity:.2f}")
```

## Error Handling and Validation

The integration includes comprehensive validation:

```python
# Validate AOP structure
validation = aop_constructor.validate_aop(result.aop_structure)
if not validation.is_valid:
    print(f"Validation issues: {validation.issues}")
    
    # Use topological analysis to identify problems
    connectivity_issues = topological_mapping.check_connectivity(topological_map)
    if connectivity_issues:
        print(f"Connectivity problems: {connectivity_issues}")
        
    # Suggest corrections
    suggestions = aop_constructor.suggest_corrections(validation.issues)
    print(f"Suggested fixes: {suggestions}")
```

## Performance Considerations

For large or complex AOPs:

```python
# Use incremental analysis for large networks
large_aop = load_large_aop("complex_pathway.json")

# Analyze subnetworks first
subnetworks = topological_mapping.identify_subnetworks(large_aop)
for subnetwork in subnetworks:
    subnetwork_analysis = topological_mapping.analyze_subnetwork(subnetwork)
    
# Combine results
full_analysis = topological_mapping.combine_subnetwork_analyses(subnetwork_analyses)

# Use sampling for robustness analysis
robustness = topological_mapping.assess_robustness_with_sampling(
    large_aop,
    sample_size=1000
)
```

## Best Practices for Integration

1. **Sequential Analysis**: Follow the natural progression from molecule → ADMET → MIE → AOP → Topology
2. **Iterative Refinement**: Use topological insights to refine AOP construction
3. **Multi-Metric Validation**: Combine biological evidence with network metrics for validation
4. **Visual Exploration**: Always generate visualizations to aid understanding
5. **Confidence Integration**: Incorporate confidence from all sources (ADMET, biological data, network analysis)
6. **Error Cross-Checking**: Use topological analysis to validate biological consistency
7. **Intervention Prioritization**: Use network centrality to prioritize intervention points

This integrated approach provides a comprehensive, multi-dimensional analysis of AOPs that leverages the strengths of each specialized agent while ensuring biological plausibility and practical applicability.