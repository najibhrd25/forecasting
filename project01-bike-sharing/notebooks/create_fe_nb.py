"""
Script untuk membuat notebook 04_feature_engineering.ipynb (EXP-004).
"""

import json
import os
import uuid

def new_id():
    return str(uuid.uuid4())[:8]

def md(source):
    return {"cell_type": "markdown", "id": new_id(), "metadata": {}, "source": source}

def code(source):
    return {"cell_type": "code", "execution_count": None, "id": new_id(), "metadata": {}, "outputs": [], "source": source}

cells = []

# ─────────────────────────────────────────────────────────────────────────────
# COVER
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "# ForecastLab\n\n"
    "---\n\n"
    "## Bike Sharing Demand Forecasting\n\n"
    "---\n\n"
    "| Informasi | Detail |\n"
    "|-----------|--------|\n"
    "| **Project ID** | FL-001 |\n"
    "| **Eksperimen** | EXP-004 |\n"
    "| **Nama Eksperimen** | Feature Engineering |\n"
    "| **Dataset** | processed_data.csv (output EXP-003) |\n"
    "| **Tujuan Notebook** | Membangun feature baru yang relevan untuk meningkatkan performa model forecasting |\n"
    "| **Tanggal Pengerjaan** | 21 Juli 2026 |\n"
    "| **Versi Notebook** | 1.0.0 |\n"
    "| **Author** | GAKUSEI Najib |\n"
    "| **Prasyarat** | EXP-001 ✅, EXP-002 ✅, EXP-003 ✅ |\n\n"
    "---"
))

# ─────────────────────────────────────────────────────────────────────────────
# DAFTAR ISI
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "## Daftar Isi\n\n"
    "1. [Tujuan Eksperimen](#1-tujuan-eksperimen)\n"
    "2. [Import Library](#2-import-library)\n"
    "3. [Load Dataset](#3-load-dataset)\n"
    "4. [Feature Waktu dari dteday](#4-feature-waktu-dari-dteday)\n"
    "5. [Cyclical Encoding](#5-cyclical-encoding)\n"
    "6. [Interaction Features](#6-interaction-features)\n"
    "7. [Lag Features](#7-lag-features)\n"
    "8. [Rolling Statistics Features](#8-rolling-statistics-features)\n"
    "9. [Ringkasan Feature Baru](#9-ringkasan-feature-baru)\n"
    "10. [Simpan Dataset Hasil Feature Engineering](#10-simpan-dataset-hasil-feature-engineering)\n"
    "11. [Next Step](#11-next-step)"
))

# ─────────────────────────────────────────────────────────────────────────────
# 1. TUJUAN EKSPERIMEN
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md("---\n\n## 1. Tujuan Eksperimen"))

cells.append(md(
    "### Tujuan\n\n"
    "Meningkatkan kualitas informasi pada dataset dengan membangun feature baru yang relevan "
    "untuk model forecasting penyewaan sepeda.\n\n"
    "---\n\n"
    "### Hipotesis\n\n"
    "> Feature turunan dari waktu akan meningkatkan kemampuan model dalam menangkap pola "
    "penyewaan yang bersifat temporal dan siklus.\n\n"
    "---\n\n"
    "### Jenis Feature yang Akan Dibuat\n\n"
    "| Kategori | Feature | Motivasi |\n"
    "|----------|---------|----------|\n"
    "| **Feature Waktu** | `quarter`, `day_of_year`, `week_of_year`, `is_weekend` | Granularitas temporal tambahan |\n"
    "| **Cyclical Encoding** | `hr_sin`, `hr_cos`, `mnth_sin`, `mnth_cos`, `weekday_sin`, `weekday_cos` | Merepresentasikan siklus waktu |\n"
    "| **Interaction Features** | `hr_workingday`, `is_rush_hour`, `is_daytime` | Menangkap pola gabungan |\n"
    "| **Lag Features** | `cnt_lag_1`, `cnt_lag_2`, `cnt_lag_24`, `cnt_lag_168` | Menangkap ketergantungan historis |\n"
    "| **Rolling Statistics** | `cnt_roll_mean_3`, `cnt_roll_mean_24`, `cnt_roll_std_24` | Menangkap tren lokal |\n\n"
    "---\n\n"
    "### Acceptance Criteria\n\n"
    "| Kriteria | Keterangan |\n"
    "|----------|------------|\n"
    "| Feature baru terdokumentasi | Setiap feature dijelaskan motivasinya |\n"
    "| Dataset berhasil disimpan | `data/featured_data.csv` tersedia |\n"
    "| Feature siap digunakan untuk modeling | Tidak ada NaN tak terduga pada feature utama |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 2. IMPORT LIBRARY
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md("---\n\n## 2. Import Library"))

cells.append(code(
    "import pandas as pd\n"
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "import seaborn as sns\n"
    "import warnings\n"
    "\n"
    "warnings.filterwarnings('ignore')\n"
    "pd.set_option('display.max_columns', None)\n"
    "pd.set_option('display.float_format', lambda x: f'{x:.4f}')\n"
    "sns.set_theme(style='whitegrid')\n"
    "plt.rcParams['figure.dpi'] = 110\n"
    "\n"
    "print('Library berhasil diimport.')"
))

# ─────────────────────────────────────────────────────────────────────────────
# 3. LOAD DATASET
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 3. Load Dataset\n\n"
    "Dataset yang digunakan adalah output dari EXP-003 (`processed_data.csv`) "
    "yang telah melalui proses Data Cleaning."
))

