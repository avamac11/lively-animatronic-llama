# AGENTS.md

## Repository Overview
This repository provides computational chemistry workflows using RDKit for molecular property prediction, virtual screening, ADMET analysis, molecular docking preparation, and chemical space exploration. It also includes capabilities for predicting Adverse Outcome Pathways (AOPs) for molecules using machine learning models, databases, and simulation techniques.

## Key Files
- `README.md`: Main project documentation with setup instructions and usage examples
- `.gitignore`: Excludes `/secret` directory and `*.pdf` files from version control
- `skills-lock.json`: Skill dependencies and configurations
- `topological_mapping/README.md`: Documentation for topological mapping tools
- `data/analysis/carcinogenesis_analysis.json`: Pre-analyzed carcinogenesis data
- `data/analysis/liver_toxicity_analysis.json`: Pre-analyzed liver toxicity data
- `examples/carcinogenesis_map.py`: Example script for carcinogenesis analysis
- `examples/example_map.py`: General example script

## Development Commands
### Installation
```bash
pip install rdkit scikit-learn tensorflow reportlab pandas matplotlib seaborn
```

### Running Examples
```bash
python examples/carcinogenesis_map.py
python examples/example_map.py
```

## Project Structure
```
cheminformatics-aop-system/
├── data/                  # Raw and processed data
│   ├── databases/          # Database exports
│   ├── features/           # Extracted features
│   ├── models/             # Trained models
│   └── analysis/           # Pre-analyzed data
├── src/                   # Source code
│   ├── cheminformatics/    # Cheminformatics modules
│   ├── aop/                # AOP prediction modules
│   └── utils/              # Utility functions
├── examples/              # Example scripts
├── topological_mapping/   # Topological mapping tools
├── tests/                 # Test cases
├── config/                # Configuration files
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation
```

## Notes
- The repository focuses on cheminformatics and AOP prediction
- Uses RDKit for molecular property calculations and analysis
- Includes machine learning models for AOP prediction
- Provides visualization tools for chemical space exploration
- The `secret` directory is intentionally excluded from version control

## Important Notices
- when applicable, use skills to solve problems/tasks and create results
- For cheminformatics tasks, use the cheminformatics skill
- For AOP prediction, use the AOP prediction capabilities in the src/aop directory
