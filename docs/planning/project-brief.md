# Project Brief - Credit Score Data Mining

## 1. Problem Statement

Build an end-to-end Data Mining workflow for Credit Score prediction and clustering from the raw dataset in `data/raw/train.csv`.

The final deliverable must be a single executable notebook (`notebooks/final_submission.ipynb`) that satisfies assignment requirements and is ready for PDF export.

## 2. Assignment-Aligned Objectives

1. Preprocess and clean raw data.
2. Export cleaned data to CSV and reload it.
3. Perform EDA (shape, dtypes, label distribution, descriptive stats).
4. Run PCA to 2D on continuous features and visualize with label colors.
5. Train and compare 3 classifiers with hyperparameter tuning and 10-fold CV using F1-score.
6. Run KMeans and DBSCAN clustering without target label in features and evaluate by ARI or NMI.

## 3. Verified Dataset Facts

- Source file: `data/raw/train.csv`
- Observed size: 100000 rows x 28 columns
- Target column: `Credit_Score`
- Target classes: `Good`, `Standard`, `Poor`
- Key risk: each `Customer_ID` appears across multiple `Month` values, which can cause severe data leakage.

## 4. Scope

### In Scope

- Data cleaning and leakage control.
- Feature preparation for supervised and unsupervised tasks.
- EDA, PCA plotting, model comparison, and clustering evaluation.
- Notebook narrative quality for review and PDF export.

### Out of Scope

- Deep learning or external pretrained models.
- Production API deployment.
- Dashboard/web app packaging.

## 5. Non-Negotiable Constraints

- Remove identifier columns: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`.
- `Type_of_Loan` can be removed (recommended due to free-text complexity).
- Use encoding for categorical variables.
- Use only continuous features for PCA.
- Use sklearn pipelines for preprocessing + model training to avoid leakage.
- Do not fit scalers/transformers on full data before split/CV.

## 6. Leakage Strategy Decision

Choose exactly one strategy and document it in notebook markdown:

1. Filter to a single month.
2. Deduplicate by `Customer_ID`.

Recommended default for this project: deduplicate by `Customer_ID` to keep one profile per customer and reduce temporal leakage.

## 7. Deliverables

1. `notebooks/final_submission.ipynb` (main submission notebook).
2. `data/processed/cleaned_credit_data.csv` (output of preprocessing stage).
3. Optional artifacts (if generated):
	- `outputs/figures/` for plots
	- `outputs/tables/` for model comparison tables
	- `outputs/metrics/` for metric summaries

## 8. Acceptance Criteria

- Notebook runs top-to-bottom with no errors.
- All required sections exist and are complete.
- Classification includes exactly 3 tuned models and 10-fold CV comparison using F1 (macro/weighted with clear note).
- Clustering excludes target label from input and reports ARI or NMI.
- Explanations and visualizations are clear enough for grading and PDF export.

## 9. Primary Risks and Mitigation

1. Leakage risk from repeated customers across months.
	- Mitigation: enforce strategy in Section 6 and verify before modeling.
2. Mixed feature types and noisy values.
	- Mitigation: explicit preprocessing pipeline and data validation checks.
3. Unstable model comparison due to inconsistent preprocessing.
	- Mitigation: unified sklearn pipelines and consistent CV strategy.
4. PDF export failure at submission time.
	- Mitigation: run export check early with nbconvert workflow.
