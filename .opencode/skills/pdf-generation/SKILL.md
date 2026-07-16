---
name: pdf-generation
description: A skill for generating PDF reports for AOP and ADMET analysis, including topological maps and project summaries.
---

## Overview
This skill provides comprehensive PDF generation capabilities for the AOP project, including ADMET scores, AOP pathways, topological maps, and project summaries. The skill uses reportlab for PDF creation and integrates with existing visualization tools. It complies with the project's data structures and formats, ensuring that generated reports are consistent and informative, with a detailed layout that includes tables, charts, and chemical structures.

## Features
- Generate AOP summary reports with detailed pathway information
- Create ADMET score reports with comprehensive analysis with specific details, beyond just absorption, distribution, metabolism, excretion, and toxicity scores. Especially include any that have a greater impact on the molecule's overall profile, such as bioavailability, half-life, and potential drug-drug interactions.
- Include topological maps and visualizations in PDF reports from analysis results
- Generate combined project summaries
- Support for tables, charts, and chemical structures
- Modular architecture for easy extension
- All information is from the AOP project and related analyses produced by agents and other skills
- The orchestrator agent can call this skill to generate PDF reports based on the results of AOP and ADMET analyses, as well as topological maps and other visualizations.
- Always include the png topological map in the PDF report, even if the user does not explicitly request it. - Generate a pdf only whenprompted by the user

## Dependencies
- reportlab: PDF generation library
- matplotlib: Chart and visualization generation
- seaborn: Statistical data visualization
- rdkit: Chemical structure rendering
- pandas: Data manipulation and table generation

## Usage

### Basic PDF Generation
```python
from pdf_generation import PDFGenerator

# Create a PDF generator instance
generator = PDFGenerator()

# Generate a PDF report
generator.generate_aop_report(
    molecule_name="Aspirin",
    aop_data=aop_results,
    output_path="aspirin_aop_report.pdf"
)
```

### ADMET Score Report
```python
from pdf_generation import PDFGenerator

generator = PDFGenerator()
generator.generate_admet_report(
    molecule_name="Paracetamol",
    admet_scores=admet_results,
    output_path="paracetamol_admet_report.pdf"
)
```

### Topological Map Report
```python
from pdf_generation import PDFGenerator

generator = PDFGenerator()
generator.generate_topological_map_report(
    molecule_name="Ibuprofen",
    map_data=topological_results,
    output_path="ibuprofen_map_report.pdf"
)
```

### Combined Project Summary
```python
from pdf_generation import PDFGenerator

generator = PDFGenerator()
generator.generate_project_summary(
    project_name="AOP Analysis Project",
    molecules_data=all_results,
    output_path="project_summary.pdf"
)
```

## Integration with Existing Workflows

The PDF generation skill integrates seamlessly with existing AOP and ADMET analysis workflows:

```python
# Example: Generate PDF after AOP analysis
from aop_analysis import analyze_molecule
aop_results = analyze_molecule("Aspirin")

from pdf_generation import PDFGenerator
generator = PDFGenerator()
generator.generate_aop_report(
    molecule_name="Aspirin",
    aop_data=aop_results,
    output_path=f"{aspirin_aop_report.pdf}"
)
```

## Configuration

The skill supports basic configuration through environment variables:

- `PDF_OUTPUT_DIR`: Default output directory for generated PDFs (default: `./output/pdf/`)
- `PDF_TEMPLATE_DIR`: Directory containing custom templates (default: `./skills/pdf-generation/templates/`)

## Templates

The skill includes built-in templates for different report types. Custom templates can be added to the `templates/` directory.

### Template Structure
```
templates/
├── aop_report_template.py
├── admet_report_template.py
├── topological_map_template.py
└── project_summary_template.py
```

## Error Handling

The skill includes comprehensive error handling for:
- Missing dependencies
- Invalid data formats
- File system errors
- PDF generation failures

## Best Practices

1. **Data Validation**: Always validate input data before generating PDFs
2. **Error Handling**: Use try-catch blocks to handle potential errors gracefully
3. **File Management**: Ensure output directories exist before generating PDFs
4. **Resource Management**: Close PDF objects properly after generation
5. **Performance**: For large datasets, consider generating PDFs in batches

## Examples

See the `examples/` directory for complete usage examples:
- `aop_report_example.py`: AOP report generation example
- `admet_report_example.py`: ADMET score report example
- `topological_map_example.py`: Topological map report example
- `project_summary_example.py`: Project summary generation example

## Troubleshooting

### Common Issues

1. **Missing Dependencies**: Ensure all required packages are installed
2. **File Permissions**: Check write permissions for the output directory
3. **Data Format Errors**: Validate input data structure and content
4. **Memory Issues**: Large PDFs may require more memory; consider batch processing

### Debugging

Enable debug mode by setting the `PDF_DEBUG` environment variable:

```bash
export PDF_DEBUG=true
```

This will provide detailed logging information for troubleshooting.

## Contributing

Contributions to the PDF generation skill are welcome. Please follow these guidelines:

1. **Code Style**: Follow PEP 8 guidelines for Python code
2. **Documentation**: Update documentation for any new features or changes
3. **Testing**: Add tests for new functionality
4. **Backward Compatibility**: Ensure changes don't break existing functionality