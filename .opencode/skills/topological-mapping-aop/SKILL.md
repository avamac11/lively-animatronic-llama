---
name: topological-mapping-aop
description: Tools and methods for creating topological maps of Adverse Outcome Pathway (AOP) networks
---

# Topological Mapping of AOP Pathways

## Description
This skill provides comprehensive tools and methods for creating topological maps of Adverse Outcome Pathway (AOP) networks. It enables visualization and analysis of complex biological pathways, identifying key nodes, critical pathways, and potential intervention points. This expanded version includes advanced features for temporal analysis, robustness assessment, and interactive visualization. ALWAYS use enhanced visualization capabilities to ensure maps are readable, well-formatted, and accessible.

## Capabilities
- **Pathway Analysis**: Analyze AOP networks to identify key biological nodes and pathways
- **Topological Mapping**: Create visual representations of AOP networks showing connections between molecular initiating events (MIEs), key events (KEs), and adverse outcomes (AOs)
- **Critical Path Identification**: Identify critical pathways that significantly contribute to adverse outcomes
- **Intervention Point Analysis**: Determine optimal intervention points to disrupt harmful pathways
- **Network Metrics**: Calculate network metrics such as betweenness centrality, degree centrality, and other topological properties
- **Temporal Analysis**: Analyze how AOP networks evolve over time using time series data
- **Robustness Assessment**: Evaluate network resilience to perturbations and identify vulnerable components
- **Interactive Visualization**: Generate interactive network visualizations for exploration and presentation

## **Every Map should include:**
- Clear labeling of nodes and edges with relevant biological information (e.g., KE1, KE2, AO1)
- Color coding for different types of nodes (MIEs, KEs, AOs) and edges (activation, inhibition)
- Node size proportional to centrality measures (degree, betweenness)
- Edge thickness proportional to confidence scores or interaction strength
- Labels for confidence and KE, MIE, AO, and Stressor.
- NO overlapping text or nodes; use text wrapping and node clustering to reduce clutter
- Use of force-directed or hierarchical layouts for better readability
- Any supplementary interactions that affect the AOP network (e.g., genetic polymorphisms, drug-drug interactions, electrolyte imbalances) should be represented as modulating nodes that influence edge strength or probability

## Use Cases
- Understanding complex biological pathways and their interactions
- Identifying key nodes that play critical roles in disease progression
- Visualizing AOP networks for research and presentation purposes
- Finding optimal intervention strategies for therapeutic development
- Analyzing robustness and sensitivity of biological networks
- Studying temporal dynamics of pathway activation and progression
- Creating interactive visualizations for educational and research purposes
- Integrating with AOP construction workflows to validate pathway structure
- Identifying critical pathways in AOPs constructed by other agents
- Finding intervention points in AOPs for drug development
- Validating biological plausibility of constructed AOPs through network analysis

## Implementation Details

### Core Components
1. **Graph Representation**: AOP pathways are represented as directed graphs where:
    - Nodes represent biological entities (genes, proteins, metabolites, etc.)
    - **Node Categories**: Nodes should be categorized by biological level (e.g., Molecular, Cellular, Organ, Organism) for visual grouping.
    - Edges represent relationships or interactions between entities
    - Edge weights represent confidence scores, interaction strengths, or potency (e.g., IC50).
    - **Modulating Nodes**: The graph should support non-linear nodes that act as "Modifiers" (e.g., Genetic Polymorphisms, Drug-Drug Interactions, Electrolyte Imbalances) which influence the strength or probability of an edge.
    - Temporal information can be incorporated for dynamic analysis
    - **ALWAYS** label edges and nodes with relevant biological information for clarity and KE1, KE2, AO1, etc.

2. **Algorithmic Analysis**:
   - Path finding algorithms to identify critical pathways
   - Centrality measures to identify key nodes
   - Network flow analysis to understand information propagation
   - Community detection to identify modular structures
   - Temporal analysis algorithms for dynamic networks
   - Robustness assessment algorithms for network resilience

