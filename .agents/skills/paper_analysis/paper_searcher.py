"""
Paper Searcher Module

This module provides functionality for searching academic papers from various sources.
"""

import requests
from typing import List, Dict, Optional


class PaperSearcher:
    """Base class for paper searching functionality."""

    def __init__(self):
        """Initialize the paper searcher."""
        pass

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search for papers using the default search method.

        Args:
            query: The search query
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        raise NotImplementedError("Subclasses must implement this method")


class ArxivSearcher(PaperSearcher):
    """Search papers from arXiv."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the arXiv searcher.

        Args:
            api_key: Optional API key for arXiv
        """
        super().__init__()
        self.api_key = api_key
        self.base_url = "http://export.arxiv.org/api/query"

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search arXiv for papers matching the query.

        Args:
            query: The search query
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        params = {
            'search_query': f'all:{query}',
            'start': 0,
            'max_results': max_results,
            'sortBy': 'relevance',
            'sortOrder': 'descending'
        }

        if self.api_key:
            params['api_key'] = self.api_key

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        results = []
        for entry in response.text.split('<entry>')[1:]:
            paper = {}
            for field in ['id', 'title', 'summary', 'author', 'published']:
                start_tag = f'<{field}>'
                end_tag = f'</{field}>'
                if start_tag in entry and end_tag in entry:
                    paper[field] = entry.split(start_tag)[1].split(end_tag)[0]
            results.append(paper)

        return results


class PubMedSearcher(PaperSearcher):
    """Search papers from PubMed."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PubMed searcher.

        Args:
            api_key: Optional API key for PubMed
        """
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search PubMed for papers matching the query.

        Args:
            query: The search query
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        params = {
            'db': 'pubmed',
            'term': query,
            'retmax': max_results,
            'retmode': 'json'
        }

        if self.api_key:
            params['api_key'] = self.api_key

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        data = response.json()
        results = []

        for id in data.get('esearchresult', {}).get('idlist', []):
            paper = {'id': id}
            results.append(paper)

        return results


class GoogleScholarSearcher(PaperSearcher):
    """Search papers from Google Scholar."""

    def __init__(self):
        """Initialize the Google Scholar searcher."""
        super().__init__()
        # Note: Google Scholar doesn't have a public API
        # This is a placeholder for future implementation

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search Google Scholar for papers matching the query.

        Args:
            query: The search query
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        raise NotImplementedError("Google Scholar search requires a custom implementation")


class CustomSearcher(PaperSearcher):
    """Custom paper searcher for specific sources."""

    def __init__(self, base_url: str, query_param: str = 'q'):
        """Initialize the custom searcher.

        Args:
            base_url: Base URL for the search API
            query_param: Query parameter name
        """
        super().__init__()
        self.base_url = base_url
        self.query_param = query_param

    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search using the custom API.

        Args:
            query: The search query
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        params = {
            self.query_param: query,
            'max_results': max_results
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        # Parse response based on API format
        # This is a placeholder - actual implementation depends on API
        return []
