"""
Content Analyzer Module

This module provides functionality for analyzing the content of academic papers.
"""

from typing import List, Dict, Optional
import re
from collections import Counter


class ContentAnalyzer:
    """Analyze the content of academic papers."""

    def __init__(self):
        """Initialize the content analyzer."""
        pass

    def analyze(self, text: str) -> Dict:
        """Analyze the content of the given text.

        Args:
            text: The paper text

        Returns:
            Dictionary containing analysis results
        """
        analysis = {
            'themes': self._extract_themes(text),
            'entities': self._extract_entities(text),
            'relationships': self._extract_relationships(text),
            'statistics': self._calculate_statistics(text),
            'keywords': self._extract_keywords(text)
        }
        
        return analysis

    def _extract_themes(self, text: str) -> List[str]:
        """Extract themes from the text.

        Args:
            text: The paper text

        Returns:
            List of themes
        """
        # Simple theme extraction based on frequent phrases
        # In a real implementation, this would use NLP techniques
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        
        # Filter out common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be', 'been', 'being'}
        filtered_words = [word for word in word_counts if word not in stop_words and len(word) > 3]
        
        # Get top themes
        themes = [word for word, _ in word_counts.most_common(20) if word in filtered_words]
        
        return themes

    def _extract_entities(self, text: str) -> List[str]:
        """Extract entities from the text.

        Args:
            text: The paper text

        Returns:
            List of entities
        """
        # Simple entity extraction based on capitalization patterns
        # In a real implementation, this would use NLP named entity recognition
        lines = text.split('\n')
        entities = []
        
        for line in lines:
            # Look for capitalized words that might be entities
            potential_entities = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', line)
            entities.extend(potential_entities)
        
        # Remove duplicates and short entities
        entities = list(set([e for e in entities if len(e.split()) > 1]))
        
        return entities

    def _extract_relationships(self, text: str) -> List[Dict]:
        """Extract relationships between entities from the text.

        Args:
            text: The paper text

        Returns:
            List of relationship dictionaries
        """
        # Simple relationship extraction based on common patterns
        # In a real implementation, this would use dependency parsing
        relationships = []
        
        # Look for patterns like "A affects B" or "A causes B"
        patterns = [
            (r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(affects|causes|influences|regulates|modulates)\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)', 'causal'),
            (r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(interacts|binds|associates)\s+with\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)', 'interaction'),
            (r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(leads to|results in|produces)\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)', 'causal')
        ]
        
        for pattern, rel_type in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                relationships.append({
                    'source': match[0],
                    'target': match[2],
                    'type': rel_type,
                    'text': f"{match[0]} {match[1]} {match[2]}"
                })
        
        return relationships

    def _calculate_statistics(self, text: str) -> Dict:
        """Calculate statistics about the text.

        Args:
            text: The paper text

        Returns:
            Dictionary containing statistics
        """
        words = re.findall(r'\b\w+\b', text)
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        stats = {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'average_sentence_length': len(words) / len(sentences) if sentences else 0,
            'unique_word_count': len(set(words))
        }
        
        return stats

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from the text.

        Args:
            text: The paper text

        Returns:
            List of keywords
        """
        # Simple keyword extraction based on frequency
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        
        # Filter out common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be', 'been', 'being'}
        filtered_words = [word for word in word_counts if word not in stop_words and len(word) > 4]
        
        # Get top keywords
        keywords = [word for word, _ in word_counts.most_common(15) if word in filtered_words]
        
        return keywords

    def compare_analyses(self, analyses: List[Dict]) -> Dict:
        """Compare multiple content analyses.

        Args:
            analyses: List of analysis dictionaries

        Returns:
            Dictionary containing comparison results
        """
        if not analyses:
            return {}
        
        comparison = {
            'common_themes': self._find_common_themes(analyses),
            'common_entities': self._find_common_entities(analyses),
            'common_keywords': self._find_common_keywords(analyses),
            'differences': self._find_differences(analyses)
        }
        
        return comparison

    def _find_common_themes(self, analyses: List[Dict]) -> List[str]:
        """Find common themes across multiple analyses.

        Args:
            analyses: List of analysis dictionaries

        Returns:
            List of common themes
        """
        all_themes = [analysis['themes'] for analysis in analyses if 'themes' in analysis]
        if not all_themes:
            return []
        
        # Find intersection of all theme lists
        common_themes = set(all_themes[0])
        for themes in all_themes[1:]:
            common_themes.intersection_update(themes)
        
        return list(common_themes)

    def _find_common_entities(self, analyses: List[Dict]) -> List[str]:
        """Find common entities across multiple analyses.

        Args:
            analyses: List of analysis dictionaries

        Returns:
            List of common entities
        """
        all_entities = [analysis['entities'] for analysis in analyses if 'entities' in analysis]
        if not all_entities:
            return []
        
        # Find intersection of all entity lists
        common_entities = set(all_entities[0])
        for entities in all_entities[1:]:
            common_entities.intersection_update(entities)
        
        return list(common_entities)

    def _find_common_keywords(self, analyses: List[Dict]) -> List[str]:
        """Find common keywords across multiple analyses.

        Args:
            analyses: List of analysis dictionaries

        Returns:
            List of common keywords
        """
        all_keywords = [analysis['keywords'] for analysis in analyses if 'keywords' in analysis]
        if not all_keywords:
            return []
        
        # Find intersection of all keyword lists
        common_keywords = set(all_keywords[0])
        for keywords in all_keywords[1:]:
            common_keywords.intersection_update(keywords)
        
        return list(common_keywords)

    def _find_differences(self, analyses: List[Dict]) -> Dict:
        """Find differences across multiple analyses.

        Args:
            analyses: List of analysis dictionaries

        Returns:
            Dictionary containing differences
        """
        differences = {}
        
        # Compare themes
        all_themes = [analysis['themes'] for analysis in analyses if 'themes' in analysis]
        if all_themes:
            unique_themes = set().union(*all_themes)
            common_themes = set(all_themes[0])
            for themes in all_themes[1:]:
                common_themes.intersection_update(themes)
            differences['unique_themes'] = list(unique_themes - common_themes)
        
        # Compare entities
        all_entities = [analysis['entities'] for analysis in analyses if 'entities' in analysis]
        if all_entities:
            unique_entities = set().union(*all_entities)
            common_entities = set(all_entities[0])
            for entities in all_entities[1:]:
                common_entities.intersection_update(entities)
            differences['unique_entities'] = list(unique_entities - common_entities)
        
        # Compare keywords
        all_keywords = [analysis['keywords'] for analysis in analyses if 'keywords' in analysis]
        if all_keywords:
            unique_keywords = set().union(*all_keywords)
            common_keywords = set(all_keywords[0])
            for keywords in all_keywords[1:]:
                common_keywords.intersection_update(keywords)
            differences['unique_keywords'] = list(unique_keywords - common_keywords)
        
        return differences
