# Data Mining Project - Credit Score Classification and Clustering

## Overview

This repository contains a course project for Data Mining focused on:

1. Credit Score classification (supervised learning)
2. Credit profile clustering (unsupervised learning)

Main submission target:
- `notebooks/final_submission.ipynb`

## Assignment Scope

The notebook must include:

1. Data preprocessing and leakage handling
2. Save cleaned CSV and reload it
3. EDA (shape, dtypes/info, label distribution, continuous stats)
4. PCA to 2D with label-colored scatter plot
5. Classification with 3 tuned models, 10-fold CV, F1 comparison
6. Clustering with KMeans + DBSCAN, evaluated using ARI or NMI
7. Conclusion and submission-ready outputs

## Dataset Facts

- Raw dataset: `data/raw/train.csv`
- Size: about 100000 rows, 28 columns
- Target label: `Credit_Score` (`Good`, `Standard`, `Poor`)
- Leakage risk: same `Customer_ID` appears in multiple `Month` rows

Important:
- You must apply exactly one leakage strategy before modeling:
	- keep one month only, or
	- deduplicate by `Customer_ID`

## Repository Structure

```text
data-mining-credit-score/
|- data/
|  |- raw/
|  |  |- train.csv
|  |- processed/
|- docs/
|  |- assignment/
|  |- planning/
|  |- report-notes/
|- notebooks/
|- src/
|- outputs/
|  |- figures/
|  |- tables/
|  |- metrics/
|- AGENTS.md
|- README.md
|- requirements.txt
```

## Setup

### 1) Create and activate virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

### 3) Launch notebook environment

```powershell
jupyter notebook
```

## Recommended Workflow

1. Open `notebooks/final_submission.ipynb`.
2. Follow required section order from `AGENTS.md`.
3. Save cleaned data to `data/processed/cleaned_credit_data.csv`.
4. Reload cleaned CSV before EDA and modeling.
5. Use sklearn pipelines + GridSearchCV + 10-fold CV for classification.
6. Exclude label for clustering and evaluate by ARI/NMI.
7. Restart kernel and run all cells before export.

## PDF Export

### Preferred option (webpdf)

```powershell
jupyter nbconvert --to webpdf notebooks/final_submission.ipynb --allow-chromium-download
```

### Latex-based option

```powershell
jupyter nbconvert --to pdf notebooks/final_submission.ipynb
```

Notes:
- `nbconvert --to pdf` needs a TeX environment (XeLaTeX).
- Some conversion flows also require Pandoc.

## Quality Checklist Before Submission

- Notebook runs top-to-bottom without error
- Leakage strategy is clearly documented
- Required columns are dropped during preprocessing
- Exactly 3 tuned classifiers are compared with 10-fold CV F1
- Clustering excludes target label and reports ARI or NMI
- Figures/tables are visible in notebook and PDF output

## Where to Read Project Rules

1. `docs/assignment/` (official assignment PDF)
2. `AGENTS.md` (execution contract for agents and contributors)
3. `docs/planning/` (phase and task breakdown)
