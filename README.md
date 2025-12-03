Team Members:

- Mohamed Osama 13007322 - Role: Modeling notebook
- Malak Khaled 13007685 - Role: evaluation notebook
- Bahy Hany 13001097 - Role: Presentation and technical report
- Mohamed Wael 13002337 - Role: Data exploration notebook

---

Summary of Results

Model Performance (Test Set)

The final model (XGBoost with hyperparameter tuning) achieved the following performance on the test set:

| Metric | Value |
|--------|-------|
| Accuracy | 93.63% |
| Precision | 63.79% |
| Recall | 73.27% |
| F1-Score | 68.20% |
| ROC-AUC | 96.79% |
| PR-AUC | 79.89% |

Confusion Matrix (Test Set)
- True Negatives (TN): 940 - Correctly identified legitimate providers
- False Positives (FP): 42 - Legitimate providers flagged as fraud
- False Negatives (FN): 27 - Fraudulent providers missed
- True Positives (TP): 74 - Correctly identified fraudulent providers

Model Comparison (Validation Set)

| Model | Precision | Recall | F1-Score | ROC-AUC | PR-AUC |
|-------|-----------|--------|----------|---------|--------|
| XGBoost (Tuned) | 0.5897 | 0.6832 | 0.6330 | 0.9311 | 0.6534 |
| Random Forest (Tuned) | 0.4845 | 0.7723 | 0.5954 | 0.9281 | 0.5906 |
| Logistic Regression (Tuned) | 0.4309 | 0.8020 | 0.5606 | 0.9284 | 0.6300 |
| Decision Tree | 0.4312 | 0.6832 | 0.5287 | 0.7413 | 0.3694 |

Selected Model: XGBoost (Tuned) - Best combined F1-Score and PR-AUC performance

Key Findings

1. Class Imbalance: Successfully handled severe class imbalance (~9.35% fraud rate) using class weighting and SMOTE strategies
2. Feature Engineering: Created 131 provider-level features from claim-level data through aggregation
3. Geographic Patterns: Identified state-level variations in fraud rates
4. Temporal Patterns: Analyzed claim trends over time for fraudulent vs legitimate providers
5. Error Analysis: Conducted detailed case studies of false positives and false negatives to understand model limitations

Business Impact

- Cost Analysis: Model demonstrates significant cost savings compared to investigating all providers or missing fraud cases
- Detection Rate: Successfully identifies 73.27% of fraudulent providers while maintaining 63.79% precision
- Actionable Insights: Feature importance analysis reveals key indicators of fraud (e.g., claim count, diagnosis diversity, financial patterns)

---

Project Objective

The goal of this project is to:
- Detect potentially fraudulent providers from Medicare claims
- Handle severe class imbalance (~10% fraudulent)
- Aggregate multilevel data (patients → claims → providers)
- Provide actionable model predictions for investigators
- Compare several ML algorithms and justify model selection
- Maintain interpretability while maximizing detection performance

---

Dataset Description

The Healthcare Provider Fraud Detection dataset contains anonymized Medicare data labeled for fraudulent and non-fraudulent providers.

Download from:https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis

The dataset consists of four files:

| File | Description |
|------|------------|
| Train_Beneficiarydata-1542865627584.csv | Demographics, coverage, and chronic conditions for each patient (BeneID) |
| Train_Inpatientdata-1542865627584.csv  | Hospital admission claims with financial, procedural, and physician details |
| Train_Outpatientdata-1542865627584.csv | Outpatient claim data (visits, tests, minor procedures) |
| Train-1542865627584.csv | Provider-level fraud labels (Yes/No) |

Key identifiers:
- BeneID → Links beneficiaries across claim tables
- Provider → Links claims to fraud label

The target variable is PotentialFraud, treated as binary:
```
Yes → 1 (fraud)
No  → 0 (legitimate)
```

---

Notebook 01 - Data Exploration and Feature Engineering

This notebook analyzes raw tables and transforms them into provider-level features.

Steps Performed:

