---
name: dontuse-admet
description: A skill that calculates ADMET scores for use with Cheminformatics and other skills
---

# ADMET Scoring Skill

## What is ADMET?
ADMET stands for Absorption, Distribution, Metabolism, Excretion, and Toxicity. It is a set of pharmacokinetic and pharmacodynamic properties that are critical in drug discovery and development. It describes how a drug behaves in the body and its potential safety and efficacy.

## Overview
This skill allows you to score molecules based on their ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties. It can also compare the ADMET profile of a given molecule to known molecules in a database. This skill supports any molecule in SMILES format and provides detailed analysis and visualization options. The implementation uses RDKit for comprehensive ADMET predictions and different functions for scoring, filtering, and comparing molecules based on their ADMET properties.

## Prediction Methods

This skill uses RDKit to perform comprehensive ADMET property predictions locally:

### Core Properties Calculated
- **Molecular Weight**: Calculated using RDKit's `Descriptors.MolWt`
- **LogP (octanol/water partition coefficient)**: Calculated using RDKit's `Descriptors.MolLogP`
- **Hydrogen Bond Donors/Acceptors**: Calculated using RDKit's `Lipinski.NumHDonors` and `Lipinski.NumHAcceptors`
- **Topological Polar Surface Area (TPSA)**: Calculated using RDKit's `Descriptors.TPSA`
- **Quantitative Estimate of Drug-likeness (QED)**: Calculated using RDKit's `QED.qed`
- **Molar Refractivity**: Calculated using RDKit's `Crippen.MolMR`

### ADMET Predictions
- **Solubility Class**: Predicted based on logP and TPSA ranges
- **Blood-Brain Barrier Permeability**: Predicted using logP and TPSA thresholds
- **CYP450 Inhibition**: Predicted based on functional group analysis
- **HERG Inhibition**: Predicted based on pharmacophore patterns
- **Metabolic Stability**: Predicted using logP and TPSA relationships

All calculations are performed locally using RDKit without external web service dependencies.

## Features
- **Universal Molecule Support**: Analyze any molecule by providing its SMILES representation
- **Comprehensive ADMET Analysis**: Get detailed predictions for Absorption, Distribution, Metabolism, Excretion, and Toxicity using RDKit-based methods
- **Molecule Comparison**: Compare ADMET profiles of multiple molecules side by side with statistical analysis
- **Similarity Analysis**: Calculate Tanimoto similarity matrix between molecules
- **Lead Identification**: Identify potential lead candidates based on customizable criteria
- **Detailed Reporting**: Generate comprehensive reports and visualizations of ADMET properties
- **Flexible Input**: Accepts any valid SMILES string for molecule representation
- **Offline Capability**: All predictions are performed locally using RDKit, no internet connection required

## Requirements
- Python 3.6 or higher
- `numpy` library (install with `pip install numpy`)
- `pandas` library (install with `pip install pandas`)
- RDKit (install with `pip install rdkit`)

## Notes
- The skill requires a valid SMILES string as input. Invalid SMILES strings may result in errors or unexpected behavior.
- Installation of RDKit may require additional dependencies depending on your operating system. Please refer to the [RDKit installation guide](https://www.rdkit.org/docs/Install.html) for detailed instructions.
- All ADMET predictions are performed locally using RDKit, so no internet connection is required after installation.
- A test script (`test_admet.py`) is provided to demonstrate all functionality and can be run with `python3 test_admet.py`.
- This skill is intended for research and educational purposes only.
- For molecule comparison, ensure you have enough molecules to generate meaningful statistics (minimum 2 molecules recommended).
- Similarity analysis uses Morgan fingerprints with radius=2 and 2048 bits for accurate comparison.

### Basic Molecule Comparison
```python
# Compare multiple molecules
molecules = [
    "CCO",  # Ethanol
    "CC(C)O",  # Isopropanol
    "CCCC",  # Butane
    "c1ccccc1",  # Benzene
    "CC(=O)O",  # Acetic acid
]

comparison_results = compare_molecules(molecules)
print("Individual Results:")
for result in comparison_results["individual_results"]:
    print(f"SMILES: {result['smiles']}")
    print(f"  MW: {result['molecular_weight']:.1f}")
    print(f"  LogP: {result['logp']:.2f}")
    print(f"  TPSA: {result['tpsa']:.1f}")
    print(f"  Lipinski Violations: {result['lipinski_violations']}")
    print(f"  ADMET Flags: {len(result['admet_flags'])}")
    print()

print("Comparison Summary:")
summary = comparison_results["comparison_summary"]
print(f"Molecular Weight - Mean: {summary['molecular_weight']['mean']:.1f}, Range: {summary['molecular_weight']['range']:.1f}")
print(f"LogP - Mean: {summary['logp']['mean']:.2f}, Range: {summary['logp']['range']:.2f}")
print(f"Lipinski Compliance: {summary['lipinski_compliance']['compliance_rate']*100:.1f}%")
```

### Similarity Analysis
```python
# Calculate similarity matrix
molecules = ["CCO", "CC(C)O", "CCCC", "c1ccccc1"]
matrix, results = get_molecule_similarity_matrix(molecules, threshold=0.5)

print("Similarity Matrix:")
for i, row in enumerate(matrix):
    print(f"{i}: {row}")

print("\nSimilarity Results:")
for result in results:
    print(f"{result['mol1']} vs {result['mol2']}: Tanimoto = {result['tanimoto']:.3f}, Similar = {result['similar']}")
```

### Lead Identification
```python
# Identify potential lead candidates
molecules = [
    "CCO",  # Ethanol
    "CC(C)O",  # Isopropanol
    "CCCC",  # Butane
    "c1ccccc1",  # Benzene
    "CC(=O)O",  # Acetic acid
    "CC1=CC=C(C=C1)C(=O)O",  # Benzoic acid
]

# Use default criteria
candidates = identify_lead_candidates(molecules)

print("Lead Candidates:")
for i, candidate in enumerate(candidates, 1):
    print(f"{i}. SMILES: {candidate['smiles']}")
    print(f"   Lead Score: {candidate['lead_score']:.1f}")
    print(f"   MW: {candidate['properties']['mw']:.1f}")
    print(f"   LogP: {candidate['properties']['logp']:.2f}")
    print(f"   Lipinski Violations: {candidate['properties']['lipinski_violations']}")
    print()

# Use custom criteria
custom_criteria = {
    "max_mw": 300,
    "max_logp": 3,
    "max_tpsa": 100,
    "max_hbd": 3,
    "max_hba": 5,
    "max_rotatable_bonds": 5,
    "max_lipinski_violations": 0,
    "max_admet_flags": 2
}

custom_candidates = identify_lead_candidates(molecules, criteria=custom_criteria)
print("Custom Criteria Candidates:")
for candidate in custom_candidates:
    print(f"SMILES: {candidate['smiles']}, Score: {candidate['lead_score']:.1f}")
```

## References
- Uses code from cheminformatics skill, which is licensed under the MIT License.
