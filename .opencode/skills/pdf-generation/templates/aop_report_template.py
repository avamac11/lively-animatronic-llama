"""
AOP Report Template

This template provides a comprehensive structure for generating AOP reports.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import datetime


def create_aop_report_template():
    """Create a template structure for AOP reports"""
    
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
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        spaceAfter=6,
        textColor=colors.darkblue,
        bold=1
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
        'subtitle_style': subtitle_style,
        'heading_style': heading_style,
        'subheading_style': subheading_style,
        'normal_style': normal_style,
        'table_style': table_style,
        'page_size': letter,
        'margins': (0.5 * inch, 0.5 * inch, 0.5 * inch, 0.5 * inch)
    }


def generate_aop_report_content(template, molecule_name, aop_data):
    """Generate content for AOP report using the template"""
    
    content = []
    
    # Title
    title = Paragraph(f"AOP Analysis Report: {molecule_name}", template['title_style'])
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
        f"This report presents the Adverse Outcome Pathway (AOP) analysis for {molecule_name}. "
        f"The analysis includes molecular initiating events, key events, and potential adverse outcomes.",
        template['normal_style']
    ))
    content.append(Spacer(1, 0.3 * inch))
    
    # Molecular Information
    content.append(Paragraph("Molecular Information", template['heading_style']))
    
    # Create molecular info table
    molecular_data = [
        ['Property', 'Value'],
        ['Molecule Name', molecule_name],
        ['SMILES', aop_data.get('smiles', 'N/A')],
        ['Molecular Weight', f"{aop_data.get('molecular_weight', 'N/A')}"],
        ['LogP', f"{aop_data.get('logp', 'N/A')}"],
        ['H-Bond Donors', f"{aop_data.get('hbond_donors', 'N/A')}"],
        ['H-Bond Acceptors', f"{aop_data.get('hbond_acceptors', 'N/A')}"],
    ]
    
    molecular_table = Table(molecular_data, colWidths=[3 * inch, 3 * inch])
    molecular_table.setStyle(template['table_style'])
    content.append(molecular_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Molecular Initiating Events
    content.append(Paragraph("Molecular Initiating Events", template['heading_style']))
    
    if 'molecular_initiating_events' in aop_data and aop_data['molecular_initiating_events']:
        mie_data = [['Event', 'Confidence', 'Description']]
        for mie in aop_data['molecular_initiating_events']:
            mie_data.append([
                mie.get('name', 'N/A'),
                f"{mie.get('confidence', 0):.2f}",
                mie.get('description', 'N/A')
            ])
        
        mie_table = Table(mie_data, colWidths=[2.5 * inch, 1 * inch, 2.5 * inch])
        mie_table.setStyle(template['table_style'])
        content.append(mie_table)
    else:
        content.append(Paragraph("No molecular initiating events identified.", template['normal_style']))
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Key Events
    content.append(Paragraph("Key Events in AOP", template['heading_style']))
    
    if 'key_events' in aop_data and aop_data['key_events']:
        for event in aop_data['key_events']:
            content.append(Paragraph(f"• {event.get('name', 'N/A')}", template['subheading_style']))
            content.append(Paragraph(event.get('description', 'N/A'), template['normal_style']))
            content.append(Spacer(1, 0.1 * inch))
    else:
        content.append(Paragraph("No key events identified.", template['normal_style']))
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Adverse Outcomes
    content.append(Paragraph("Adverse Outcomes", template['heading_style']))
    
    if 'adverse_outcomes' in aop_data and aop_data['adverse_outcomes']:
        ao_data = [['Outcome', 'Severity', 'Evidence']]
        for ao in aop_data['adverse_outcomes']:
            ao_data.append([
                ao.get('name', 'N/A'),
                ao.get('severity', 'N/A'),
                ao.get('evidence', 'N/A')
            ])
        
        ao_table = Table(ao_data, colWidths=[3 * inch, 1.5 * inch, 1.5 * inch])
        ao_table.setStyle(template['table_style'])
        content.append(ao_table)
    else:
        content.append(Paragraph("No adverse outcomes identified.", template['normal_style']))
    
    content.append(Spacer(1, 0.3 * inch))
    
    # Recommendations
    content.append(Paragraph("Recommendations", template['heading_style']))
    
    if 'recommendations' in aop_data and aop_data['recommendations']:
        for rec in aop_data['recommendations']:
            content.append(Paragraph(f"• {rec}", template['normal_style']))
    else:
        content.append(Paragraph("No specific recommendations at this time.", template['normal_style']))
    
    return content