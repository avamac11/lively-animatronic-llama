"""
Paper Analysis Skill Module

This module provides the main PaperAnalysisSkill class that orchestrates all paper analysis components.
"""

from typing import List, Dict, Optional, Any
from .paper_searcher import PaperSearcher, ArxivSearcher, PubMedSearcher
from .paper_reader import PaperReaderWrapper
from .key_point_extractor import KeyPointExtractor
from .content_analyzer import ContentAnalyzer
from .paper_comparator import PaperComparator
from .information_compressor import InformationCompressor
from .citation_extractor import CitationExtractor
from .analysis_visualizer import AnalysisVisualizer
from .aop_integrator import AOPIntegrator


class PaperAnalysisSkill:
    """Main class for the Paper Analysis Skill that orchestrates all components."""

    def __init__(self):
        """Initialize the Paper Analysis Skill with all components."""
        self.paper_searcher = PaperSearcher()
        self.paper_reader = PaperReaderWrapper()
        self.key_point_extractor = KeyPointExtractor()
        self.content_analyzer = ContentAnalyzer()
        self.paper_comparator = PaperComparator()
        self.information_compressor = InformationCompressor()
        self.citation_extractor = CitationExtractor()
        self.analysis_visualizer = AnalysisVisualizer()
        self.aop_integrator = AOPIntegrator()
        self.config = {}

    def configure(self, config: Dict) -> None:
        """Configure the Paper Analysis Skill.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        
        # Configure paper searcher if API keys are provided
        if 'paper_search' in config:
            search_config = config['paper_search']
            if 'arxiv_api_key' in search_config:
                self.paper_searcher = ArxivSearcher(api_key=search_config['arxiv_api_key'])
            if 'pubmed_api_key' in search_config:
                self.paper_searcher = PubMedSearcher(api_key=search_config['pubmed_api_key'])

    def search_papers(self, query: str, source: str = 'arxiv', max_results: int = 10) -> List[Dict]:
        """Search for papers using the specified source.

        Args:
            query: The search query
            source: The search source ('arxiv', 'pubmed', etc.)
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        if source == 'arxiv':
            searcher = ArxivSearcher()
        elif source == 'pubmed':
            searcher = PubMedSearcher()
        else:
            searcher = PaperSearcher()
        
        return searcher.search(query, max_results)

    def read_paper(self, file_path: str) -> str:
        """Read a paper from the given file path.

        Args:
            file_path: Path to the paper file

        Returns:
            Extracted text from the paper
        """
        return self.paper_reader.read_paper(file_path)

    def analyze_paper(self, text: str) -> Dict:
        """Analyze the content of a paper.

        Args:
            text: The paper text to analyze

        Returns:
            Dictionary containing analysis results
        """
        return self.content_analyzer.analyze(text)

    def extract_key_points(self, text: str) -> List[str]:
        """Extract key points from paper text.

        Args:
            text: The paper text

        Returns:
            List of key points
        """
        return self.key_point_extractor.extract_key_points(text)

    def compress_information(self, text: str, max_length: int = 500) -> str:
        """Compress paper text to a specified maximum length.

        Args:
            text: The paper text to compress
            max_length: Maximum length of the compressed text

        Returns:
            Compressed text
        """
        return self.information_compressor.compress(text, max_length)

    def extract_citations(self, text: str) -> List[Dict]:
        """Extract citations from paper text.

        Args:
            text: The paper text

        Returns:
            List of citation dictionaries
        """
        return self.citation_extractor.extract_citations(text)

    def compare_papers(self, texts: List[str]) -> Dict:
        """Compare multiple papers.

        Args:
            texts: List of paper texts to compare

        Returns:
            Dictionary containing comparison results
        """
        return self.paper_comparator.compare(texts)

    def visualize_analysis(self, analysis: Dict, output_file: Optional[str] = None) -> Any:
        """Visualize analysis results.

        Args:
            analysis: Analysis results dictionary
            output_file: Optional output file path

        Returns:
            Matplotlib figure
        """
        if 'relationships' in analysis:
            return self.analysis_visualizer.visualize_relationships(analysis['relationships'], output_file)
        return None

    def extract_aop_evidence(self, text: str) -> Dict:
        """Extract AOP-relevant evidence from paper text.

        Args:
            text: The paper text to analyze

        Returns:
            Dictionary containing AOP evidence
        """
        return self.aop_integrator.extract_aop_evidence(text)

    def build_aop_skeleton(self, text: str) -> Dict:
        """Build a skeleton AOP from paper text.

        Args:
            text: The paper text to analyze

        Returns:
            Dictionary representing an AOP skeleton
        """
        return self.aop_integrator.build_aop_skeleton(text)

    def validate_aop_evidence(self, evidence: Dict) -> Dict:
        """Validate AOP evidence for completeness and consistency.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            Dictionary containing validation results
        """
        return self.aop_integrator.validate_aop_evidence(evidence)

    def analyze_paper_workflow(self, file_path: str) -> Dict:
        """Complete workflow for analyzing a paper from file to final analysis.

        Args:
            file_path: Path to the paper file

        Returns:
            Dictionary containing complete analysis results
        """
        # Read the paper
        text = self.read_paper(file_path)
        
        # Extract key points
        key_points = self.extract_key_points(text)
        
        # Analyze content
        analysis = self.analyze_paper(text)
        
        # Extract citations
        citations = self.extract_citations(text)
        
        # Extract AOP evidence
        aop_evidence = self.extract_aop_evidence(text)
        
        # Build AOP skeleton
        aop_skeleton = self.build_aop_skeleton(text)
        
        # Validate AOP evidence
        aop_validation = self.validate_aop_evidence(aop_evidence)
        
        # Create executive summary
        summary = self.information_compressor.create_executive_summary(text)
        
        return {
            'text': text,
            'key_points': key_points,
            'analysis': analysis,
            'citations': citations,
            'aop_evidence': aop_evidence,
            'aop_skeleton': aop_skeleton,
            'aop_validation': aop_validation,
            'summary': summary
        }

    def compare_papers_workflow(self, file_paths: List[str]) -> Dict:
        """Complete workflow for comparing multiple papers.

        Args:
            file_paths: List of paths to paper files

        Returns:
            Dictionary containing comparison results
        """
        # Read all papers
        texts = [self.read_paper(file_path) for file_path in file_paths]
        
        # Analyze each paper
        analyses = [self.analyze_paper(text) for text in texts]
        
        # Compare papers
        comparison = self.compare_papers(texts)
        
        # Extract AOP evidence from each paper
        aop_evidences = [self.extract_aop_evidence(text) for text in texts]
        
        # Build AOP skeletons
        aop_skeletons = [self.build_aop_skeleton(text) for text in texts]
        
        return {
            'texts': texts,
            'analyses': analyses,
            'comparison': comparison,
            'aop_evidences': aop_evidences,
            'aop_skeletons': aop_skeletons
        }

    def search_and_analyze(self, query: str, source: str = 'arxiv', max_results: int = 5) -> Dict:
        """Search for papers and analyze the top results.

        Args:
            query: The search query
            source: The search source
            max_results: Maximum number of results to analyze

        Returns:
            Dictionary containing search and analysis results
        """
        # Search for papers
        search_results = self.search_papers(query, source, max_results)
        
        # For demonstration, we'll return the search results
        # In a real implementation, you might download and analyze the papers
        return {
            'query': query,
            'source': source,
            'search_results': search_results,
            'analysis_count': min(max_results, len(search_results))
        }