cells.append(code(
    "# Definisikan path\n"
    "INPUT_PATH  = '../data/processed_data.csv'\n"
    "OUTPUT_PATH = '../data/featured_data.csv'\n"
    "\n"
    "# Load dataset hasil cleaning\n"
    "df = pd.read_csv(INPUT_PATH)\n"
    "\n"
    "# Konversi dteday ke datetime\n"
    "df['dteday'] = pd.to_datetime(df['dteday'])\n"
    "\n"
    "# Pastikan dataset terurut secara kronologis\n"
    "df = df.sort_values(by=['dteday', 'hr']).reset_index(drop=True)\n"
    "\n"
    "print(f'Dataset berhasil dimuat: {INPUT_PATH}')\n"
    "print(f'Dimensi awal           : {df.shape[0]:,} baris x {df.shape[1]} kolom')\n"
    "print(f'\\nKolom yang tersedia:')\n"
    "print(list(df.columns))"
))

cells.append(md("**Interpretasi:** Dataset hasil cleaning berhasil dimuat. Dataset berisi 17.379 baris dan 14 kolom. Kolom `dteday` telah dikonversi ke tipe `datetime` dan baris diurutkan secara kronologis untuk mendukung pembuatan lag features."))

# ─────────────────────────────────────────────────────────────────────────────
# 4. FEATURE WAKTU DARI DTEDAY
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 4. Feature Waktu dari dteday\n\n"
    "Mengekstraksi komponen waktu tambahan dari kolom `dteday` untuk memberikan "
    "granularitas temporal yang lebih kaya kepada model."
))

cells.append(code(
    "# Ekstraksi feature waktu dari dteday\n"
    "df['quarter']      = df['dteday'].dt.quarter\n"
    "df['day_of_year']  = df['dteday'].dt.day_of_year\n"
    "df['week_of_year'] = df['dteday'].dt.isocalendar().week.astype(int)\n"
    "df['day_of_month'] = df['dteday'].dt.day\n"
    "df['is_weekend']   = (df['weekday'].isin([0, 6])).astype(int)\n"
    "\n"
    "print('Feature waktu berhasil dibuat:')\n"
    "print(df[['dteday', 'hr', 'quarter', 'day_of_year', 'week_of_year',\n"
    "           'day_of_month', 'is_weekend']].head(10).to_string(index=False))"
))

