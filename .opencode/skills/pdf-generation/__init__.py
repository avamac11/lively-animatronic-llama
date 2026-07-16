"""
PDF Generation Skill - Main module

This module provides comprehensive PDF generation capabilities for the AOP project.
"""

from .pdf_generator import PDFGenerator
from .aop_report import AOPReportGenerator
from .admet_report import ADMETReportGenerator
from .topological_map_report import TopologicalMapReportGenerator
from .project_summary import ProjectSummaryGenerator

__all__ = [
    'PDFGenerator',
    'AOPReportGenerator',
    'ADMETReportGenerator',
    'TopologicalMapReportGenerator',
    'ProjectSummaryGenerator'
]

__version__ = "1.0.0"
__author__ = "AOP Project Team"
__description__ = "PDF generation capabilities for AOP project analysis results"