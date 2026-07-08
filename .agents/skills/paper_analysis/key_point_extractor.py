"""
Key Point Extractor Module

This module provides functionality for extracting key points from academic papers.
"""

from typing import List, Dict
import re


class KeyPointExtractor:
    """Extract key points from paper text."""

    def __init__(self):
        """Initialize the key point extractor."""
        pass

    def extract_key_points(self, text: str) -> List[str]:
        """Extract key points from the given text.

        Args:
            text: The paper text

        Returns:
            List of key points
        """
        # Split text into sections
        sections = self._split_into_sections(text)
        
        # Extract key points from each section
        key_points = []
        for section_name, section_text in sections.items():
            if section_name.lower() in ['abstract', 'introduction', 'conclusion', 'results']:
                points = self._extract_points_from_section(section_text)
                key_points.extend(points)
        
        return key_points

    def _split_into_sections(self, text: str) -> Dict[str, str]:
        """Split text into sections based on headers.

        Args:
            text: The paper text

        Returns:
            Dictionary mapping section names to section text
        """
        sections = {}
        current_section = "Main Text"
        
        # Split by newlines and process each line
        lines = text.split('\n')
        section_text = []
        
        for line in lines:
            line = line.strip()
            # Check if line is a potential section header
            if self._is_section_header(line):
                # Save previous section
                if current_section and section_text:
                    sections[current_section] = '\n'.join(section_text)
                # Start new section
                current_section = line
                section_text = []
            else:
                section_text.append(line)
        
        # Save last section
        if current_section and section_text:
            sections[current_section] = '\n'.join(section_text)
        
        return sections

    def _is_section_header(self, line: str) -> bool:
        """Check if a line is a section header.

        Args:
            line: The line to check

        Returns:
            True if the line is a section header, False otherwise
        """
        # Simple heuristic: headers are typically in ALL CAPS or followed by a colon
        return (line.isupper() or line.endswith(':')) and len(line) > 3

    def _extract_points_from_section(self, text: str) -> List[str]:
        """Extract key points from a section of text.

        Args:
            text: The section text

        Returns:
            List of key points from the section
        """
        points = []
        
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Filter out short sentences and add to points
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 20:  # Minimum length for a meaningful sentence
                points.append(sentence)
        
        return points

    def extract_key_points_with_context(self, text: str) -> List[Dict]:
        """Extract key points with their context (section, position).

        Args:
            text: The paper text

        Returns:
            List of dictionaries containing key points with context
        """
        sections = self._split_into_sections(text)
        key_points = []
        
        for section_name, section_text in sections.items():
            points = self._extract_points_from_section(section_text)
            for point in points:
                key_points.append({
                    'section': section_name,
                    'text': point,
                    'position': len(key_points) + 1
                })
        
        return key_points

    def extract_summary(self, text: str, max_length: int = 500) -> str:
        """Extract a summary from the text.

        Args:
            text: The paper text
            max_length: Maximum length of the summary

        Returns:
            Summary text
        """
        # Get key points
        key_points = self.extract_key_points(text)
        
        # Join key points and truncate if necessary
        summary = ' '.join(key_points)
        if len(summary) > max_length:
            summary = summary[:max_length] + '...'
        
        return summary
