---
name: admet-scoring
description: A skill that gives context about ADMET scoring for use with Cheminformatics and other skills
---

# ADMET Scoring Skill

## What is ADMET?
ADMET stands for Absorption, Distribution, Metabolism, Excretion, and Toxicity. It is a set of pharmacokinetic and pharmacodynamic properties that are critical in drug discovery and development. It describes how a drug behaves in the body and its potential safety and efficacy.

## Overview
This skill allows you to score molecules based on their ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties. It can also compare the ADMET profile of a given molecule to known molecules in a database. The admetSAR 3.0 webserver is used for scoring, and the skill can generate comprehensive reports summarizing the ADMET properties and comparisons. This skill supports any molecule in SMILES format and provides detailed analysis and visualization options.

## Usage


## Functions


## Example




## Data Sources
- [admetSAR 3.0: Predict](https://lmmd.ecust.edu.cn/admetsar3/predict.php): This skill uses the admetSAR 3.0 webserver for predicting ADMET properties of molecules. The webserver provides comprehensive ADMET predictions for any molecule in SMILES format.

## Features
- **Universal Molecule Support**: Analyze any molecule by providing its SMILES representation
- **Comprehensive ADMET Analysis**: Get detailed predictions for Absorption, Distribution, Metabolism, Excretion, and Toxicity
- **Molecule Comparison**: Compare ADMET profiles of multiple molecules side by side
- **Detailed Reporting**: Generate comprehensive reports and visualizations of ADMET properties
- **Flexible Input**: Accepts any valid SMILES string for molecule representation

## Requirements
- Python 3.6 or higher
- `requests` library (install with `pip install requests`)
- Internet connection to access the admetSAR 3.0 webserver

## Notes
- The skill requires a valid SMILES string as input. Invalid SMILES strings may result in errors or unexpected behavior.
- The admetSAR 3.0 webserver may have rate limits or usage restrictions. Please refer to their terms of service for more information.
- This skill is intended for research and educational purposes only.

