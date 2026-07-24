# Experiment Plan

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-002 |
| Nama Project | Power Consumption Demand Forecasting |
| Dokumen | Experiment Plan |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Status | Aktif |

---

# Tujuan Dokumen

Dokumen ini digunakan sebagai panduan seluruh eksperimen yang dilakukan selama pengembangan proyek. Setiap eksperimen memiliki tujuan, hipotesis, input, output, serta indikator keberhasilan yang jelas.

---

# Aturan Eksperimen

## 1. Satu Eksperimen, Satu Tujuan
Setiap eksperimen hanya memiliki satu tujuan utama.

## 2. Eksperimen Bersifat Berurutan
Setiap eksperimen memiliki ketergantungan terhadap eksperimen sebelumnya.

## 3. Seluruh Eksperimen Harus Terdokumentasi
Setiap eksperimen minimal memiliki: Tujuan, Hipotesis, Notebook, Input, Output, Hasil, Insight, Status.

## 4. Reproducibility
Seluruh eksperimen harus dapat dijalankan ulang dengan output yang sama.

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

## Hipotesis
Dataset memiliki struktur yang lengkap, tidak terdapat missing value yang signifikan, dan seluruh feature sesuai dengan dokumentasi pada Data Dictionary.

## Notebook
```
01_data_understanding.ipynb
```

## Input
- Dataset `powerconsumption.csv`
- Data Dictionary

## Aktivitas
- Memuat dataset
- Menampilkan dimensi dataset
- Memeriksa nama kolom
- Memeriksa tipe data
- Memeriksa missing value
- Memeriksa duplicate data
- Menampilkan statistik deskriptif
- Memastikan target prediksi

## Output
- Ringkasan dataset
- Statistik deskriptif
- Validasi struktur dataset

## Status
✅ Completed

---

# EXP-002 — Exploratory Data Analysis (EDA)

## Tujuan
Menemukan pola, tren, distribusi, hubungan antar feature, serta insight awal yang dapat digunakan untuk proses feature engineering dan modeling.

## Hipotesis
Dataset memiliki pola harian dan pola musiman yang memengaruhi konsumsi daya listrik.

## Notebook
```
02_eda.ipynb
```

## Input
- Dataset hasil validasi
- Data Dictionary

## Aktivitas
- Distribusi konsumsi daya per zona
- Tren konsumsi daya harian, mingguan, bulanan
- Distribusi suhu dan kelembaban
- Hubungan suhu dengan konsumsi daya
- Correlation matrix

## Output
- Grafik EDA
- Insight setiap feature

## Status
✅ Completed

---

# EXP-003 — Data Cleaning

## Tujuan
Memastikan dataset siap digunakan untuk proses feature engineering dan modeling.

## Hipotesis
Dataset relatif bersih namun masih memerlukan validasi terhadap outlier, tipe data, serta konsistensi nilai.

## Notebook
```
03_preprocessing.ipynb
```

## Aktivitas
- Validasi missing value
- Validasi duplicate
- Validasi outlier
- Validasi tipe data
- Konversi Datetime
- Menyimpan dataset hasil preprocessing

## Output
- Dataset bersih
- Laporan preprocessing

## Status
✅ Completed

---

# EXP-004 — Feature Engineering

## Tujuan
Meningkatkan kualitas informasi pada dataset dengan membangun feature baru yang relevan untuk forecasting.

## Hipotesis
Feature turunan dari waktu akan meningkatkan kemampuan model dalam menangkap pola konsumsi daya.

## Notebook
```
04_feature_engineering.ipynb
```

## Aktivitas
- Membuat feature waktu (jam, hari, bulan, weekday/weekend)
- Membuat feature cyclic (sin dan cos untuk jam)
- Membuat lag feature
- Membuat rolling statistics (mean, std)
- Menyimpan dataset hasil feature engineering

## Output
- Dataset dengan feature baru
- Dokumentasi feature engineering

## Status
✅ Completed

---

# EXP-005 — Time Series Diagnostics

## Tujuan
Menganalisis karakteristik data time series sebelum proses pemodelan dilakukan.

## Hipotesis
Dataset memiliki tren, pola musiman (seasonality), pola harian, autokorelasi, dan ketergantungan terhadap observasi sebelumnya.

## Notebook
```
05_time_series_analysis.ipynb
```

## Aktivitas
- Plot time series
- Moving Average & Rolling Statistics
- ACF & PACF
- Augmented Dickey Fuller Test
- Time Series Decomposition

## Output
- Grafik tren
- Grafik seasonality
- Hasil ADF Test
- Grafik decomposition

## Status
✅ Completed

---

# EXP-006 — Baseline Forecasting

