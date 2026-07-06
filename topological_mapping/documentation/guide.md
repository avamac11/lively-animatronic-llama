# Topological Mapping for Adverse Outcome Pathways (AOPs)

## Overview
Topological mapping is a powerful approach for visualizing and analyzing Adverse Outcome Pathways (AOPs). This method helps researchers understand the complex relationships between Molecular Initiating Events (MIEs), Key Events (KEs), and Adverse Outcomes (AOs) in a structured way.

## What is Topological Mapping?
Topological mapping represents AOPs as directed graphs where:
- **Nodes** represent Key Events (KEs), Molecular Initiating Events (MIEs), or Adverse Outcomes (AOs)
- **Edges** represent relationships or dependencies between events
- **Directionality** indicates the flow from cause to effect
- **Node Attributes**: Biological entities with metadata (name, description, type)
- **Edge Attributes**: Relationship characteristics (weight, evidence strength, type)

## Key Components of a Topological Map

### Node Types
1. **Molecular Initiating Event (MIE)**: The starting point of the pathway
2. **Key Events (KEs)**: Intermediate biological events
3. **Adverse Outcome (AO)**: The final endpoint or effect

### Edge Types
1. **Causal Relationships**: Direct cause-effect connections
2. **Regulatory Relationships**: Modulatory or feedback connections
3. **Temporal Relationships**: Time-dependent connections
4. **Conditional Relationships**: Context-dependent connections

## Benefits of Topological Mapping
1. **Visual Clarity**: Provides an intuitive representation of complex pathways
2. **Network Analysis**: Enables identification of critical nodes and bottlenecks
3. **Pathway Comparison**: Facilitates comparison between different AOPs
4. **Data Integration**: Allows incorporation of multiple data types and sources
5. **Predictive Modeling**: Supports development of predictive models for risk assessment

## Steps to Create a Topological Map for AOPs

### 1. Define the AOP Structure
- **Identify the Molecular Initiating Event (MIE)**: The initial chemical or biological interaction
- **List all Key Events (KEs) in sequence**: Intermediate biological events
- **Define the Adverse Outcome (AO)**: The final observable effect
- **Document node attributes**: Name, description, biological context, and metadata

### 2. Represent as a Graph
```
MIE → KE1 → KE2 → ... → KEn → AO
```

### 3. Add Relationship Details
For each connection, document:
- **Type of relationship**: Causal, regulatory, temporal, or conditional
- **Strength of evidence**: Strong, moderate, weak, or uncertain
- **Temporal relationships**: Time delays, sequence constraints
- **Quantitative data**: Weight values, confidence intervals
- **Biological context**: Species, tissue, experimental conditions

### 4. Organize the Visualization
- **Node organization**: Group related events spatially
- **Color coding**: Use consistent colors for node types (MIE, KE, AO)
- **Edge styling**: Different line styles for relationship types
- **Labels**: Clear, descriptive text for nodes and edges

### 5. Analyze the Topology
- **Identify critical nodes**: Highly connected KEs using centrality measures
- **Find alternative pathways**: Multiple routes from MIE to AO
- **Detect feedback loops**: Cyclic relationships in the network
- **Calculate shortest paths**: Optimal routes from MIE to AO
- **Identify bottlenecks**: Nodes with high betweenness centrality

## Tools for Topological Mapping

### Software Options
1. **Cytoscape**: Open-source platform for visualizing complex networks with advanced layout algorithms
2. **Gephi**: Graph visualization and analysis software with interactive features
3. **R/Bioconductor**: Packages like `igraph` and `visNetwork` for statistical analysis
4. **Python Libraries**: NetworkX, igraph, matplotlib, plotly, and seaborn
5. **Pathvisio**: Pathway visualization and editing tool with biological databases

### Python Implementation (Recommended)

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
graph = nx.DiGraph()

# Define nodes with attributes
nodes = {
    'MIE': {'type': 'MIE', 'name': 'Chemical Exposure', 'description': 'Initial chemical interaction'},
    'KE1': {'type': 'KE', 'name': 'Oxidative Stress', 'description': 'Production of reactive oxygen species'},
    'KE2': {'type': 'KE', 'name': 'DNA Damage', 'description': 'Genetic material alteration'},
    'KE3': {'type': 'KE', 'name': 'Cell Cycle Arrest', 'description': 'Disruption of cell division'},
    'AO': {'type': 'AO', 'name': 'Carcinogenesis', 'description': 'Cancer development'}
}

