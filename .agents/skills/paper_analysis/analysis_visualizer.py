"""
Analysis Visualizer Module

This module provides functionality for visualizing analysis results from academic papers.
"""

from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import networkx as nx
from .content_analyzer import ContentAnalyzer
from .paper_comparator import PaperComparator


class AnalysisVisualizer:
    """Visualize analysis results from academic papers."""

    def __init__(self):
        """Initialize the analysis visualizer."""
        pass

    def visualize_relationships(self, relationships: List[Dict], output_file: Optional[str] = None) -> plt.Figure:
        """Visualize relationships between entities.

        Args:
            relationships: List of relationship dictionaries
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        # Create a directed graph
        graph = nx.DiGraph()
        
        # Add nodes and edges
        for rel in relationships:
            graph.add_edge(rel['source'], rel['target'], type=rel['type'])
        
        # Draw the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(graph, seed=42)
        
        # Draw nodes
        nx.draw_networkx_nodes(graph, pos, node_size=3000, node_color='skyblue', alpha=0.9)
        
        # Draw edges with different colors based on type
        edge_colors = {'causal': 'red', 'interaction': 'green', 'other': 'blue'}
        for edge_type in edge_colors:
            edges = [(u, v) for u, v, d in graph.edges(data=True) if d['type'] == edge_type]
            nx.draw_networkx_edges(graph, pos, edgelist=edges, 
                                  width=2, edge_color=edge_colors[edge_type],
                                  arrowstyle='->', arrowsize=20)
        
        # Draw labels
        nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold')
        
        # Add title
        plt.title('Entity Relationships', fontsize=14, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return plt.gcf()

    def visualize_comparison(self, comparison: Dict, output_file: Optional[str] = None) -> plt.Figure:
        """Visualize comparison results.

        Args:
            comparison: Comparison results dictionary
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        # Create a figure with multiple subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Common vs Unique themes
        if 'common_themes' in comparison and 'unique_themes' in comparison:
            themes_data = [
                ('Common Themes', len(comparison['common_themes'])),
                ('Unique Themes', len(comparison['unique_themes']))
            ]
            themes_labels, themes_values = zip(*themes_data)
            axes[0, 0].bar(themes_labels, themes_values, color=['green', 'orange'])
            axes[0, 0].set_title('Themes Comparison')
            axes[0, 0].set_ylabel('Count')
        
        # Plot 2: Common vs Unique entities
        if 'common_entities' in comparison and 'unique_entities' in comparison:
            entities_data = [
                ('Common Entities', len(comparison['common_entities'])),
                ('Unique Entities', len(comparison['unique_entities']))
            ]
            entities_labels, entities_values = zip(*entities_data)
            axes[0, 1].bar(entities_labels, entities_values, color=['green', 'orange'])
            axes[0, 1].set_title('Entities Comparison')
            axes[0, 1].set_ylabel('Count')
        
        # Plot 3: Common vs Unique keywords
        if 'common_keywords' in comparison and 'unique_keywords' in comparison:
            keywords_data = [
                ('Common Keywords', len(comparison['common_keywords'])),
                ('Unique Keywords', len(comparison['unique_keywords']))
            ]
            keywords_labels, keywords_values = zip(*keywords_data)
            axes[1, 0].bar(keywords_labels, keywords_values, color=['green', 'orange'])
            axes[1, 0].set_title('Keywords Comparison')
            axes[1, 0].set_ylabel('Count')
        
        # Plot 4: Scores
        if 'commonality_score' in comparison and 'diversity_score' in comparison:
            scores_data = [
                ('Commonality Score', comparison['commonality_score']),
                ('Diversity Score', comparison['diversity_score'])
            ]
            scores_labels, scores_values = zip(*scores_data)
            axes[1, 1].bar(scores_labels, scores_values, color=['green', 'blue'])
            axes[1, 1].set_title('Comparison Scores')
            axes[1, 1].set_ylabel('Score')
            axes[1, 1].set_ylim(0, 1)
        
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return fig

    def visualize_keywords(self, keywords: List[str], output_file: Optional[str] = None) -> plt.Figure:
        """Visualize keyword frequency.

        Args:
            keywords: List of keywords
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        from collections import Counter
        
        # Count keyword frequency
        keyword_counts = Counter(keywords)
        
        # Get top keywords
        top_keywords = keyword_counts.most_common(15)
        labels, values = zip(*top_keywords)
        
        # Create bar plot
        plt.figure(figsize=(12, 8))
        plt.barh(labels, values, color='skyblue')
        plt.title('Top Keywords', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Frequency')
        plt.ylabel('Keyword')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return plt.gcf()

    def visualize_citation_network(self, citation_network: Dict, output_file: Optional[str] = None) -> plt.Figure:
        """Visualize a citation network.

        Args:
            citation_network: Citation network dictionary
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        graph = citation_network['graph']
        
        # Draw the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(graph, seed=42)
        
        # Draw nodes
        nx.draw_networkx_nodes(graph, pos, node_size=3000, node_color='skyblue', alpha=0.9)
        
        # Draw edges
        nx.draw_networkx_edges(graph, pos, width=2, edge_color='gray', 
                              arrowstyle='->', arrowsize=20)
        
        # Draw labels
        nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold')
        
        # Add title
        plt.title('Citation Network', fontsize=14, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return plt.gcf()

    def visualize_paper_clusters(self, clusters: List[List[int]], output_file: Optional[str] = None) -> plt.Figure:
        """Visualize paper clusters.

        Args:
            clusters: List of clusters, where each cluster is a list of paper indices
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        # Create a graph where nodes in the same cluster are connected
        graph = nx.Graph()
        
        # Add nodes
        for i in range(len(clusters)):
            for paper_idx in clusters[i]:
                graph.add_node(paper_idx, cluster=i)
        
        # Connect nodes in the same cluster
        for cluster in clusters:
            for i in range(len(cluster)):
                for j in range(i + 1, len(cluster)):
                    graph.add_edge(cluster[i], cluster[j])
        
        # Draw the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(graph, seed=42)
        
        # Draw nodes with different colors for each cluster
        cluster_colors = ['red', 'green', 'blue', 'orange', 'purple']
        for i, cluster in enumerate(clusters):
            nx.draw_networkx_nodes(graph, pos, nodelist=cluster, 
                                  node_size=3000, node_color=cluster_colors[i % len(cluster_colors)],
                                  alpha=0.9, label=f'Cluster {i+1}')
        
        # Draw edges
        nx.draw_networkx_edges(graph, pos, width=1, edge_color='gray', alpha=0.5)
        
        # Draw labels
        nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold')
        
        # Add title and legend
        plt.title('Paper Clusters', fontsize=14, fontweight='bold', pad=20)
        plt.axis('off')
        plt.legend()
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return plt.gcf()

    def visualize_analysis_results(self, analysis: Dict, output_file: Optional[str] = None) -> plt.Figure:
        """Visualize analysis results.

        Args:
            analysis: Analysis results dictionary
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        # Create a figure with multiple subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Keywords
        if 'keywords' in analysis:
            self.visualize_keywords(analysis['keywords'], output_file=None)
            axes[0, 0].set_title('Top Keywords')
        
        # Plot 2: Themes
        if 'themes' in analysis:
            axes[0, 1].barh(range(len(analysis['themes'])), [1] * len(analysis['themes']), 
                           tick_label=analysis['themes'])
            axes[0, 1].set_title('Themes')
            axes[0, 1].set_xlabel('Presence')
            axes[0, 1].set_ylabel('Theme')
        
        # Plot 3: Entities
        if 'entities' in analysis:
            axes[1, 0].barh(range(len(analysis['entities'])), [1] * len(analysis['entities']), 
                           tick_label=analysis['entities'])
            axes[1, 0].set_title('Entities')
            axes[1, 0].set_xlabel('Presence')
            axes[1, 0].set_ylabel('Entity')
        
        # Plot 4: Statistics
        if 'statistics' in analysis:
            stats = analysis['statistics']
            stats_labels = list(stats.keys())
            stats_values = list(stats.values())
            axes[1, 1].bar(stats_labels, stats_values, color='skyblue')
            axes[1, 1].set_title('Text Statistics')
            axes[1, 1].set_ylabel('Value')
        
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return fig

    def visualize_comparison_matrix(self, similarity_scores: List[tuple], output_file: Optional[str] = None) -> plt.Figure:
        """Visualize a similarity matrix.

        Args:
            similarity_scores: List of (i, j, score) tuples
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        # Create a matrix
        n = max(i for i, _, _ in similarity_scores) + 1
        matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        
        for i, j, score in similarity_scores:
            matrix[i][j] = score
            matrix[j][i] = score  # Symmetric matrix
        
        # Create heatmap
        plt.figure(figsize=(10, 8))
        plt.imshow(matrix, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.title('Similarity Matrix', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Paper Index')
        plt.ylabel('Paper Index')
        plt.xticks(range(n))
        plt.yticks(range(n))
        plt.tight_layout()
        
        # Save if output file is specified
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        
        return plt.gcf()
