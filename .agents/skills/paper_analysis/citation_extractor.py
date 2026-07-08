"""
Citation Extractor Module

This module provides functionality for extracting citations and references from academic papers.
"""

from typing import List, Dict
import re


class CitationExtractor:
    """Extract citations and references from academic papers."""

    def __init__(self):
        """Initialize the citation extractor."""
        pass

    def extract_citations(self, text: str) -> List[Dict]:
        """Extract citations from the text.

        Args:
            text: The paper text

        Returns:
            List of citation dictionaries
        """
        citations = []
        
        # Look for citation patterns like [1], [2], etc.
        citation_matches = re.findall(r'\[(\d+)\]', text)
        
        for citation in citation_matches:
            citations.append({
                'citation': citation,
                'text': f"[{citation}]"
            })
        
        return citations

    def extract_references(self, text: str) -> List[Dict]:
        """Extract references from the text.

        Args:
            text: The paper text

        Returns:
            List of reference dictionaries
        """
        references = []
        
        # Look for reference sections
        sections = self._split_into_sections(text)
        
        if 'References' in sections:
            ref_text = sections['References']
            references = self._parse_references(ref_text)
        elif 'Bibliography' in sections:
            ref_text = sections['Bibliography']
            references = self._parse_references(ref_text)
        
        return references

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

    def _parse_references(self, text: str) -> List[Dict]:
        """Parse references from text.

        Args:
            text: The reference section text

        Returns:
            List of reference dictionaries
        """
        references = []
        
        # Split into individual references
        ref_blocks = re.split(r'\n\s*\n', text)
        
        for i, ref_block in enumerate(ref_blocks, 1):
            ref_block = ref_block.strip()
            if not ref_block:
                continue
            
            # Try to extract author, title, journal, year, etc.
            reference = {
                'id': i,
                'text': ref_block
            }
            
            # Extract authors
            author_match = re.search(r'^([^\.]+)\.', ref_block)
            if author_match:
                reference['authors'] = author_match.group(1).strip()
            
            # Extract year
            year_match = re.search(r'(\d{4})', ref_block)
            if year_match:
                reference['year'] = year_match.group(1)
            
            # Extract title
            title_match = re.search(r'"([^"]+)"', ref_block)
            if title_match:
                reference['title'] = title_match.group(1)
            
            references.append(reference)
        
        return references

    def extract_citation_context(self, text: str) -> List[Dict]:
        """Extract citations with their context.

        Args:
            text: The paper text

        Returns:
            List of citation dictionaries with context
        """
        citation_contexts = []
        
        # Find all citations
        citation_matches = re.finditer(r'([^\[]+)\[(\d+)\]', text)
        
        for match in citation_matches:
            context = match.group(1).strip()
            citation = match.group(2)
            
            citation_contexts.append({
                'citation': citation,
                'context': context,
                'full_text': f"{context} [{citation}]"
            })
        
        return citation_contexts

    def create_citation_network(self, texts: List[str]) -> Dict:
        """Create a citation network from multiple papers.

        Args:
            texts: List of paper texts

        Returns:
            Dictionary representing the citation network
        """
        import networkx as nx
        
        # Create a directed graph
        graph = nx.DiGraph()
        
        # Add nodes for each paper
        for i, text in enumerate(texts):
            graph.add_node(i, text=text)
        
        # Find citations between papers
        for i, text1 in enumerate(texts):
            citations1 = self.extract_citations(text1)
            
            for citation in citations1:
                # Check if this citation points to another paper
                for j, text2 in enumerate(texts):
                    if i != j:
                        # Simple check: does text2 contain the cited reference?
                        # In a real implementation, this would be more sophisticated
                        if citation['citation'] in text2:
                            graph.add_edge(i, j, citation=citation['citation'])
        
        return {
            'graph': graph,
            'nodes': list(graph.nodes()),
            'edges': list(graph.edges())
        }

    def analyze_citation_patterns(self, text: str) -> Dict:
        """Analyze citation patterns in the text.

        Args:
            text: The paper text

        Returns:
            Dictionary containing citation pattern analysis
        """
        citations = self.extract_citations(text)
        citation_contexts = self.extract_citation_context(text)
        
        analysis = {
            'total_citations': len(citations),
            'unique_citations': len(set([c['citation'] for c in citations])),
            'citation_frequency': self._calculate_citation_frequency(citations),
            'citation_contexts': citation_contexts,
            'citation_density': self._calculate_citation_density(text, citations)
        }
        
        return analysis

    def _calculate_citation_frequency(self, citations: List[Dict]) -> Dict:
        """Calculate citation frequency.

        Args:
            citations: List of citation dictionaries

        Returns:
            Dictionary containing citation frequency information
        """
        from collections import Counter
        
        citation_counts = Counter([c['citation'] for c in citations])
        
        return {
            'most_cited': citation_counts.most_common(5),
            'frequency_distribution': dict(citation_counts)
        }

    def _calculate_citation_density(self, text: str, citations: List[Dict]) -> float:
        """Calculate citation density (citations per word).

        Args:
            text: The paper text
            citations: List of citation dictionaries

        Returns:
            Citation density
        """
        word_count = len(re.findall(r'\b\w+\b', text))
        citation_count = len(citations)
        
        return citation_count / word_count if word_count > 0 else 0.0
