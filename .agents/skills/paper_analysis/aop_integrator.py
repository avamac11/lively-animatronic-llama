"""
AOP Integrator Module

This module provides functionality for integrating paper analysis with Adverse Outcome Pathway (AOP) frameworks.
"""

from typing import List, Dict, Optional
from .content_analyzer import ContentAnalyzer
from .key_point_extractor import KeyPointExtractor
import re


class AOPIntegrator:
    """Integrate paper analysis with Adverse Outcome Pathway (AOP) frameworks."""

    def __init__(self):
        """Initialize the AOP integrator."""
        self.content_analyzer = ContentAnalyzer()
        self.key_point_extractor = KeyPointExtractor()

    def extract_aop_evidence(self, text: str) -> Dict:
        """Extract AOP-relevant evidence from paper text.

        Args:
            text: The paper text to analyze

        Returns:
            Dictionary containing AOP evidence organized by pathway components
        """
        # Extract key points and relationships
        key_points = self.key_point_extractor.extract_key_points(text)
        analysis = self.content_analyzer.analyze(text)
        relationships = analysis['relationships']

        # Organize evidence by AOP components
        aop_evidence = {
            'molecular_initiating_events': self._extract_mie_evidence(key_points, relationships),
            'key_events': self._extract_key_event_evidence(key_points, relationships),
            'adverse_outcomes': self._extract_adverse_outcome_evidence(key_points),
            'mechanistic_relationships': self._extract_mechanistic_relationships(relationships),
            'uncertainty_notes': self._extract_uncertainty_notes(text)
        }

        return aop_evidence

    def _extract_mie_evidence(self, key_points: List[str], relationships: List[Dict]) -> List[Dict]:
        """Extract Molecular Initiating Event (MIE) evidence.

        Args:
            key_points: List of key points from the paper
            relationships: List of relationships between entities

        Returns:
            List of MIE evidence dictionaries
        """
        mie_evidence = []
        
        # Look for patterns that might indicate MIEs
        mie_patterns = [
            r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(binds|interacts|reacts)\s+with\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)',
            r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(inhibits|activates|modulates)\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)',
            r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(causes|induces|triggers)\s+(damage|stress|activation)'
        ]
        
        for point in key_points:
            for pattern in mie_patterns:
                matches = re.findall(pattern, point, re.IGNORECASE)
                for match in matches:
                    mie_evidence.append({
                        'mie': match[0],
                        'interaction': match[1],
                        'target': match[2] if len(match) > 2 else None,
                        'evidence': point,
                        'confidence': 'medium'
                    })
        
        return mie_evidence

    def _extract_key_event_evidence(self, key_points: List[str], relationships: List[Dict]) -> List[Dict]:
        """Extract Key Event (KE) evidence.

        Args:
            key_points: List of key points from the paper
            relationships: List of relationships between entities

        Returns:
            List of key event evidence dictionaries
        """
        key_events = []
        
        # Look for biological processes and pathways
        ke_patterns = [
            r'(activation|inhibition|phosphorylation|dephosphorylation)\s+of\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)',
            r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)\s+(leads to|results in|causes)\s+(activation|inhibition|expression)',
            r'(pathway|signaling|cascade)\s+(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b)'
        ]
        
        for point in key_points:
            for pattern in ke_patterns:
                matches = re.findall(pattern, point, re.IGNORECASE)
                for match in matches:
                    event_type = match[0] if len(match) > 1 else 'process'
                    entity = match[1] if len(match) > 1 else match[0]
                    key_events.append({
                        'event_type': event_type,
                        'entity': entity,
                        'evidence': point,
                        'confidence': 'medium'
                    })
        
        # Also extract from relationships
        for rel in relationships:
            key_events.append({
                'event_type': rel['type'],
                'entity': f"{rel['source']} -> {rel['target']}",
                'source': rel['source'],
                'target': rel['target'],
                'evidence': rel['text'],
                'confidence': 'high'
            })
        
        return key_events

    def _extract_adverse_outcome_evidence(self, key_points: List[str]) -> List[Dict]:
        """Extract Adverse Outcome (AO) evidence.

        Args:
            key_points: List of key points from the paper

        Returns:
            List of adverse outcome evidence dictionaries
        """
        adverse_outcomes = []
        
        # Look for patterns that might indicate adverse outcomes
        ao_patterns = [
            r'(toxicity|damage|injury|disease|pathology)',
            r'(death|mortality|lesion|fibrosis|necrosis)',
            r'(impairment|dysfunction|failure)'
        ]
        
        for point in key_points:
            for pattern in ao_patterns:
                if re.search(pattern, point, re.IGNORECASE):
                    adverse_outcomes.append({
                        'outcome': point[:100] + '...' if len(point) > 100 else point,
                        'evidence': point,
                        'confidence': 'medium'
                    })
        
        return adverse_outcomes

    def _extract_mechanistic_relationships(self, relationships: List[Dict]) -> List[Dict]:
        """Extract mechanistic relationships for AOP construction.

        Args:
            relationships: List of relationships between entities

        Returns:
            List of mechanistic relationship dictionaries
        """
        mechanistic_relationships = []
        
        for rel in relationships:
            mechanistic_relationships.append({
                'source': rel['source'],
                'target': rel['target'],
                'relationship_type': rel['type'],
                'evidence': rel['text'],
                'confidence': 'high'
            })
        
        return mechanistic_relationships

    def _extract_uncertainty_notes(self, text: str) -> List[str]:
        """Extract uncertainty notes and limitations from the text.

        Args:
            text: The paper text

        Returns:
            List of uncertainty notes
        """
        uncertainty_notes = []
        
        # Look for sections that might contain limitations
        sections = self.key_point_extractor._split_into_sections(text)
        
        for section_name, section_text in sections.items():
            if any(keyword in section_name.lower() for keyword in ['limitation', 'uncertainty', 'limitation', 'constraint', 'caveat']):
                sentences = re.split(r'(?<=[.!?])\s+', section_text)
                for sentence in sentences:
                    if len(sentence.strip()) > 20:
                        uncertainty_notes.append(sentence.strip())
        
        return uncertainty_notes[:5]  # Return top 5 uncertainty notes

    def build_aop_skeleton(self, text: str) -> Dict:
        """Build a skeleton AOP from the paper text.

        Args:
            text: The paper text to analyze

        Returns:
            Dictionary representing an AOP skeleton
        """
        evidence = self.extract_aop_evidence(text)
        
        # Build the AOP skeleton
        aop_skeleton = {
            'molecular_initiating_events': evidence['molecular_initiating_events'],
            'key_events': evidence['key_events'],
            'adverse_outcomes': evidence['adverse_outcomes'],
            'relationships': evidence['mechanistic_relationships'],
            'uncertainty_notes': evidence['uncertainty_notes'],
            'confidence_score': self._calculate_confidence_score(evidence),
            'completeness_score': self._calculate_completeness_score(evidence)
        }
        
        return aop_skeleton

    def _calculate_confidence_score(self, evidence: Dict) -> float:
        """Calculate overall confidence score for the AOP evidence.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            Confidence score (0-1)
        """
        confidence_scores = {
            'high': 1.0,
            'medium': 0.7,
            'low': 0.4
        }
        
        total_confidence = 0
        total_items = 0
        
        # Calculate confidence from different evidence types
        for evidence_type in ['molecular_initiating_events', 'key_events', 'mechanistic_relationships']:
            for item in evidence[evidence_type]:
                confidence = confidence_scores.get(item.get('confidence', 'medium'), 0.7)
                total_confidence += confidence
                total_items += 1
        
        return total_confidence / total_items if total_items > 0 else 0.0

    def _calculate_completeness_score(self, evidence: Dict) -> float:
        """Calculate completeness score for the AOP evidence.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            Completeness score (0-1)
        """
        # Check presence of different AOP components
        components_present = 0
        total_components = 4
        
        if evidence['molecular_initiating_events']:
            components_present += 1
        if evidence['key_events']:
            components_present += 1
        if evidence['adverse_outcomes']:
            components_present += 1
        if evidence['mechanistic_relationships']:
            components_present += 1
        
        return components_present / total_components

    def validate_aop_evidence(self, evidence: Dict) -> Dict:
        """Validate AOP evidence for completeness and consistency.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            Dictionary containing validation results
        """
        validation = {
            'is_complete': self._check_completeness(evidence),
            'has_consistent_relationships': self._check_relationship_consistency(evidence),
            'confidence_score': self._calculate_confidence_score(evidence),
            'completeness_score': self._calculate_completeness_score(evidence),
            'issues': self._identify_issues(evidence)
        }
        
        return validation

    def _check_completeness(self, evidence: Dict) -> bool:
        """Check if the AOP evidence is complete.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            True if evidence is complete, False otherwise
        """
        return (len(evidence['molecular_initiating_events']) > 0 and
                len(evidence['key_events']) > 0 and
                len(evidence['adverse_outcomes']) > 0 and
                len(evidence['mechanistic_relationships']) > 0)

    def _check_relationship_consistency(self, evidence: Dict) -> bool:
        """Check if the relationships are consistent.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            True if relationships are consistent, False otherwise
        """
        # Simple consistency check: ensure relationships connect MIE to KE to AO
        relationships = evidence['mechanistic_relationships']
        
        if not relationships:
            return False
        
        # Check if there are connections between different components
        sources = {rel['source'] for rel in relationships}
        targets = {rel['target'] for rel in relationships}
        
        # If sources and targets overlap, relationships are likely consistent
        return bool(sources.intersection(targets))

    def _identify_issues(self, evidence: Dict) -> List[str]:
        """Identify potential issues with the AOP evidence.

        Args:
            evidence: AOP evidence dictionary

        Returns:
            List of identified issues
        """
        issues = []
        
        if not evidence['molecular_initiating_events']:
            issues.append('No Molecular Initiating Events identified')
        
        if not evidence['key_events']:
            issues.append('No Key Events identified')
        
        if not evidence['adverse_outcomes']:
            issues.append('No Adverse Outcomes identified')
        
        if not evidence['mechanistic_relationships']:
            issues.append('No mechanistic relationships identified')
        
        if len(evidence['uncertainty_notes']) > 0:
            issues.append(f'{len(evidence["uncertainty_notes"])} uncertainty notes identified')
        
        return issues