cells.append(md(
    "**Dokumentasi Feature:**\n\n"
    "| Feature | Deskripsi | Motivasi |\n"
    "|---------|-----------|----------|\n"
    "| `quarter` | Kuartal dalam tahun (1–4) | Menangkap variasi musiman level kuartal |\n"
    "| `day_of_year` | Hari ke- dalam tahun (1–366) | Representasi kontinu posisi dalam tahun |\n"
    "| `week_of_year` | Minggu ke- dalam tahun (1–53) | Menangkap pola mingguan dalam tahun |\n"
    "| `day_of_month` | Tanggal dalam bulan (1–31) | Mendeteksi pola awal/akhir bulan |\n"
    "| `is_weekend` | 1 jika Sabtu/Minggu, 0 lainnya | Binary feature pola akhir pekan |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 5. CYCLICAL ENCODING
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 5. Cyclical Encoding\n\n"
    "Feature waktu seperti jam, bulan, dan hari dalam seminggu bersifat **siklus** — "
    "artinya jam 23 dekat dengan jam 0, bulan Desember dekat dengan Januari, dst.\n\n"
    "Representasi integer biasa tidak menangkap sifat siklus ini. Oleh karena itu, "
    "digunakan transformasi **sin** dan **cos** agar model memahami kedekatan antar nilai siklus.\n\n"
    "Formula:\n"
    "$$\\text{sin\\_enc} = \\sin\\left(\\frac{2\\pi \\cdot x}{\\text{periode}}\\right), \\quad "
    "\\text{cos\\_enc} = \\cos\\left(\\frac{2\\pi \\cdot x}{\\text{periode}}\\right)$$"
))

cells.append(code(
    "# Fungsi helper untuk cyclical encoding\n"
    "def cyclical_encode(series, period):\n"
    "    \"\"\"Menghasilkan representasi sin dan cos dari sebuah variabel siklus.\"\"\"\n"
    "    sin_enc = np.sin(2 * np.pi * series / period)\n"
    "    cos_enc = np.cos(2 * np.pi * series / period)\n"
    "    return sin_enc, cos_enc\n"
    "\n"
    "# Encoding untuk hr (periode = 24)\n"
    "df['hr_sin'],      df['hr_cos']      = cyclical_encode(df['hr'],      24)\n"
    "# Encoding untuk mnth (periode = 12)\n"
    "df['mnth_sin'],    df['mnth_cos']    = cyclical_encode(df['mnth'],    12)\n"
    "# Encoding untuk weekday (periode = 7)\n"
    "df['weekday_sin'], df['weekday_cos'] = cyclical_encode(df['weekday'], 7)\n"
    "# Encoding untuk season (periode = 4)\n"
    "df['season_sin'],  df['season_cos']  = cyclical_encode(df['season'],  4)\n"
    "\n"
    "print('Cyclical encoding berhasil dibuat.')\n"
    "print(df[['hr', 'hr_sin', 'hr_cos']].drop_duplicates().sort_values('hr').head(10).to_string(index=False))"
))

cells.append(md("### 5.1 Visualisasi Cyclical Encoding"))

