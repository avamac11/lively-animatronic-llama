# Implementation
# python
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem, Draw, Lipinski, DataStructs
from rdkit.Chem import rdMolDescriptors, QED
from rdkit.Chem import Crippen, FragmentCatalog
import pandas as pd
from typing import List, Dict, Tuple, Optional
import numpy as np

def molecular_properties(smiles: str) -> dict:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    return {
        "smiles": smiles,
        "mw": Descriptors.MolWt(mol),
        "logp": Descriptors.MolLogP(mol),
        "hbd": Descriptors.NumHDonors(mol),
        "hba": Descriptors.NumHAcceptors(mol),
        "tpsa": Descriptors.TPSA(mol),
        "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
        "rings": Descriptors.RingCount(mol),
        "lipinski_violations": sum([
            Descriptors.MolWt(mol) > 500,
            Descriptors.MolLogP(mol) > 5,
            Descriptors.NumHDonors(mol) > 5,
            Descriptors.NumHAcceptors(mol) > 10,
        ]),
    }

def predict_admet_properties(smiles: str) -> dict:
    """Predict comprehensive ADMET properties using RDKit-based methods"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    # Calculate various ADMET-related properties using RDKit
    admet_props = {
        "qed": QED.qed(mol),
        "molar_refractivity": Crippen.MolMR(mol),
        "hba_lipinski": Lipinski.NumHAcceptors(mol),
        "hbd_lipinski": Lipinski.NumHDonors(mol),
        "num_rotatable_bonds": Lipinski.NumRotatableBonds(mol),
        "num_aromatic_rings": Lipinski.NumAromaticRings(mol),
        "num_saturated_rings": Lipinski.NumSaturatedRings(mol),
        "tpsa": Descriptors.TPSA(mol),
        "logp": Descriptors.MolLogP(mol),
        "molecular_weight": Descriptors.MolWt(mol),
    }
    
    # Add some basic ADMET predictions based on property ranges
    admet_props["solubility_class"] = predict_solubility_class(admet_props["logp"], admet_props["tpsa"])
    admet_props["bbb_permeability"] = predict_bbb_permeability(admet_props["logp"], admet_props["tpsa"])
    admet_props["cytochrome_p450_inhibition"] = predict_cyp450_inhibition(mol)
    admet_props["herg_inhibition"] = predict_herg_inhibition(mol)
    admet_props["metabolic_stability"] = predict_metabolic_stability(admet_props["logp"], admet_props["tpsa"])
    
    return admet_props

def enhanced_molecular_analysis(smiles: str) -> dict:
    """Comprehensive molecular analysis combining basic properties and ADMET predictions"""
    basic_props = molecular_properties(smiles)
    admet_props = predict_admet_properties(smiles)
    
    # Merge properties
    combined = {**basic_props, **admet_props}
    combined["admet_flags"] = admet_flags(combined)
    
    return combined

def lipinski_filter(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["lipinski_violations"] <= 1].copy()

def similarity_search(query_smiles: str, library: list[str], threshold: float = 0.7) -> list[dict]:
    query_mol = Chem.MolFromSmiles(query_smiles)
    query_fp = AllChem.GetMorganFingerprintAsBitVect(query_mol, radius=2, nBits=2048)

    results = []
    for smi in library:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        tanimoto = DataStructs.TanimotoSimilarity(query_fp, fp)
        if tanimoto >= threshold:
            results.append({"smiles": smi, "tanimoto": tanimoto})

    return sorted(results, key=lambda x: -x["tanimoto"])

def predict_solubility_class(logp: float, tpsa: float) -> str:
    """Predict solubility class based on logP and TPSA"""
    if logp > 4.5 or tpsa > 130:
        return "low"
    elif logp > 2.5 or tpsa > 80:
        return "moderate"
    else:
        return "high"

def predict_bbb_permeability(logp: float, tpsa: float) -> bool:
    """Predict blood-brain barrier permeability"""
    # Simple model: high logP and low TPSA suggest BBB penetration
    return logp > 2.0 and tpsa < 90

def predict_cyp450_inhibition(mol: Chem.Mol) -> bool:
    """Predict CYP450 inhibition potential based on functional groups"""
    # Check for common CYP450 inhibitors
    smiles = Chem.MolToSmiles(mol)
    inhibitors = [
        "N(C)=O",  # Amides
        "C(=O)O",  # Carboxylic acids
        "c1ccccc1",  # Aromatic rings
        "[N+](=O)[O-]",  # Nitro groups
        "C#N",  # Nitriles
    ]
    return any(inhibitor in smiles for inhibitor in inhibitors)

def predict_herg_inhibition(mol: Chem.Mol) -> bool:
    """Predict HERG channel inhibition potential"""
    # Simple model based on basic nitrogen and aromatic systems
    smiles = Chem.MolToSmiles(mol)
    herg_pharmacophores = [
        "N",  # Basic nitrogen
        "c1ccccc1",  # Aromatic rings
        "C(=O)N",  # Amides
        "C#N",  # Nitriles
    ]
    return any(pharmacophore in smiles for pharmacophore in herg_pharmacophores)

def predict_metabolic_stability(logp: float, tpsa: float) -> str:
    """Predict metabolic stability"""
    if logp > 4.0 and tpsa < 70:
        return "low"
    elif logp > 3.0 or tpsa < 90:
        return "moderate"
    else:
        return "high"

def admet_flags(props: dict) -> list[str]:
    flags = []
    if props["logp"] > 5:
        flags.append("High lipophilicity: poor aqueous solubility risk")
    if props["tpsa"] > 140:
        flags.append("High TPSA: poor membrane permeability risk")
    if props["mw"] > 500:
        flags.append("High MW: poor oral absorption risk")
    if props["rotatable_bonds"] > 10:
        flags.append("High flexibility: poor oral bioavailability risk")
    if props["hbd"] > 5:
        flags.append("High H-bond donors: poor permeability risk")
    if props["hba"] > 10:
        flags.append("High H-bond acceptors: poor solubility risk")
    if props["rings"] > 4:
        flags.append("High ring count: potential metabolic instability")
    
    # Toxicity-related flags
    if props.get("herg_inhibition", False):
        flags.append("HERG inhibition: cardiac toxicity risk (QT prolongation)")
    if props.get("cytochrome_p450_inhibition", False):
        flags.append("CYP450 inhibition: drug-drug interaction potential")
    if props.get("cytochrome_p450_induction", False):
        flags.append("CYP450 induction: metabolic enzyme modulation")
    if props.get("skin_sensitization", False):
        flags.append("Skin sensitization: dermal toxicity risk")
    if props.get("eye_irritation", False):
        flags.append("Eye irritation: ocular toxicity potential")
    
    # Metabolism-related flags
    if props.get("metabolic_stability", "") == "low":
        flags.append("Low metabolic stability: short half-life risk")
    
    # Distribution-related flags
    if props.get("bbb_permeability", False):
        flags.append("Blood-brain barrier penetration: CNS toxicity risk")
    
    # Solubility-related flags
    if props.get("solubility_class", "") == "low":
        flags.append("Low solubility: formulation challenges")
    
    return flags

def compare_molecules(smiles_list: List[str]) -> Dict[str, List[Dict]]:
    """
    Compare multiple molecules based on their ADMET properties.
    
    Args:
        smiles_list: List of SMILES strings to compare
        
    Returns:
        Dictionary containing comparison results with detailed analysis
    """
    results = []
    comparison_data = {
        "molecular_weight": [],
        "logp": [],
        "tpsa": [],
        "hbd": [],
        "hba": [],
        "rotatable_bonds": [],
        "lipinski_violations": [],
        "admet_flags_count": [],
        "admet_flags": []
    }
    
    for smiles in smiles_list:
        try:
            # Get comprehensive analysis for each molecule
            analysis = enhanced_molecular_analysis(smiles)
            
            # Extract key properties
            props = {
                "smiles": smiles,
                "molecular_weight": analysis["mw"],
                "logp": analysis["logp"],
                "tpsa": analysis["tpsa"],
                "hbd": analysis["hbd"],
                "hba": analysis["hba"],
                "rotatable_bonds": analysis["rotatable_bonds"],
                "lipinski_violations": analysis["lipinski_violations"],
                "admet_flags": analysis["admet_flags"],
                "admet_flags_count": len(analysis["admet_flags"])
            }
            
            results.append(props)
            
            # Store data for comparison
            for key in comparison_data.keys():
                if key == "admet_flags":
                    comparison_data[key].append(analysis["admet_flags"])
                elif key == "admet_flags_count":
                    comparison_data[key].append(len(analysis["admet_flags"]))
                else:
                    comparison_data[key].append(analysis[key])
                    
        except Exception as e:
            print(f"Error analyzing molecule {smiles}: {e}")
            continue
    
    return {
        "individual_results": results,
        "comparison_summary": generate_comparison_summary(comparison_data)
    }

def generate_comparison_summary(comparison_data: Dict) -> Dict:
    """
    Generate summary statistics for molecule comparison.
    
    Args:
        comparison_data: Dictionary containing comparison data
        
    Returns:
        Dictionary containing summary statistics
    """
    summary = {}
    
    # Calculate basic statistics for numerical properties
    numerical_props = ["molecular_weight", "logp", "tpsa", "hbd", "hba", "rotatable_bonds", "lipinski_violations", "admet_flags_count"]
    
    for prop in numerical_props:
        values = comparison_data[prop]
        if values:
            summary[prop] = {
                "mean": np.mean(values),
                "std": np.std(values),
                "min": np.min(values),
                "max": np.max(values),
                "range": np.max(values) - np.min(values)
            }
    
    # Analyze ADMET flags
    all_flags = []
    for flags_list in comparison_data["admet_flags"]:
        all_flags.extend(flags_list)
    
    if all_flags:
        unique_flags = list(set(all_flags))
        flag_frequency = {flag: all_flags.count(flag) for flag in unique_flags}
        summary["admet_flags_analysis"] = {
            "total_unique_flags": len(unique_flags),
            "flag_frequency": flag_frequency,
            "most_common_flags": sorted(flag_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
        }
    
    # Lipinski compliance analysis
    lipinski_compliant = sum(1 for v in comparison_data["lipinski_violations"] if v <= 1)
    summary["lipinski_compliance"] = {
        "compliant_count": lipinski_compliant,
        "total_count": len(comparison_data["lipinski_violations"]),
        "compliance_rate": lipinski_compliant / len(comparison_data["lipinski_violations"]) if comparison_data["lipinski_violations"] else 0
    }
    
    return summary

def get_molecule_similarity_matrix(smiles_list: List[str], threshold: float = 0.5) -> Tuple[List[List[float]], List[Dict]]:
    """
    Calculate similarity matrix between molecules using Tanimoto similarity.
    
    Args:
        smiles_list: List of SMILES strings
        threshold: Similarity threshold for considering molecules similar
        
    Returns:
        Tuple containing similarity matrix and detailed similarity results
    """
    molecules = []
    fingerprints = []
    
    # Generate fingerprints for all molecules
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        molecules.append(smiles)
        fingerprints.append(fp)
    
    # Calculate similarity matrix
    n = len(fingerprints)
    similarity_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    similarity_results = []
    
    for i in range(n):
        for j in range(i, n):
            tanimoto = DataStructs.TanimotoSimilarity(fingerprints[i], fingerprints[j])
            similarity_matrix[i][j] = tanimoto
            similarity_matrix[j][i] = tanimoto
            
            if i != j:  # Skip self-comparison
                similarity_results.append({
                    "mol1": molecules[i],
                    "mol2": molecules[j],
                    "tanimoto": tanimoto,
                    "similar": tanimoto >= threshold
                })
    
    return similarity_matrix, similarity_results

def identify_lead_candidates(smiles_list: List[str], criteria: Optional[Dict] = None) -> List[Dict]:
    """
    Identify potential lead candidates based on ADMET properties.
    
    Args:
        smiles_list: List of SMILES strings to evaluate
        criteria: Dictionary of criteria for lead identification (optional)
        
    Returns:
        List of lead candidates with scores
    """
    if criteria is None:
        # Default criteria for drug-like molecules
        criteria = {
            "max_mw": 500,
            "max_logp": 5,
            "max_tpsa": 140,
            "max_hbd": 5,
            "max_hba": 10,
            "max_rotatable_bonds": 10,
            "max_lipinski_violations": 1,
            "max_admet_flags": 3
        }
    
    candidates = []
    
    for smiles in smiles_list:
        try:
            analysis = enhanced_molecular_analysis(smiles)
            
            # Calculate lead score (0-100)
            score = 100
            
            # Penalize for criteria violations with more aggressive scoring
            if analysis["mw"] > criteria["max_mw"]:
                penalty = min(40, (analysis["mw"] - criteria["max_mw"]) / criteria["max_mw"] * 100)
                score -= penalty
            if analysis["logp"] > criteria["max_logp"]:
                penalty = min(30, (analysis["logp"] - criteria["max_logp"]) / criteria["max_logp"] * 100)
                score -= penalty
            if analysis["tpsa"] > criteria["max_tpsa"]:
                penalty = min(25, (analysis["tpsa"] - criteria["max_tpsa"]) / criteria["max_tpsa"] * 100)
                score -= penalty
            if analysis["hbd"] > criteria["max_hbd"]:
                penalty = min(20, (analysis["hbd"] - criteria["max_hbd"]) / criteria["max_hbd"] * 100)
                score -= penalty
            if analysis["hba"] > criteria["max_hba"]:
                penalty = min(20, (analysis["hba"] - criteria["max_hba"]) / criteria["max_hba"] * 100)
                score -= penalty
            if analysis["rotatable_bonds"] > criteria["max_rotatable_bonds"]:
                penalty = min(15, (analysis["rotatable_bonds"] - criteria["max_rotatable_bonds"]) / criteria["max_rotatable_bonds"] * 100)
                score -= penalty
            if analysis["lipinski_violations"] > criteria["max_lipinski_violations"]:
                penalty = (analysis["lipinski_violations"] - criteria["max_lipinski_violations"]) * 30
                score -= penalty
            # Apply different penalties based on flag severity
            flag_penalties = 0
            for flag in analysis["admet_flags"]:
                if "toxic" in flag.lower() or "inhibition" in flag.lower():
                    flag_penalties += 15  # High penalty for toxicity/toxicity-related flags
                elif "solubility" in flag.lower() or "permeability" in flag.lower():
                    flag_penalties += 8  # Moderate penalty for formulation issues
                elif "metabolic" in flag.lower() or "stability" in flag.lower():
                    flag_penalties += 10  # Moderate penalty for metabolic issues
                else:
                    flag_penalties += 5  # Low penalty for other flags
            
            score -= flag_penalties
            
            # Ensure score is between 0 and 100
            score = max(0, min(100, score))
            
            candidates.append({
                "smiles": smiles,
                "lead_score": score,
                "properties": analysis,
                "criteria_violations": {
                    "mw": analysis["mw"] > criteria["max_mw"],
                    "logp": analysis["logp"] > criteria["max_logp"],
                    "tpsa": analysis["tpsa"] > criteria["max_tpsa"],
                    "hbd": analysis["hbd"] > criteria["max_hbd"],
                    "hba": analysis["hba"] > criteria["max_hba"],
                    "rotatable_bonds": analysis["rotatable_bonds"] > criteria["max_rotatable_bonds"],
                    "lipinski_violations": analysis["lipinski_violations"] > criteria["max_lipinski_violations"],
                    "admet_flags": len(analysis["admet_flags"]) > criteria["max_admet_flags"]
                }
            })
            
        except Exception as e:
            print(f"Error evaluating molecule {smiles}: {e}")
            continue
    
    # Sort by lead score (descending)
    candidates.sort(key=lambda x: x["lead_score"], reverse=True)
    
    return candidates

# This does not include ALL ADMET properties, but provides a comprehensive overview of key properties 
# relevant to drug discovery. Further refinement and integration with experimental data would enhance 
# predictive accuracy.