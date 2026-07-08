"""
Basic Usage Examples for Paper Analysis Skill

This file demonstrates basic usage of the paper analysis skill components.
"""

from paper_analysis import (
    PaperAnalysisSkill,
    AOPIntegrator,
    PaperSearcher,
    ArxivSearcher,
    PubMedSearcher,
    PaperReaderWrapper,
    KeyPointExtractor,
    ContentAnalyzer,
    PaperComparator,
    InformationCompressor,
    CitationExtractor,
    AnalysisVisualizer
)


def demonstrate_basic_usage():
    """Demonstrate basic usage of the paper analysis skill."""
    print("=== Basic Usage Examples ===")
    
    # Example 1: Using PaperAnalysisSkill (main orchestrator)
    print("\n1. Using PaperAnalysisSkill (main orchestrator):")
    skill = PaperAnalysisSkill()
    
    # Configure with API keys (if available)
    skill.configure({
        "paper_search": {
            "arxiv_api_key": "your_api_key_here",
            "pubmed_api_key": "your_api_key_here"
        }
    })
    
    # Search for papers
    search_results = skill.search_papers("adverse outcome pathway", source="arxiv", max_results=3)
    print(f"Found {len(search_results)} papers")
    
    # Example 2: AOP Integration
    print("\n2. AOP Integration:")
    integrator = AOPIntegrator()
    
    # Sample text (in real usage, this would be extracted from a paper)
    sample_text = """
    The study investigates the molecular initiating event where chemical X binds to protein Y,
    causing activation of pathway Z. This leads to phosphorylation of kinase A, which then
    causes inhibition of target B. The final adverse outcome is liver toxicity as measured by
    increased ALT levels in treated animals.
    """
    
    # Extract AOP evidence
    aop_evidence = integrator.extract_aop_evidence(sample_text)
    print(f"Extracted {len(aop_evidence['molecular_initiating_events'])} MIEs")
    print(f"Extracted {len(aop_evidence['key_events'])} key events")
    print(f"Extracted {len(aop_evidence['adverse_outcomes'])} adverse outcomes")
    
    # Build AOP skeleton
    aop_skeleton = integrator.build_aop_skeleton(sample_text)
    print(f"AOP confidence score: {aop_skeleton['confidence_score']:.2f}")
    print(f"AOP completeness score: {aop_skeleton['completeness_score']:.2f}")
    
    # Validate AOP evidence
    validation = integrator.validate_aop_evidence(aop_evidence)
    print(f"AOP validation complete: {validation['is_complete']}")
    
    # Example 3: Individual Components
    print("\n3. Individual Components:")
    
    # Paper reading
    reader = PaperReaderWrapper()
    # text = reader.read_paper("example.pdf")  # Uncomment to read actual file
    
    # Key point extraction
    extractor = KeyPointExtractor()
    key_points = extractor.extract_key_points(sample_text)
    print(f"Extracted {len(key_points)} key points")
    
    # Content analysis
    analyzer = ContentAnalyzer()
    analysis = analyzer.analyze(sample_text)
    print(f"Found {len(analysis['themes'])} themes")
    print(f"Found {len(analysis['entities'])} entities")
    print(f"Found {len(analysis['relationships'])} relationships")
    
    # Information compression
    compressor = InformationCompressor()
    summary = compressor.compress(sample_text, max_length=100)
    print(f"Compressed summary: {summary}")
    
    # Citation extraction
    citation_extractor = CitationExtractor()
    citations = citation_extractor.extract_citations(sample_text)
    print(f"Found {len(citations)} citations")
    
    # Paper comparison
    comparator = PaperComparator()
    comparison = comparator.compare([sample_text, sample_text[:100] + " different content"])
    print(f"Comparison complete with commonality score: {comparison['commonality_score']:.2f}")
    
    print("\n=== Examples Complete ===")


if __name__ == "__main__":
    demonstrate_basic_usage()