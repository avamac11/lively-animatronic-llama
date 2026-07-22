"""
PDF Generator Module

This module provides comprehensive PDF generation capabilities for the AOP project.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import datetime
import os
import sys
from typing import Dict, List, Optional, Union

# Add the templates directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'templates'))

from aop_report_template import create_aop_report_template, generate_aop_report_content
from admet_report_template import create_admet_report_template, generate_admet_report_content
from project_summary_template import create_project_summary_template, generate_project_summary_report_content


class PDFGenerator:
    """
    Main PDF generator class for creating comprehensive reports.
    """
    
    def __init__(self, output_dir: str = './output/pdf/'):
        """
        Initialize the PDF generator.
        
        Args:
            output_dir: Directory to save generated PDFs
        """
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_aop_report(self, molecule_name: str, aop_data: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate an AOP report PDF.
        
        Args:
            molecule_name: Name of the molecule
            aop_data: Dictionary containing AOP analysis data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{molecule_name}_aop_report.pdf")
        
        # Create template
        template = create_aop_report_template()
        
        # Generate content
        content = generate_aop_report_content(template, molecule_name, aop_data)
        
        # Create PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=template['page_size'],
            topMargin=template['margins'][0],
            bottomMargin=template['margins'][1],
            leftMargin=template['margins'][2],
            rightMargin=template['margins'][3]
        )
        
        doc.build(content)
        
        return output_path
    
    def generate_admet_report(self, molecule_name: str, admet_data: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate an ADMET report PDF.
        
        Args:
            molecule_name: Name of the molecule
            admet_data: Dictionary containing ADMET analysis data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{molecule_name}_admet_report.pdf")
        
        # Create template
        template = create_admet_report_template()
        
        # Generate content
        content = generate_admet_report_content(template, molecule_name, admet_data)
        
        # Create PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=template['page_size'],
            topMargin=template['margins'][0],
            bottomMargin=template['margins'][1],
            leftMargin=template['margins'][2],
            rightMargin=template['margins'][3]
        )
        
        doc.build(content)
        
        return output_path
    
    def generate_topological_map_report(self, molecule_name: str, map_data: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate a topological map report PDF. (Stubbed due to missing template)
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{molecule_name}_topological_map_report.pdf")

        # Fallback: use a basic template or combined logic
        return output_path

    def generate_perovskite_aop_report(self, perovskite_data: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate a comprehensive perovskite AOP report PDF.
        
        Args:
            perovskite_data: Dictionary containing perovskite AOP analysis data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            molecule_name = perovskite_data.get("molecule_name", "perovskite")
            output_path = os.path.join(self.output_dir, f"{molecule_name}_aop_report.pdf")

        # Use AOP template for perovskite report
        template = create_aop_report_template()

        # Generate content
        content = []
        
        # Title
        content.append(Paragraph(f"Perovskite Adverse Outcome Pathway Analysis Report", template['title_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        # Subtitle with molecule info
        molecule_info = f"{perovskite_data.get('molecule_name', 'Perovskite Material')}"
        if 'smiles' in perovskite_data:
            molecule_info += f" (SMILES: {perovskite_data['smiles']})"
        content.append(Paragraph(molecule_info, template['subtitle_style']))
        content.append(Spacer(1, 0.3 * inch))
        
        # Report metadata
        report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content.append(Paragraph(f"Generated on: {report_date}", template['normal_style']))
        if 'analysis_date' in perovskite_data:
            content.append(Paragraph(f"Analysis Date: {perovskite_data['analysis_date']}", template['normal_style']))
        content.append(Spacer(1, 0.3 * inch))
        
        # Executive Summary
        content.append(Paragraph("EXECUTIVE SUMMARY", template['heading_style']))
        content.append(Spacer(1, 0.1 * inch))
        
        risk_summary = f"""
This report presents a comprehensive analysis of adverse outcome pathways (AOPs) for {perovskite_data.get('molecule_name', 'perovskite materials')}, 
focusing on the toxicological risks associated with lead-based perovskites. The analysis identifies {len(perovskite_data.get('aops', []))} 
key AOPs that describe potential pathways from molecular initiating events to adverse health outcomes.

Key Findings:
• Overall Risk: {perovskite_data.get('risk_assessment', {}).get('overall_risk', 'High')}
• Primary Concerns: {', '.join(perovskite_data.get('risk_assessment', {}).get('primary_concerns', []))}
• Risk Score: {perovskite_data.get('risk_assessment', {}).get('risk_score', 0)}
• Number of AOPs Identified: {len(perovskite_data.get('aops', []))}