3. **Visualization**:
    - Use text wrapping and node clustering to reduce clutter and ensure no information is lost in complex networks
   - Force-directed layouts for network visualization
   - Hierarchical layouts for pathway representation
   - Interactive visualizations with zoom and pan capabilities
   - Temporal visualization for dynamic networks

### Key Functions
- `create_topological_map(pathway_data)`: Create a topological map from pathway data
- `analyze_critical_paths(map)`: Identify critical pathways in the network
- `find_intervention_points(map)`: Find optimal intervention points
- `calculate_network_metrics(map)`: Calculate various network metrics
- `visualize_map(map, config=None)`: Generate visual representations of the map with customizable styling
- `visualize_enhanced(map, config=None)`: Create enhanced visualizations with advanced formatting options
- `visualize_interactive(map, config=None)`: Create interactive network visualizations with Plotly
- `visualize_temporal(map, time_series_data, config=None)`: Generate temporal visualizations and animations
- `visualize_3d(map, config=None)`: Create 3D visualizations for complex networks
- `analyze_temporal_dynamics(map, time_series_data)`: Analyze temporal evolution of the network
- `find_robustness_metrics(map)`: Assess network resilience to perturbations
- `validate_aop_structure(map)`: Validate AOP biological plausibility through network analysis
- `compare_networks(map1, map2)`: Compare two AOP networks for similarity
- `create_comprehensive_visualization(map, critical_paths, intervention_points)`: Create integrated visualization
- `identify_subnetworks(map)`: Identify modular components in complex networks
- `assess_robustness_with_sampling(map, sample_size)`: Efficient robustness assessment for large networks

### Enhanced Visualization API

The visualization system provides comprehensive customization options to create readable, accessible, and publication-quality topological maps:

#### Visualization Configuration Options

```python
# Comprehensive visualization configuration
vis_config = {
    # Layout options
    'layout': 'hierarchical',  # 'force_directed', 'circular', 'cluster'
    'layout_kwargs': {'scale': 2.0, 'center': (0, 0)},
    
    # Node styling
    'node_size_scale': 1000,  # Base size for nodes
    'node_size_min': 50,     # Minimum node size
    'node_size_max': 2000,   # Maximum node size
    'node_color_by': 'type', # 'type', 'degree', 'betweenness', 'closeness'
    'node_color_scheme': 'colorblind_friendly',  # 'viridis', 'plasma', 'cividis'
    'node_border_width': 1.5,
    'node_border_color': 'black',
    'node_alpha': 0.9,
    
    # Edge styling
    'edge_linewidth_scale': 2,  # Base edge thickness
    'edge_linewidth_min': 0.5,  # Minimum edge thickness
    'edge_linewidth_max': 5.0,  # Maximum edge thickness
    'edge_color_by': 'weight',  # 'type', 'weight', 'confidence'
    'edge_color_scheme': 'RdYlGn',  # Green-Red gradient
    'edge_alpha': 0.4,          # Edge transparency
    'edge_style': 'solid',      # 'solid', 'dashed', 'dotted'
    
    # Label options
    'show_labels': True,
    'label_fontsize': 10,
    'label_fontweight': 'normal',
    'label_color': 'black',
    'label_offset': 0.05,
    
    # Figure options
    'figsize': (16, 12),       # Figure dimensions
    'dpi': 300,                # Resolution
    'facecolor': 'white',      # Background color
    'edgecolor': 'white',      # Figure edge color
    
    # Title and legend
    'title': 'AOP Network Topology',
    'title_fontsize': 16,
    'title_fontweight': 'bold',
    'with_legend': True,
    'legend_fontsize': 9,
    'legend_loc': 'upper right',
    
    # Color mapping
    'color_mapping': {
        'MIE': 'red',
        'KE': 'blue',
        'AO': 'darkred',
        'intermediate': 'lightblue'
    },
    
    # Interactive options
    'interactive': False,      # Use Plotly for interactive
    'hover_info': ['name', 'type', 'degree', 'betweenness'],
    
    # Animation options (for temporal)
    'animation_speed': 'medium',  # 'slow', 'medium', 'fast'
    'frames': 10,
    'fps': 2,
    'output_format': 'gif'      # 'gif', 'mp4', 'html'
}

# Generate enhanced visualization
fig = topological_map.visualize_enhanced(config=vis_config)
```

