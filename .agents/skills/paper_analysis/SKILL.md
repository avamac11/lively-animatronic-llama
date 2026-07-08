---
name: paper-analysis
schema_version: 1.0
description: Enables searching, reading, analyzing, and comparing academic papers with AOP integration capabilities
---

# Paper Analysis Skill

## Overview
This skill enables searching for academic papers, reading them, extracting key points, analyzing content, and comparing/compressing information. It supports multiple paper formats (PDF, HTML, plain text) and includes citation analysis, reference extraction, and collaboration features.

## Features
- **Paper Search**: Search for academic papers using various sources (arXiv, PubMed, Google Scholar, etc.)
- **Paper Reading**: Extract text from PDF, HTML, and plain text files
- **Key Point Extraction**: Identify and extract key points from papers
- **Content Analysis**: Analyze paper content for themes, entities, and relationships
- **Comparison**: Compare information across multiple papers
- **Information Compression**: Summarize and compress paper content
- **Citation Analysis**: Extract and analyze citations and references
- **Collaboration**: Support team-based research with shared annotations and insights
- **Visualization**: Generate visualizations of paper relationships and analysis results

## Dependencies
- Python 3.8+
- `pdfplumber` for PDF text extraction
- `pypdf` for PDF processing
- `requests` for API interactions
- `networkx` for graph-based analysis
- `matplotlib` for visualization
- `spaCy` for NLP tasks (optional)
- `transformers` for advanced text analysis (optional)

## Installation
```bash
pip install pdfplumber pypdf requests networkx matplotlib
# Optional for advanced NLP
pip install spacy transformers
python -m spacy download en_core_web_sm
```

## Usage

### Search for Papers
```python
from paper_analysis import PaperSearcher

# Search using arXiv API
searcher = PaperSearcher()
results = searcher.search_arxiv("adverse outcome pathway", max_results=10)

# Search using PubMed API
pubmed_results = searcher.search_pubmed("liver toxicity", max_results=5)
```

### Read Papers
```python
from paper_analysis import PaperReader

# Read PDF file
reader = PaperReader()
pdf_text = reader.read_pdf("paper.pdf")

# Read HTML file
html_text = reader.read_html("paper.html")

# Read plain text file
text = reader.read_text("paper.txt")
```

### Extract Key Points
```python
from paper_analysis import KeyPointExtractor

extractor = KeyPointExtractor()
key_points = extractor.extract_key_points(pdf_text)
print("Key Points:", key_points)
```

### Analyze Content
```python
from paper_analysis import ContentAnalyzer

analyzer = ContentAnalyzer()
analysis = analyzer.analyze(pdf_text)
print("Themes:", analysis.themes)
print("Entities:", analysis.entities)
print("Relationships:", analysis.relationships)
```

### Compare Papers
```python
from paper_analysis import PaperComparator

comparator = PaperComparator()
comparison = comparator.compare([paper1_text, paper2_text, paper3_text])
print("Common Themes:", comparison.common_themes)
print("Differences:", comparison.differences)
```

### Compress Information
```python
from paper_analysis import InformationCompressor

compressor = InformationCompressor()
summary = compressor.compress(pdf_text, max_length=500)
print("Summary:", summary)
```

### Extract Citations
```python
from paper_analysis import CitationExtractor

extractor = CitationExtractor()
citations = extractor.extract_citations(pdf_text)
print("Citations:", citations)
```

### Visualize Analysis
```python
from paper_analysis import AnalysisVisualizer

visualizer = AnalysisVisualizer()
visualizer.visualize_relationships(analysis.relationships, output_file="relationships.png")
visualizer.visualize_comparison(comparison, output_file="comparison.png")
```

## Integration with AOP Skill
This skill can integrate with the AOP skill to extract mechanistic evidence chains from papers:

```python
from paper_analysis import AOPIntegrator

integrator = AOPIntegrator()
aop_evidence = integrator.extract_aop_evidence(pdf_text)
print("AOP Evidence:", aop_evidence)

# Build a complete AOP skeleton
aop_skeleton = integrator.build_aop_skeleton(pdf_text)
print("AOP Skeleton:", aop_skeleton)

# Validate AOP evidence
aop_validation = integrator.validate_aop_evidence(aop_evidence)
print("AOP Validation:", aop_validation)
```


## Architecture
The skill is designed to be modular and extensible:

```
PaperAnalysisSkill
├── PaperSearcher
│   ├── ArxivSearcher
│   ├── PubMedSearcher
│   ├── GoogleScholarSearcher
│   └── CustomSearcher
├── PaperReader
│   ├── PDFReader
│   ├── HTMLReader
│   └── TextReader
├── KeyPointExtractor
├── ContentAnalyzer
├── PaperComparator
├── InformationCompressor
├── CitationExtractor
├── AnalysisVisualizer
├── AOPIntegrator
└── PaperAnalysisSkill (main orchestrator)
```

## Configuration
The skill can be configured through a configuration file:

```python
from paper_analysis import PaperAnalysisSkill

skill = PaperAnalysisSkill()
skill.configure({
    "paper_search": {
        "arxiv_api_key": "your_api_key",
        "pubmed_api_key": "your_api_key"
    },
    "nlp": {
        "model": "spacy",
        "use_transformers": False
    },
    "collaboration": {
        "shared_storage_path": "/path/to/shared/storage"  # For future collaboration features
    }
})
```

## Best Practices
1. **Paper Search**: Use specific queries to get relevant results
2. **Text Extraction**: Ensure proper handling of different paper formats
3. **Key Point Extraction**: Focus on abstract, introduction, and conclusion sections
4. **Content Analysis**: Use domain-specific NLP models for better results
5. **Comparison**: Normalize text before comparing across papers
6. **Information Compression**: Maintain key information while reducing length
7. **Citation Analysis**: Validate extracted citations against reference lists
8. **Visualization**: Use appropriate visualization techniques for different types of analysis

## Limitations
- Advanced NLP features require additional dependencies
- Citation extraction accuracy depends on paper formatting
- Collaboration features are planned for future implementation
- Performance may vary with large paper collections

## Future Enhancements
- Support for more paper search sources
- Advanced NLP models for better analysis
- Machine learning for automated key point extraction
- Integration with reference managers
- Support for version control of annotations
- Advanced visualization techniques

## Examples
See the `examples/` directory for more detailed examples of using this skill.

## Usage with PaperAnalysisSkill (Main Orchestrator)
The `PaperAnalysisSkill` class provides a convenient way to use all components together:

```python
from paper_analysis import PaperAnalysisSkill

# Create and configure the skill
skill = PaperAnalysisSkill()
skill.configure({
    "paper_search": {
        "arxiv_api_key": "your_api_key"
    }
})

# Complete workflow for analyzing a paper
results = skill.analyze_paper_workflow("paper.pdf")
print("Analysis Results:", results)

# Search and analyze papers
search_results = skill.search_and_analyze("adverse outcome pathway", source="arxiv")
print("Search Results:", search_results)
```
