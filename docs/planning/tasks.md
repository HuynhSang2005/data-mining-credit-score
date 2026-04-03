# Tasks - Execution Backlog

This checklist is designed for both human contributors and AI-Agent execution.

## A. Setup and Inputs

- [ ] Confirm required files exist: `data/raw/train.csv`, `docs/assignment/Huong Dan Do An Credit Score.pdf` (or equivalent file name), `notebooks/`.
- [ ] Install dependencies from `requirements.txt` in a clean environment.
- [ ] Record run metadata in notebook (date, environment, package versions).

Done when:
- Environment can launch Jupyter and import all required packages.

## B. Requirement Parsing and Guardrails

- [ ] Read assignment PDF and extract mandatory requirements.
- [ ] Lock a leakage strategy (single month or deduplicate by `Customer_ID`).
- [ ] Document modeling constraints in notebook markdown.

Done when:
- Notebook contains a short "Assumptions and Constraints" section before preprocessing.

## C. Data Preprocessing

- [ ] Load raw data from `data/raw/train.csv`.
- [ ] Apply leakage strategy.
- [ ] Drop required identifier columns: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`.
- [ ] Optionally drop `Type_of_Loan` (recommended).
- [ ] Clean invalid/noisy values in numeric columns (e.g., impossible negative values if present).
- [ ] Encode categorical columns to numeric representations.
- [ ] Export cleaned dataset to `data/processed/cleaned_credit_data.csv`.
- [ ] Reload the cleaned CSV into a fresh DataFrame for downstream tasks.

Done when:
- Cleaned CSV exists and can be reloaded without transformation errors.

## D. EDA

- [ ] Show data shape.
- [ ] Show data types (`dtypes` or equivalent summary).
- [ ] Show class distribution for `Credit_Score`.
- [ ] Show descriptive stats (`min`, `max`, `mean`) for continuous features.
- [ ] Add short interpretation notes (imbalance, outliers, spread).

Done when:
- All four required EDA outputs are visible in notebook with concise commentary.

## E. PCA Visualization

- [ ] Build a dataset with continuous features only.
- [ ] Standardize continuous features.
- [ ] Reduce to 2 principal components.
- [ ] Plot 2D scatter with color by true `Credit_Score` label.
- [ ] Add interpretation note (cluster overlap/separation).

Done when:
- PCA section has both code and a readable figure in notebook output.

## F. Classification

- [ ] Select exactly 3 models from: KNN, Random Forest, Naive Bayes, AdaBoost, SVM.
- [ ] Build sklearn pipelines for each model (including preprocessing where required).
- [ ] Tune hyperparameters using `GridSearchCV`.
- [ ] Evaluate with k-fold CV (`k=10`) using F1-score (`macro` or `weighted`, with rationale).
- [ ] Produce a comparison table and identify the best model.

Done when:
- Notebook contains tuned parameter sets and a final ranking table for 3 models.

## G. Clustering

- [ ] Remove target label column from clustering input.
- [ ] Scale features for distance-based clustering.
- [ ] Run KMeans (`n_clusters=3` baseline).
- [ ] Run DBSCAN (tune at least `eps` and `min_samples`).
- [ ] Evaluate clusters using ground-truth labels with ARI or NMI.
- [ ] Compare KMeans vs DBSCAN in a compact results table.

Done when:
- Both algorithms run successfully and report at least one accepted metric (ARI or NMI).

## H. Notebook Finalization

- [ ] Ensure notebook sections follow required order.
- [ ] Restart kernel and run all cells top-to-bottom.
- [ ] Remove accidental debug prints/noisy intermediate outputs.
- [ ] Add final conclusion summarizing key findings.

Done when:
- End-to-end execution succeeds with no cell errors.

## I. Submission Readiness

- [ ] Export notebook output to PDF.
- [ ] Confirm PDF includes code, plots, and results.
- [ ] Validate file names and submission artifacts.

Done when:
- Submission package is ready: `.ipynb` + PDF.

## Quick Review Checklist

- [ ] No leakage from time-series duplicates.
- [ ] No label used in clustering input.
- [ ] No preprocessing fit on full dataset before CV.
- [ ] Exactly 3 tuned classification models.
- [ ] Correct evaluation metrics used and explained.
