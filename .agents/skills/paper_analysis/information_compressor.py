"""
Information Compressor Module

This module provides functionality for compressing and summarizing information from academic papers.
"""

from typing import List, Dict
from .key_point_extractor import KeyPointExtractor
from .content_analyzer import ContentAnalyzer


class InformationCompressor:
    """Compress and summarize information from academic papers."""

    def __init__(self):
        """Initialize the information compressor."""
        self.key_point_extractor = KeyPointExtractor()
        self.content_analyzer = ContentAnalyzer()

    def compress(self, text: str, max_length: int = 500) -> str:
        """Compress the text to a specified maximum length.

        Args:
            text: The paper text to compress
            max_length: Maximum length of the compressed text

        Returns:
            Compressed text
        """
        # Extract key points
        key_points = self.key_point_extractor.extract_key_points(text)
        
        # Join key points and truncate if necessary
        compressed = ' '.join(key_points)
        if len(compressed) > max_length:
            compressed = compressed[:max_length] + '...'
        
        return compressed

    def create_abstract(self, text: str, max_length: int = 200) -> str:
        """Create an abstract from the paper text.

        Args:
            text: The paper text
            max_length: Maximum length of the abstract

        Returns:
            Abstract text
        """
        # Extract key points from important sections
        sections = self.key_point_extractor._split_into_sections(text)
        important_sections = ['Abstract', 'Introduction', 'Conclusion', 'Results']
        
        key_points = []
        for section_name in important_sections:
            if section_name in sections:
                points = self.key_point_extractor._extract_points_from_section(sections[section_name])
                key_points.extend(points[:3])  # Take up to 3 points from each section
        
        # Create abstract
        abstract = ' '.join(key_points)
        if len(abstract) > max_length:
            abstract = abstract[:max_length] + '...'
        
        return abstract

    def create_executive_summary(self, text: str) -> Dict:
        """Create an executive summary of the paper.

        Args:
            text: The paper text

        Returns:
            Dictionary containing the executive summary
        """
        # Analyze content
        analysis = self.content_analyzer.analyze(text)
        
        # Extract key points
        key_points = self.key_point_extractor.extract_key_points(text)
        
        # Create summary
        summary = {
            'title': self._extract_title(text),
            'authors': self._extract_authors(text),
            'publication': self._extract_publication_info(text),
            'key_points': key_points[:5],  # Top 5 key points
            'themes': analysis['themes'][:10],  # Top 10 themes
            'entities': analysis['entities'][:10],  # Top 10 entities
            'keywords': analysis['keywords'][:10],  # Top 10 keywords
            'statistics': analysis['statistics'],
            'summary': self.compress(text, max_length=300)
        }
        
        return summary

    def _extract_title(self, text: str) -> str:
        """Extract the title from the text.

        Args:
            text: The paper text

        Returns:
            Extracted title
        """
        # Simple title extraction - look for the first line that's likely a title
        lines = text.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            line = line.strip()
            if len(line) > 20 and not line.isupper() and not line.endswith(':'):
                return line
        
        return "Untitled"

    def _extract_authors(self, text: str) -> List[str]:
        """Extract authors from the text.

        Args:
            text: The paper text

        Returns:
            List of authors
        """
        # Simple author extraction - look for patterns like "Author: Name"
        import re
        authors = re.findall(r'Author[:\s]+([^\n]+)', text)
        
        if not authors:
            # Look for lines that might contain authors
            lines = text.split('\n')
            for line in lines[:20]:  # Check first 20 lines
                line = line.strip()
                if 'by' in line.lower():
                    authors = [line.split('by')[-1].strip()]
                    break
        
        return authors if authors else ["Unknown"]

    def _extract_publication_info(self, text: str) -> Dict:
        """Extract publication information from the text.

        Args:
            text: The paper text

        Returns:
            Dictionary containing publication information
        """
        import re
        
        info = {
            'journal': "Unknown",
            'year': "Unknown",
            'volume': "Unknown",
            'issue': "Unknown",
            'pages': "Unknown"
        }
        
        # Simple pattern matching for publication info
        journal_match = re.search(r'Journal[:\s]+([^\n]+)', text)
        if journal_match:
            info['journal'] = journal_match.group(1).strip()
        
        year_match = re.search(r'(\d{4})', text)
        if year_match:
            info['year'] = year_match.group(1)
        
        return info

    def compress_multiple(self, texts: List[str], max_length: int = 500) -> List[str]:
        """Compress multiple texts.

        Args:
            texts: List of paper texts to compress
            max_length: Maximum length of each compressed text

        Returns:
            List of compressed texts
        """
        return [self.compress(text, max_length) for text in texts]

    def create_comparison_summary(self, texts: List[str]) -> Dict:
        """Create a summary comparing multiple papers.

        Args:
            texts: List of paper texts to compare

        Returns:
            Dictionary containing comparison summary
        """
        from .paper_comparator import PaperComparator
        
        comparator = PaperComparator()
        comparison = comparator.compare(texts)
        
        # Create summary
        summary = {
            'paper_count': len(texts),
            'common_themes': comparison['common_themes'],
            'common_entities': comparison['common_entities'],
            'common_keywords': comparison['common_keywords'],
            'unique_themes': comparison.get('unique_themes', []),
            'unique_entities': comparison.get('unique_entities', []),
            'unique_keywords': comparison.get('unique_keywords', []),
            'commonality_score': comparison['commonality_score'],
            'diversity_score': comparison['diversity_score'],
            'individual_summaries': [self.create_executive_summary(text) for text in texts]
        }
        
        return summary
