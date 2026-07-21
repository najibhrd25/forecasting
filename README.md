# Forecasting Engineering Laboratory

Selamat datang di repositori utama **Forecasting Engineering Laboratory**! Repositori ini digunakan untuk mengelola, melacak, dan mendokumentasikan berbagai proyek analisis data time series dan peramalan (forecasting) secara terstruktur.

Repositori ini dirancang untuk menampung beberapa proyek pembelajaran dari awal hingga akhir (end-to-end).

---

## Struktur Repositori

Setiap proyek ditempatkan pada direktori terpisah dengan dokumentasi dan dataset masing-masing:

```
Forecasting Engineering/
│
├── .gitignore
├── README.md                          # Dokumentasi utama repositori
│
└── project01-bike-sharing/            # Proyek 1: Peramalan Permintaan Sepeda
    ├── data/                          # Dataset (raw, processed, featured) & Visualisasi
    ├── docs/                          # Dokumen PRD, Data Dictionary, Rencana Eksperimen
    └── notebooks/                     # Notebook eksperimen (EXP-001, EXP-002, dst.)
```

---

## Daftar Proyek

| No | Project ID | Nama Proyek | Status | Keterangan |
|---|---|---|---|---|
| 1 | **FL-001** | [Bike Sharing Demand Forecasting](./project01-bike-sharing/) | 🟨 In Progress | Memprediksi jumlah penyewaan sepeda berdasarkan faktor cuaca dan waktu |
| 2 | — | Project 2 | ⬜ Not Started | *TBA* |
| 3 | — | Project 3 | ⬜ Not Started | *TBA* |
| 4 | — | Project 4 | ⬜ Not Started | *TBA* |
| 5 | — | Project 5 | ⬜ Not Started | *TBA* |

---

## Standar & Metodologi Eksperimen

Setiap proyek dalam repositori ini mengikuti alur eksperimen terstruktur:
1. **EXP-001**: Data Understanding
2. **EXP-002**: Exploratory Data Analysis (EDA)
3. **EXP-003**: Data Cleaning (Preprocessing)
4. **EXP-004**: Feature Engineering
5. **EXP-005**: Time Series Diagnostics
6. **EXP-006 s.d. EXP-011**: Pemodelan & Algoritma
7. **EXP-012 s.d. EXP-013**: Tuning & Evaluasi
8. **EXP-014**: Dashboard Visualisasi

*Dibuat oleh Najib Bahrudin — 2026.*
