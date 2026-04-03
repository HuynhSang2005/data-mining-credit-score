# AGENTS.md

## 1. Mission

This repository is a Data Mining course project for Credit Score Classification and Clustering.

Primary delivery target:
- `notebooks/final_submission.ipynb`

Required quality:
- runs top-to-bottom without errors
- satisfies assignment requirements exactly
- includes clear narrative, figures, and metric tables
- can be exported to PDF for submission

## 2. Source-of-Truth Priority

When instructions conflict, apply this priority order:

1. Assignment PDF in `docs/assignment/`
2. This file (`AGENTS.md`)
3. Planning docs in `docs/planning/`
4. README usage notes

## 3. Verified Dataset Facts

- Raw file: `data/raw/train.csv`
- Approx size: 100000 rows, 28 columns
- Target label: `Credit_Score` with classes `Good`, `Standard`, `Poor`
- Critical risk: same `Customer_ID` appears across multiple `Month` values (time leakage risk)

## 4. Non-Negotiable Requirements

### 4.1 Preprocessing

- Load raw dataset.
- Mitigate leakage using exactly one strategy:
	- keep a single month, or
	- deduplicate by `Customer_ID`
- Drop identifier columns: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`
- `Type_of_Loan`: optional drop, but recommended
- Encode categorical variables
- Save cleaned file to CSV and reload it before EDA/modeling

### 4.2 EDA

- Show shape
- Show dtypes/info
- Show label distribution for `Credit_Score`
- Show descriptive statistics for continuous features (`min`, `max`, `mean` at minimum)

### 4.3 PCA

- Use only continuous features
- Standardize those features
- Reduce to 2 components
- Plot 2D scatter with color by true label

### 4.4 Classification

- Select 3 models from allowed set: KNN, Random Forest, Naive Bayes, AdaBoost, SVM
- Use `GridSearchCV` for hyperparameter tuning
- Use 10-fold cross-validation
- Compare models by F1-score (macro or weighted, documented)

### 4.5 Clustering

- Exclude target label from clustering input
- Run KMeans and DBSCAN
- Evaluate using label-aware external metrics: ARI or NMI

## 5. Leakage Prevention Protocol

Before any model training, an agent must verify all checks below:

1. A leakage strategy was explicitly applied and documented.
2. No transformer/scaler is fit on full dataset before split/CV.
3. Pipeline encapsulates preprocessing + estimator for classification.
4. Clustering input does not include `Credit_Score`.

If any check fails, stop and fix before proceeding.

## 6. Notebook Contract (Required Section Order)

1. Imports and configuration
2. Load raw data
3. Preprocessing and leakage handling
4. Save cleaned CSV
5. Reload cleaned CSV
6. EDA
7. PCA visualization
8. Classification (3 tuned models + 10-fold CV)
9. Clustering (KMeans + DBSCAN + ARI/NMI)
10. Conclusion

## 7. Engineering Rules

- Use deterministic random seeds where applicable.
- Keep code reproducible and restart-safe.
- Keep explanations concise and grading-focused.
- Prefer official references for methodology:
	- scikit-learn docs for pipelines, CV, metrics
	- Jupyter/nbconvert docs for export behavior

## 8. Artifact Paths

- Raw input: `data/raw/train.csv`
- Cleaned data: `data/processed/cleaned_credit_data.csv`
- Main notebook: `notebooks/final_submission.ipynb`
- Optional outputs:
	- `outputs/figures/`
	- `outputs/tables/`
	- `outputs/metrics/`

## 9. Definition of Done

All conditions must be true:

1. Notebook executes from first cell to last cell without error.
2. Every assignment requirement is addressed with evidence (tables/plots/metrics).
3. Classification compares 3 tuned models with 10-fold CV F1.
4. Clustering includes both KMeans and DBSCAN and reports ARI or NMI.
5. PDF export succeeds and is readable.

## 10. Common Failure Modes to Avoid

- Leakage from repeated customers across months
- Preprocessing outside CV pipeline
- Including label in clustering features
- Comparing models without hyperparameter tuning
- Missing explanations for metric choices
