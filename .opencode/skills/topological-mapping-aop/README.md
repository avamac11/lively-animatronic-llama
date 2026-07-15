# Topological Mapping of AOP Pathways Skill

This skill provides comprehensive tools for creating and analyzing topological maps of Adverse Outcome Pathway (AOP) networks.

## Overview

The topological mapping skill enables visualization and analysis of complex biological pathways, helping to identify key nodes, critical pathways, and potential intervention points in AOP networks. This expanded version includes advanced features for network analysis, dynamic pathway modeling, and integration with chemical informatics.

## Installation

To use this skill, ensure you have the required dependencies installed:

```bash
pip install networkx matplotlib numpy pandas scikit-learn
```

For chemical structure handling (optional):

```bash
pip install rdkit
```

For advanced temporal analysis (optional):

```bash
pip install pandas numpy
```

## Configuration

The skill can be configured through configuration files or parameters:

```python
config = {
    # Visualization settings
    'layout': 'force_directed',
    'node_size': 500,
    'edge_alpha': 0.3,
    'figsize': (12, 10),
    'interactive': True,
    
    # Analysis settings
    'critical_path_threshold': 0.8,
    'centrality_metric': 'betweenness',
    'max_path_length': 10,
    'temporal_window': 5,
    
    # Output settings
    'output_format': 'png',
    'dpi': 300,
    'save_path': 'output/pathway_map.png',
    'include_timestamps': True
}
```

## API Reference

### Core Functions

#### `create_topological_map(pathway_data, config=None)`
Create a topological map from pathway data.

**Parameters:**
- `pathway_data`: Dictionary or object containing pathway information
- `config`: Optional configuration dictionary

**Returns:**
- TopologicalMap object representing the AOP network

#### `analyze_critical_paths(topological_map, metric='betweenness', config=None)`
Identify critical pathways in the network.

**Parameters:**
- `topological_map`: TopologicalMap object
- `metric`: Centrality metric to use ('betweenness', 'degree', 'closeness', 'eigenvector')
- `config`: Optional configuration dictionary

**Returns:**
- List of critical pathways sorted by importance

#### `find_intervention_points(topological_map, config=None)`
Find optimal intervention points in the network.

**Parameters:**
- `topological_map`: TopologicalMap object
- `config`: Optional configuration dictionary

**Returns:**
- List of intervention points with importance scores

#### `calculate_network_metrics(topological_map, include=None, config=None)`
Calculate various network metrics.

**Parameters:**
- `topological_map`: TopologicalMap object
- `include`: List of metrics to calculate (degree, betweenness, closeness, eigenvector, etc.)
- `config`: Optional configuration dictionary

**Returns:**
- Dictionary of network metrics

#### `visualize_map(topological_map, config=None)`
Generate visual representations of the topological map.

**Parameters:**
- `topological_map`: TopologicalMap object
- `config`: Optional configuration dictionary

**Returns:**
- Matplotlib figure object

#### `analyze_temporal_dynamics(topological_map, time_series_data, config=None)`
Analyze temporal dynamics of the AOP network.

**Parameters:**
- `topological_map`: TopologicalMap object
- `time_series_data`: Time series data for temporal analysis
- `config`: Optional configuration dictionary

**Returns:**
- Temporal analysis results

#### `find_robustness_metrics(topological_map, config=None)`
Calculate robustness metrics for the network.

**Parameters:**
- `topological_map`: TopologicalMap object
- `config`: Optional configuration dictionary

**Returns:**
- Dictionary of robustness metrics

## Data Formats

The skill supports various data formats for AOP pathways:

### JSON Format
```json
{
    "nodes": [
        {
            "id": "MIE1",
            "type": "molecular_initiating_event",
            "name": "Chemical Exposure",
            "description": "Initial chemical exposure",
            "timepoint": 0
        },
        {
            "id": "KE1",
            "type": "key_event",
            "name": "Protein Activation",
            "description": "Activation of target protein",
            "timepoint": 1
        }
    ],
    "edges": [
        {
            "source": "MIE1",
            "target": "KE1",
            "weight": 0.95,
            "confidence": "high",
            "type": "activation",
            "temporal_weight": 1.0
        }
    ]
}
```

