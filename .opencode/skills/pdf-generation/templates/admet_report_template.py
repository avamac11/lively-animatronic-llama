"""
ADMET Report Template

This template provides a comprehensive structure for generating ADMET reports.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import datetime


def create_admet_report_template():
    """Create a template structure for ADMET reports"""
    
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


def generate_admet_report_content(template, molecule_name, admet_data):
    """Generate content for ADMET report using the template"""
    
    content = []
    
    # Title
    title = Paragraph(f"ADMET Analysis Report: {molecule_name}", template['title_style'])
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
        f"This report presents the ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) "
        f"analysis for {molecule_name}. The analysis includes key pharmacokinetic and pharmacodynamic properties.",
        template['normal_style']
    ))
    content.append(Spacer(1, 0.3 * inch))
    
    # Molecular Information
    content.append(Paragraph("Molecular Information", template['heading_style']))
    
    # Create molecular info table
    molecular_data = [
        ['Property', 'Value'],
        ['Molecule Name', molecule_name],
        ['SMILES', admet_data.get('smiles', 'N/A')],
        ['Molecular Weight', f"{admet_data.get('molecular_weight', 'N/A')}"],
        ['LogP', f"{admet_data.get('logp', 'N/A')}"],
        ['H-Bond Donors', f"{admet_data.get('hbond_donors', 'N/A')}"],
        ['H-Bond Acceptors', f"{admet_data.get('hbond_acceptors', 'N/A')}"],
    ]
    
    molecular_table = Table(molecular_data, colWidths=[3 * inch, 3 * inch])
    molecular_table.setStyle(template['table_style'])
    content.append(molecular_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Absorption Properties
    content.append(Paragraph("Absorption Properties", template['heading_style']))
    
    absorption_data = [
        ['Property', 'Value', 'Interpretation'],
        ['Solubility (AqSolDB)', f"{admet_data.get('Solubility_AqSolDB', 'N/A'):.2f}", 
         admet_data.get('solubility_interpretation', 'N/A')],
        ['Oral Bioavailability (Ma)', f"{admet_data.get('Bioavailability_Ma', 'N/A'):.2f}",
         admet_data.get('bioavailability_interpretation', 'N/A')],
        ['P-glycoprotein Substrate', f"{admet_data.get('Pgp_Broccatelli', 'N/A'):.2f}",
         admet_data.get('pgp_interpretation', 'N/A')],
    ]
    
    absorption_table = Table(absorption_data, colWidths=[3 * inch, 1.5 * inch, 1.5 * inch])
    absorption_table.setStyle(template['table_style'])
    content.append(absorption_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Distribution Properties
    content.append(Paragraph("Distribution Properties", template['heading_style']))
    
    distribution_data = [
        ['Property', 'Value', 'Interpretation'],
        ['Blood-Brain Barrier Permeability', f"{admet_data.get('BBB_Martins', 'N/A'):.2f}",
         admet_data.get('bbb_interpretation', 'N/A')],
        ['Plasma Protein Binding', f"{admet_data.get('PPB_Adams', 'N/A'):.2f}",
         admet_data.get('ppb_interpretation', 'N/A')],
        ['Volume of Distribution', f"{admet_data.get('VDss_Lombardo', 'N/A'):.2f}",
         admet_data.get('vd_interpretation', 'N/A')],
    ]
    
    distribution_table = Table(distribution_data, colWidths=[3 * inch, 1.5 * inch, 1.5 * inch])
    distribution_table.setStyle(template['table_style'])
    content.append(distribution_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Metabolism Properties
    content.append(Paragraph("Metabolism Properties", template['heading_style']))
    
    metabolism_data = [
        ['Property', 'Value', 'Interpretation'],
        ['Half-life (Obach)', f"{admet_data.get('Half_Life_Obach', 'N/A'):.2f} hours",
         admet_data.get('half_life_interpretation', 'N/A')],
        ['Clearance (Hepatocyte, AZ)', f"{admet_data.get('Clearance_Hepatocyte_AZ', 'N/A'):.2f} mL/min/kg",
         admet_data.get('clearance_interpretation', 'N/A')],
        ['CYP3A4 Inhibition', f"{admet_data.get('CYP3A4_Veith', 'N/A'):.2f}",
         admet_data.get('cy3a4_interpretation', 'N/A')],
    ]
    
    metabolism_table = Table(metabolism_data, colWidths=[3 * inch, 2 * inch, 1 * inch])
    metabolism_table.setStyle(template['table_style'])
    content.append(metabolism_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Toxicity Properties
    content.append(Paragraph("Toxicity Properties", template['heading_style']))
    
    toxicity_data = [
        ['Property', 'Value', 'Interpretation'],
        ['Ames Mutagenicity', f"{admet_data.get('AMES', 'N/A'):.2f}",
         admet_data.get('ames_interpretation', 'N/A')],
        ['hERG Inhibition', f"{admet_data.get('hERG', 'N/A'):.2f}",
         admet_data.get('herg_interpretation', 'N/A')],
        ['Drug-Induced Liver Injury', f"{admet_data.get('DILI', 'N/A'):.2f}",
         admet_data.get('dili_interpretation', 'N/A')],
        ['Skin Sensitization', f"{admet_data.get('Skin_Sensitization', 'N/A'):.2f}",
         admet_data.get('skin_sensitization_interpretation', 'N/A')],
    ]
    
    toxicity_table = Table(toxicity_data, colWidths=[3 * inch, 1.5 * inch, 1.5 * inch])
    toxicity_table.setStyle(template['table_style'])
    content.append(toxicity_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Drug-likeness Assessment
    content.append(Paragraph("Drug-likeness Assessment", template['heading_style']))
    
    drug_likeness_data = [
        ['Property', 'Value', 'Status'],
        ['Lipinski Rule of 5', admet_data.get('lipinski_status', 'N/A'), ''],  # Empty third column for alignment
        ['Molecular Weight', f"{admet_data.get('molecular_weight', 'N/A')}", 
         admet_data.get('mw_status', 'N/A')],
        ['LogP', f"{admet_data.get('logp', 'N/A')}", admet_data.get('logp_status', 'N/A')],
        ['H-Bond Donors', f"{admet_data.get('hbond_donors', 'N/A')}", 
         admet_data.get('hbd_status', 'N/A')],
        ['H-Bond Acceptors', f"{admet_data.get('hbond_acceptors', 'N/A')}", 
         admet_data.get('hba_status', 'N/A')],
    ]
    
    drug_likeness_table = Table(drug_likeness_data, colWidths=[3 * inch, 2 * inch, 1 * inch])
    drug_likeness_table.setStyle(template['table_style'])
    content.append(drug_likeness_table)
    content.append(Spacer(1, 0.3 * inch))
    
    # Summary and Recommendations
    content.append(Paragraph("Summary and Recommendations", template['heading_style']))
    content.append(Paragraph(admet_data.get('summary', 'No summary available.'), template['normal_style']))
    content.append(Spacer(1, 0.2 * inch))
    
    if 'recommendations' in admet_data and admet_data['recommendations']:
        content.append(Paragraph("Recommendations:", template['subheading_style']))
        for rec in admet_data['recommendations']:
            content.append(Paragraph(f"• {rec}", template['normal_style']))
    
    return content