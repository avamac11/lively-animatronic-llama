---
name: admet-ai-scoring
description: Predict ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) properties of chemical compounds from SMILES strings using ADMET-AI, a local open-source Python package with pretrained graph neural network models. Use this skill whenever the user wants to evaluate drug-likeness, toxicity, bioavailability, blood-brain barrier permeability, CYP450 interactions, or other pharmacokinetic/toxicological properties of a molecule or list of molecules — even if they say "admetSAR", "ADMET properties", "check this compound for toxicity", "is this molecule drug-like", or paste in a SMILES string and ask about its safety/pharmacokinetics. Also use for batch screening of compound libraries (CSV of SMILES) for lead optimization or virtual screening filtering.
---

# ADMET Prediction

Predicts pharmacokinetic and toxicity properties of small molecules from their SMILES representation, using [ADMET-AI](https://github.com/swansonk14/admet_ai) — an open-source, locally-run graph neural network (Chemprop-RDKit) trained on 41 ADMET endpoints from the Therapeutics Data Commons. No API key, no network access, and no rate limits required; everything runs on-device after a one-time install.

**Note on admetSAR:** If the user specifically asks for "admetSAR," know that admetSAR (the website at lmmd.ecust.edu.cn) has no public API — it's a rate-limited web form with no documented, stable way to script against it. ADMET-AI is the recommended local substitute: it covers overlapping endpoints, has no rate limits, and is scored competitively against admetSAR on published benchmarks. Mention this substitution to the user briefly if they asked for admetSAR by name.

## Setup (one-time per environment)

Check if it's already installed before reinstalling:

```bash
python3 -c "import admet_ai" 2>/dev/null && echo "already installed" || pip install admet-ai --break-system-packages
```

Installation pulls in RDKit, Chemprop, PyTorch, and other deps, so it can take a few minutes and needs a few GB of disk. The first `ADETModel()` call also downloads pretrained model weights (~cached after first use).

If installation fails with a missing shared library error (e.g. `libXrender.so.1`), that's a system dependency, not a Python one — tell the user to install it via their OS package manager (e.g. `apt-get install -y libxrender1` on Ubuntu/Debian).

## Making predictions

### Quick path: use the bundled script

For most requests, run `scripts/predict_admet.py`, which wraps the ADMET-AI Python API and prints/saves results in a clean format.

**Single molecule:**
```bash
python3 scripts/predict_admet.py --smiles "CC(=O)OC1=CC=CC=C1C(=O)O"
```

**Multiple molecules inline:**
```bash
python3 scripts/predict_admet.py --smiles "CCO" "CC(=O)OC1=CC=CC=C1C(=O)O"
```

**Batch from a CSV** (must have a `smiles` column; add `--smiles-column` if it's named differently):
```bash
python3 scripts/predict_admet.py --input compounds.csv --output predictions.csv
```

The script prints a short human-readable summary to stdout for a handful of the most decision-relevant properties (drug-likeness, BBB permeability, hepatotoxicity (DILI), hERG inhibition, Ames mutagenicity, solubility, half-life) and always writes the full 41-property table to CSV when `--output` is given, or to `admet_predictions.csv` in the working directory by default for batch runs.

### Direct Python API (for custom pipelines)

When the user wants ADMET predictions integrated into a larger script rather than run standalone, use the library directly:

```python
from admet_ai import ADMETModel

model = ADMETModel()

# Single molecule -> dict of property: value
preds = model.predict(smiles="CC(=O)OC1=CC=CC=C1C(=O)O")

# List of molecules -> pandas DataFrame (index=SMILES, columns=properties)
preds_df = model.predict(smiles=["CCO", "CC(=O)OC1=CC=CC=C1C(=O)O"])
```

Classification properties (e.g. BBB permeability, DILI, Ames mutagenicity, hERG inhibition) return a probability between 0 and 1 that the molecule has that property — not a hard yes/no. Regression properties (e.g. half-life, solubility, clearance) return the predicted value directly, in the units documented in `references/endpoints.md`.

### Command-line tool (alternative to the bundled script)

ADMET-AI also installs a CLI directly:

```bash
admet_predict --smiles_path compounds.csv --save_path predictions.csv
```

Use the bundled `scripts/predict_admet.py` instead when the user wants readable output or wants both single-SMILES and CSV input handled by one interface — fall back to `admet_predict` only if the bundled script errors out for some reason.

## Interpreting and presenting results

- **Never present a raw 41-column table as the whole answer.** Summarize the properties most relevant to what the user asked (e.g. if they asked about oral drugs, lead with absorption/bioavailability/CYP metabolism; if they asked about safety, lead with the toxicity endpoints).
- State classification outputs as probabilities/likelihoods, not certainties ("~78% probability of BBB permeability" rather than "this molecule crosses the BBB").
- See `references/endpoints.md` for the full list of the 41 endpoints, what each measures, units for regression endpoints, and how to interpret the classification probabilities (higher = more likely to have the labeled property, e.g. higher DILI score = more likely hepatotoxic).
- These are machine-learning predictions from a model trained on public datasets, not experimental measurements or a substitute for wet-lab ADMET assays or regulatory toxicology — say so if the user seems to be treating results as a final safety determination.