## Tujuan
Membangun model baseline sebagai pembanding seluruh model Machine Learning.

## Hipotesis
Model sederhana mampu memberikan gambaran awal mengenai tingkat kesulitan forecasting pada dataset.

## Notebook
```
06_baseline_model.ipynb
```

## Model
- Naive Forecast
- Moving Average
- Seasonal Naive

## Aktivitas
- Membuat Naive Forecast
- Membuat Moving Average Forecast
- Membuat Seasonal Naive
- Menghitung MAE, RMSE, MAPE
- Visualisasi hasil prediksi

## Status
⬜ Not Started

---

# EXP-007 — Linear Regression

## Tujuan
Membangun model regresi linear sebagai baseline Machine Learning.

## Hipotesis
Hubungan linear antar feature mampu menjelaskan sebagian variasi konsumsi daya.

## Notebook
```
07_linear_regression.ipynb
```

## Aktivitas
- Training
- Prediction
- Evaluation
- Feature Importance (Coefficient)

## Status
✅ Completed

---

# EXP-008 — Decision Tree

## Tujuan
Membandingkan model non-linear pertama dengan Linear Regression.

## Hipotesis
Decision Tree mampu menangkap hubungan non-linear yang tidak dapat dipelajari oleh Linear Regression.

## Notebook
```
08_decision_tree.ipynb
```

## Aktivitas
- Training
- Prediction
- Evaluation

## Status
✅ Completed

---

# EXP-009 — Random Forest

## Tujuan
Membangun model ensemble untuk meningkatkan stabilitas prediksi.

## Hipotesis
Random Forest menghasilkan performa lebih baik dibanding Decision Tree karena mengurangi overfitting.

## Notebook
```
09_random_forest.ipynb
```

## Aktivitas
- Training
- Prediction
- Feature Importance
- Evaluation

## Status
✅ Completed

---

# EXP-010 — Gradient Boosting

## Tujuan
Membangun model ensemble berbasis boosting untuk meningkatkan akurasi prediksi.

## Hipotesis
Gradient Boosting mampu memperbaiki kesalahan model sebelumnya secara bertahap.

## Notebook
```
10_gradient_boosting.ipynb
```

## Aktivitas
- Training Model
- Prediction
- Feature Importance
- Residual Analysis
- Evaluation

## Status
⬜ Not Started

---

# EXP-011 — XGBoost

## Tujuan
Membangun model XGBoost sebagai model utama yang akan dibandingkan dengan seluruh model sebelumnya.

## Hipotesis
XGBoost menghasilkan performa terbaik pada dataset tabular karena mampu menangani hubungan non-linear secara efektif.

## Notebook
```
11_xgboost.ipynb
```

## Aktivitas
- Training
- Prediction
- Feature Importance
- Evaluation

## Status
✅ Completed

---

# EXP-012 — Hyperparameter Tuning

## Tujuan
Mengoptimalkan performa model terbaik melalui pencarian kombinasi hyperparameter yang lebih baik.

## Hipotesis
Performa model dapat ditingkatkan melalui proses tuning tanpa mengubah dataset.

## Notebook
```
12_hyperparameter_tuning.ipynb
```

## Metode
- Grid Search

## Aktivitas
- Menentukan parameter yang akan diuji
- Cross Validation
- Training
- Evaluation
- Menyimpan parameter terbaik

## Status
✅ Completed

---

# EXP-013 — Error Analysis & Model Evaluation

## Tujuan
Mengevaluasi seluruh model dan memahami karakteristik kesalahan prediksi.

## Hipotesis
Tidak semua kesalahan prediksi terjadi secara acak. Error memiliki pola yang dapat dianalisis.

## Notebook
```
13_evaluation.ipynb
```

## Aktivitas
- Perbandingan Model
- Error Distribution
- Residual Plot
- Error per Jam
- Error per Suhu

## Status
✅ Completed

---

# EXP-014 — Dashboard & Inference

## Tujuan
Menyediakan media visualisasi hasil forecasting agar mudah dipahami oleh pengguna.

## Hipotesis
Visualisasi yang baik akan mempermudah interpretasi hasil model.

## Notebook
```
14_dashboard.ipynb
```

## Dashboard Minimal
- KPI Card
- Grafik Historis
- Grafik Prediksi
- Model Performance
- Feature Importance

## Status
✅ Completed

---

# EXP-015 — Final Documentation

## Tujuan
Menyusun seluruh hasil eksperimen menjadi dokumentasi akhir proyek.

## Aktivitas
- Review Notebook
- Review Dokumentasi
- Review Model
- Review Dashboard
- Review Repository

## Deliverable
ForecastLab FL-002 Release v1.0

## Status
⬜ Not Started
