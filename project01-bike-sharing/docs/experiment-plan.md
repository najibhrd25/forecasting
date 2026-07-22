# Experiment Plan

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-001 |
| Nama Project | Bike Sharing Demand Forecasting |
| Dokumen | Experiment Plan |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Status | Aktif |

---

# Tujuan Dokumen

Dokumen ini digunakan sebagai panduan seluruh eksperimen yang dilakukan selama pengembangan proyek.

Setiap eksperimen memiliki tujuan, hipotesis, input, output, serta indikator keberhasilan yang jelas.

Dokumen ini juga berfungsi sebagai log perkembangan proyek sehingga seluruh proses dapat ditelusuri kembali.

---

# Aturan Eksperimen

Seluruh eksperimen pada proyek ForecastLab harus mengikuti prinsip berikut.

## 1. Satu Eksperimen, Satu Tujuan

Setiap eksperimen hanya memiliki satu tujuan utama.

Contoh:

- Memahami dataset
- Membersihkan data
- Melatih model
- Mengevaluasi model

Eksperimen tidak diperbolehkan memiliki terlalu banyak tujuan dalam satu notebook.

---

## 2. Eksperimen Bersifat Berurutan

Setiap eksperimen memiliki ketergantungan terhadap eksperimen sebelumnya.

Contoh.

EXP-002 tidak boleh dimulai apabila EXP-001 belum selesai.

EXP-006 tidak boleh dimulai apabila preprocessing belum selesai.

---

## 3. Seluruh Eksperimen Harus Terdokumentasi

Setiap eksperimen minimal memiliki.

- Tujuan
- Hipotesis
- Notebook
- Input
- Output
- Hasil
- Insight
- Status

---

## 4. Reproducibility

Seluruh eksperimen harus dapat dijalankan ulang.

Notebook harus menghasilkan output yang sama apabila dijalankan menggunakan dataset yang sama.

---

# Workflow Eksperimen

```

Project Setup

↓

EXP-001

↓

EXP-002

↓

EXP-003

↓

EXP-004

↓

EXP-005

↓

EXP-006

↓

EXP-007

↓

EXP-008

↓

EXP-009

↓

EXP-010

↓

EXP-011

↓

EXP-012

↓

EXP-013

↓

EXP-014

↓

EXP-015

```

Setiap eksperimen hanya dapat dimulai apabila eksperimen sebelumnya telah selesai.

---

# Status Eksperimen

| Status | Arti |
|----------|------|
| ⬜ Not Started | Belum dimulai |
| 🟨 In Progress | Sedang dikerjakan |
| ✅ Completed | Selesai |
| 🔄 Revisi | Perlu diperbaiki |
| ❌ Dibatalkan | Tidak digunakan |

---

# Ringkasan Seluruh Eksperimen

| ID | Nama Eksperimen | Notebook | Status |
|----|-----------------|----------|--------|
| EXP-001 | Data Understanding | 01_data_understanding.ipynb | ✅ |
| EXP-002 | Exploratory Data Analysis | 02_eda.ipynb | ✅ |
| EXP-003 | Data Cleaning | 03_preprocessing.ipynb | ✅ |
| EXP-004 | Feature Engineering | 04_feature_engineering.ipynb | ✅ |
| EXP-005 | Time Series Analysis | 05_time_series_analysis.ipynb | ✅ |
| EXP-006 | Baseline Forecasting | 06_baseline_model.ipynb | ✅ |
| EXP-007 | Linear Regression | 07_linear_regression.ipynb | ✅ |
| EXP-008 | Decision Tree | 08_decision_tree.ipynb | ✅ |
| EXP-009 | Random Forest | 09_random_forest.ipynb | ✅ |
| EXP-010 | Gradient Boosting | 10_gradient_boosting.ipynb | ✅ |
| EXP-011 | XGBoost | 11_xgboost.ipynb | ✅ |
| EXP-012 | Hyperparameter Tuning | 12_hyperparameter_tuning.ipynb | ✅ |
| EXP-013 | Model Evaluation | 13_evaluation.ipynb | ✅ |
| EXP-014 | Dashboard | 14_dashboard.ipynb | ✅ |
| EXP-015 | Final Documentation | - | ✅ |