Data Inspection
- Dataset shape
- Column types
- Value distributions
- Missing values
- Duplicate detection

Fraud Distribution
- Fraud ratio
- Bar plots of class imbalance

Domain-Oriented Validations
- Illegal financial values
- Admission–Discharge inconsistencies
- Claim start/end date integrity
- LOS validity

Exploratory Insights
- Beneficiary demographics
- Claim amount distributions
- Diagnosis and procedure diversity
- Provider patterns by state
- Temporal trends in claims

---

Feature Engineering (Provider-Level)

Claims are aggregated at the Provider level using:
- Counts: number of claims, number of unique beneficiaries
- Sums/Means: reimbursements, deductible amounts
- Diversity: unique procedures, unique diagnosis codes
- Ratios:
  - Claims per beneficiary
  - Inpatient/Outpatient ratio
- Temporal and geographic features

The resulting table is saved as provider_level_features.csv

---

Notebook 02 - Modeling and Hyperparameter Tuning

This notebook trains multiple ML models and compares them fairly.

Train/Validation/Test Split
- Stratified
- 60 / 20 / 20
- Consistent across models

Class imbalance handling
Three strategies:
1. Class weights
2. SMOTE oversampling
3. SMOTE + Tomek Links

Models Implemented
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting / XGBoost

Each model was evaluated using:
- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC
- Confusion Matrix

Hyperparameter tuning
Performed via GridSearchCV (CV=5):
- Logistic Regression C parameter
- Random Forest depth/estimators/splits
- XGBoost learning rate and depth

---

Model Selection Criteria

Fraud detection prioritizes recall and precision for fraud cases, not accuracy.

Performance Metric
A combined score: Combined = normalized(F1) + normalized(PR-AUC)

Selected Model:
XGBoost (tuned)

Why?
- Best F1-score
- Highest PR-AUC
- Robust to imbalance
- Handles non-linear patterns

---

Notebook 03 - Evaluation and Error Analysis

Evaluation performed on unseen test set (20%).

Metrics Reported
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion matrix (absolute and normalized)

Performance Visualization
- ROC curve
- Precision–Recall curve

---

Cost-Based Analysis

We simulate business cost scenarios:

- False Positives → investigation costs
- False Negatives → undetected fraud loss


This demonstrates:
- Why fraud detection is cost-sensitive
- Why minimizing false negatives matters

---

Error Case Studies (FP and FN)

We manually inspect 2–3 providers of each type:

False Positives
Why legitimate providers were flagged:
- unusually high claim counts
- unusual beneficiary patterns
- specialty behavior

False Negatives
Why fraud was missed:
- well-camouflaged patterns
- similar behavior to normal providers
- insufficient engineered features

This section helps auditors understand where the model fails.

---

Model Storage

Saved files:
/data/models/
  ├ best_model.pkl
  ├ scaler.pkl
  ├ model_results.pkl
  ├ model_comparison.csv
  └ test_indices.csv

---

Environment Setup

Requirements
- Python: 3.9 or higher
- Operating System: macOS, Linux, or Windows

Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd fraud_detection_project
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Required Packages

The project uses the following key libraries (see requirements.txt for exact versions):
- pandas==2.1.3 - Data manipulation and analysis
- numpy==1.26.2 - Numerical computing
- matplotlib==3.8.2 - Plotting and visualization
- seaborn==0.13.0 - Statistical data visualization
- scikit-learn==1.3.2 - Machine learning algorithms and utilities
- xgboost==2.0.3 - Gradient boosting framework
- imbalanced-learn==0.11.0 - Handling class imbalance (SMOTE, etc.)
- jupyter==1.0.0 - Jupyter notebook environment
- joblib - Model serialization (included with scikit-learn)

Reproducibility

All random operations use a fixed seed for reproducibility:
```python
np.random.seed(42)
```

---

Reproduction Instructions

Step 1: Download Dataset

Download the Healthcare Provider Fraud Detection dataset from Kaggle:
- Link:https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis

