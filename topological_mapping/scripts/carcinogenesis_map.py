#!/usr/bin/env python3
"""
Example Topological Map: Carcinogenesis AOP

This script creates a topological map for a simplified Adverse Outcome Pathway
representing chemical-induced carcinogenesis.

Location: topological_mapping/scripts/carcinogenesis_map.py
"""

import networkx as nx
import matplotlib.pyplot as plt
import json

# Create a directed graph for the carcinogenesis AOP
graph = nx.DiGraph()

# Define nodes (Molecular Initiating Event, Key Events, Adverse Outcome)
nodes = {
    'MIE': 'Chemical Carcinogen Exposure (e.g., Benzo[a]pyrene)',
    'KE1': 'DNA Adduct Formation',
    'KE2': 'DNA Damage',
    'KE3': 'Mutagenesis',
    'KE4': 'Cell Proliferation',
    'KE5': 'Tumor Suppressor Inactivation',
    'KE6': 'Oncogene Activation',
    'AO': 'Carcinogenesis'
}

# Add nodes to the graph
graph.add_nodes_from(nodes.keys())

# Define edges with relationship attributes
edges = [
    # MIE to first KE
    ('MIE', 'KE1', {
        'weight': 0.95,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Carcinogen metabolism produces reactive intermediates'
    }),
    
    # KE1 to KE2
    ('KE1', 'KE2', {
        'weight': 0.90,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'DNA adducts cause DNA damage'
    }),
    
    # KE2 to KE3
    ('KE2', 'KE3', {
        'weight': 0.85,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Unrepaired DNA damage leads to mutations'
    }),
    
    # KE3 to KE4
    ('KE3', 'KE4', {
        'weight': 0.75,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Mutations in growth control genes cause proliferation'
    }),
    
    # KE3 to KE5 (parallel pathway)
    ('KE3', 'KE5', {
        'weight': 0.70,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Mutations in tumor suppressor genes'
    }),
    
    # KE3 to KE6 (parallel pathway)
    ('KE3', 'KE6', {
        'weight': 0.65,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Mutations in oncogenes'
    }),
    
    # KE4 to KE5
    ('KE4', 'KE5', {
        'weight': 0.60,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Proliferation increases mutation frequency'
    }),
    
    # KE5 to KE6
    ('KE5', 'KE6', {
        'weight': 0.55,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Tumor suppressor loss promotes oncogene activation'
    }),
    
    # KE6 to AO
    ('KE6', 'AO', {
        'weight': 0.95,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Oncogene activation leads to uncontrolled cell growth'
    })
]

# Add edges to the graph
graph.add_edges_from(edges)

# Visualize the topological map
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(graph, seed=42, k=0.6)

# Color nodes by type
node_colors = {'MIE': 'lightgreen', 'KE1': 'skyblue', 'KE2': 'skyblue', 
               'KE3': 'skyblue', 'KE4': 'skyblue', 'KE5': 'skyblue', 
               'KE6': 'skyblue', 'AO': 'salmon'}
colors = [node_colors[node] for node in graph.nodes()]

# Draw nodes with labels
node_labels = {node: f"{node}\n{nodes[node]}" for node in graph.nodes()}
nx.draw_networkx_nodes(graph, pos, node_size=3000, node_color=colors, alpha=0.9)
nx.draw_networkx_labels(graph, pos, labels=node_labels, font_size=9, font_weight='bold')

# Draw edges with weights
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edges(graph, pos, width=2, arrowsize=20, edge_color='gray')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=7)

# Add title and adjust layout
plt.title('Topological Map: Chemical-Induced Carcinogenesis AOP', 
          fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Save visualization to the visualizations directory
output_path = '/home/avam11/lively-animatronic-llama/topological_mapping/visualizations/carcinogenesis.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Visualization saved to: {output_path}")

# Perform topological analysis
print("\n" + "=" * 60)
print("TOPOLOGICAL ANALYSIS OF CARCINOGENESIS AOP")
print("=" * 60)

# 1. Basic graph properties
print(f"\n1. Graph Properties:")
print(f"   - Number of nodes: {graph.number_of_nodes()}")
print(f"   - Number of edges: {graph.number_of_edges()}")
print(f"   - Is directed: {nx.is_directed(graph)}")

# 2. Centrality measures
print(f"\n2. Centrality Measures:")

# Degree centrality (number of connections)
degree_centrality = nx.degree_centrality(graph)
print(f"   Degree Centrality:")
for node, score in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"     {node}: {score:.3f}")

