Assignment 4: Survival Analysis using the RADCURE Dataset

**Course**: Machine Learning in Bioinformatics  
**Student**: Suma Ambati  
**Date**: July 2025  

## Project Structure
reddy-4/
├── Data/
│ └── RADCURE_Clinical_v04_20241219.xlsx
├── Scripts/
│ └── main.ipynb
├── README.md
└── output/
├── cox_summary_table.png
├── km_curve.png
└── rsf_model_performance.png


## Objective

This project performs **survival analysis** on a clinical dataset of head and neck cancer patients (RADCURE), focusing on:

- **Kaplan-Meier Estimator**
- **Log-Rank Test**
- **Cox Proportional Hazards Model**
- **Random Survival Forest (RSF)**

The aim is to evaluate how **cancer stage (Stage III vs IV)** and **patient age** influence survival time.

---

## Data Source

- **File**: `RADCURE_Clinical_v04_20241219.xlsx`
- **Sample Size**: ~3259 patients
- **Key Variables**:
  - `Length FU`: Follow-up duration in months
  - `event`: Death (1) or Censored (0)
  - `Stage`: Cancer stage (III or IV)
  - `Age`: Age at diagnosis

---

## Methods Overview

### 1. Kaplan-Meier Estimator
- Compared survival probabilities over time for Stage III vs IV
- Plotted survival curves with 95% confidence intervals

### 2. Log-Rank Test
- Tested for statistical difference between survival distributions
- Reported p-value to confirm significance

### 3. Cox Proportional Hazards Model
- Multivariate model using `Age` and `Stage_num`
- Output: Hazard ratios, confidence intervals, significance

### 4. Random Survival Forest (RSF)
- Tree-based model fitted on Age and Stage
- Evaluated via Concordance Index (C-index)

---

## Key Results

| Method        | Result                                           |
|---------------|--------------------------------------------------|
| Log-Rank Test | p < 0.005 → Significant survival difference      |
| CoxPH         | Age HR = 1.05, Stage HR = 1.33 (both significant)|
| RSF           | Concordance Index = 0.602                        |

---

## Deliverables

- `main.ipynb` (fully annotated analysis)
- `README.md` (this file)
- PDF Report (optional based on rubric)
- Output figures (KM plot, Cox summary, etc.)

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/sumareddy01/reddy-4.git
   cd reddy-4
2.Activate environment (e.g., Pixi or Conda)
3. Launch Jupyter:
jupyter notebook Scripts/main.ipynb

##Dependencies
lifelines

matplotlib

scikit-learn

sksurv (scikit-survival)

pandas, numpy

##Notes
Missing values were handled by dropping incomplete rows.

Only Stage III and IV patients were included to ensure group comparability.

Concordance Index was used for RSF performance evaluation.

