"""
Project Summary Report Template

This template provides a comprehensive structure for generating project summary reports.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import datetime


def create_project_summary_template():
    """Create a template structure for project summary reports"""
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=30,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        leading=24,
        spaceAfter=12,
        textColor=colors.darkred
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=14,
        leading=18,
        spaceAfter=6,
        textColor=colors.darkgreen
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=6
    )
    
    # Table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.gray),
    ])
    
    return {
        'styles': styles,
        'title_style': title_style,
        'heading_style': heading_style,
        'subheading_style': subheading_style,
        'normal_style': normal_style,
        'table_style': table_style,
        'page_size': letter,
        'margins': (0.5 * inch, 0.5 * inch, 0.5 * inch, 0.5 * inch)
    }


def generate_project_summary_report_content(template, project_name, project_data):
    """Generate content for project summary report using the template"""
    
    content = []
    
    # Title
    title = Paragraph(f"Project Summary Report: {project_name}", template['title_style'])
    content.append(title)
    content.append(Spacer(1, 0.2 * inch))
    
    # Report metadata
    report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata = f"Generated on: {report_date}"
    content.append(Paragraph(metadata, template['normal_style']))
    content.append(Spacer(1, 0.2 * inch))
    
    # Executive Summary
    content.append(Paragraph("Executive Summary", template['heading_style']))
    content.append(Paragraph(
        f"This report presents a comprehensive summary of the {project_name} project. "
        f"The analysis includes multiple molecules with their ADMET properties, "
        f"AOP pathways, and topological mappings.",
        template['normal_style']
    ))
    content.append(Spacer(1, 0.3 * inch))
    
    # Project Overview
    content.append(Paragraph("Project Overview", template['heading_style']))
    content.append(Paragraph(project_data.get('overview', 'No overview available.'), template['normal_style']))
    content.append(Spacer(1, 0.3 * inch))
    
    # Molecule Summary Table
    content.append(Paragraph("Molecule Summary", template['heading_style']))
    
    if 'molecules' in project_data and project_data['molecules']:
        # Create summary table
        summary_data = [
            ['Molecule', 'Molecular Weight', 'LogP', 'Bioavailability', 'Toxicity Risk', 'Status']
        ]
        
        for molecule in project_data['molecules']:
            summary_data.append([
                molecule.get('name', 'N/A'),
                f"{molecule.get('molecular_weight', 'N/A')}",
                f"{molecule.get('logp', 'N/A')}",
                f"{molecule.get('bioavailability', 'N/A'):.2f}",
                molecule.get('toxicity_risk', 'N/A'),
                molecule.get('status', 'N/A')
            ])
        
        summary_table = Table(summary_data, colWidths=[2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch, 1 * inch])
        summary_table.setStyle(template['table_style'])
        content.append(summary_table)
    else:
        content.append(Paragraph("No molecule data available.", template['normal_style']))
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Detailed Analysis by Molecule
    for molecule in project_data.get('molecules', []):
        molecule_name = molecule.get('name', 'Unknown')
        
        content.append(Paragraph(f"Detailed Analysis: {molecule_name}", template['heading_style']))
        
        # ADMET Summary
        content.append(Paragraph("ADMET Summary", template['subheading_style']))
        
        admet_data = [
            ['Property', 'Value', 'Status'],
            ['Absorption', molecule.get('absorption', 'N/A'), molecule.get('absorption_status', 'N/A')],
            ['Distribution', molecule.get('distribution', 'N/A'), molecule.get('distribution_status', 'N/A')],
            ['Metabolism', molecule.get('metabolism', 'N/A'), molecule.get('metabolism_status', 'N/A')],
            ['Excretion', molecule.get('excretion', 'N/A'), molecule.get('excretion_status', 'N/A')],
            ['Toxicity', molecule.get('toxicity', 'N/A'), molecule.get('toxicity_status', 'N/A')],
        ]
        
        admet_table = Table(admet_data, colWidths=[2.5 * inch, 2 * inch, 1.5 * inch])
        admet_table.setStyle(template['table_style'])
        content.append(admet_table)
        
        # AOP Summary
        content.append(Paragraph("AOP Summary", template['subheading_style']))
        
        if 'aop_summary' in molecule:
            aop_summary = molecule['aop_summary']
            content.append(Paragraph(f"Key Events: {aop_summary.get('key_events', 'N/A')}", template['normal_style']))
            content.append(Paragraph(f"Adverse Outcomes: {aop_summary.get('adverse_outcomes', 'N/A')}", template['normal_style']))
            content.append(Paragraph(f"Risk Level: {aop_summary.get('risk_level', 'N/A')}", template['normal_style']))
        
        # Recommendations
        if 'recommendations' in molecule and molecule['recommendations']:
            content.append(Paragraph("Recommendations:", template['subheading_style']))
            for rec in molecule['recommendations']:
                content.append(Paragraph(f"• {rec}", template['normal_style']))
        
        content.append(Spacer(1, 0.3 * inch))
    
    # Project Statistics
    content.append(Paragraph("Project Statistics", template['heading_style']))
    
    if 'statistics' in project_data:
        stats_data = [['Metric', 'Value']]
        for metric, value in project_data['statistics'].items():
            stats_data.append([metric, f"{value}"])
        
        stats_table = Table(stats_data, colWidths=[3 * inch, 3 * inch])
        stats_table.setStyle(template['table_style'])
        content.append(stats_table)
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Overall Findings
    content.append(Paragraph("Overall Findings", template['heading_style']))
    content.append(Paragraph(project_data.get('findings', 'No findings available.'), template['normal_style']))
    content.append(Spacer(1, 0.3 * inch))
    
    # Project Recommendations
    content.append(Paragraph("Project Recommendations", template['heading_style']))
    
    if 'recommendations' in project_data and project_data['recommendations']:
        for rec in project_data['recommendations']:
            content.append(Paragraph(f"• {rec}", template['normal_style']))
    else:
        content.append(Paragraph("No project-wide recommendations at this time.", template['normal_style']))
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Conclusion
    content.append(Paragraph("Conclusion", template['heading_style']))
    content.append(Paragraph(project_data.get('conclusion', 'No conclusion available.'), template['normal_style']))
    
    return content