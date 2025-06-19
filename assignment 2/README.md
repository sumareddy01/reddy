## Regression Task:

Goal: Predict cholesterol levels (chol).

Model: ElasticNet Regression (combines L1 and L2 regularization).

Evaluation metrics: R² and RMSE.

Hyperparameters tuned: alpha and l1_ratio.

Heatmaps visualize model performance across different parameter combinations.

## Classification Task:

Goal: Predict presence of heart disease (num) as a binary label.

Models used: Logistic Regression and k-Nearest Neighbors (k-NN).

Evaluation metrics: Accuracy, F1 Score, AUROC, and AUPRC.

Hyperparameter tuning for logistic regression (penalty, solver) and k-NN (n_neighbors).

Plots generated: ROC Curve and Precision-Recall Curve for best model.

## Structure:

Data/heart_disease_uci.csv: Raw dataset.

Scripts/main.ipynb: Jupyter Notebook with full implementation.

README.md: Documentation and instructions.

## How to Run:

Clone the repo and navigate to the project folder.

Install dependencies (e.g., scikit-learn, pandas, seaborn).

Launch the Jupyter Notebook to explore the analysis.

Dependencies (can be added to requirements.txt):

pandas, numpy, matplotlib, seaborn, scikit-learn.