## Troubleshooting

### AOP Wiki API Issues

**Problem: Connection errors or timeouts**
- **Cause**: AOP Wiki API may be unavailable or experiencing issues
- **Solution**: 
  - Check your internet connection
  - Verify the AOP Wiki service status at https://aopwiki.org/
  - Implement retry logic with exponential backoff
  - Use cached results when API is unavailable

**Problem: No results found for chemical**
- **Cause**: Chemical may not be in the AOP Wiki database
- **Solution**: 
  - Try different chemical names or CAS registry numbers
  - Check for synonyms or alternative identifiers
  - Use the search functionality to find similar chemicals
  - Consider that not all chemicals have curated AOP data

**Problem: API rate limiting**
- **Cause**: Making too many requests in a short period
- **Solution**:
  - Implement request throttling
  - Cache frequently accessed results
  - Use batch processing where possible
  - Consider implementing a local cache of AOP data

**Problem: Invalid or malformed data**
- **Cause**: AOP Wiki API response format may change
- **Solution**:
  - Implement robust error handling and data validation
  - Check the API documentation for any changes
  - Use try-catch blocks around data parsing operations

### Integration Issues

**Problem: Import errors for AOP Wiki API**
- **Cause**: AOP Wiki API package not properly installed
- **Solution**:
  - Ensure the package is installed: `pip install -e /path/to/aop_wiki_api`
  - Check that the package is in your Python path
  - Verify dependencies are installed (requests)

**Problem: Context manager not working**
- **Cause**: Improper usage of context managers
- **Solution**:
  - Always use `with AOPWikiClient() as client:` pattern
  - Ensure proper indentation in context blocks
  - Check for exceptions that might prevent proper cleanup

**Problem: Session not closing properly**
- **Cause**: Manual session management issues
- **Solution**:
  - Use context managers for automatic cleanup
  - Call `client.close()` explicitly if not using context managers
  - Ensure proper exception handling around session operations

  
### Error Handling
The AOP Wiki API integration includes comprehensive error handling:

- **Request exceptions**: Handled gracefully with informative error messages
- **Timeout handling**: Configurable timeout values for API requests (default: 30 seconds)
- **Missing data**: Proper handling of cases where data is not available
- **API failures**: Retry logic and fallback mechanisms
- **Context management**: Automatic session cleanup even when errors occur

The skill returns structured error responses that include:
- Error message describing what went wrong
- Context information (chemical names, SMILES, MIE IDs, etc.)
- HTTP status codes when available
- Suggestions for troubleshooting

**Error Handling Patterns:**

```python
# Standard error handling pattern
def get_known_miess_from_aop_wiki(self, chemical_name: str = None, cas_rn: str = None) -> Dict:
    try:
        with AOPWikiClient() as client:
            miess = client.get_miess_for_chemical(chemical_name=chemical_name, cas_rn=cas_rn)
            # Process results...
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}", "chemical_name": chemical_name, "cas_rn": cas_rn}
    except Exception as e:
        return {"error": str(e), "chemical_name": chemical_name, "cas_rn": cas_rn}

# Graceful degradation pattern
def get_aop_predictions(self, smiles: str) -> Dict:
    try:
        # Try to get AOP Wiki data
        known_miess = self.get_known_miess_from_aop_wiki(chemical_name="benzene")
        if "error" in known_miess:
            # Fallback to prediction-only mode
            return self._get_prediction_only_result(smiles)
        # Continue with full analysis...
    except Exception as e:
        # Return partial results with error indication
        return {
            "error": str(e),
            "smiles": smiles,
            "partial_results": self.predict_molecular_initiating_events(smiles)
        }
```

**Common Error Scenarios:**

1. **Network Issues**: Connection errors, timeouts, DNS failures
2. **API Unavailable**: AOP Wiki service downtime
3. **Rate Limiting**: Too many requests in short period
4. **Invalid Data**: Malformed API responses
5. **Not Found**: Chemical or MIE not in database
6. **Authentication**: If API requires authentication in future

**Best Practices for Error Handling:**
- Always wrap API calls in try-catch blocks
- Provide meaningful error messages to users
- Implement retry logic for transient failures
- Use graceful degradation when possible
- Log errors for debugging and monitoring
- Consider implementing circuit breakers for repeated failures