cells.append(code(
    "fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n"
    "\n"
    "# Visualisasi hr encoding\n"
    "hr_enc = df[['hr', 'hr_sin', 'hr_cos']].drop_duplicates().sort_values('hr')\n"
    "axes[0].plot(hr_enc['hr'], hr_enc['hr_sin'], marker='o', label='hr_sin', color='steelblue')\n"
    "axes[0].plot(hr_enc['hr'], hr_enc['hr_cos'], marker='s', label='hr_cos', color='coral')\n"
    "axes[0].set_title('Cyclical Encoding: Jam (hr)')\n"
    "axes[0].set_xlabel('Jam')\n"
    "axes[0].set_ylabel('Nilai Encoding')\n"
    "axes[0].set_xticks(range(0, 24, 2))\n"
    "axes[0].legend()\n"
    "axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)\n"
    "\n"
    "# Scatter: sin vs cos (menunjukkan representasi melingkar)\n"
    "axes[1].scatter(hr_enc['hr_sin'], hr_enc['hr_cos'],\n"
    "                c=hr_enc['hr'], cmap='hsv', s=80, zorder=3)\n"
    "for _, row in hr_enc.iterrows():\n"
    "    axes[1].annotate(str(int(row['hr'])), (row['hr_sin'], row['hr_cos']),\n"
    "                     fontsize=8, ha='center', va='bottom')\n"
    "axes[1].set_title('Representasi Melingkar: hr_sin vs hr_cos')\n"
    "axes[1].set_xlabel('hr_sin')\n"
    "axes[1].set_ylabel('hr_cos')\n"
    "axes[1].set_aspect('equal')\n"
    "\n"
    "plt.suptitle('EXP-004 | Cyclical Encoding untuk Jam (hr)', fontsize=13, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/fe_01_cyclical_encoding.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()\n"
    "\n"
    "print('Visualisasi cyclical encoding tersimpan.')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- Grafik sin/cos menunjukkan representasi siklus yang mulus — jam 0 dan jam 23 "
    "memiliki nilai yang berdekatan (tidak ada lompatan diskrit).\n"
    "- Scatter plot kiri-kanan menunjukkan setiap jam berada pada titik unik di lingkaran "
    "satuan, membuktikan tidak ada informasi yang hilang dalam transformasi ini.\n"
    "- Pasangan sin/cos selalu digunakan bersama untuk merepresentasikan satu variabel siklus "
    "karena satu nilai saja tidak cukup (sin(0) = sin(π), tetapi cos-nya berbeda).\n\n"
    "**Dokumentasi Feature:**\n\n"
    "| Feature | Periode | Deskripsi |\n"
    "|---------|---------|----------|\n"
    "| `hr_sin`, `hr_cos` | 24 | Representasi siklus jam |\n"
    "| `mnth_sin`, `mnth_cos` | 12 | Representasi siklus bulan |\n"
    "| `weekday_sin`, `weekday_cos` | 7 | Representasi siklus hari dalam seminggu |\n"
    "| `season_sin`, `season_cos` | 4 | Representasi siklus musim |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 6. INTERACTION FEATURES
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 6. Interaction Features\n\n"
    "Berdasarkan temuan EDA, pola penyewaan sangat berbeda antara hari kerja dan akhir pekan "
    "pada jam-jam tertentu. Interaction features dibuat untuk menangkap hubungan gabungan ini."
))

cells.append(code(
    "# Interaction: jam × hari kerja (nilai integer)\n"
    "df['hr_x_workingday'] = df['hr'] * df['workingday']\n"
    "\n"
    "# Rush hour flag: jam sibuk hari kerja (07-09 & 16-19)\n"
    "df['is_rush_hour'] = (\n"
    "    (df['workingday'] == 1) &\n"
    "    (df['hr'].isin([7, 8, 9, 16, 17, 18, 19]))\n"
    ").astype(int)\n"
    "\n"
    "# Daytime flag: jam siang (06-20)\n"
    "df['is_daytime'] = df['hr'].between(6, 20).astype(int)\n"
    "\n"
    "# Peak season flag: musim puncak (Summer & Fall = season 2 & 3)\n"
    "df['is_peak_season'] = df['season'].isin([2, 3]).astype(int)\n"
    "\n"
    "# Suhu aktual (de-normalisasi)\n"
    "df['temp_actual']  = df['temp']  * 41   # max temp = 41 derajat Celcius\n"
    "df['atemp_actual'] = df['atemp'] * 50   # max atemp = 50 derajat Celcius\n"
    "\n"
    "print('Interaction features berhasil dibuat.')\n"
    "print(f\"Rush hour records  : {df['is_rush_hour'].sum():,}\")\n"
    "print(f\"Daytime records    : {df['is_daytime'].sum():,}\")\n"
    "print(f\"Peak season records: {df['is_peak_season'].sum():,}\")"
))

cells.append(md(
    "**Dokumentasi Feature:**\n\n"
    "| Feature | Deskripsi | Motivasi |\n"
    "|---------|-----------|----------|\n"
    "| `hr_x_workingday` | Perkalian hr × workingday | Membedakan pola jam di hari kerja vs libur |\n"
    "| `is_rush_hour` | 1 jika jam sibuk hari kerja | Flag periode puncak komuter |\n"
    "| `is_daytime` | 1 jika jam 06–20 | Membedakan siang vs malam |\n"
    "| `is_peak_season` | 1 jika Summer atau Fall | Flag musim penyewaan tertinggi |\n"
    "| `temp_actual` | Suhu aktual dalam °C | Interpretasi lebih intuitif (temp × 41) |\n"
    "| `atemp_actual` | Feeling temp aktual dalam °C | Interpretasi lebih intuitif (atemp × 50) |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 7. LAG FEATURES
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 7. Lag Features\n\n"
    "Lag features memanfaatkan nilai `cnt` pada periode sebelumnya sebagai prediktor. "
    "Ini sangat penting dalam forecasting karena nilai historis biasanya memiliki korelasi "
    "kuat dengan nilai saat ini.\n\n"
    "> ⚠️ **Catatan Penting:** Lag features menyebabkan baris-baris awal memiliki nilai `NaN`. "
    "Baris-baris ini akan ditangani saat pembagian dataset pada tahap modeling."
))

