# Adverse Outcome Pathway (AOP) Prediction System

## Overview
This project focuses on predicting Adverse Outcome Pathways (AOPs) for molecules using machine learning models, databases, and simulation techniques. The primary focus is on new, unknown molecules, with support for known molecules as well.

## Project Goals
- Predict AOPs for new molecules using known data and machine learning
- Provide known AOPs for reference molecules
- Generate comprehensive reports in PDF format
- Build a scalable system for AOP prediction and analysis

##### TBD #####
## Technology Stack
- **Primary Language**: Python
- **Key Libraries**: 
  - RDKit for chemical informatics
  - scikit-learn for machine learning
  - TensorFlow/PyTorch for deep learning
  - ReportLab for PDF generation
  - Requests for API interactions

## Data Sources
- **Public Databases**:
  - AOP-Wiki
  - ChEMBL
  - PubChem
  - CTDbase
  - Other toxicology databases

## System Architecture

### Core Components
1. **Data Ingestion Module**: Collects and preprocesses data from various sources
2. **Chemical Feature Extraction**: Extracts molecular descriptors and features
3. **Machine Learning Models**: 
   - Classification models for AOP prediction
   - Regression models for quantitative predictions
   - Similarity-based models for known molecule matching
4. **Simulation Engine**: Simulates biological pathways and interactions
5. **Report Generation**: Creates comprehensive PDF and markdown reports with predictions

### Workflow
1. **Input**: Molecule structure (SMILES, InChI, or SDF), all known relevant information (interactions, other known effects, uses, environment)
2. **Feature Extraction**: Calculate molecular descriptors and properties
3. **Database Search**: Check for known AOPs in reference databases
4. **Model Prediction**: Run ML models for AOP prediction
5. **Simulation**: Simulate biological pathways if needed
6. **Report Generation**: Create PDF report with all findings

## Setup Instructions

### Prerequisites
- TBD

### Installation

### Configuration


## Usage

### Predicting AOPs for New Molecules
```python?
```

### Getting Known AOPs
```python?
```

## Project Structure
``` MAYBE
aop-prediction-system/
├── data/                  # Raw and processed data
│   ├── databases/          # Database exports
│   ├── features/           # Extracted features
│   └── models/             # Trained models
├── src/                   # Source code
│   ├── data_ingestion/     # Data collection modules
│   ├── feature_extraction/ # Feature extraction code
│   ├── models/             # ML model implementations
│   ├── simulation/         # Simulation engine
│   ├── reporting/          # Report generation
│   └── utils/              # Utility functions
├── tests/                 # Test cases
├── config/                # Configuration files
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation
```

## Database Integration

### Supported Databases
- **AOP-Wiki**: Comprehensive AOP knowledge base
- **ChEMBL**: Bioactive compound database
- **PubChem**: Chemical substance database
- **CTDbase**: Comparative Toxicogenomics Database

### Database Connection
The system uses REST APIs and direct database connections where available. API keys should be stored in the `.env` file.

## Model Training

### Training Data
- Molecular structures with known AOPs
- Biological pathway data
- Environments data
- Toxicological endpoints

### Model Types
1. **Random Forest Classifier**: For AOP classification
2. **Neural Networks**: For complex pattern recognition
3. **Similarity Models**: For known molecule matching

### Training Process
```bash
python
```

## Evaluation Metrics


## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License
This project is licensed under the BST License - see the LICENSE file for details.

## Contact
For questions or issues, please contact:

## Future Enhancements
- Integration with more databases
- Advanced simulation capabilities
- Web interface for easier access
- Batch processing for multiple molecules
- API endpoints for programmatic access
- Confirming results and integrating approved data