# Add nodes with attributes
graph.add_nodes_from(nodes)

# Define edges with comprehensive attributes
edges = [
    ('MIE', 'KE1', {
        'weight': 0.95,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Chemical metabolism produces reactive oxygen species'
    }),
    ('KE1', 'KE2', {
        'weight': 0.85,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Oxidative stress causes DNA damage'
    }),
    ('KE2', 'KE3', {
        'weight': 0.75,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'DNA damage triggers cell cycle arrest'
    }),
    ('KE3', 'AO', {
        'weight': 0.90,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Prolonged cell cycle arrest leads to carcinogenesis'
    })
]

graph.add_edges_from(edges)

# Visualize with enhanced formatting
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(graph, seed=42, k=0.5)

# Color nodes by type
node_colors = {'MIE': 'lightgreen', 'KE': 'skyblue', 'AO': 'salmon'}
colors = [node_colors[nodes[node]['type']] for node in graph.nodes()]

# Draw nodes with labels
labels = {node: f"{nodes[node]['name']}" for node in graph.nodes()}
nx.draw_networkx_nodes(graph, pos, node_size=3000, node_color=colors, alpha=0.9)
nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10, font_weight='bold')

# Draw edges with different styles based on type
edge_types = nx.get_edge_attributes(graph, 'type')
for edge, edge_type in edge_types.items():
    if edge_type == 'causal':
        nx.draw_networkx_edges(graph, pos, edgelist=[edge], width=2, 
                              arrowstyle='->', arrowsize=20, edge_color='gray')

# Add edge labels with weight and evidence
edge_info = {edge: f"w={data['weight']}\nev={data['evidence']}" 
             for edge, data in graph.edges.items()}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_info, font_size=8)

# Add title and legend
plt.title('Enhanced Topological Map of Adverse Outcome Pathway', 
          fontsize=14, fontweight='bold', pad=20)

# Create legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='MIE', 
               markerfacecolor='lightgreen', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Key Event', 
               markerfacecolor='skyblue', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Adverse Outcome', 
               markerfacecolor='salmon', markersize=10)
]
plt.legend(handles=legend_elements, loc='upper right')