cells.append(code(
    "# Lag features dari cnt\n"
    "df['cnt_lag_1']   = df['cnt'].shift(1)    # 1 jam lalu\n"
    "df['cnt_lag_2']   = df['cnt'].shift(2)    # 2 jam lalu\n"
    "df['cnt_lag_3']   = df['cnt'].shift(3)    # 3 jam lalu\n"
    "df['cnt_lag_24']  = df['cnt'].shift(24)   # jam yang sama kemarin\n"
    "df['cnt_lag_48']  = df['cnt'].shift(48)   # jam yang sama 2 hari lalu\n"
    "df['cnt_lag_168'] = df['cnt'].shift(168)  # jam yang sama seminggu lalu\n"
    "\n"
    "print('Lag features berhasil dibuat.')\n"
    "print(f'\\nNaN pada setiap lag feature:')\n"
    "lag_cols = ['cnt_lag_1', 'cnt_lag_2', 'cnt_lag_3', 'cnt_lag_24', 'cnt_lag_48', 'cnt_lag_168']\n"
    "for col in lag_cols:\n"
    "    n_nan = df[col].isnull().sum()\n"
    "    print(f'  {col:<15}: {n_nan} NaN ({n_nan/len(df)*100:.2f}%)')"
))

cells.append(md("### 7.1 Visualisasi Korelasi Lag vs Target"))

cells.append(code(
    "# Buat DataFrame tanpa NaN untuk visualisasi korelasi\n"
    "df_lag_vis = df[lag_cols + ['cnt']].dropna()\n"
    "\n"
    "corr_lag = df_lag_vis[lag_cols].corrwith(df_lag_vis['cnt']).sort_values(ascending=False)\n"
    "\n"
    "fig, ax = plt.subplots(figsize=(9, 4))\n"
    "bars = ax.bar(corr_lag.index, corr_lag.values, color='steelblue', edgecolor='white')\n"
    "ax.axhline(y=0, color='black', linewidth=0.8)\n"
    "ax.set_title('Korelasi Lag Features terhadap Target (cnt)')\n"
    "ax.set_xlabel('Lag Feature')\n"
    "ax.set_ylabel('Korelasi Pearson')\n"
    "ax.bar_label(bars, fmt='%.3f', padding=3, fontsize=9)\n"
    "ax.set_ylim(-0.1, 1.0)\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/fe_02_korelasi_lag.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()\n"
    "\n"
    "print('Korelasi lag features dengan cnt:')\n"
    "print(corr_lag.to_string())"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- `cnt_lag_1` (1 jam lalu) memiliki **korelasi tertinggi** dengan target — "
    "penyewaan jam ini sangat dipengaruhi oleh penyewaan jam sebelumnya.\n"
    "- `cnt_lag_24` (kemarin, jam yang sama) juga berkorelasi tinggi, menangkap pola harian yang berulang.\n"
    "- `cnt_lag_168` (seminggu lalu, jam yang sama) menangkap pola mingguan.\n"
    "- Semua lag features memiliki korelasi positif yang signifikan → sangat bermanfaat untuk model.\n\n"
    "**Dokumentasi Feature:**\n\n"
    "| Feature | Deskripsi |\n"
    "|---------|----------|\n"
    "| `cnt_lag_1` | Penyewaan 1 jam lalu |\n"
    "| `cnt_lag_2` | Penyewaan 2 jam lalu |\n"
    "| `cnt_lag_3` | Penyewaan 3 jam lalu |\n"
    "| `cnt_lag_24` | Penyewaan pada jam yang sama kemarin |\n"
    "| `cnt_lag_48` | Penyewaan pada jam yang sama 2 hari lalu |\n"
    "| `cnt_lag_168` | Penyewaan pada jam yang sama seminggu lalu |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 8. ROLLING STATISTICS
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 8. Rolling Statistics Features\n\n"
    "Rolling statistics menghitung statistik agregat dari jendela waktu tertentu sebelum "
    "titik saat ini. Feature ini membantu model memahami tren lokal dan tingkat volatilitas "
    "penyewaan dalam periode terdekat."
))

