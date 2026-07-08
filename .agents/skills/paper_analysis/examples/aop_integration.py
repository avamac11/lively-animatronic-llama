"""
AOP Integration Examples for Paper Analysis Skill

This file demonstrates AOP-specific functionality of the paper analysis skill.
"""

from paper_analysis import AOPIntegrator, PaperAnalysisSkill


def demonstrate_aop_integration():
    """Demonstrate AOP integration functionality."""
    print("=== AOP Integration Examples ===")
    
    # Create AOP integrator
    integrator = AOPIntegrator()
    
    # Sample paper text (in real usage, this would be extracted from an actual paper)
    sample_paper_text = """
    Abstract
    Chemical exposure to TCDD leads to activation of the aryl hydrocarbon receptor (AhR), 
    which is the molecular initiating event in this adverse outcome pathway. The activated 
    AhR translocates to the nucleus and binds to xenobiotic response elements, causing 
    upregulation of CYP1A1 expression. This key event triggers a cascade of downstream 
    effects including oxidative stress and inflammation. The final adverse outcome is 
    hepatic fibrosis, as evidenced by increased collagen deposition in liver tissue.
    
    Introduction
    The aryl hydrocarbon receptor (AhR) is a ligand-activated transcription factor that 
    mediates the toxic effects of dioxins and related compounds. Upon binding to TCDD, 
    AhR undergoes a conformational change that allows it to dissociate from its chaperone 
    proteins and translocate to the nucleus. In the nucleus, AhR forms a heterodimer with 
    the aryl hydrocarbon receptor nuclear translocator (ARNT) and binds to xenobiotic 
    response elements in the promoter regions of target genes.
    
    Results
    Treatment of mice with TCDD (10 µg/kg) resulted in significant activation of AhR 
    within 6 hours, as measured by nuclear translocation assays. CYP1A1 mRNA levels 
    increased 50-fold at 24 hours post-treatment. Histological analysis revealed 
    increased collagen deposition in the liver at 7 days, with fibrosis scores 
    increasing from 0.5 ± 0.2 in controls to 3.2 ± 0.5 in treated animals (p < 0.01).
    
    Discussion
    These results demonstrate a clear adverse outcome pathway from TCDD exposure 
    through AhR activation to hepatic fibrosis. The molecular initiating event is 
    TCDD binding to AhR, which causes the key event of CYP1A1 upregulation. This 
    leads to oxidative stress and ultimately results in the adverse outcome of 
    hepatic fibrosis. The pathway shows high biological plausibility and is supported 
    by multiple lines of evidence from in vitro and in vivo studies.
    
    Limitations
    While this study provides strong evidence for the proposed AOP, some uncertainties 
    remain regarding the exact mechanisms of oxidative stress and the role of 
    inflammatory mediators. Further studies are needed to fully elucidate these 
    intermediate steps.
    """
    
    print("\n1. Extracting AOP Evidence:")
    
    # Extract AOP evidence
    aop_evidence = integrator.extract_aop_evidence(sample_paper_text)
    
    print(f"   Molecular Initiating Events: {len(aop_evidence['molecular_initiating_events'])}")
    for mie in aop_evidence['molecular_initiating_events'][:2]:  # Show first 2
        print(f"     - {mie['mie']} ({mie['interaction']}) -> {mie['target']}")
    
    print(f"   Key Events: {len(aop_evidence['key_events'])}")
    for ke in aop_evidence['key_events'][:3]:  # Show first 3
        print(f"     - {ke['event_type']}: {ke['entity']}")
    
    print(f"   Adverse Outcomes: {len(aop_evidence['adverse_outcomes'])}")
    for ao in aop_evidence['adverse_outcomes'][:2]:  # Show first 2
        print(f"     - {ao['outcome'][:50]}...")
    
    print(f"   Mechanistic Relationships: {len(aop_evidence['mechanistic_relationships'])}")
    for rel in aop_evidence['mechanistic_relationships'][:2]:  # Show first 2
        print(f"     - {rel['source']} {rel['relationship_type']} {rel['target']}")
    
    print(f"   Uncertainty Notes: {len(aop_evidence['uncertainty_notes'])}")
    for note in aop_evidence['uncertainty_notes'][:2]:  # Show first 2
        print(f"     - {note[:60]}...")
    
    print("\n2. Building AOP Skeleton:")
    
    # Build AOP skeleton
    aop_skeleton = integrator.build_aop_skeleton(sample_paper_text)
    
    print(f"   Confidence Score: {aop_skeleton['confidence_score']:.3f}")
    print(f"   Completeness Score: {aop_skeleton['completeness_score']:.3f}")
    print(f"   Total Components: {sum(len(v) for v in aop_skeleton.values() if isinstance(v, list))}")
    
    print("\n3. Validating AOP Evidence:")
    
    # Validate AOP evidence
    validation = integrator.validate_aop_evidence(aop_evidence)
    
    print(f"   Is Complete: {validation['is_complete']}")
    print(f"   Has Consistent Relationships: {validation['has_consistent_relationships']}")
    print(f"   Confidence Score: {validation['confidence_score']:.3f}")
    print(f"   Completeness Score: {validation['completeness_score']:.3f}")
    print(f"   Issues: {len(validation['issues'])}")
    for issue in validation['issues']:
        print(f"     - {issue}")
    
    print("\n4. Using PaperAnalysisSkill for Complete Workflow:")
    
    # Use the main skill class
    skill = PaperAnalysisSkill()
    
    # Simulate complete workflow (without actual file I/O)
    print("   Creating executive summary...")
    summary = {
        'title': 'TCDD-induced hepatic fibrosis via AhR activation',
        'authors': ['Researcher A', 'Researcher B'],
        'publication': 'Toxicology and Applied Pharmacology',
        'key_points': aop_evidence['key_events'][:5],
        'themes': ['AhR', 'TCDD', 'hepatic fibrosis', 'CYP1A1', 'oxidative stress'],
        'entities': ['AhR', 'TCDD', 'CYP1A1', 'hepatic fibrosis'],
        'keywords': ['AhR', 'TCDD', 'hepatic fibrosis', 'CYP1A1', 'oxidative stress'],
        'statistics': {'word_count': 1200, 'sentence_count': 60},
        'summary': 'This study demonstrates an adverse outcome pathway from TCDD exposure through AhR activation to hepatic fibrosis.'
    }
    
    print(f"   Summary Title: {summary['title']}")
    print(f"   Key Themes: {', '.join(summary['themes'][:3])}")
    print(f"   Word Count: {summary['statistics']['word_count']}")
    
    print("\n=== AOP Integration Examples Complete ===")


if __name__ == "__main__":
    demonstrate_aop_integration()