---

# Detail Eksperimen

---

# EXP-001 — Data Understanding

## Tujuan

Memahami struktur dataset, tipe data, kualitas data, serta karakteristik awal dataset sebelum dilakukan analisis lebih lanjut.

---

## Hipotesis

Dataset memiliki struktur yang lengkap, tidak terdapat missing value yang signifikan, dan seluruh feature sesuai dengan dokumentasi pada Data Dictionary.

---

## Notebook

```
01_data_understanding.ipynb
```

---

## Input

- Dataset `hour.csv`
- Data Dictionary
- PRD

---

## Aktivitas

- Memuat dataset
- Menampilkan dimensi dataset
- Memeriksa nama kolom
- Memeriksa tipe data
- Memeriksa missing value
- Memeriksa duplicate data
- Menampilkan statistik deskriptif
- Memastikan target prediksi
- Memastikan feature sesuai Data Dictionary

---

## Output

- Ringkasan dataset
- Statistik deskriptif
- Validasi struktur dataset
- Catatan awal dataset

---

## Acceptance Criteria

- Dataset berhasil dimuat
- Jumlah record sesuai dokumentasi
- Jumlah kolom sesuai dokumentasi
- Missing value telah diperiksa
- Duplicate telah diperiksa
- Target telah dipastikan

---

## Deliverable

- Notebook selesai
- Dataset tervalidasi
- Insight awal ditulis

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-002 — Exploratory Data Analysis (EDA)

## Tujuan

Menemukan pola, tren, distribusi, hubungan antar feature, serta insight awal yang dapat digunakan untuk proses feature engineering dan modeling.

---

## Hipotesis

Dataset memiliki pola musiman dan pola harian yang memengaruhi jumlah penyewaan sepeda.

---

## Notebook

```
02_eda.ipynb
```

---

## Input

- Dataset hasil validasi
- Data Dictionary

---

## Aktivitas

### Analisis Target

- Distribusi `cnt`
- Histogram
- Boxplot
- Outlier
- Skewness

---

### Analisis Time Series

- Tren harian
- Tren bulanan
- Tren tahunan
- Pola per jam
- Pola weekday
- Pola weekend

---

### Analisis Cuaca

- Temperatur
- Feeling Temperature
- Humidity
- Wind Speed
- Weather Situation

---

### Analisis Korelasi

- Correlation Matrix
- Heatmap
- Scatter Plot
- Pair Plot (opsional)

---

### Analisis Feature

- Season
- Holiday
- Working Day
- Hour
- Month

---

## Output

- Grafik EDA
- Insight setiap feature
- Daftar feature penting
- Potensi feature engineering

---

## Acceptance Criteria

- Seluruh feature dianalisis
- Target dianalisis
- Insight minimal satu untuk setiap kelompok feature
- Grafik diberi interpretasi

---

## Deliverable

- Notebook EDA
- Insight EDA
- Daftar feature penting

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-003 — Data Cleaning

## Tujuan

Memastikan dataset siap digunakan untuk proses feature engineering dan modeling.

---

## Hipotesis

Dataset relatif bersih namun masih memerlukan validasi terhadap outlier, tipe data, serta konsistensi nilai.

---

## Notebook

```
03_preprocessing.ipynb
```

---

## Aktivitas

- Validasi missing value
- Validasi duplicate
- Validasi outlier
- Validasi tipe data
- Menghapus feature yang tidak digunakan
- Menyimpan dataset hasil preprocessing

---

## Output

- Dataset bersih
- Laporan preprocessing

---

## Acceptance Criteria

- Dataset siap modeling
- Dataset berhasil disimpan

---

## Deliverable

```
processed_data.csv
```

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-004 — Feature Engineering

## Tujuan

Meningkatkan kualitas informasi pada dataset dengan membangun feature baru yang relevan untuk forecasting.

---

## Hipotesis

Feature turunan dari waktu akan meningkatkan kemampuan model dalam menangkap pola penyewaan.

---

## Notebook

```
04_feature_engineering.ipynb
```

---

## Aktivitas

