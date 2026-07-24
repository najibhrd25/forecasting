# Product Requirements Document (PRD)

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-002 |
| Nama Project | Power Consumption Demand Forecasting |
| Dokumen | Product Requirements Document |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Status | Aktif |

---

# 1. Latar Belakang

Kebutuhan energi listrik terus meningkat seiring pertumbuhan populasi dan aktivitas ekonomi. Prediksi konsumsi daya yang akurat sangat penting untuk perencanaan distribusi energi, penghematan biaya, dan pengelolaan beban jaringan listrik.

Data konsumsi daya dari 3 zona memberikan informasi yang berguna untuk memahami pola konsumsi energi dan memprediksi kebutuhan di masa depan.

---

# 2. Tujuan Proyek

## Tujuan Utama

Membangun model prediksi konsumsi daya listrik pada 3 zona (Zone 1, Zone 2, Zone 3) dengan tingkat akurasi tinggi berdasarkan data historis dan variabel pendukung.

## Tujuan Spesifik

1. Memahami karakteristik dataset konsumsi daya
2. Membersihkan dan mempersiapkan data untuk modeling
3. Membangun feature baru yang relevan untuk forecasting
4. Melatih beberapa model machine learning dan membandingkan performanya
5. Memilih model terbaik dan mengoptimalkan hyperparameter
6. Menganalisis error untuk memahami karakteristik kesalahan prediksi
7. Menyediakan dashboard untuk visualisasi hasil forecasting

---

# 3. Ruang Lingkup

## Yang Termasuk

- Data Understanding
- Exploratory Data Analysis
- Data Cleaning & Preprocessing
- Feature Engineering
- Time Series Analysis
- Model Training (Baseline, Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost)
- Hyperparameter Tuning
- Model Evaluation & Error Analysis
- Dashboard & Inference

## Yang Tidak Termasuk

- Deploy model ke production
- Real-time prediction system
- Integrasi dengan sistem energi nyata
- Optimasi jaringan distribusi listrik

---

# 4. Dataset

## Sumber Dataset

- **Nama**: Power Consumption Dataset
- **Sumber**: UCI Machine Learning Repository
- **Format**: CSV
- **Ukuran**: 52.417 baris, 9 kolom
- **Interval**: 10 menit
- **Periode**: 1 Januari 2017 - 30 Desember 2017

## Deskripsi Dataset

Dataset berisi data konsumsi daya listrik dari 3 zona di suatu daerah, diukur setiap 10 menit selama tahun 2017. Dataset juga mencakup variabel cuaca seperti suhu, kelembaban, kecepatan angin, dan diffuse flows.

---

# 5. Target Prediksi

| Target | Deskripsi | Tipe Data |
|--------|-----------|-----------|
| PowerConsumption_Zone1 | Konsumsi daya zona 1 | Numerik (kWh) |
| PowerConsumption_Zone2 | Konsumsi daya zona 2 | Numerik (kWh) |
| PowerConsumption_Zone3 | Konsumsi daya zona 3 | Numerik (kWh) |

Catatan: Setiap zona akan dimodelkan secara terpisah atau dengan multi-output.

---

# 6. Fitur (Features)

| Nama Fitur | Deskripsi | Tipe Data |
|------------|-----------|-----------|
| Datetime | Timestamp pengukuran (per 10 menit) | Datetime |
| Temperature | Suhu udara | Numerik |
| Humidity | Kelembaban udara | Numerik |
| WindSpeed | Kecepatan angin | Numerik |
| GeneralDiffuseFlows | Diffuse flow umum | Numerik |
| DiffuseFlows | Diffuse flow spesifik | Numerik |

---

# 7. Metodologi

## Tahapan Eksperimen

```
Data Understanding
↓
Exploratory Data Analysis
↓
Data Cleaning
↓
Feature Engineering
↓
Time Series Analysis
↓
Baseline Forecasting
↓
Model Training
↓
Hyperparameter Tuning
↓
Model Evaluation
↓
Dashboard & Inference
```

---

# 8. Metrik Evaluasi

| Metrik | Digunakan | Keterangan |
|---------|-----------|------------|
| MAE | ✅ | Mean Absolute Error |
| RMSE | ✅ | Root Mean Squared Error |
| MAPE | ✅ | Mean Absolute Percentage Error |
| R² Score | ✅ | Coefficient of Determination |
| Training Time | ✅ | Waktu pelatihan model |

---

# 9. Definisi Keberhasilan Proyek

Sebuah proyek dinyatakan selesai apabila seluruh kondisi berikut telah terpenuhi.

## Dokumen

- Seluruh dokumen telah selesai ditulis
- Seluruh notebook memiliki penjelasan yang jelas
- Seluruh eksperimen terdokumentasi

## Data

- Dataset dipahami dengan baik
- Tidak terdapat masalah kualitas data yang belum ditangani

## Model

- Minimal 5 model machine learning berhasil dibandingkan
- Model terbaik dipilih berdasarkan metrik evaluasi
- Hyperparameter model terbaik telah dioptimasi

## Visualisasi

- Visualisasi mampu menjelaskan distribusi data, pola historis, hasil prediksi, dan performa model

## Dashboard

- Dashboard mampu digunakan untuk menampilkan hasil forecasting secara interaktif

---

# 10. Dashboard

Dashboard sederhana yang mampu:

- Menampilkan hasil prediksi
- Menampilkan grafik historis konsumsi daya
- Menampilkan performa model
- Menampilkan insight utama

---

# 11. Timeline

| Fase | Aktivitas | Estimasi Waktu |
|------|-----------|----------------|
| Fase 1 | Data Understanding & EDA | 1 hari |
| Fase 2 | Preprocessing & Feature Engineering | 1 hari |
| Fase 3 | Baseline & Model Training | 1 hari |
| Fase 4 | Hyperparameter Tuning & Evaluation | 1 hari |
| Fase 5 | Dashboard & Final Documentation | 1 hari |

---

# 12. Risiko

| Risiko | Kemungkinan | Dampak | Mitigasi |
|--------|-------------|--------|----------|
| Data quality issues | Sedang | Tinggi | Validasi menyeluruh di EXP-001 & EXP-003 |
| Overfitting | Sedang | Sedang | Regularisasi, cross-validation |
| Long training time | Rendah | Sedang | Feature selection, model sederhana |
| Concept drift | Rendah | Tinggi | Monitoring model periodik |