### CSV Format
Nodes and edges can be provided as separate CSV files with columns:
- Nodes: id, type, name, description, timepoint (optional)
- Edges: source, target, weight, confidence, type, temporal_weight (optional)

## Troubleshooting

### Common Issues

1. **Graph Connectivity Errors**: Ensure your pathway data forms a connected graph
2. **Visualization Errors**: Check that matplotlib is properly installed
3. **Missing Data**: Verify all required fields are present in your data
4. **Performance Issues**: For large networks, consider reducing the number of metrics calculated
5. **Temporal Analysis Errors**: Ensure time series data is properly formatted
6. **Robustness Analysis Errors**: Verify network has sufficient connectivity for robustness metrics

### Debugging Tips

- Use `validate_pathway_data()` to check data integrity
- Set `debug=True` in configuration for verbose output
- Check network metrics to understand graph properties
- Visualize subgraphs to isolate issues
- Use `analyze_subnetwork()` for focused analysis on specific pathways
- Check temporal alignment with `validate_time_series()`

## How to Analyze and Interact with Topological Maps

### Basic Analysis Workflow

1. **Load and Create the Map**
   ```python
   # Load your AOP data
   pathway_data = load_aop_data("your_pathway.json")
   
   # Create topological map
   topological_map = create_topological_map(pathway_data)
   ```

2. **Explore Network Properties**
   ```python
   # Get basic network statistics
   print(f"Number of nodes: {topological_map.number_of_nodes()}")
   print(f"Number of edges: {topological_map.number_of_edges()}")
   
   # Check connectivity
   print(f"Is connected: {topological_map.is_connected()}")
   ```

3. **Analyze Critical Pathways**
   ```python
   # Identify critical pathways
   critical_paths = analyze_critical_paths(topological_map)
   
   # Display top 5 critical paths
   for i, path in enumerate(critical_paths[:5], 1):
       print(f"Path {i}: {path}")
   ```

4. **Find Intervention Points**
   ```python
   # Find optimal intervention points
   intervention_points = find_intervention_points(topological_map)
   
   # Display intervention points sorted by importance
   for point, score in sorted(intervention_points.items(), key=lambda x: x[1], reverse=True):
       print(f"{point}: Importance score = {score:.2f}")
   ```

### Interactive Exploration

#### Using Matplotlib Visualizations
```python
# Create basic visualization with enhanced styling
fig, ax = visualize_map(topological_map, 
                       layout='hierarchical',
                       color_scheme='colorblind_friendly')

# Customize the plot with improved readability
plt.title("AOP Network Topology", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Save the visualization with high resolution
fig.savefig("aop_network.png", dpi=300, bbox_inches='tight')
```

#### Using Interactive Visualizations
```python
# Generate interactive plot with Plotly (enhanced)
fig = topological_map.visualize_interactive(
    layout='force_directed',
    node_size=800,
    show_labels=True,
    color_by='betweenness',
    color_scheme='viridis',
    edge_alpha=0.3,
    hover_info=['name', 'type', 'degree', 'betweenness']
)

# Show the interactive plot with tooltips
fig.show()

# Save as HTML for sharing with improved styling
fig.write_html("interactive_aop_network.html")
```

#### Advanced Visualization Options
```python
# Create enhanced visualization with custom styling
vis_config = {
    'layout': 'hierarchical',
    'node_size_scale': 1000,
    'edge_alpha': 0.4,
    'figsize': (16, 12),
    'dpi': 300,
    'color_scheme': 'colorblind_friendly',
    'show_labels': True,
    'label_fontsize': 10,
    'node_border_width': 1.5,
    'edge_linewidth_scale': 2,
    'with_legend': True,
    'legend_fontsize': 9
}

# Generate enhanced visualization
fig = topological_map.visualize_enhanced(config=vis_config)

# Add comprehensive legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='MIE', 
               markerfacecolor='red', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='KE', 
               markerfacecolor='blue', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='AO', 
               markerfacecolor='darkred', markersize=10)
]
fig.legend(handles=legend_elements, loc='upper right')

plt.title("Enhanced AOP Network Visualization", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### Temporal Visualization
```python
# Visualize temporal dynamics with animation
animation_config = {
    'frames': 10,
    'animation_speed': 'medium',
    'color_scheme': 'plasma',
    'show_progress': True,
    'output_format': 'gif',
    'fps': 2
}

