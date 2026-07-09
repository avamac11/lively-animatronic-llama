#!/usr/bin/env python3
"""
Calculate ADMET score for benzene using the admet-scoring skill
"""

import sys
sys.path.append('/home/avam11/lively-animatronic-llama/.opencode/skills/admet-scoring')

from SKILL import enhanced_molecular_analysis, admet_flags

def calculate_admet_score(smiles: str) -> dict:
    """Calculate comprehensive ADMET score for a molecule"""
    
    # Get enhanced molecular analysis
    analysis = enhanced_molecular_analysis(smiles)
    
    # Calculate ADMET score components
    score_components = {
        'molecular_weight': min(100, max(0, 100 - (analysis['mw'] - 200) / 300 * 100)),
        'logp': min(100, max(0, 100 - abs(analysis['logp'] - 2.5) / 2.5 * 100)),
        'tpsa': min(100, max(0, 100 - (analysis['tpsa'] - 50) / 90 * 100)),
        'hbd': min(100, max(0, 100 - analysis['hbd'] / 5 * 100)),
        'hba': min(100, max(0, 100 - analysis['hba'] / 10 * 100)),
        'rotatable_bonds': min(100, max(0, 100 - analysis['rotatable_bonds'] / 10 * 100)),
        'lipinski_violations': max(0, 100 - analysis['lipinski_violations'] * 30),
        'qed': analysis['qed'] * 100,
    }
    
    # Calculate overall ADMET score (weighted average)
    weights = {
        'molecular_weight': 0.15,
        'logp': 0.15,
        'tpsa': 0.15,
        'hbd': 0.10,
        'hba': 0.10,
        'rotatable_bonds': 0.05,
        'lipinski_violations': 0.10,
        'qed': 0.20,
    }
    
    weighted_score = sum(score_components[prop] * weights[prop] for prop in weights)
    
    # Penalize for ADMET flags
    flag_penalties = 0
    for flag in analysis['admet_flags']:
        if 'toxic' in flag.lower() or 'inhibition' in flag.lower():
            flag_penalties += 15
        elif 'solubility' in flag.lower() or 'permeability' in flag.lower():
            flag_penalties += 8
        elif 'metabolic' in flag.lower() or 'stability' in flag.lower():
            flag_penalties += 10
        else:
            flag_penalties += 5
    
    final_score = max(0, min(100, weighted_score - flag_penalties))
    
    return {
        'analysis': analysis,
        'score_components': score_components,
        'weights': weights,
        'weighted_score': weighted_score,
        'flag_penalties': flag_penalties,
        'final_score': final_score,
        'admet_flags': analysis['admet_flags']
    }

def main():
    benzene_smiles = 'c1ccccc1'
    
    print('CALCULATING ADMET SCORE FOR BENZENE')
    print('=' * 50)
    print()
    
    result = calculate_admet_score(benzene_smiles)
    
    print('MOLECULAR PROPERTIES')
    print('-' * 30)
    print(f'SMILES: {benzene_smiles}')
    print(f'Molecular Weight: {result["analysis"]["mw"]:.1f} g/mol')
    print(f'LogP: {result["analysis"]["logp"]:.2f}')
    print(f'H-Bond Donors: {result["analysis"]["hbd"]}')
    print(f'H-Bond Acceptors: {result["analysis"]["hba"]}')
    print(f'TPSA: {result["analysis"]["tpsa"]:.1f} Å²')
    print(f'Rotatable Bonds: {result["analysis"]["rotatable_bonds"]}')
    print(f'Lipinski Violations: {result["analysis"]["lipinski_violations"]}')
    print(f'QED Score: {result["analysis"]["qed"]:.3f}')
    print()
    
    print('ADMET SCORE COMPONENTS')
    print('-' * 30)
    for component, score in result['score_components'].items():
        weight = result['weights'][component]
        print(f'{component.replace("_", " ").title()}: {score:.1f} (weight: {weight:.2f})')
    print()
    
    print('SCORE CALCULATION')
    print('-' * 30)
    print(f'Weighted Score: {result["weighted_score"]:.1f}')
    print(f'Flag Penalties: {result["flag_penalties"]}')
    print(f'Final ADMET Score: {result["final_score"]:.1f}/100')
    print()
    
    print('ADMET FLAGS')
    print('-' * 30)
    if result['admet_flags']:
        for i, flag in enumerate(result['admet_flags'], 1):
            print(f'{i}. {flag}')
    else:
        print('No ADMET flags detected')
    print()
    
    print('INTERPRETATION')
    print('-' * 30)
    if result['final_score'] >= 70:
        print('EXCELLENT: Very favorable ADMET properties')
    elif result['final_score'] >= 50:
        print('GOOD: Generally favorable ADMET properties')
    elif result['final_score'] >= 30:
        print('FAIR: Moderate ADMET properties, may require optimization')
    else:
        print('POOR: Unfavorable ADMET properties, significant issues identified')
    
    print()
    print('RECOMMENDATIONS')
    print('-' * 30)
    if result['final_score'] < 50:
        print('• Consider structural modifications to improve ADMET properties')
        print('• Address specific ADMET flags identified above')
        print('• Conduct experimental validation of predicted properties')
        print('• Evaluate safer alternatives if benzene is being considered for pharmaceutical use')

if __name__ == '__main__':
    main()