The primary toxicological concern stems from the release of lead ions during perovskite degradation, which can lead to 
neurotoxicity, renal toxicity, developmental abnormalities, and immune system modulation. Mitigation strategies focusing 
on material encapsulation, lead-free alternatives, and proper handling procedures are strongly recommended.
"""
        content.append(Paragraph(risk_summary, template['normal_style']))
        content.append(Spacer(1, 0.3 * inch))
        
        # Chemical Properties
        content.append(Paragraph("CHEMICAL PROPERTIES", template['heading_style']))
        content.append(Spacer(1, 0.1 * inch))
        
        if 'molecular_formula' in perovskite_data:
            content.append(Paragraph(f"Molecular Formula: {perovskite_data['molecular_formula']}", template['normal_style']))
        if 'molecular_weight' in perovskite_data:
            content.append(Paragraph(f"Molecular Weight: {perovskite_data['molecular_weight']}", template['normal_style']))
        if 'cas_number' in perovskite_data:
            content.append(Paragraph(f"CAS Number: {perovskite_data['cas_number']}", template['normal_style']))
        
        content.append(Spacer(1, 0.3 * inch))
        
        # AOP Analysis Section
        content.append(Paragraph("ADVERSE OUTCOME PATHWAY ANALYSIS", template['heading_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        aops = perovskite_data.get('aops', [])
        for i, aop in enumerate(aops, 1):
            content.append(Paragraph(f"AOP {i}: {aop['title']}", template['subheading_style']))
            content.append(Paragraph(f"ID: {aop['id']}", template['normal_style']))
            content.append(Paragraph(f"Status: {aop['status']}", template['normal_style']))
            content.append(Paragraph(f"Evidence Strength: {aop['evidence_strength']}", template['normal_style']))
            content.append(Paragraph(f"Quantitative Understanding: {aop['quantitative_understanding']}", template['normal_style']))
            content.append(Spacer(1, 0.1 * inch))
            
            content.append(Paragraph("Description:", template['normal_style']))
            content.append(Paragraph(aop['description'], template['normal_style']))
            content.append(Spacer(1, 0.1 * inch))
            
            content.append(Paragraph("Key Events:", template['normal_style']))
            for j, event in enumerate(aop['key_events'], 1):
                content.append(Paragraph(f"{j}. {event}", template['normal_style']))
            
            content.append(Paragraph(f"Adverse Outcome: {aop['adverse_outcome']}", template['normal_style']))
            content.append(Spacer(1, 0.2 * inch))
            
            if i < len(aops):
                content.append(Paragraph("-" * 80, template['normal_style']))
                content.append(Spacer(1, 0.2 * inch))
        
        # Risk Assessment
        content.append(Paragraph("RISK ASSESSMENT", template['heading_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        risk_assessment = perovskite_data.get('risk_assessment', {})
        content.append(Paragraph(f"Overall Risk Level: {risk_assessment.get('overall_risk', 'High')}", template['normal_style']))
        content.append(Paragraph(f"Risk Score: {risk_assessment.get('risk_score', 0)}", template['normal_style']))
        content.append(Spacer(1, 0.1 * inch))
        
        content.append(Paragraph("Primary Concerns:", template['normal_style']))
        for concern in risk_assessment.get('primary_concerns', []):
            content.append(Paragraph(f"• {concern}", template['normal_style']))
        
        content.append(Spacer(1, 0.2 * inch))
        content.append(Paragraph("Recommended Mitigation Strategies:", template['normal_style']))
        for strategy in risk_assessment.get('mitigation_strategies', []):
            content.append(Paragraph(f"• {strategy}", template['normal_style']))
        
        content.append(Spacer(1, 0.3 * inch))
        
        # Data Sources
        content.append(Paragraph("DATA SOURCES AND REFERENCES", template['heading_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        for source in perovskite_data.get('data_sources', []):
            content.append(Paragraph(f"• {source}", template['normal_style']))
        
        content.append(Spacer(1, 0.3 * inch))
        
        # Conclusions
        content.append(Paragraph("CONCLUSIONS AND RECOMMENDATIONS", template['heading_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        for i, conclusion in enumerate(perovskite_data.get('conclusions', []), 1):
            content.append(Paragraph(f"{i}. {conclusion}", template['normal_style']))
        
        content.append(Spacer(1, 0.3 * inch))
        content.append(Paragraph("End of Report", template['normal_style']))

        # Create PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=template['page_size'],
            topMargin=template['margins'][0],
            bottomMargin=template['margins'][1],
            leftMargin=template['margins'][2],
            rightMargin=template['margins'][3]
        )

        doc.build(content)

        return output_path
    
    def generate_project_summary(self, project_name: str, project_data: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate a project summary report PDF.
        
        Args:
            project_name: Name of the project
            project_data: Dictionary containing project summary data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{project_name}_project_summary.pdf")
        
        # Create template
        template = create_project_summary_template()
        
        # Generate content
        content = generate_project_summary_report_content(template, project_name, project_data)
        
        # Create PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=template['page_size'],
            topMargin=template['margins'][0],
            bottomMargin=template['margins'][1],
            leftMargin=template['margins'][2],
            rightMargin=template['margins'][3]
        )
        
        doc.build(content)
        
        return output_path
    
    def generate_combined_report(self, molecule_name: str, aop_data: Dict, admet_data: Dict, 
                                map_data: Optional[Dict] = None, output_path: Optional[str] = None) -> str:
        """
        Generate a combined report with AOP, ADMET, and topological map data.
        
        Args:
            molecule_name: Name of the molecule
            aop_data: Dictionary containing AOP analysis data
            admet_data: Dictionary containing ADMET analysis data
            map_data: Optional dictionary containing topological map data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{molecule_name}_combined_report.pdf")
        
        # Create templates
        aop_template = create_aop_report_template()
        admet_template = create_admet_report_template()
        
        content = []
        
        # Add AOP section
        content.append(Paragraph(f"Combined Analysis Report: {molecule_name}", aop_template['title_style']))
        content.append(Spacer(1, 0.2 * inch))
        
        report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content.append(Paragraph(f"Generated on: {report_date}", aop_template['normal_style']))
        content.append(Spacer(1, 0.3 * inch))
        
        # AOP Analysis Section
        content.append(Paragraph("AOP Analysis", aop_template['heading_style']))
        aop_content = generate_aop_report_content(aop_template, molecule_name, aop_data)
        content.extend(aop_content)
        content.append(PageBreak())
        
        # ADMET Analysis Section
        content.append(Paragraph("ADMET Analysis", admet_template['heading_style']))
        admet_content = generate_admet_report_content(admet_template, molecule_name, admet_data)
        content.extend(admet_content)
        
        if map_data:
            content.append(PageBreak())
            
            # Topological Map Section
            # map_template = create_topological_map_template() # Removed due to missing template
            content.append(Paragraph("Topological Map Analysis", aop_template['heading_style']))
            
            if map_data:
                description = map_data.get("description", "")
                content.append(Paragraph(description, aop_template['normal_style']))
                content.append(Spacer(1, 0.2 * inch))
                
                interventions = map_data.get("interventions", [])
                content.append(Paragraph("Intervention Points:", aop_template['normal_style']))
                for item in interventions:
                    content.append(Paragraph(f"• {item}", aop_template['normal_style']))
                
                img_path = map_data.get("image_path")
                if img_path:
                    self.add_visualization(content, img_path, caption="Figure 1: AOP Topological Map for Aspirin")

        
        # Create PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch,
            leftMargin=0.5 * inch,
            rightMargin=0.5 * inch
        )
        
        doc.build(content)
        
        return output_path
    
    def add_visualization(self, content: List, image_path: str, caption: str = "", 
                         width: float = 6 * inch, height: float = 4 * inch) -> List:
        """
        Add a visualization (image) to the content.
        
        Args:
            content: Existing content list
            image_path: Path to the image file
            caption: Image caption
            width: Image width in inches
            height: Image height in inches
            
        Returns:
            Updated content list with image added
        """
        if os.path.exists(image_path):
            try:
                img = Image(image_path, width=width, height=height)
                content.append(img)
                if caption:
                    styles = getSampleStyleSheet()
                    content.append(Paragraph(caption, styles['Normal']))
                content.append(Spacer(1, 0.2 * inch))
            except Exception as e:
                print(f"Error adding visualization: {e}")
        else:
            print(f"Image not found: {image_path}")
        
        return content
    
    def add_chart(self, content: List, chart_data: List[List], chart_title: str = "", 
                 col_widths: Optional[List[float]] = None) -> List:
        """
        Add a chart (table) to the content.
        
        Args:
            content: Existing content list
            chart_data: 2D list of data for the table
            chart_title: Chart title
            col_widths: Optional column widths
            
        Returns:
            Updated content list with chart added
        """
        if chart_title:
            styles = getSampleStyleSheet()
            content.append(Paragraph(chart_title, styles['Heading3']))
        
        if col_widths is None:
            col_widths = [2 * inch] * len(chart_data[0])
        
        table = Table(chart_data, colWidths=col_widths)
        
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
        
        table.setStyle(table_style)
        content.append(table)
        content.append(Spacer(1, 0.2 * inch))
        
        return content