# Generate animated visualization showing pathway progression
temporal_fig = topological_map.visualize_temporal(
    time_series_data,
    config=animation_config
)

# Save animation
temporal_fig.save("aop_temporal_animation.gif", writer='pillow')
```

#### 3D Visualization for Complex Networks
```python
# Create 3D visualization for complex networks
fig_3d = topological_map.visualize_3d(
    layout='force_directed',
    node_size=500,
    color_by='degree',
    elevation=30,
    azimuth=45
)

# Show 3D plot with interactive controls
fig_3d.show()

# Save 3D visualization
fig_3d.write_html("aop_3d_network.html")
```

### Advanced Analysis Techniques

#### Temporal Analysis
Analyze how AOP networks evolve over time:

```python
# Load time series data
time_series = load_time_series_data("pathway_timeline.csv")

# Analyze temporal dynamics
temporal_results = topological_map.analyze_temporal_dynamics(time_series)

# Get dynamic metrics
dynamic_metrics = temporal_results.get_dynamic_metrics()
print(f"Temporal dynamics: {dynamic_metrics}")

# Visualize temporal evolution
visualize_temporal_evolution(topological_map, time_series)
```

#### Robustness Analysis
Assess network resilience to perturbations:

```python
# Calculate robustness metrics
robustness_metrics = topological_map.find_robustness_metrics()

# Display robustness scores
print(f"Resilience score: {robustness_metrics.resilience_score:.2f}")
print(f"Vulnerability index: {robustness_metrics.vulnerability_index:.2f}")

# Simulate node removal to test network resilience
perturbation_results = topological_map.simulate_perturbations(
    nodes_to_remove=["KE1", "KE2"],
    iterations=100
)

# Get resilience score
resilience_score = perturbation_results.get_resilience_score()
print(f"Resilience after perturbation: {resilience_score:.2f}")
```

#### Network Metrics Analysis
```python
# Calculate comprehensive network metrics
metrics = calculate_network_metrics(topological_map, 
                                   include=['degree', 'betweenness', 'closeness', 'eigenvector'])