#### Layout Algorithms

1. **Force-Directed**: Natural organization based on physical simulation
   - Best for: Small to medium networks with natural clustering
   - Parameters: `scale`, `k` (repulsion strength), `iterations`

2. **Hierarchical**: Organizes nodes by temporal progression
   - Best for: Pathways with clear temporal ordering
   - Parameters: `level_separation`, `node_distance`, `rank_separation`

3. **Circular**: Nodes arranged in a circle
   - Best for: Cyclic pathways and feedback loops
   - Parameters: `scale`, `rotation`

4. **Cluster-Based**: Groups related nodes together
   - Best for: Large networks with modular structure
   - Parameters: `cluster_algorithm`, `cluster_threshold`

#### Color Schemes

- **Colorblind-Friendly**: 'viridis', 'plasma', 'cividis', 'inferno'
- **High Contrast**: 'Set1', 'Set2', 'Set3'
- **Sequential**: 'Blues', 'Reds', 'Greens', 'Purples', 'Oranges'
- **Diverging**: 'RdYlGn', 'RdBu', 'Spectral'

#### Output Formats

- **Static Images**: PNG, PDF

#### Accessibility Features

- **Colorblind Mode**: Automatic detection and alternative palettes
- **High Contrast Mode**: Enhanced visibility for all elements
- **Screen Reader Support**: Alternative text descriptions
- **Responsive Design**: Adapts to different display sizes

#### Advanced Features

- **Edge Bundling**: Reduces clutter in dense networks
- **Node Clustering**: Groups related nodes automatically
- **Temporal Heatmaps**: Shows activation patterns over time
- **Subnetwork Extraction**: Focus on specific pathways
- **Comparative Visualization**: Side-by-side network comparison
- **Interactive Tooltips**: Detailed information on hover

### Visualization Improvements

The topological mapping skill provides enhanced visualization capabilities to make complex AOP networks more readable and better formatted:

#### 1. **Enhanced Layout Algorithms**
- **Force-Directed Layout**: Optimized for balanced node distribution, reducing overlaps
- **Hierarchical Layout**: Organizes nodes by temporal progression (MIE → KE → AO)
- **Circular Layout**: Useful for cyclic pathways and feedback loops
- **Cluster-Based Layout**: Groups related nodes together using community detection

#### 2. **Improved Node and Edge Styling**
- **Color Coding**: 
  - Molecular Initiating Events (MIEs): Red
  - Key Events (KEs): Blue
  - Adverse Outcomes (AOs): Dark Red
  - Intermediate nodes: Light Blue
- **Size Scaling**: Node size proportional to centrality measures (degree, betweenness)
- **Edge Thickness**: Weighted by confidence scores or interaction strength
- **Edge Colors**: Green for activation, Red for inhibition, Gray for unknown

#### 3. **Interactive Features**
- **Node Highlighting**: Click nodes to highlight their connections
- **Edge Filtering**: Toggle edges by weight/confidence threshold
- **Dynamic Zooming**: Smooth zoom and pan capabilities
- **Tooltip Information**: Hover over nodes/edges to see detailed information

#### 4. **Accessibility Enhancements**
- **Colorblind-Friendly Palettes**: Multiple color schemes for accessibility
- **Clear Labels**: Readable font sizes (10pt for nodes, 8pt for edge labels)
- **High Contrast**: Ensures visibility against backgrounds
- **Legend System**: Comprehensive legend explaining all visual elements

