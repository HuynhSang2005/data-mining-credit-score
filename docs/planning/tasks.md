# Tasks - Execution Backlog

This checklist is designed for both human contributors and AI-Agent execution.

## A. Setup and Inputs

- [x] Confirm required files exist: `data/raw/train.csv`, `docs/assignment/Huong Dan Do An Credit Score.pdf` (or equivalent file name), `notebooks/`.
- [x] Install dependencies from `requirements.txt` in a clean environment.
- [ ] Record run metadata in notebook (date, environment, package versions).

Done when:
- Environment can launch Jupyter and import all required packages.

## B. Requirement Parsing and Guardrails

- [x] Read assignment PDF and extract mandatory requirements.
- [x] Lock a leakage strategy (single month or deduplicate by `Customer_ID`).
- [x] Document modeling constraints in notebook markdown.

Done when:
- Notebook contains a short "Assumptions and Constraints" section before preprocessing.

## C. Data Preprocessing

- [x] Load raw data from `data/raw/train.csv`.
- [x] Apply leakage strategy.
- [x] Drop required identifier columns: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`.
- [x] Optionally drop `Type_of_Loan` (recommended).
- [x] Clean invalid/noisy values in numeric columns (e.g., impossible negative values if present).
- [x] Encode categorical columns to numeric representations.
- [x] Export cleaned dataset to `data/processed/cleaned_credit_data.csv`.
- [x] Reload the cleaned CSV into a fresh DataFrame for downstream tasks.

Done when:
- Cleaned CSV exists and can be reloaded without transformation errors.

## D. EDA

- [x] Show data shape.
- [x] Show data types (`dtypes` or equivalent summary).
- [x] Show class distribution for `Credit_Score`.
- [x] Show descriptive stats (`min`, `max`, `mean`) for continuous features.
- [x] Add short interpretation notes (imbalance, outliers, spread).

Done when:
- All four required EDA outputs are visible in notebook with concise commentary.

## E. PCA Visualization

- [x] Build a dataset with continuous features only.
- [x] Standardize continuous features.
- [x] Reduce to 2 principal components.
- [x] Plot 2D scatter with color by true `Credit_Score` label.
- [x] Add interpretation note (cluster overlap/separation).

Done when:
- PCA section has both code and a readable figure in notebook output.

## F. Classification

- [x] Select exactly 3 models from: KNN, Random Forest, Naive Bayes, AdaBoost, SVM.
- [x] Build sklearn pipelines for each model (including preprocessing where required).
- [x] Tune hyperparameters using `GridSearchCV`.
- [x] Evaluate with k-fold CV (`k=10`) using F1-score (`macro` or `weighted`, with rationale).
- [x] Produce a comparison table and identify the best model.

Done when:
- Notebook contains tuned parameter sets and a final ranking table for 3 models.

## G. Clustering

- [x] Remove target label column from clustering input.
- [x] Scale features for distance-based clustering.
- [x] Run KMeans (`n_clusters=3` baseline).
- [x] Run DBSCAN (tune at least `eps` and `min_samples`).
- [x] Evaluate clusters using ground-truth labels with ARI or NMI.
- [x] Compare KMeans vs DBSCAN in a compact results table.

Done when:
- Both algorithms run successfully and report at least one accepted metric (ARI or NMI).

## H. Notebook Finalization

- [x] Ensure notebook sections follow required order.
- [x] Restart kernel and run all cells top-to-bottom.
- [x] Remove accidental debug prints/noisy intermediate outputs.
- [x] Add final conclusion summarizing key findings.

Done when:
- End-to-end execution succeeds with no cell errors.

## I. Submission Readiness

- [x] Export notebook output to PDF.
- [x] Confirm PDF includes code, plots, and results.
- [x] Validate file names and submission artifacts.

Done when:
- Submission package is ready: `.ipynb` + PDF.

## Quick Review Checklist

- [x] No leakage from time-series duplicates.
- [x] No label used in clustering input.
- [x] No preprocessing fit on full dataset before CV.
- [x] Exactly 3 tuned classification models.
- [x] Correct evaluation metrics used and explained.
