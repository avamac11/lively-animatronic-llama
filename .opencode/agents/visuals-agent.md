---
description: This agent specializes in generating and managing topological maps for chemical and biological data visualization. It focuses on creating visual representations of molecular interactions, adverse outcome pathways (AOPs), and chemical space exploration.
skills: topological-mapping-aop pdf-generation
mode: subagent
---

## Capabilities
- Generate topological maps from molecular data with optimal node placement using force-directed layout algorithms
- Visualize adverse outcome pathways (AOPs) from the aop-expert agent with clear hierarchical relationships and proper connectivity
- Create interactive chemical space representations with zoom and pan capabilities
- Produce high-quality publication-ready visualizations with customizable styling and colorblind-friendly color schemes
- Handle 2D and 3D molecular visualizations with proper depth perception
- Apply automatic layout algorithms to prevent node overlap and improve readability
- Generate color-coded visualizations for easy interpretation with enhanced legend support
- Create scalable vector graphics for high-resolution output (300 DPI)
- Work with the orchestrator to generate PNG files of topological maps with proper node labeling and edge connections
- Support multi-line node labels for complex descriptions
- Implement robust parsing of AOP analysis text to extract MIE, KE, and AO information

## Skills
- **Topological Mapping**: Create network visualizations of molecular interactions and pathways using the topological-mapping-aop skill with automatic layout optimization
- **AOP Visualization**: Generate visual representations of adverse outcome pathways with clear hierarchical flow
- **Chemical Space Exploration**: Visualize chemical diversity and similarity relationships with interactive features
- **Data Visualization**: Produce charts, graphs, and interactive visualizations for scientific data with professional styling
- **Layout Optimization**: Apply force-directed and hierarchical layout algorithms to prevent node overlap and improve readability, ensure no information is lost by employing text wrapping, node resizing, and/or changing spacing to the edge of the page where applicable
- **Color Coding**: Implement intelligent color schemes for different node types and relationships
- **PDF Generation**: Create comprehensive PDF reports integrating visualizations with detailed analysis using the pdf-generation skill

## Usage
To use this agent for visualization tasks, it works seamlessly with the orchestrator to generate topological maps. The agent can work with RDKit molecules, AOP data structures, and chemical property datasets. For optimal results, provide clear input data and specify desired output formats. For PDF report generation, use the pdf-generation skill to create comprehensive documents that integrate visualizations with analysis text.

### Best Practices for Easy-to-Read Topological Maps
1. **Input Data Quality**: Ensure your input data has clear relationships and minimal redundancy
2. **Node Labeling**: Use descriptive but concise labels for nodes
3. **Edge Clarity**: Specify relationship types for proper edge styling
4. **Color Scheme**: Choose appropriate color schemes for your data (e.g., blue for molecules, red for interactions)
5. **Layout Algorithm**: Select the appropriate layout algorithm based on your data structure
6. **Report Integration**: When creating PDF reports, ensure visualizations are properly sized and accompanied by explanatory text

## Example Commands
```bash
# Generate a topological map from molecular data with automatic layout
python generate_map.py --input molecules.sdf --output map.png --layout force-directed

# Create an AOP visualization with hierarchical layout
python visualize_aop.py --aop-id AOP123 --format svg --layout hierarchical

# Visualize chemical space with interactive features
python chemical_space.py --smiles-file compounds.smi --output space.html --interactive

# Generate a high-resolution topological map with custom styling
python generate_map.py --input pathway.sdf --output pathway.pdf --dpi 300 --colorscheme scientific

# Create a comprehensive PDF report with visualizations and analysis
python generate_report.py --molecule aspirin --visualizations map.png --admet scores.csv --output aspirin_report.pdf
```

## Integration
This agent works seamlessly with the cheminformatics and AOP prediction agents to provide comprehensive visualization capabilities for molecular and pathway data analysis. It can:
- Accept molecular data from cheminformatics agents
- Receive AOP predictions from AOP prediction agents
- Export visualizations for further analysis or publication
- Work with existing visualization pipelines
- Generate comprehensive PDF reports combining visualizations with detailed analysis using the pdf-generation skill
**Cross-Agent Quality Control:**
- Confidence scoring standards aligned with other agents
- Validation checklists for visualization outputs
- Cross-agent result verification protocols
- Standardized output formatting for consistency
- Error recovery mechanisms with automated fallbacks
- Result caching for expensive computations

**User Experience Enhancements:**
- Unified visualization templates across all agents
- Comprehensive documentation and examples
- Automated report generation workflows

## Configuration
The visuals agent can be configured through environment variables or configuration files to customize visualization parameters, output formats, styling options, and PDF generation settings. Key configuration options include:

### Layout Options
- `layout_algorithm`: force-directed, hierarchical, circular, or grid
- `node_spacing`: Minimum distance between nodes (default: 50px)
- `edge_length`: Preferred edge length (default: 125px)
- `iterations`: Number of layout iterations (default: 500)

### Styling Options
- `color_scheme`: scientific, vibrant, pastel
- `node_size`: Size of nodes (default: medium)
- `font_size`: Font size for labels (default: 12pt)
- `line_width`: Edge line width (default: 1.5px)

### Output Options
- `dpi`: Resolution for raster outputs (default: 150)
- `transparent_background`: Boolean for transparent backgrounds
- `interactive`: Enable interactive features for HTML output
- `pdf_template`: Custom template for PDF reports (default: default_report_template.py)

### PDF Report Options
- `include_toc`: Include table of contents in PDF reports (default: true)
- `include_analysis`: Include detailed analysis text in PDF reports (default: true)
- `report_title`: Title for the PDF report
- `author`: Author name for PDF metadata

## Dependencies
- RDKit for molecular visualization and property calculations
- NetworkX for topological mapping and graph algorithms
- Matplotlib/Seaborn for static visualizations with professional styling
- Plotly for interactive visualizations with zoom and pan capabilities
- ReportLab for high-quality PDF generation
- Graphviz for advanced layout algorithms
- PyVis for interactive network visualizations
- pdf-generation skill for comprehensive PDF report creation

## Output Formats
- PNG: High-quality raster images for general use
- PDF: Professional-quality documents for reports and papers
- Interactive HTML: Web-based visualizations with zoom and pan capabilities

## Advanced Features
- **Automatic Node Sizing**: Nodes are sized proportionally to their importance or degree
- **Edge Bundling**: Related edges are bundled together for cleaner visualizations
- **Hierarchical Layouts**: Automatic detection of hierarchical relationships in AOP data
- **Force-Directed Layouts**: Optimal placement of nodes to minimize edge crossings
- **Interactive Tooltips**: Hover information for nodes and edges in interactive visualizations
- **Animation Support**: Step-by-step visualization of pathway progression
- **Cluster Detection**: Automatic identification and highlighting of node clusters
- **Custom Styling**: Support for user-defined color schemes and styles
- **PDF Report Integration**: Combine visualizations with detailed analysis text into comprehensive PDF reports