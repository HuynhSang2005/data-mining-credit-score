# Project Phases and Quality Gates

## Phase 0 - Requirement Lock

Objective:
- Parse assignment and convert to executable constraints.

Key actions:
- Read assignment PDF.
- Confirm required methods, metrics, and deliverables.
- Decide and document leakage strategy.

Exit criteria:
- A written requirement checklist exists in notebook/planning docs.

## Phase 1 - Data Preparation

Objective:
- Build a reliable cleaned dataset for all downstream analysis.

Key actions:
- Load raw CSV.
- Apply leakage mitigation (single month or deduplicate by `Customer_ID`).
- Remove identifier columns and optional free-text noise.
- Handle missing/invalid values and encode categorical features.
- Save cleaned CSV to `data/processed/cleaned_credit_data.csv` and reload it.

Exit criteria:
- Cleaned dataset is persisted and reproducible.

## Phase 2 - EDA Baseline

Objective:
- Produce mandatory descriptive analysis outputs.

Key actions:
- Report shape and dtypes.
- Report target label distribution.
- Report descriptive statistics for continuous features.
- Note key observations (imbalance, outliers, feature ranges).

Exit criteria:
- EDA section is complete and interpretable by reviewer.

## Phase 3 - PCA Visualization

Objective:
- Provide 2D projection of continuous feature space for intuitive inspection.

Key actions:
- Select continuous features only.
- Standardize selected features.
- Fit PCA to 2 components.
- Plot 2D scatter with color by true label.

Exit criteria:
- Notebook shows PCA figure and short interpretation.

## Phase 4 - Classification Pipeline

Objective:
- Compare tuned classification models using fair evaluation.

Key actions:
- Select 3 algorithms from the allowed list.
- Build sklearn pipelines.
- Run hyperparameter tuning via `GridSearchCV`.
- Evaluate with 10-fold cross-validation and F1-score.
- Produce model comparison table.

Exit criteria:
- Three tuned models are reported with comparable F1 metrics.

## Phase 5 - Clustering Pipeline

Objective:
- Run unsupervised learning and evaluate against known labels.

Key actions:
- Remove label from clustering inputs.
- Scale features.
- Run KMeans and DBSCAN.
- Evaluate with ARI or NMI against `Credit_Score`.

Exit criteria:
- Both clustering models are evaluated and compared.

## Phase 6 - Final Notebook and Submission

Objective:
- Deliver a clean, executable notebook and PDF-ready output.

Key actions:
- Ensure section order follows assignment.
- Restart kernel and run all.
- Remove noisy output and add concise conclusion.
- Export to PDF and validate readability.

Exit criteria:
- Submission artifacts are ready: `final_submission.ipynb` + PDF.

## Global Quality Gates (apply to all phases)

1. No data leakage in preprocessing or validation.
2. Reproducible code path (top-to-bottom notebook run).
3. Metrics and method choices are justified briefly.
4. Outputs are clear for both human grading and AI review.
