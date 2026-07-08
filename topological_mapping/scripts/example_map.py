#!/usr/bin/env python3
"""
Example Topological Map for an Adverse Outcome Pathway (AOP)

This script creates a topological map for a simplified AOP representing
chemical-induced liver toxicity.

Location: topological_mapping/scripts/example_map.py
"""

import networkx as nx
import matplotlib.pyplot as plt
import json

# Create a directed graph for the AOP
graph = nx.DiGraph()

# Define nodes (Molecular Initiating Event, Key Events, Adverse Outcome)
nodes = {
    'MIE': 'Chemical Exposure (e.g., Acetaminophen)',
    'KE1': 'Oxidative Stress',
    'KE2': 'Mitochondrial Dysfunction',
    'KE3': 'Endoplasmic Reticulum Stress',
    'KE4': 'Inflammation',
    'KE5': 'Cell Death (Apoptosis/Necrosis)',
    'AO': 'Liver Toxicity'
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
        'description': 'Chemical metabolism produces reactive oxygen species'
    }),
    
    # KE1 to KE2
    ('KE1', 'KE2', {
        'weight': 0.85,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Oxidative stress damages mitochondrial membranes'
    }),
    
    # KE1 to KE3 (parallel pathway)
    ('KE1', 'KE3', {
        'weight': 0.75,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'Oxidative stress disrupts protein folding'
    }),
    
    # KE2 to KE4
    ('KE2', 'KE4', {
        'weight': 0.80,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Mitochondrial dysfunction triggers inflammatory response'
    }),
    
    # KE3 to KE4
    ('KE3', 'KE4', {
        'weight': 0.70,
        'evidence': 'moderate',
        'type': 'causal',
        'description': 'ER stress activates NF-κB pathway'
    }),
    
    # KE4 to KE5
    ('KE4', 'KE5', {
        'weight': 0.90,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Chronic inflammation leads to cell death'
    }),
    
    # KE5 to AO
    ('KE5', 'AO', {
        'weight': 0.98,
        'evidence': 'strong',
        'type': 'causal',
        'description': 'Extensive cell death results in tissue damage'
    })
]

# Add edges to the graph
graph.add_edges_from(edges)

# Visualize the topological map with improved clarity
plt.figure(figsize=(16, 12))
pos = nx.spring_layout(graph, seed=42, k=0.8)  # Increased k for better spacing

# Color nodes by type with distinct colors
node_colors = {'MIE': '#98FB98', 'KE1': '#87CEFA', 'KE2': '#87CEFA', 
               'KE3': '#87CEFA', 'KE4': '#87CEFA', 'KE5': '#87CEFA', 'AO': '#FFA07A'}
colors = [node_colors[node] for node in graph.nodes()]

# Draw nodes with improved styling
node_labels = {node: f"{node}\n{nodes[node]}" for node in graph.nodes()}
nx.draw_networkx_nodes(graph, pos, node_size=3500, node_color=colors, alpha=0.9, edgecolors='black', linewidths=1.5)

# Draw labels with better positioning
nx.draw_networkx_labels(graph, pos, labels=node_labels, font_size=11, font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1))

# Draw edges with improved styling to avoid overlap
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edges(graph, pos, width=2.5, arrowsize=25, edge_color='gray', connectionstyle='arc3,rad=0.2')

# Create a separate figure for edge labels to avoid overlap
plt.figure(figsize=(16, 12))
plt.axis('off')
nx.draw_networkx_nodes(graph, pos, node_size=3500, node_color=colors, alpha=0.9, edgecolors='black', linewidths=1.5)
nx.draw_networkx_labels(graph, pos, labels=node_labels, font_size=11, font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1))
nx.draw_networkx_edges(graph, pos, width=2.5, arrowsize=25, edge_color='gray', connectionstyle='arc3,rad=0.2')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=9, font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.5))

# Add title and adjust layout
plt.title('Topological Map: Chemical-Induced Liver Toxicity AOP', 
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()

# Save visualization to the visualizations directory
output_path = '/home/avam11/lively-animatronic-llama/topological_mapping/visualizations/liver_toxicity.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Visualization saved to: {output_path}")

# Perform topological analysis
print("\n" + "=" * 60)
print("TOPOLOGICAL ANALYSIS OF LIVER TOXICITY AOP")
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
        'critical_nodes': critical_nodes
    }
}

# Save data to the data directory
output_data_path = '/home/avam11/lively-animatronic-llama/topological_mapping/data/liver_toxicity_analysis.json'
with open(output_data_path, 'w') as f:
    json.dump(graph_data, f, indent=2)

print(f"\nGraph data saved to: {output_data_path}")
print(f"\nTo run this example:")
print(f"  cd topological_mapping")
print(f"  python scripts/example_map.py")