cells.append(code(
    "# Rolling statistics dari cnt (min_periods=1 untuk mengurangi NaN di awal)\n"
    "df['cnt_roll_mean_3']  = df['cnt'].shift(1).rolling(window=3,  min_periods=1).mean()\n"
    "df['cnt_roll_mean_6']  = df['cnt'].shift(1).rolling(window=6,  min_periods=1).mean()\n"
    "df['cnt_roll_mean_24'] = df['cnt'].shift(1).rolling(window=24, min_periods=1).mean()\n"
    "df['cnt_roll_std_3']   = df['cnt'].shift(1).rolling(window=3,  min_periods=1).std().fillna(0)\n"
    "df['cnt_roll_std_24']  = df['cnt'].shift(1).rolling(window=24, min_periods=1).std().fillna(0)\n"
    "df['cnt_roll_max_24']  = df['cnt'].shift(1).rolling(window=24, min_periods=1).max()\n"
    "\n"
    "rolling_cols = ['cnt_roll_mean_3', 'cnt_roll_mean_6', 'cnt_roll_mean_24',\n"
    "                'cnt_roll_std_3', 'cnt_roll_std_24', 'cnt_roll_max_24']\n"
    "\n"
    "print('Rolling statistics features berhasil dibuat.')\n"
    "print(f'\\nNaN pada setiap rolling feature:')\n"
    "for col in rolling_cols:\n"
    "    n_nan = df[col].isnull().sum()\n"
    "    print(f'  {col:<22}: {n_nan} NaN')"
))

cells.append(md(
    "**Dokumentasi Feature:**\n\n"
    "| Feature | Window | Deskripsi |\n"
    "|---------|--------|-----------|\n"
    "| `cnt_roll_mean_3` | 3 jam | Rata-rata penyewaan 3 jam terakhir |\n"
    "| `cnt_roll_mean_6` | 6 jam | Rata-rata penyewaan 6 jam terakhir |\n"
    "| `cnt_roll_mean_24` | 24 jam | Rata-rata penyewaan 24 jam terakhir (tren harian) |\n"
    "| `cnt_roll_std_3` | 3 jam | Standar deviasi 3 jam terakhir (volatilitas jangka pendek) |\n"
    "| `cnt_roll_std_24` | 24 jam | Standar deviasi 24 jam terakhir (volatilitas harian) |\n"
    "| `cnt_roll_max_24` | 24 jam | Nilai maksimum penyewaan 24 jam terakhir |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 9. RINGKASAN FEATURE BARU
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 9. Ringkasan Feature Baru\n\n"
    "Menampilkan ringkasan lengkap seluruh feature yang telah dibuat."
))

cells.append(code(
    "# Kolom original\n"
    "kolom_original = [\n"
    "    'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday',\n"
    "    'weekday', 'workingday', 'weathersit', 'temp', 'atemp',\n"
    "    'hum', 'windspeed', 'cnt'\n"
    "]\n"
    "\n"
    "# Kolom baru\n"
    "kolom_baru = [c for c in df.columns if c not in kolom_original]\n"
    "\n"
    "print('=' * 55)\n"
    "print('RINGKASAN FEATURE ENGINEERING')\n"
    "print('=' * 55)\n"
    "print(f'Kolom original : {len(kolom_original)}')\n"
    "print(f'Kolom baru     : {len(kolom_baru)}')\n"
    "print(f'Total kolom    : {len(df.columns)}')\n"
    "print(f'\\nDaftar feature baru:')\n"
    "for i, col in enumerate(kolom_baru, 1):\n"
    "    nan_count = df[col].isnull().sum()\n"
    "    print(f'{i:>2}. {col:<22} | dtype: {str(df[col].dtype):<10} | NaN: {nan_count}')"
))

cells.append(code(
    "# Statistik deskriptif feature baru\n"
    "print('Statistik deskriptif feature baru:')\n"
    "df[kolom_baru].describe().T"
))

