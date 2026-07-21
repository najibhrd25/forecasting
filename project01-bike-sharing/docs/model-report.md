# Model Report

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-001 |
| Nama Project | Bike Sharing Demand Forecasting |
| Dokumen | Model Report |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Status | Draft |

---

# Tujuan Dokumen

Dokumen ini digunakan untuk mendokumentasikan seluruh model Machine Learning yang dikembangkan pada proyek ForecastLab.

Seluruh model akan dicatat secara sistematis sehingga proses evaluasi, perbandingan, reproduksi, dan deployment dapat dilakukan dengan mudah.

Dokumen ini juga berfungsi sebagai **Model Registry** selama pengembangan proyek.

---

# Ruang Lingkup

Dokumen ini mencakup.

- Baseline Model
- Machine Learning Model
- Hyperparameter
- Evaluation Metrics
- Training Time
- Feature Importance
- Model Comparison
- Deployment Recommendation

---

# Standar Evaluasi

Seluruh model dievaluasi menggunakan metrik yang sama.

| Metrik | Digunakan |
|---------|-----------|
| MAE | ✅ |
| RMSE | ✅ |
| MAPE | ✅ |
| R² Score | ✅ |
| Training Time | ✅ |

Seluruh model wajib menggunakan dataset dan proses preprocessing yang sama agar hasil evaluasi dapat dibandingkan secara adil.

---

# Model Registry

| ID | Model | Notebook | Status |
|----|--------|----------|--------|
| M-001 | Naive Forecast | 06_baseline_model.ipynb | ⬜ |
| M-002 | Moving Average | 06_baseline_model.ipynb | ⬜ |
| M-003 | Linear Regression | 07_linear_regression.ipynb | ⬜ |
| M-004 | Decision Tree | 08_decision_tree.ipynb | ⬜ |
| M-005 | Random Forest | 09_random_forest.ipynb | ⬜ |
| M-006 | Gradient Boosting | 10_gradient_boosting.ipynb | ⬜ |
| M-007 | XGBoost | 11_xgboost.ipynb | ⬜ |
| M-008 | Tuned Best Model | 12_hyperparameter_tuning.ipynb | ⬜ |

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

Seluruh model disimpan pada folder.

```
models/
```

Minimal terdiri atas.

```
model.pkl

model.json
```

File JSON berisi metadata model.