plt.axis('off')
plt.tight_layout()
plt.savefig('enhanced_aop_map.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Advanced Topological Analysis

### Centrality Measures
- **Degree Centrality**: Number of connections per node (identifies hubs)
- **Betweenness Centrality**: Importance as a bridge between nodes (identifies bottlenecks)
- **Closeness Centrality**: Proximity to other nodes (identifies central nodes)
- **Eigenvector Centrality**: Influence based on connections to other influential nodes

### Path Analysis
- **Shortest path identification**: Find optimal routes from MIE to AO
- **All-paths enumeration**: List all possible pathways
- **Critical path analysis**: Identify essential pathways
- **Path length distribution**: Analyze pathway complexity

### Community Detection
- **Identify modules**: Group related events into functional units
- **Understand pathway organization**: Reveal hierarchical structure
- **Find functional clusters**: Group nodes with similar functions

### Network Metrics
- **Density**: Measure of network connectivity
- **Transitivity**: Tendency to form clusters
- **Reciprocity**: Measure of bidirectional relationships
- **Assortativity**: Preference for nodes to connect with similar nodes

### Temporal Analysis
- **Dynamic network analysis**: Track changes over time
- **Time-dependent centrality**: Identify evolving critical nodes
- **Temporal pathways**: Analyze time-critical routes

## Best Practices for Clear Topological Maps

### Visual Design Principles
1. **Consistent Color Coding**: Use the same colors for node types throughout
2. **Clear Labeling**: Ensure all nodes and edges have descriptive labels
3. **Appropriate Spacing**: Avoid overcrowding nodes
4. **Directional Clarity**: Use arrows to clearly show directionality
5. **Hierarchical Layout**: Organize nodes from MIE to AO in a logical flow

### Data Organization
1. **Comprehensive Metadata**: Document all node and edge attributes
2. **Standardized Naming**: Use consistent naming conventions
3. **Evidence Documentation**: Clearly record evidence strength for each relationship
4. **Version Control**: Maintain versions as knowledge evolves
5. **Interoperability**: Use standard formats (SBML, BioPAX) for data exchange

### Analysis Workflow
1. **Start Simple**: Begin with basic pathway structure
2. **Add Complexity Gradually**: Incorporate additional details as needed
3. **Validate Regularly**: Cross-check with experimental data
4. **Iterate**: Refine based on new evidence
5. **Document Changes**: Keep track of modifications and rationale

## Best Practices

1. **Standardization**: Use consistent naming conventions for nodes
2. **Evidence Documentation**: Clearly document evidence strength for each relationship
3. **Version Control**: Maintain versions of topological maps as knowledge evolves
4. **Integration**: Combine with other data types (genomics, proteomics, etc.)
5. **Validation**: Cross-validate with experimental data
6. **Interoperability**: Use standard formats (SBML, BioPAX) for data exchange

## Applications

1. **Risk Assessment**: Identify critical points for intervention and mitigation
2. **Toxicology**: Understand mechanisms of toxicity and chemical interactions
3. **Drug Development**: Identify potential off-target effects and safety concerns
4. **Regulatory Science**: Support evidence-based decision making and policy development
5. **Epidemiology**: Model disease progression pathways and identify intervention points
6. **Systems Biology**: Integrate multiple data types for comprehensive pathway analysis
7. **Personalized Medicine**: Identify individual variability in pathway responses

## Example: Enhanced Topological Map of a Simple AOP

```mermaid
graph TD
    subgraph "Molecular Initiating Event"
        A[Chemical Exposure
        <br> (e.g., Acetaminophen)]
    end
    
    subgraph "Key Events"
        B[Oxidative Stress
        <br> (Reactive Oxygen Species)]
        C[Mitochondrial Dysfunction
        <br> (ATP Depletion)]
        D[Endoplasmic Reticulum Stress
        <br> (Protein Misfolding)]
        E[Inflammation
        <br> (Cytokine Release)]
        F[Cell Death
        <br> (Apoptosis/Necrosis)]
    end
    
    subgraph "Adverse Outcome"
        G[Liver Toxicity
        <br> (Hepatocellular Damage)]
    end
    
    A -->|weight: 0.95| B
    B -->|weight: 0.85| C
    B -->|weight: 0.75| D
    C -->|weight: 0.80| E
    D -->|weight: 0.70| E
    E -->|weight: 0.90| F
    F -->|weight: 0.98| G
    
    style A fill:#90EE90,stroke:#32CD32
    style B fill:#87CEFA,stroke:#4682B4
    style C fill:#87CEFA,stroke:#4682B4
    style D fill:#87CEFA,stroke:#4682B4
    style E fill:#87CEFA,stroke:#4682B4
    style F fill:#87CEFA,stroke:#4682B4
    style G fill:#FFA07A,stroke:#CD5C5C
```

## Resources

### AOP Resources
- **AOP-Wiki**: [https://aopwiki.org](https://aopwiki.org)
- **OECD AOP Development**: [https://www.oecd.org/chemicalsafety/risk-assessment/aop-development.htm](https://www.oecd.org/chemicalsafety/risk-assessment/aop-development.htm)
- **AOP Knowledge Base**: [https://aopkb.org](https://aopkb.org)

### Network Analysis Tools
- **NetworkX documentation**: [https://networkx.org/documentation/stable/](https://networkx.org/documentation/stable/)
- **Cytoscape tutorials**: [https://cytoscape.org/tutorials.html](https://cytoscape.org/tutorials.html)
- **Gephi documentation**: [https://gephi.org/users/](https://gephi.org/users/)
- **igraph documentation**: [https://igraph.org/python/](https://igraph.org/python/)

### Visualization Guides
- **Matplotlib gallery**: [https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html)
- **Plotly documentation**: [https://plotly.com/python/](https://plotly.com/python/)
- **Mermaid.js**: [https://mermaid.js.org/](https://mermaid.js.org/)

## Conclusion
Topological mapping provides a powerful framework for understanding and analyzing Adverse Outcome Pathways. By representing AOPs as networks with comprehensive node and edge attributes, researchers can gain new insights into the complex relationships between biological events, identify critical points for intervention, and develop more effective strategies for risk assessment and mitigation.