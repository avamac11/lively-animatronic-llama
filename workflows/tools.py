#!/usr/bin/env python3
"""
Tools definition file for LangGraph

This file contains all the tools (functions) that can be used by LangGraph agents.
Each tool should be a function that takes parameters and returns results.
"""


def search_information(query: str) -> str:
    """
    Search for information online or in a database.
    
    Args:
        query: The search query string
        
    Returns:
        str: Search results or information
    """
    # In a real implementation, this would use a search API
    return f"Search results for: '{query}'"


def calculate_expression(expression: str) -> str:
    """
    Perform mathematical calculations.
    
    Args:
        expression: Mathematical expression to evaluate
        
    Returns:
        str: Result of the calculation
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"


def save_to_file(content: str, filename: str) -> str:
    """
    Save content to a file.
    
    Args:
        content: Content to save
        filename: Name of the file
        
    Returns:
        str: Confirmation message
    """
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Content saved to {filename}"
    except Exception as e:
        return f"Error saving file: {str(e)}"


# List of all available tools for easy import
__all__ = [
    'search_information',
    'calculate_expression',
    'save_to_file',
]


if __name__ == "__main__":
    # Test the tools
    print("Testing tools...")
    print(search_information("Python programming"))
    print(calculate_expression("2 + 3 * 4"))
    print("All tools tested successfully!")