- Place the following CSV files in the data/ directory:
  - Train_Beneficiarydata-1542865627584.csv
  - Train_Inpatientdata-1542865627584.csv
  - Train_Outpatientdata-1542865627584.csv
  - Train-1542865627584.csv

Step 2: Run Notebooks Sequentially

Execute the notebooks in order:

1. 01_data_exploration_and_feature_engineering.ipynb
   - Loads and explores all datasets
   - Performs data quality assessment
   - Conducts exploratory data analysis (including geographic and temporal patterns)
   - Creates provider-level features through aggregation
   - Saves processed features to data/provider_level_features.csv
   - Expected output: provider_level_features.csv (5410 rows, 134 columns)

2. 02_modeling.ipynb
   - Loads processed features
   - Creates train/validation/test split (60/20/20)
   - Implements class imbalance handling strategies
   - Trains and tunes multiple models (Logistic Regression, Random Forest, XGBoost, Decision Tree)
   - Performs hyperparameter tuning using GridSearchCV
   - Compares models and discusses trade-offs (interpretability vs performance)
   - Selects best model based on F1-Score and PR-AUC
   - Saves trained models to data/models/
   - Expected output: Best model (XGBoost), scaler, and comparison results

3. 03_evaluation.ipynb
   - Loads best model and test set
   - Evaluates model on unseen test data
   - Generates comprehensive metrics and visualizations
   - Performs cost-based analysis
   - Conducts error analysis with case studies (2-3 false positives, 2-3 false negatives)
   - Expected output: Evaluation metrics, confusion matrix, ROC/PR curves, error analysis

Step 3: Verify Results

After running all notebooks, verify:
- data/provider_level_features.csv exists (5410 rows)
- data/models/best_model.pkl exists
- Test set metrics match expected values (see Summary of Results above)

Notes

- Execution Time: Full pipeline takes approximately 30-60 minutes depending on hardware
- Memory Requirements: At least 4GB RAM recommended
- Jupyter: Ensure Jupyter is installed and running: jupyter notebook or jupyter lab

---

Project Structure

```
fraud_detection_project/
├── README.md
├── requirements.txt
├── data/
│   ├── Train_Beneficiarydata-1542865627584.csv
│   ├── Train_Inpatientdata-1542865627584.csv
│   ├── Train_Outpatientdata-1542865627584.csv
│   ├── Train-1542865627584.csv
│   ├── provider_level_features.csv
│   └── models/
│      ├── best_model.pkl
│      ├── scaler.pkl
│      ├── model_results.pkl
│      ├── model_comparison.csv
│      └── test_indices.csv
├── notebooks/
│   ├── 01_data_exploration_and_feature_engineering.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_evaluation.ipynb
└── reports/
    ├── technical_report.pdf
    └── presentation_notes.md
```

---

Methodology Summary

1. Data Exploration: Comprehensive analysis of all datasets, relationships, data quality, and patterns
2. Feature Engineering: Aggregation of claim-level data to provider-level features (131 features)
3. Class Imbalance Handling: Multiple strategies evaluated (class weighting, SMOTE, SMOTE+Tomek)
4. Model Comparison: Four algorithms evaluated (Logistic Regression, Random Forest, XGBoost, Decision Tree)
5. Hyperparameter Tuning: GridSearchCV with 5-fold cross-validation
6. Evaluation: Comprehensive metrics including Precision, Recall, F1, ROC-AUC, PR-AUC
7. Error Analysis: Detailed case studies of false positives and false negatives
8. Geographic and Temporal Analysis: State-level fraud patterns and temporal trends

Key Features

- Provider-Level Aggregation: Transforms claim-level data into provider-level features
- Comprehensive EDA: Geographic patterns, temporal trends, and behavioral comparisons
- Multiple Models: Evaluated 4 different algorithms with hyperparameter tuning
- Class Imbalance Handling: Multiple strategies tested and compared
- Trade-offs Analysis: Detailed discussion of interpretability vs performance
- Error Analysis: Case studies of model failures to guide improvements