# Betweenness centrality (importance as bridge)
betweenness = nx.betweenness_centrality(graph, normalized=True)
print(f"\n   Betweenness Centrality:")
for node, score in sorted(betweenness.items(), key=lambda x: x[1], reverse=True):
    print(f"     {node}: {score:.3f}")

# Closeness centrality (proximity to other nodes)
closeness = nx.closeness_centrality(graph)
print(f"\n   Closeness Centrality:")
for node, score in sorted(closeness.items(), key=lambda x: x[1], reverse=True):
    print(f"     {node}: {score:.3f}")

# 3. Path analysis
print(f"\n3. Path Analysis:")
all_simple_paths = list(nx.all_simple_paths(graph, source='MIE', target='AO'))
print(f"   Number of simple paths from MIE to AO: {len(all_simple_paths)}")
print(f"   All paths:")
for i, path in enumerate(all_simple_paths, 1):
    path_str = " → ".join(path)
    print(f"     Path {i}: {path_str}")

# Find shortest path
shortest_path = nx.shortest_path(graph, source='MIE', target='AO', weight='weight')
print(f"\n   Shortest path (by weight):")
print(f"     {" → ".join(shortest_path)}")

# 4. Critical nodes analysis
print(f"\n4. Critical Nodes Analysis:")
critical_nodes = [node for node, score in betweenness.items() if score > 0.1]
print(f"   Nodes with high betweenness (>0.1): {critical_nodes}")
print(f"   These nodes are critical for pathway connectivity")

# 5. Evidence strength analysis
print(f"\n5. Evidence Strength Analysis:")
evidence_scores = nx.get_edge_attributes(graph, 'evidence')
strong_evidence = {edge: score for edge, score in evidence_scores.items() if score == 'strong'}
moderate_evidence = {edge: score for edge, score in evidence_scores.items() if score == 'moderate'}
print(f"   Strong evidence connections: {len(strong_evidence)}")
print(f"   Moderate evidence connections: {len(moderate_evidence)}")

# 6. Network complexity analysis
print(f"\n6. Network Complexity Analysis:")
try:
    print(f"   Average path length: {nx.average_shortest_path_length(graph, weight='weight'):.2f}")
except nx.NetworkXError:
    print(f"   Average path length: N/A (graph not strongly connected)")
print(f"   Graph density: {nx.density(graph):.3f}")
print(f"   Number of connected components: {nx.number_weakly_connected_components(graph)}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

# Save the graph data for further analysis
graph_data = {
    'nodes': nodes,
    'edges': edges,
    'analysis': {
        'degree_centrality': degree_centrality,
        'betweenness_centrality': betweenness,
        'closeness_centrality': closeness,
        'all_paths': all_simple_paths,
        'shortest_path': shortest_path,
        'critical_nodes': critical_nodes,
        'average_path_length': nx.average_shortest_path_length(graph, weight='weight') if nx.is_strongly_connected(graph) else None,
        'graph_density': nx.density(graph),
        'connected_components': nx.number_weakly_connected_components(graph)
    }
}

# Save data to the data directory
output_data_path = '/home/avam11/lively-animatronic-llama/topological_mapping/data/carcinogenesis_analysis.json'
with open(output_data_path, 'w') as f:
    json.dump(graph_data, f, indent=2)

print(f"\nGraph data saved to: {output_data_path}")
print(f"\nTo run this example:")
print(f"  cd topological_mapping")
print(f"  python scripts/carcinogenesis_map.py")
print(f"\nThis example demonstrates a more complex AOP with multiple parallel pathways")
print(f"from DNA damage to carcinogenesis, highlighting the importance of KE3 (Mutagenesis)")
print(f"as a central hub in the pathway.")