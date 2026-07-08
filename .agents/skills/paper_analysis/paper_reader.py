"""
Paper Reader Module

This module provides functionality for reading academic papers from various formats.
"""

import pdfplumber
from typing import Optional
import re


class PaperReader:
    """Base class for paper reading functionality."""

    def read(self, file_path: str) -> str:
        """Read a paper from the given file path.

        Args:
            file_path: Path to the paper file

        Returns:
            Extracted text from the paper
        """
        raise NotImplementedError("Subclasses must implement this method")


class PDFReader(PaperReader):
    """Read papers from PDF files."""

    def __init__(self):
        """Initialize the PDF reader."""
        super().__init__()

    def read(self, file_path: str) -> str:
        """Read text from a PDF file.

        Args:
            file_path: Path to the PDF file

        Returns:
            Extracted text from the PDF
        """
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text


class HTMLReader(PaperReader):
    """Read papers from HTML files."""

    def __init__(self):
        """Initialize the HTML reader."""
        super().__init__()

    def read(self, file_path: str) -> str:
        """Read text from an HTML file.

        Args:
            file_path: Path to the HTML file

        Returns:
            Extracted text from the HTML
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Simple HTML text extraction
        # Remove script and style elements
        text = re.sub(r'<(script|style).*?>.*?</\1>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        return text


class TextReader(PaperReader):
    """Read papers from plain text files."""

    def __init__(self):
        """Initialize the text reader."""
        super().__init__()

    def read(self, file_path: str) -> str:
        """Read text from a plain text file.

        Args:
            file_path: Path to the text file

        Returns:
            Content of the text file
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()


class PaperReaderFactory:
    """Factory for creating appropriate paper readers based on file extension."""

    @staticmethod
    def create_reader(file_path: str) -> PaperReader:
        """Create a paper reader based on the file extension.

        Args:
            file_path: Path to the paper file

        Returns:
            Appropriate PaperReader instance
        """
        extension = file_path.lower().split('.')[-1]
        
        if extension == 'pdf':
            return PDFReader()
        elif extension == 'html':
            return HTMLReader()
        elif extension in ['txt', 'md']:
            return TextReader()
        else:
            raise ValueError(f"Unsupported file format: {extension}")


class PaperReaderWrapper:
    """Wrapper class that automatically selects the appropriate reader."""

    def __init__(self):
        """Initialize the paper reader wrapper."""
        pass

    def read_paper(self, file_path: str) -> str:
        """Read a paper from the given file path, automatically selecting the appropriate reader.

        Args:
            file_path: Path to the paper file

        Returns:
            Extracted text from the paper
        """
        reader = PaperReaderFactory.create_reader(file_path)
        return reader.read(file_path)
