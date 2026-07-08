"""
Paper Comparator Module

This module provides functionality for comparing multiple academic papers.
"""

from typing import List, Dict
from .content_analyzer import ContentAnalyzer


class PaperComparator:
    """Compare multiple academic papers."""

    def __init__(self):
        """Initialize the paper comparator."""
        self.analyzer = ContentAnalyzer()

    def compare(self, texts: List[str]) -> Dict:
        """Compare multiple papers.

        Args:
            texts: List of paper texts to compare

        Returns:
            Dictionary containing comparison results
        """
        # Analyze each paper
        analyses = [self.analyzer.analyze(text) for text in texts]
        
        # Compare analyses
        comparison = self.analyzer.compare_analyses(analyses)
        
        # Add additional comparison metrics
        comparison.update({
            'paper_count': len(texts),
            'commonality_score': self._calculate_commonality_score(comparison),
            'diversity_score': self._calculate_diversity_score(comparison, len(texts))
        })
        
        return comparison

    def _calculate_commonality_score(self, comparison: Dict) -> float:
        """Calculate a commonality score based on shared content.

        Args:
            comparison: Comparison results dictionary

        Returns:
            Commonality score (0-1)
        """
        common_items = 0
        total_items = 0
        
        for key in ['common_themes', 'common_entities', 'common_keywords']:
            if key in comparison:
                common_items += len(comparison[key])
                total_items += len(comparison[key])  # This is a simplification
        
        return common_items / total_items if total_items > 0 else 0.0

    def _calculate_diversity_score(self, comparison: Dict, paper_count: int) -> float:
        """Calculate a diversity score based on unique content.

        Args:
            comparison: Comparison results dictionary
            paper_count: Number of papers being compared

        Returns:
            Diversity score (0-1)
        """
        unique_items = 0
        total_items = 0
        
        for key in ['unique_themes', 'unique_entities', 'unique_keywords']:
            if key in comparison:
                unique_items += len(comparison[key])
                total_items += len(comparison[key])  # This is a simplification
        
        # Normalize by paper count
        return min(unique_items / (total_items * paper_count), 1.0) if total_items > 0 else 0.0

    def compare_with_analysis(self, analyses: List[Dict]) -> Dict:
        """Compare multiple papers using pre-computed analyses.

        Args:
            analyses: List of pre-computed analysis dictionaries

        Returns:
            Dictionary containing comparison results
        """
        # Compare analyses
        comparison = self.analyzer.compare_analyses(analyses)
        
        # Add additional comparison metrics
        comparison.update({
            'paper_count': len(analyses),
            'commonality_score': self._calculate_commonality_score(comparison),
            'diversity_score': self._calculate_diversity_score(comparison, len(analyses))
        })
        
        return comparison

    def find_most_similar(self, texts: List[str], target_text: str) -> Dict:
        """Find the most similar paper to a target text.

        Args:
            texts: List of paper texts to compare
            target_text: The target paper text

        Returns:
            Dictionary containing similarity results
        """
        # Analyze all papers
        analyses = [self.analyzer.analyze(text) for text in texts]
        target_analysis = self.analyzer.analyze(target_text)
        
        # Calculate similarity scores
        similarity_scores = []
        for i, analysis in enumerate(analyses):
            score = self._calculate_similarity_score(analysis, target_analysis)
            similarity_scores.append((i, score))
        
        # Find most similar
        most_similar_idx, max_score = max(similarity_scores, key=lambda x: x[1])
        
        return {
            'most_similar_index': most_similar_idx,
            'similarity_score': max_score,
            'similarity_scores': similarity_scores
        }

    def _calculate_similarity_score(self, analysis1: Dict, analysis2: Dict) -> float:
        """Calculate similarity score between two analyses.

        Args:
            analysis1: First analysis dictionary
            analysis2: Second analysis dictionary

        Returns:
            Similarity score (0-1)
        """
        score = 0.0
        
        # Compare themes
        if 'themes' in analysis1 and 'themes' in analysis2:
            common_themes = set(analysis1['themes']) & set(analysis2['themes'])
            theme_score = len(common_themes) / max(len(analysis1['themes']), len(analysis2['themes']))
            score += theme_score * 0.4  # 40% weight
        
        # Compare entities
        if 'entities' in analysis1 and 'entities' in analysis2:
            common_entities = set(analysis1['entities']) & set(analysis2['entities'])
            entity_score = len(common_entities) / max(len(analysis1['entities']), len(analysis2['entities']))
            score += entity_score * 0.3  # 30% weight
        
        # Compare keywords
        if 'keywords' in analysis1 and 'keywords' in analysis2:
            common_keywords = set(analysis1['keywords']) & set(analysis2['keywords'])
            keyword_score = len(common_keywords) / max(len(analysis1['keywords']), len(analysis2['keywords']))
            score += keyword_score * 0.3  # 30% weight
        
        return score

    def cluster_papers(self, texts: List[str], threshold: float = 0.5) -> List[List[int]]:
        """Cluster papers based on similarity.

        Args:
            texts: List of paper texts to cluster
            threshold: Similarity threshold for clustering (0-1)

        Returns:
            List of clusters, where each cluster is a list of paper indices
        """
        # Analyze all papers
        analyses = [self.analyzer.analyze(text) for text in texts]
        
        # Calculate similarity matrix
        similarity_matrix = []
        for i, analysis1 in enumerate(analyses):
            row = []
            for j, analysis2 in enumerate(analyses):
                if i == j:
                    row.append(1.0)  # Perfect similarity with self
                else:
                    score = self._calculate_similarity_score(analysis1, analysis2)
                    row.append(score)
            similarity_matrix.append(row)
        
        # Simple clustering algorithm
        clusters = []
        assigned = [False] * len(texts)
        
        for i in range(len(texts)):
            if not assigned[i]:
                cluster = [i]
                assigned[i] = True
                
                # Find similar papers
                for j in range(i + 1, len(texts)):
                    if similarity_matrix[i][j] >= threshold and not assigned[j]:
                        cluster.append(j)
                        assigned[j] = True
                
                clusters.append(cluster)
        
        return clusters