- Membuat feature waktu
- Membuat feature cyclic (`sin` dan `cos` untuk jam/bulan)
- Membuat lag feature
- Membuat rolling statistics
- Encoding feature kategorikal bila diperlukan
- Menyimpan dataset hasil feature engineering

---

## Output

- Dataset dengan feature baru
- Dokumentasi feature engineering

---

## Acceptance Criteria

- Feature baru terdokumentasi
- Dataset berhasil disimpan
- Feature siap digunakan untuk modeling

---

## Deliverable

```
featured_data.csv
```

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)
---

# EXP-005 — Time Series Diagnostics

## Tujuan

Menganalisis karakteristik data time series sebelum proses pemodelan dilakukan.

Eksperimen ini bertujuan memahami pola data sehingga pemilihan model forecasting dapat dilakukan secara tepat.

---

## Hipotesis

Dataset memiliki:

- Tren
- Pola musiman (seasonality)
- Pola harian
- Autokorelasi
- Ketergantungan terhadap observasi sebelumnya

---

## Notebook

```
05_time_series_analysis.ipynb
```

---

## Input

- featured_data.csv

---

## Aktivitas

### Analisis Tren

- Plot time series
- Moving Average
- Rolling Mean
- Rolling Standard Deviation

---

### Analisis Seasonality

- Pola per jam
- Pola per hari
- Pola per bulan
- Pola weekday
- Pola weekend

---

### Analisis Autocorrelation

- ACF
- PACF

---

### Stationarity Test

- Augmented Dickey Fuller Test (ADF)

---

### Time Series Decomposition

Memisahkan data menjadi:

- Trend
- Seasonality
- Residual

---

## Output

- Grafik tren
- Grafik seasonality
- Hasil ADF Test
- Grafik decomposition

---

## Acceptance Criteria

- Trend berhasil dianalisis
- Seasonality berhasil ditemukan
- Stationarity diketahui
- Autocorrelation diketahui

---

## Deliverable

Notebook Time Series Analysis

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-006 — Baseline Forecasting

## Tujuan

Membangun model baseline sebagai pembanding seluruh model Machine Learning.

---

## Hipotesis

Model sederhana mampu memberikan gambaran awal mengenai tingkat kesulitan forecasting pada dataset.

---

## Notebook

```
06_baseline_model.ipynb
```

---

## Model

- Naive Forecast
- Moving Average

---

## Aktivitas

- Membuat Naive Forecast
- Membuat Moving Average Forecast
- Menghitung MAE
- Menghitung RMSE
- Menghitung MAPE
- Visualisasi hasil prediksi

---

## Output

Baseline Performance

---

## Acceptance Criteria

- Minimal dua baseline selesai
- Seluruh metrik dihitung

---

## Deliverable

Notebook Baseline

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-007 — Linear Regression

## Tujuan

Membangun model regresi linear sebagai baseline Machine Learning.

---

## Hipotesis

Hubungan linear antar feature mampu menjelaskan sebagian variasi jumlah penyewaan sepeda.

---

## Notebook

```
07_linear_regression.ipynb
```

---

## Aktivitas

- Training
- Prediction
- Evaluation
- Feature Importance (Coefficient)

---

## Evaluasi

- MAE
- RMSE
- MAPE
- R² Score

---

## Output

Model Linear Regression

---

## Acceptance Criteria

- Model berhasil dilatih
- Prediksi berhasil dibuat
- Evaluasi selesai

---

## Deliverable

```
linear_regression.pkl
```

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-008 — Decision Tree

## Tujuan

Membandingkan model non-linear pertama dengan Linear Regression.

---

## Hipotesis

Decision Tree mampu menangkap hubungan non-linear yang tidak dapat dipelajari oleh Linear Regression.

---

## Notebook

```
08_decision_tree.ipynb
```

---

## Aktivitas

- Training
- Prediction
- Visualisasi Tree (Opsional)
- Evaluation

---

## Output

Decision Tree Model

---

## Acceptance Criteria

- Model selesai
- Evaluasi selesai

---

## Deliverable

```
decision_tree.pkl
```

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-009 — Random Forest

## Tujuan

