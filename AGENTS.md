# AGENTS.md

## Repository Overview 
This repository provides computational chemistry workflows using RDKit and PubChem for molecular property prediction, virtual screening, ADMET analysis, molecular docking preparation, and chemical space exploration. It also includes capabilities for predicting Adverse Outcome Pathways (AOPs) for molecules using machine learning models, databases, and simulation techniques. The agents, skills, and tools in this repository are to be used to predict the potential pathways of specific molecules, including their AOPs, ADMET scores, and toxicology analysis. The goal is for this workflow to be used for underesearched or new molecules.

## Key Files
- `README.md`: Main project documentation with setup instructions and usage examples
- `.gitignore`: Excludes `/secret` directory and `*.pdf` files from version control
- `skills-lock.json`: Skill dependencies and configurations
- `examples/example_map.py`: General example script for topological map
- `LICENSE.txt`: Project license information

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
│   │   └── aop_wiki_api/   # AOP Wiki API client
│   └── utils/              # Utility functions
├── examples/              # Example scripts
├── skills/                # Agent skills and capabilities
│   ├── aop-pathway/        # AOP pathway analysis
│   ├── find-skills/        # Skill discovery
│   └── dontuse-admet/      # ADMET analysis (deprecated)
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
- Includes an AOP Wiki API client for accessing external AOP data

## Important Notices
- When applicable, use skills to solve problems/tasks and create results
- For cheminformatics tasks, use the cheminformatics skill
- For AOP prediction, use the AOP prediction capabilities in the src/aop directory
- When calculating ADMET properties, scores, etc, use the skills/admet-scoring, along with the cheminformatics skill, but prioritize using scoring from the admet-scoring skill to use in parallel with cheminformatics
- All file operations must be confined to the current directory (`/home/avam11/lively-animatronic-llama`)
- No external directory access is permitted to save files to regardless of skill(s) used

## Usage Examples
- Use the `generate_orforglipron_aop.py` script to generate AOP predictions for specific molecules
- Run `aspirin aop/analyze_aspirin.py` for aspirin-specific AOP analysis examples
- Check `skills/aop-pathway/SKILL.md` for detailed AOP pathway analysis capabilities