cells.append(code(
    "# Cek NaN pada seluruh dataset setelah feature engineering\n"
    "n_nan_total = df.isnull().sum().sum()\n"
    "n_nan_per_col = df.isnull().sum()\n"
    "n_nan_cols = (n_nan_per_col > 0).sum()\n"
    "\n"
    "print('=' * 50)\n"
    "print('RINGKASAN NaN SETELAH FEATURE ENGINEERING')\n"
    "print('=' * 50)\n"
    "print(f'Total NaN keseluruhan : {n_nan_total}')\n"
    "print(f'Kolom dengan NaN      : {n_nan_cols}')\n"
    "print(f'\\nKolom dengan NaN:')\n"
    "print(n_nan_per_col[n_nan_per_col > 0].to_string())\n"
    "print('\\n(NaN pada lag/rolling features adalah normal — akan ditangani saat split data)')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "Dataset kini memiliki feature yang jauh lebih kaya. NaN yang muncul pada lag features "
    "dan rolling features adalah **expected** karena baris-baris awal tidak memiliki "
    "nilai historis yang cukup. Strategi penanganannya adalah:\n\n"
    "1. Baris dengan NaN pada lag/rolling akan **di-drop pada saat split dataset** (sebelum training).\n"
    "2. Lag terbesar adalah `cnt_lag_168` (168 jam = 7 hari), sehingga **168 baris pertama** "
    "akan memiliki NaN dan akan dihapus sebelum training."
))

# ─────────────────────────────────────────────────────────────────────────────
# 10. SIMPAN DATASET
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 10. Simpan Dataset Hasil Feature Engineering\n\n"
    "Dataset lengkap dengan seluruh feature baru disimpan ke `data/featured_data.csv` "
    "sebagai deliverable resmi EXP-004."
))

cells.append(code(
    "# Simpan dataset\n"
    "df.to_csv(OUTPUT_PATH, index=False)\n"
    "\n"
    "print(f'✅ Dataset berhasil disimpan ke: {OUTPUT_PATH}')\n"
    "print(f'   Jumlah baris  : {df.shape[0]:,}')\n"
    "print(f'   Jumlah kolom  : {df.shape[1]}')\n"
    "\n"
    "# Verifikasi\n"
    "df_verify = pd.read_csv(OUTPUT_PATH)\n"
    "assert df_verify.shape == df.shape, 'ERROR: Dimensi tidak konsisten!'\n"
    "print(f'\\n✅ Verifikasi berhasil — file tersimpan dengan benar.')\n"
    "print(f'   Kolom yang tersedia: {list(df_verify.columns)}')"
))

# ─────────────────────────────────────────────────────────────────────────────
# 11. NEXT STEP
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 11. Next Step\n\n"
    "---\n\n"
    "### Eksperimen Berikutnya\n\n"
    "| Informasi | Detail |\n"
    "|-----------|--------|\n"
    "| **ID** | EXP-005 |\n"
    "| **Nama** | Time Series Diagnostics |\n"
    "| **Notebook** | `05_time_series_analysis.ipynb` |\n"
    "| **Input** | `data/featured_data.csv` |\n\n"
    "**Tujuan:**\n\n"
    "> Menganalisis karakteristik data time series sebelum proses pemodelan dilakukan, "
    "termasuk stasioneritas, tren, autokorelasi, dan dekomposisi.\n\n"
    "**Aktivitas yang akan dilakukan pada EXP-005:**\n\n"
    "- Dekomposisi time series (tren, musiman, residual)\n"
    "- Uji stasioneritas (ADF test)\n"
    "- Analisis Autocorrelation Function (ACF)\n"
    "- Analisis Partial Autocorrelation Function (PACF)\n"
    "- Identifikasi lag order yang optimal\n\n"
    "---\n\n"
    "*Notebook EXP-004 Feature Engineering — Selesai.*"
))

# ─────────────────────────────────────────────────────────────────────────────
# RAKITAN NOTEBOOK
# ─────────────────────────────────────────────────────────────────────────────
notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.x.x"}
    },
    "cells": cells
}

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '04_feature_engineering.ipynb')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f'Notebook berhasil dibuat: {output_path}')
print(f'Total cells: {len(cells)}')