Membangun model ensemble untuk meningkatkan stabilitas prediksi.

---

## Hipotesis

Random Forest menghasilkan performa lebih baik dibanding Decision Tree karena mengurangi overfitting.

---

## Notebook

```
09_random_forest.ipynb
```

---

## Aktivitas

- Training
- Prediction
- Feature Importance
- Evaluation

---

## Output

Random Forest Model

---

## Acceptance Criteria

- Model selesai
- Importance berhasil divisualisasikan

---

## Deliverable

```
random_forest.pkl
```

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-010 — Gradient Boosting

## Tujuan

Membangun model ensemble berbasis boosting untuk meningkatkan akurasi prediksi dibandingkan Random Forest.

---

## Hipotesis

Gradient Boosting mampu memperbaiki kesalahan model sebelumnya secara bertahap sehingga menghasilkan prediksi yang lebih akurat.

---

## Notebook

```
10_gradient_boosting.ipynb
```

---

## Input

- featured_data.csv

---

## Aktivitas

- Training Model
- Prediction
- Feature Importance
- Residual Analysis
- Evaluation

---

## Hyperparameter Awal

- n_estimators
- learning_rate
- max_depth
- min_samples_split
- min_samples_leaf

---

## Evaluasi

- MAE
- RMSE
- MAPE
- R² Score
- Training Time

---

## Output

- Gradient Boosting Model
- Grafik Prediksi
- Grafik Residual
- Feature Importance

---

## Deliverable

```
gradient_boosting.pkl

gradient_boosting.json
```

---

## Metadata Model

Model metadata disimpan dalam format JSON.

Informasi minimal meliputi.

- Nama Model
- Versi Dataset
- Feature yang digunakan
- Hyperparameter
- Evaluation Metrics
- Training Time
- Timestamp

---

## Acceptance Criteria

- Model berhasil dilatih
- Metadata berhasil disimpan
- Evaluasi selesai
- Visualisasi selesai

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-011 — XGBoost

## Tujuan

Membangun model XGBoost sebagai model utama yang akan dibandingkan dengan seluruh model sebelumnya.

---

## Hipotesis

XGBoost menghasilkan performa terbaik pada dataset tabular karena mampu menangani hubungan non-linear secara efektif.

---

## Notebook

```
11_xgboost.ipynb
```

---

## Aktivitas

- Training
- Prediction
- Feature Importance
- SHAP Analysis (Opsional)
- Evaluation

---

## Hyperparameter Awal

- n_estimators
- learning_rate
- max_depth
- subsample
- colsample_bytree
- random_state

---

## Evaluasi

- MAE
- RMSE
- MAPE
- R²

---

## Output

- Model XGBoost
- Feature Importance
- Prediction Plot

---

## Deliverable

```
xgboost.pkl

xgboost.json
```

---

## Acceptance Criteria

- Model berhasil dibuat
- Evaluasi selesai
- Metadata tersimpan

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-012 — Hyperparameter Tuning

## Tujuan

Mengoptimalkan performa model terbaik melalui pencarian kombinasi hyperparameter yang lebih baik.

---

## Hipotesis

Performa model dapat ditingkatkan melalui proses tuning tanpa mengubah dataset.

---

## Notebook

```
12_hyperparameter_tuning.ipynb
```

---

## Model yang Dituning

Model terbaik berdasarkan hasil EXP-007 hingga EXP-011.

---

## Metode

- Grid Search
- Random Search

(Catatan: Bayesian Optimization dapat dipertimbangkan pada pengembangan berikutnya.)

---

## Aktivitas

- Menentukan parameter yang akan diuji
- Cross Validation
- Training
- Evaluation
- Menyimpan parameter terbaik

---

## Output

- Best Parameters
- Best Model
- Comparison Before vs After

---

## Deliverable

```
best_model.pkl

best_model.json
```

---

## Acceptance Criteria

- Hyperparameter terbaik ditemukan
- Model terbaik berhasil disimpan
- Hasil dibandingkan dengan model awal

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-013 — Error Analysis & Model Evaluation

## Tujuan

Mengevaluasi seluruh model dan memahami karakteristik kesalahan prediksi.

