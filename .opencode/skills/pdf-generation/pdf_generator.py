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
from topological_map_template import create_topological_map_template, generate_topological_map_report_content
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
        Generate a topological map report PDF.
        
        Args:
            molecule_name: Name of the molecule
            map_data: Dictionary containing topological map data
            output_path: Optional custom output path
            
        Returns:
            Path to the generated PDF file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, f"{molecule_name}_topological_map_report.pdf")
        
        # Create template
        template = create_topological_map_template()
        
        # Generate content
        content = generate_topological_map_report_content(template, molecule_name, map_data)
        
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
            map_template = create_topological_map_template()
            content.append(Paragraph("Topological Map Analysis", map_template['heading_style']))
            map_content = generate_topological_map_report_content(map_template, molecule_name, map_data)
            content.extend(map_content)
        
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