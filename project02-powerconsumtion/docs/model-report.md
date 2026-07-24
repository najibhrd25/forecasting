# Model Report

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-002 |
| Nama Project | Power Consumption Demand Forecasting |
| Dokumen | Model Report |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Status | Draft |

---

# Tujuan Dokumen

Dokumen ini digunakan untuk mendokumentasikan seluruh model Machine Learning yang dikembangkan pada proyek ForecastLab. Seluruh model akan dicatat secara sistematis sehingga proses evaluasi, perbandingan, reproduksi, dan deployment dapat dilakukan dengan mudah.

---

# Standar Evaluasi

| Metrik | Digunakan |
|---------|-----------|
| MAE | ✅ |
| RMSE | ✅ |
| MAPE | ✅ |
| R² Score | ✅ |
| Training Time | ✅ |

---

# Model Registry

| ID | Model | Notebook | Status |
|----|--------|----------|--------|
| M-001 | Naive Forecast | 06_baseline_model.ipynb | ✅ |
| M-002 | Moving Average | 06_baseline_model.ipynb | ✅ |
| M-003 | Seasonal Naive | 06_baseline_model.ipynb | ✅ |
| M-004 | Linear Regression | 07_linear_regression.ipynb | ✅ |
| M-005 | Decision Tree | 08_decision_tree.ipynb | ✅ |
| M-006 | Random Forest | 09_random_forest.ipynb | ✅ |
| M-007 | Gradient Boosting | 10_gradient_boosting.ipynb | ✅ |
| M-008 | XGBoost | 11_xgboost.ipynb | ✅ |
| M-009 | Tuned Best Model | 12_hyperparameter_tuning.ipynb | ✅ |

---

# Workflow Evaluasi Model

```
Feature Engineering
↓
Training
↓
Prediction
↓
Evaluation
↓
Residual Analysis
↓
Feature Importance
↓
Comparison
↓
Model Selection
↓
Model Saving
↓
Deployment
```

---

# Standar Penyimpanan Model

Seluruh model disimpan pada folder:

```
models/
```

Minimal terdiri atas:

```
model.pkl
model.json
```

File JSON berisi metadata model:

- Nama Model
- Versi Dataset
- Feature yang digunakan
- Hyperparameter
- Evaluation Metrics
- Training Time
- Timestamp