---

## Hipotesis

Tidak semua kesalahan prediksi terjadi secara acak. Error memiliki pola yang dapat dianalisis.

---

## Notebook

```
13_evaluation.ipynb
```

---

## Aktivitas

### Perbandingan Model

- Baseline
- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

---

### Analisis Error

- Error Distribution
- Residual Plot
- Error per Jam
- Error per Musim
- Error per Kondisi Cuaca

---

### Evaluasi

- MAE
- RMSE
- MAPE
- R²

---

## Output

- Tabel Perbandingan Model
- Grafik Error
- Grafik Residual
- Kesimpulan Model Terbaik

---

## Acceptance Criteria

- Seluruh model dibandingkan
- Error berhasil dianalisis
- Model terbaik dipilih

---

## Deliverable

evaluation_report.csv

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-014 — Dashboard & Inference

## Tujuan

Menyediakan media visualisasi hasil forecasting agar mudah dipahami oleh pengguna.

---

## Hipotesis

Visualisasi yang baik akan mempermudah interpretasi hasil model.

---

## Notebook

```
14_dashboard.ipynb
```

---

## Aktivitas

- Load Best Model
- Load Metadata
- Load Dataset
- Prediction
- Visualisasi

---

## Dashboard Minimal

- KPI Card
- Grafik Historis
- Grafik Prediksi
- Model Performance
- Feature Importance

---

## Output

Dashboard Forecasting

---

## Acceptance Criteria

- Dashboard berjalan
- Model berhasil digunakan
- Visualisasi lengkap

---

## Deliverable

Dashboard Application

---

## Status

✅ Completed

---

## Insight

(Diisi setelah eksperimen selesai)

---

# EXP-015 — Final Documentation

## Tujuan

Menyusun seluruh hasil eksperimen menjadi dokumentasi akhir proyek.

---

## Aktivitas

- Review Notebook
- Review Dokumentasi
- Review Model
- Review Dashboard
- Review Repository

---

## Checklist

- README
- PRD
- Data Dictionary
- Experiment Plan
- Model Report
- Dashboard
- Notebook
- Models
- Dataset
- Assets

---

## Output

Repository siap dipublikasikan.

---

## Acceptance Criteria

- Seluruh notebook selesai
- Seluruh dokumen selesai
- Repository rapi
- Project dapat dijalankan ulang

---

## Deliverable

ForecastLab FL-001 Release v1.0

---

## Status

✅ Completed

---

## Insight

(Diisi setelah proyek selesai)

---

# Lampiran A — Struktur Folder Eksperimen

```

FL-001/

├── data/
│
├── docs/
│   ├── 01_PRD.md
│   ├── 02_DATA_DICTIONARY.md
│   ├── 03_EXPERIMENT_PLAN.md
│   ├── 04_MODEL_REPORT.md
│   ├── 05_ROADMAP.md
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_time_series_analysis.ipynb
│   ├── 06_baseline_model.ipynb
│   ├── 07_linear_regression.ipynb
│   ├── 08_decision_tree.ipynb
│   ├── 09_random_forest.ipynb
│   ├── 10_gradient_boosting.ipynb
│   ├── 11_xgboost.ipynb
│   ├── 12_hyperparameter_tuning.ipynb
│   ├── 13_evaluation.ipynb
│   └── 14_dashboard.ipynb
│
├── models/
│   ├── *.pkl
│   └── *.json
│
├── assets/
│
└── README.md

```

---

# Lampiran B — Standar Metadata Model

Setiap model yang disimpan wajib memiliki file metadata dalam format JSON.

Contoh struktur:

```json
{
  "model_name": "Random Forest",
  "version": "1.0.0",
  "dataset": "featured_data.csv",
  "features": [
    "season",
    "hr",
    "temp",
    "hum",
    "windspeed"
  ],
  "hyperparameters": {
    "n_estimators": 200,
    "max_depth": 12
  },
  "metrics": {
    "mae": 24.81,
    "rmse": 36.42,
    "mape": 12.5,
    "r2": 0.91
  },
  "training_time_seconds": 3.42,
  "created_at": "2026-07-21T10:30:00"
}
```