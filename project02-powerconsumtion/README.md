# Project 02 — Power Consumption Demand Forecasting

---

## Deskripsi Proyek

Proyek **Power Consumption Demand Forecasting (Project ID: FL-002)** berfokus pada pembangunan model prediksi konsumsi daya listrik di 3 zona (Zone 1, Zone 2, Zone 3) berdasarkan data historis dari sistem pengukuran konsumsi daya serta variabel-variabel pendukung seperti suhu, kelembaban, kecepatan angin, dan diffuse flows.

Tujuan utama dari proyek ini adalah membangun model forecasting terbaik secara end-to-end dengan mengikuti standar dokumentasi dan rencana eksperimen industri yang ketat.

---

## Informasi Proyek

- **Project ID**: FL-002
- **Domain**: Data Science / Forecasting / Time Series Analysis
- **Dataset**: Power Consumption Dataset (UCI Machine Learning Repository)
- **Target Prediksi**: `PowerConsumption_Zone1`, `PowerConsumption_Zone2`, `PowerConsumption_Zone3`
- **Status**: ✅ Completed (Final Release v1.0)

---

## Struktur Folder

```
project02-powerconsumtion/
│
├── README.md                      # Dokumentasi Proyek 02
├── data/                          # Dataset dan Visualisasi
│   ├── powerconsumption.csv       # Data mentah (raw)
│   ├── processed_data.csv         # Data hasil cleaning
│   ├── featured_data.csv          # Data hasil feature engineering
│   ├── evaluation_report.csv      # Laporan evaluasi model
│   └── *.png                      # Visualisasi eksperimen
│
├── docs/                          # Dokumen Referensi (Single Source of Truth)
│   ├── prd.md                     # Product Requirements Document
│   ├── data-dictionary.md         # Penjelasan Detail Kolom
│   ├── experiment-plan.md         # Rencana Eksperimen
│   └── model-report.md            # Laporan Hasil Evaluasi Model
│
├── models/                        # Model tersimpan
│   ├── best_model.pkl             # Model terbaik hasil tuning
│   └── best_model.json            # Metadata model
│
└── notebooks/                     # Notebook Jupyter Eksperimen
    ├── 01_data_understanding.ipynb
    ├── 02_eda.ipynb
    ├── 03_preprocessing.ipynb
    ├── 04_feature_engineering.ipynb
    ├── 05_time_series_analysis.ipynb
    ├── 06_baseline_model.ipynb
    ├── 07_linear_regression.ipynb
    ├── 08_decision_tree.ipynb
    ├── 09_random_forest.ipynb
    ├── 10_gradient_boosting.ipynb
    ├── 11_xgboost.ipynb
    ├── 12_hyperparameter_tuning.ipynb
    ├── 13_evaluation.ipynb
    └── 14_dashboard.ipynb
```

---

## Log Eksperimen & Status

Eksperimen berjalan secara berurutan dan terdokumentasi lengkap pada [Experiment Plan](./docs/experiment-plan.md):

| Eksperimen ID | Nama Eksperimen | Notebook | Status | Deliverables |
|---|---|---|---|---|
| **EXP-001** | Data Understanding | `01_data_understanding.ipynb` | ✅ Completed | Dataset tervalidasi & struktur awal dipahami |
| **EXP-002** | Exploratory Data Analysis | `02_eda.ipynb` | ✅ Completed | Visualisasi pola suhu, kelembaban, dan konsumsi daya |
| **EXP-003** | Data Cleaning | `03_preprocessing.ipynb` | ✅ Completed | `processed_data.csv` siap pakai |
| **EXP-004** | Feature Engineering | `04_feature_engineering.ipynb` | ✅ Completed | `featured_data.csv` (Lag, Cyclic, Interaction) |
| **EXP-005** | Time Series Diagnostics | `05_time_series_analysis.ipynb` | ✅ Completed | Karakteristik time series dianalisis |
| **EXP-006** | Baseline Forecasting | `06_baseline_model.ipynb` | ✅ Completed | Naive, Moving Average, Seasonal Naive |
| **EXP-007** | Linear Regression | `07_linear_regression.ipynb` | ✅ Completed | Model regresi linear |
| **EXP-008** | Decision Tree | `08_decision_tree.ipynb` | ✅ Completed | Decision Tree |
| **EXP-009** | Random Forest | `09_random_forest.ipynb` | ✅ Completed | Random Forest |
| **EXP-010** | Gradient Boosting | `10_gradient_boosting.ipynb` | ✅ Completed | Gradient Boosting Regressor |
| **EXP-011** | XGBoost | `11_xgboost.ipynb` | ✅ Completed | XGBoost sebagai model utama |
| **EXP-012** | Hyperparameter Tuning | `12_hyperparameter_tuning.ipynb` | ✅ Completed | Grid Search XGBoost |
| **EXP-013** | Model Evaluation | `13_evaluation.ipynb` | ✅ Completed | Perbandingan semua model & error analysis |
| **EXP-014** | Dashboard | `14_dashboard.ipynb` | ✅ Completed | Dashboard interaktif |
| **EXP-015** | Final Documentation | - | ✅ Completed | Dokumentasi akhir & repository siap |

---

## Petunjuk Penggunaan

### Prasyarat
Instalasi package Python yang dibutuhkan:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib jupyter nbconvert
```

### Menjalankan Seluruh Notebook Secara Berurutan
```bash
cd project02-powerconsumtion/notebooks
jupyter nbconvert --to notebook --execute 01_data_understanding.ipynb --output 01_data_understanding.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 02_eda.ipynb --output 02_eda.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 03_preprocessing.ipynb --output 03_preprocessing.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 04_feature_engineering.ipynb --output 04_feature_engineering.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 05_time_series_analysis.ipynb --output 05_time_series_analysis.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 06_baseline_model.ipynb --output 06_baseline_model.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 07_linear_regression.ipynb --output 07_linear_regression.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 08_decision_tree.ipynb --output 08_decision_tree.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 09_random_forest.ipynb --output 09_random_forest.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 10_gradient_boosting.ipynb --output 10_gradient_boosting.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 11_xgboost.ipynb --output 11_xgboost.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 12_hyperparameter_tuning.ipynb --output 12_hyperparameter_tuning.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 13_evaluation.ipynb --output 13_evaluation.ipynb --ExecutePreprocessor.timeout=600 && \
jupyter nbconvert --to notebook --execute 14_dashboard.ipynb --output 14_dashboard.ipynb --ExecutePreprocessor.timeout=600
```

Atau jalankan satu per satu:
```bash
jupyter nbconvert --to notebook --execute <nama_notebook>.ipynb --output <nama_notebook>.ipynb
```
