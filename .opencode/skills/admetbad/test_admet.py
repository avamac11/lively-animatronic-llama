#!/usr/bin/env python3
"""
Test script for the updated ADMET scoring skill without admetSAR dependency.
"""

from SKILL import molecular_properties, predict_admet_properties, enhanced_molecular_analysis, compare_molecules, identify_lead_candidates
import json

def test_basic_functionality():
    """Test basic ADMET functionality"""
    print("=== Testing Basic ADMET Functionality ===")
    
    # Test molecules
    test_molecules = [
        ("CCO", "Ethanol"),
        ("CC(C)O", "Isopropanol"),
        ("c1ccccc1", "Benzene"),
        ("CCCCCCCCCCCC", "Dodecane"),
        ("CC(=O)O", "Acetic acid"),
    ]
    
    for smiles, name in test_molecules:
        print(f"\n--- {name} ({smiles}) ---")
        
        # Get molecular properties
        props = molecular_properties(smiles)
        print(f"MW: {props['mw']:.1f}, LogP: {props['logp']:.2f}, TPSA: {props['tpsa']:.1f}")
        
        # Get ADMET properties
        admet_props = predict_admet_properties(smiles)
        print(f"QED: {admet_props['qed']:.3f}, Solubility: {admet_props['solubility_class']}")
        print(f"BBB Permeability: {admet_props['bbb_permeability']}, CYP450 Inhibition: {admet_props['cytochrome_p450_inhibition']}")
        
        # Get enhanced analysis
        enhanced = enhanced_molecular_analysis(smiles)
        print(f"ADMET Flags: {len(enhanced['admet_flags'])} flags")
        for flag in enhanced['admet_flags']:
            print(f"  - {flag}")

def test_comparison():
    """Test molecule comparison functionality"""
    print("\n\n=== Testing Molecule Comparison ===")
    
    molecules = [
        "CCO",      # Ethanol
        "CC(C)O",   # Isopropanol  
        "CCCC",     # Butane
        "c1ccccc1", # Benzene
        "CC(=O)O",  # Acetic acid
    ]
    
    comparison_results = compare_molecules(molecules)
    
    print("Individual Results:")
    for result in comparison_results["individual_results"]:
        print(f"\nSMILES: {result['smiles']}")
        print(f"  MW: {result['molecular_weight']:.1f}")
        print(f"  LogP: {result['logp']:.2f}")
        print(f"  TPSA: {result['tpsa']:.1f}")
        print(f"  Lipinski Violations: {result['lipinski_violations']}")
        print(f"  ADMET Flags: {result['admet_flags_count']}")
    
    print(f"\nComparison Summary:")
    summary = comparison_results["comparison_summary"]
    print(f"  Average MW: {summary['molecular_weight']['mean']:.1f}")
    print(f"  Average LogP: {summary['logp']['mean']:.2f}")
    print(f"  Lipinski Compliance: {summary['lipinski_compliance']['compliance_rate']*100:.1f}%")

def test_lead_identification():
    """Test lead candidate identification"""
    print("\n\n=== Testing Lead Candidate Identification ===")
    
    molecules = [
        "CCO",           # Ethanol - good candidate
        "CC(C)O",        # Isopropanol - good candidate
        "CCCCCCCCCCCC",  # Dodecane - poor candidate
        "c1ccccc1",      # Benzene - moderate candidate
        "CC(=O)O",       # Acetic acid - good candidate
    ]
    
    candidates = identify_lead_candidates(molecules)
    
    print("Lead Candidates (sorted by score):")
    for i, candidate in enumerate(candidates, 1):
        print(f"\n{i}. {candidate['smiles']} - Score: {candidate['lead_score']:.1f}")
        violations = [k for k, v in candidate['criteria_violations'].items() if v]
        if violations:
            print(f"   Violations: {', '.join(violations)}")
        else:
            print(f"   No violations")

if __name__ == "__main__":
    test_basic_functionality()
    test_comparison()
    test_lead_identification()
    print("\n=== All tests completed successfully! ===")