# Display degree centrality
print("Degree centrality:")
for node, degree in sorted(metrics['degree'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {node}: {degree:.2f}")

# Display betweenness centrality
print("\nBetweenness centrality:")
for node, betweenness in sorted(metrics['betweenness'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {node}: {betweenness:.2f}")
```

### Practical Use Cases

#### Use Case 1: Drug Target Identification
```python
# Find nodes with high betweenness centrality (potential drug targets)
high_betweenness_nodes = [node for node, score in metrics['betweenness'].items() 
                         if score > 0.5]

print(f"Potential drug targets: {high_betweenness_nodes}")
```

#### Use Case 2: Pathway Comparison
```python
# Compare two different AOP networks
pathway1 = create_topological_map(data1)
pathway2 = create_topological_map(data2)

# Calculate similarity
similarity_score = topological_map.compare_networks(pathway1, pathway2)
print(f"Network similarity: {similarity_score:.2f}")
```

#### Use Case 3: Critical Path Analysis
```python
# Get the most critical path
most_critical_path = critical_paths[0]

# Visualize just this critical path
critical_path_subgraph = topological_map.get_subgraph(most_critical_path)
visualize_map(critical_path_subgraph, title="Most Critical Path")
```

### Tips for Effective Analysis

1. **Start with Visual Exploration**: Always visualize your network first to understand its structure
2. **Use Multiple Metrics**: Combine different centrality measures for comprehensive analysis
3. **Focus on Critical Paths**: Prioritize analysis of the most critical pathways
4. **Test Robustness**: Assess how the network responds to perturbations
5. **Consider Temporal Dynamics**: If time series data is available, analyze how the network evolves
6. **Validate Findings**: Cross-check computational results with biological knowledge
7. **Iterate**: Refine your analysis based on initial findings and questions that arise

## Visualization Best Practices and Formatting

### Creating Readable Topological Maps

#### 1. **Choose the Right Layout**
- **Small networks (≤50 nodes)**: Force-directed layout for natural organization
- **Medium networks (50-200 nodes)**: Hierarchical layout for temporal clarity
- **Large networks (>200 nodes)**: Cluster-based layout to reduce complexity
- **Cyclic pathways**: Circular layout to show feedback loops

#### 2. **Optimize Node and Edge Styling**
- **Node Size**: Scale by importance (degree, betweenness centrality)
- **Node Color**: Use consistent color coding:
  - Red: Molecular Initiating Events (MIEs)
  - Blue: Key Events (KEs)
  - Dark Red: Adverse Outcomes (AOs)
  - Light Blue: Intermediate nodes
- **Edge Thickness**: Proportional to confidence/weight (0.5-3.0 range)
- **Edge Color**: 
  - Green: Activation
  - Red: Inhibition
  - Gray: Unknown interaction type

#### 3. **Improve Readability**
- **Font Sizes**: 
  - Node labels: 10pt (minimum 8pt)
  - Edge labels: 8pt
  - Titles: 14-16pt bold
  - Legends: 9pt
- **Spacing**: 
  - Node padding: 0.1-0.3
  - Edge alpha: 0.3-0.5 for reduced clutter
- **Aspect Ratio**: Use 16:9 or 4:3 for presentations, square for publications

#### 4. **Add Contextual Information**
- **Legends**: Always include explaining colors, shapes, and sizes
- **Annotations**: Add text boxes for key insights
- **Scale Bars**: For spatial relationships in 3D visualizations
- **Timelines**: For temporal visualizations

#### 5. **Accessibility Considerations**
- **Colorblind-Friendly Palettes**: Use 'viridis', 'plasma', or 'cividis'
- **High Contrast**: Ensure text is readable on backgrounds
- **Alternative Text**: Include descriptions for screen readers
- **Simplified Versions**: Provide reduced-complexity versions for clarity

#### 6. **Output Quality**
- **Resolution**: 300 DPI for print, 150 DPI for web
- **File Formats**: 
  - SVG: For scalable vector graphics (best for publications)
  - PNG: For raster images with transparency
  - PDF: For high-quality print output
  - HTML: For interactive web visualizations
- **Dimensions**: 
  - Presentation: 16" × 12" (16:9 aspect ratio)
  - Publication: 8" × 6" (4:3 aspect ratio)
  - Thumbnail: 400 × 300 pixels

#### 7. **Customization Examples**

**Basic Readable Visualization:**
```python
fig = visualize_map(topological_map, 
                   layout='hierarchical',
                   color_scheme='colorblind_friendly',
                   node_size_scale=800,
                   edge_alpha=0.4,
                   figsize=(12, 10),
                   dpi=300)
```

**Presentation-Ready Visualization:**
```python
presentation_config = {
    'layout': 'hierarchical',
    'node_size_scale': 1200,
    'edge_alpha': 0.3,
    'figsize': (16, 12),
    'dpi': 150,
    'color_scheme': 'high_contrast',
    'show_labels': True,
    'label_fontsize': 11,
    'title': 'AOP Network Analysis',
    'title_fontsize': 16,
    'with_legend': True,
    'legend_fontsize': 10
}

fig = topological_map.visualize_enhanced(config=presentation_config)
```

**Publication-Quality Visualization:**
```python
publication_config = {
    'layout': 'hierarchical',
    'node_size_scale': 600,
    'edge_alpha': 0.5,
    'figsize': (8, 6),
    'dpi': 300,
    'color_scheme': 'colorblind_friendly',
    'show_labels': True,
    'label_fontsize': 9,
    'title': 'Adverse Outcome Pathway Network',
    'title_fontsize': 12,
    'with_legend': True,
    'legend_fontsize': 8,
    'font_family': 'Arial',
    'edge_linewidth_scale': 1.5
}

fig = topological_map.visualize_enhanced(config=publication_config)
fig.savefig('aop_network_publication.svg', format='svg', bbox_inches='tight')
```

### Troubleshooting Visualization Issues

**Problem: Overlapping Nodes**
- Solution: Use hierarchical or cluster-based layout
- Alternative: Increase node spacing with `node_spacing=0.5`

**Problem: Unreadable Labels**
- Solution: Reduce node density or use smaller font
- Alternative: Show labels only on hover in interactive mode

**Problem: Cluttered Edges**
- Solution: Reduce edge alpha (`edge_alpha=0.3`) or filter by weight
- Alternative: Use edge bundling for dense connections

**Problem: Color Confusion**
- Solution: Use colorblind-friendly palette
- Alternative: Add patterns or shapes to differentiate

**Problem: Large Network Performance**
- Solution: Use cluster-based layout and focus on subnetworks
- Alternative: Reduce number of nodes/edges displayed

## Integration with AOP Construction

This skill is designed to integrate seamlessly with the aop-constructor agent and other AOP-related agents. Here's how to use it in a complete workflow:

### Integration Workflow

1. **AOP Construction**: Use the aop-expert agent to build the AOP structure
2. **Topological Analysis**: Use this skill to analyze the network properties
3. **Intervention Identification**: Find optimal intervention points
4. **Validation**: Validate the biological plausibility of the AOP
5. **Visualization**: Create comprehensive visualizations

### Example Integration

```python
# Import required agents and skills
from aop_constructor import AOPConstructor
from topological_mapping import TopologicalAnalyzer

# Step 1: Construct AOP
aop_constructor = AOPConstructor()
result = aop_constructor.analyze_molecule("CC(=O)OC1=CC=CC=C1C(=O)O")

# Step 2: Get AOP data
aop_data = result.aop_structure

# Step 3: Create topological analyzer
topological_analyzer = TopologicalAnalyzer()

# Step 4: Analyze network properties
topological_map = topological_analyzer.create_topological_map(aop_data)
critical_paths = topological_analyzer.analyze_critical_paths(topological_map)
intervention_points = topological_analyzer.find_intervention_points(topological_map)

# Step 5: Validate and visualize
validation = topological_analyzer.validate_aop_structure(topological_map)
visualization = topological_analyzer.create_comprehensive_visualization(
    topological_map, critical_paths, intervention_points
)

# Step 6: Return integrated results
integrated_result = {
    'aop_structure': aop_data,
    'topological_analysis': {
        'critical_paths': critical_paths,
        'intervention_points': intervention_points,
        'validation': validation,
        'visualization': visualization
    }
}
```

### Agent Coordination

When used as part of the aop-constructor agent, this skill provides:

- **Network Validation**: Ensures constructed AOPs have biologically plausible structures
- **Critical Path Identification**: Highlights the most important pathways in the AOP
- **Intervention Strategy**: Identifies optimal points for therapeutic intervention
- **Comprehensive Visualization**: Creates integrated visualizations combining biological and topological information

### Best Practices for Integration

1. **Sequential Analysis**: Follow molecule → ADMET → MIE → AOP → Topology progression
2. **Iterative Refinement**: Use topological insights to refine AOP construction
3. **Multi-Metric Validation**: Combine biological evidence with network metrics
4. **Visual Exploration**: Always generate visualizations to aid understanding
5. **Error Cross-Checking**: Use topological analysis to validate biological consistency

## License

This skill is licensed under the MIT License. See LICENSE.txt for details

## Support

For issues and questions, please refer to the main project documentation or open an issue in the repository.
