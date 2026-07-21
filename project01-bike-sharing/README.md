# Project 01 — Bike Sharing Demand Forecasting

---

## Deskripsi Proyek

Proyek **Bike Sharing Demand Forecasting (Project ID: FL-001)** berfokus pada pembangunan model prediksi jumlah penyewaan sepeda berdasarkan data historis dari sistem Capital Bikeshare (Washington D.C., USA) serta variabel-variabel pendukung seperti waktu, cuaca, musim, dan hari kerja.

Tujuan utama dari proyek ini adalah membangun model forecasting terbaik secara end-to-end dengan mengikuti standar dokumentasi dan rencana eksperimen industri yang ketat.

---

## Informasi Proyek

- **Project ID**: FL-001
- **Domain**: Data Science / Forecasting / Time Series Analysis
- **Dataset**: Bike Sharing Dataset (UCI Machine Learning Repository)
- **Target Prediksi**: `cnt` (Total penyewaan sepeda per jam)
- **Status**: 🟨 In Development (Eksperimen Aktif: EXP-005)

---

## Struktur Folder

```
project01-bike-sharing/
│
├── README.md                      # Dokumentasi Proyek 01
├── data/                          # Dataset dan Visualisasi hasil EDA
│   ├── day.csv                    # Data harian (raw)
│   ├── hour.csv                   # Data per jam (raw)
│   ├── processed_data.csv         # Data hasil cleaning (EXP-003)
│   └── featured_data.csv          # Data hasil feature engineering (EXP-004)
│
├── docs/                          # Dokumen Referensi (Single Source of Truth)
│   ├── prd.md                     # Product Requirements Document
│   ├── data-dictionary.md         # Penjelasan Detail Kolom
│   ├── experiment-plan.md         # Rencana Eksperimen
│   └── model-report.md            # Laporan Hasil Evaluasi Model
│
└── notebooks/                     # Notebook Jupyter Eksperimen
    ├── 01_data_understanding.ipynb
    ├── 02_eda.ipynb
    ├── 03_preprocessing.ipynb
    ├── 04_feature_engineering.ipynb
    └── 05_time_series_analysis.ipynb
```

---

## Log Eksperimen & Status

Eksperimen berjalan secara berurutan dan terdokumentasi lengkap pada [Experiment Plan](./docs/experiment-plan.md):

| Eksperimen ID | Nama Eksperimen | Notebook | Status | Deliverables |
|---|---|---|---|---|
| **EXP-001** | Data Understanding | `01_data_understanding.ipynb` | ✅ Completed | Dataset tervalidasi & struktur awal dipahami |
| **EXP-002** | Exploratory Data Analysis | `02_eda.ipynb` | ✅ Completed | Visualisasi pola musiman, jam, dan cuaca |
| **EXP-003** | Data Cleaning | `03_preprocessing.ipynb` | ✅ Completed | `processed_data.csv` siap pakai |
| **EXP-004** | Feature Engineering | `04_feature_engineering.ipynb` | ✅ Completed | `featured_data.csv` (Lag, Cyclic, Interaction) |
| **EXP-005** | Time Series Diagnostics | `05_time_series_analysis.ipynb` | ✅ Completed | Karakteristik time series dianalisis (ADF, ACF/PACF, Decomp) |
| **EXP-006** | Baseline Forecasting | `06_baseline_model.ipynb` | ⬜ Not Started | *Berikutnya* |

---

## Petunjuk Penggunaan

### Prasyarat
Instalasi package Python yang dibutuhkan:
```bash
pip install pandas numpy matplotlib seaborn jinja2 nbconvert
```

### Menjalankan Notebook
1. Masuk ke folder notebook:
   ```bash
   cd project01-bike-sharing/notebooks
   ```
2. Jalankan jupyter notebook atau buka via VS Code / editor pilihan Anda.