#### 5. **Advanced Visualization Options**
- **Temporal Heatmaps**: Show activation patterns over time
- **Subnetwork Extraction**: Focus on specific pathways while maintaining context
- **Comparative Visualization**: Side-by-side network comparison


#### 7. **Customization API**
```python
# Custom visualization configuration
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
    'legend_fontsize': 9,
    'interactive': True,
    'animation_speed': 'medium'
}

# Generate enhanced visualization
fig = topological_map.visualize_enhanced(config=vis_config)
```

#### 8. **Best Practices for Readable Visualizations**
- **For Small Networks**: Use force-directed layout with high detail
- **For Large Networks**: Use hierarchical or cluster-based layouts
- **For Temporal Analysis**: Use animation or heatmap overlays
- **For Presentations**: Use high-contrast color schemes and large fonts

These improvements ensure that topological maps are not only informative but also visually appealing and accessible to a wide range of users, from researchers to stakeholders without technical backgrounds.

## Example Usage

### Basic Usage

```python
# Load pathway data
pathway_data = load_aop_data("aspirin_aop.json")

# Create topological map
topological_map = create_topological_map(pathway_data)

# Analyze critical pathways
critical_paths = analyze_critical_paths(topological_map)

# Find intervention points
intervention_points = find_intervention_points(topological_map)

# Visualize the map
visualize_map(topological_map)

# Analyze temporal dynamics (if time series data available)
time_series = load_time_series_data("aspirin_timeline.csv")
temporal_results = topological_map.analyze_temporal_dynamics(time_series)

# Assess network robustness
robustness_metrics = topological_map.find_robustness_metrics()
```

### Integration with AOP Construction

```python
# Integration with aop-constructor workflow
from aop_constructor import AOPConstructor
from topological_mapping import TopologicalAnalyzer

# Step 1: Construct AOP using aop-constructor
aop_constructor = AOPConstructor()
molecule = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
result = aop_constructor.analyze_molecule(molecule)

# Step 2: Get AOP data from the result
aop_data = result.aop_structure

# Step 3: Create topological analyzer
topological_analyzer = TopologicalAnalyzer()

# Step 4: Create topological map from AOP data
topological_map = topological_analyzer.create_topological_map(aop_data)

# Step 5: Analyze the network
critical_paths = topological_analyzer.analyze_critical_paths(topological_map)
intervention_points = topological_analyzer.find_intervention_points(topological_map)
metrics = topological_analyzer.calculate_network_metrics(topological_map)

# Step 6: Validate AOP structure
validation = topological_analyzer.validate_aop_structure(topological_map)
if validation.is_valid:
    print("AOP structure is biologically plausible")
else:
    print(f"Validation issues: {validation.issues}")

# Step 7: Generate comprehensive visualization
visualization = topological_analyzer.create_comprehensive_visualization(
    topological_map,
    critical_paths,
    intervention_points
)
visualization.save("integrated_aop_analysis.png")
```

## Dependencies
- Python 3.8+
- NetworkX for graph operations
- Matplotlib or Plotly for visualization
- NumPy for numerical operations
- Pandas for data manipulation
- scikit-learn for machine learning algorithms (temporal analysis)
- RDKit for chemical structure handling (optional)

## Configuration
The skill can be configured through a configuration file that specifies:
- Default visualization parameters
- Thresholds for identifying critical pathways
- Weighting schemes for edge importance
- Output formats for visualization
- Temporal analysis parameters
- Robustness assessment settings
- Interactive visualization options

## Performance Considerations
- For large networks, consider using efficient graph algorithms
- Implement caching for frequently accessed network metrics
- Use incremental updates for dynamic networks
- Consider parallel processing for computationally intensive operations
- Optimize temporal analysis by using appropriate time windows
- Use sampling for robustness analysis on very large networks
- Consider memory-efficient data structures for complex visualizations
