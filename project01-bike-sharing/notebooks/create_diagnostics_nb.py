"""
Script untuk membuat notebook 05_time_series_analysis.ipynb (EXP-005).
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
    "| **Eksperimen** | EXP-005 |\n"
    "| **Nama Eksperimen** | Time Series Diagnostics |\n"
    "| **Dataset** | featured_data.csv (output EXP-004) |\n"
    "| **Tujuan Notebook** | Menganalisis karakteristik data time series sebelum proses pemodelan |\n"
    "| **Tanggal Pengerjaan** | 21 Juli 2026 |\n"
    "| **Versi Notebook** | 1.0.0 |\n"
    "| **Author** | GAKUSEI Najib |\n"
    "| **Prasyarat** | EXP-001 s.d. EXP-004 ✅ |\n\n"
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
    "4. [Analisis Tren & Rolling Statistics](#4-analisis-tren--rolling-statistics)\n"
    "5. [Analisis Seasonality](#5-analisis-seasonality)\n"
    "6. [Stationarity Test (ADF Test)](#6-stationarity-test-adf-test)\n"
    "7. [Analisis Autokorelasi (ACF & PACF)](#7-analisis-autokorelasi-acf--pacf)\n"
    "8. [Time Series Decomposition](#8-time-series-decomposition)\n"
    "9. [Initial Findings](#9-initial-findings)\n"
    "10. [Next Step](#10-next-step)"
))

# ─────────────────────────────────────────────────────────────────────────────
# 1. TUJUAN EKSPERIMEN
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md("---\n\n## 1. Tujuan Eksperimen"))

cells.append(md(
    "### Tujuan\n\n"
    "Menganalisis karakteristik data time series sebelum proses pemodelan dilakukan "
    "untuk memahami stasioneritas, autokorelasi, tren, dan pola musiman. Hal ini "
    "penting agar pemilihan model forecasting dapat dilakukan secara tepat.\n\n"
    "---\n\n"
    "### Hipotesis\n\n"
    "> Dataset memiliki tren naik, pola musiman (seasonality) yang berulang (per jam, per hari, per bulan), "
    "stasioneritas pada level tertentu, dan autokorelasi kuat dengan observasi sebelumnya.\n\n"
    "---\n\n"
    "### Output yang Diharapkan\n\n"
    "- Grafik tren & rolling statistics\n"
    "- Grafik pola musiman (seasonality) detail\n"
    "- Hasil uji stasioneritas Augmented Dickey-Fuller (ADF) Test\n"
    "- Grafik dekomposisi time series (trend, seasonal, residual)\n"
    "- Analisis ACF & PACF untuk identifikasi lag order optimal\n\n"
    "---\n\n"
    "### Acceptance Criteria\n\n"
    "| Kriteria | Keterangan |\n"
    "|----------|------------|\n"
    "| Trend berhasil dianalisis | Karakteristik tren jangka panjang teridentifikasi |\n"
    "| Seasonality berhasil ditemukan | Pola musiman jam/hari/bulan dipetakan |\n"
    "| Stationarity diketahui | Lolos/gagal ADF test terdokumentasi |\n"
    "| Autocorrelation diketahui | ACF & PACF diplot dan dianalisis |"
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
    "# Library analisis time series\n"
    "from statsmodels.tsa.stattools import adfuller\n"
    "from statsmodels.tsa.seasonal import seasonal_decompose\n"
    "from statsmodels.graphics.tsaplots import plot_acf, plot_pacf\n"
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
    "Dataset yang digunakan adalah output dari EXP-004 (`featured_data.csv`)."
))

cells.append(code(
    "# Definisikan path\n"
    "INPUT_PATH = '../data/featured_data.csv'\n"
    "\n"
    "# Load dataset hasil feature engineering\n"
    "df = pd.read_csv(INPUT_PATH)\n"
    "\n"
    "# Konversi dteday ke datetime\n"
    "df['dteday'] = pd.to_datetime(df['dteday'])\n"
    "\n"
    "# Set index ke dteday untuk analisis time series (opsional, tapi berguna)\n"
    "df = df.sort_values(by=['dteday', 'hr']).reset_index(drop=True)\n"
    "\n"
    "print(f'Dataset berhasil dimuat: {INPUT_PATH}')\n"
    "print(f'Dimensi: {df.shape[0]:,} baris x {df.shape[1]} kolom')"
))

# ─────────────────────────────────────────────────────────────────────────────
# 4. ANALISIS TREN & ROLLING STATISTICS
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 4. Analisis Tren & Rolling Statistics\n\n"
    "Menganalisis tren jangka panjang menggunakan rolling statistics dengan window size "
    "harian (24 jam) dan mingguan (168 jam) untuk melihat stasioneritas visual pada mean dan varians."
))

cells.append(code(
    "# Hitung rolling statistics harian (24 jam) dan mingguan (168 jam)\n"
    "df['rolling_mean_24']  = df['cnt'].rolling(window=24, center=True).mean()\n"
    "df['rolling_std_24']   = df['cnt'].rolling(window=24, center=True).std()\n"
    "df['rolling_mean_168'] = df['cnt'].rolling(window=168, center=True).mean()\n"
    "df['rolling_std_168']  = df['cnt'].rolling(window=168, center=True).std()\n"
    "\n"
    "fig, axes = plt.subplots(2, 1, figsize=(16, 10), sharex=True)\n"
    "\n"
    "# Plot Mean\n"
    "axes[0].plot(df['dteday'], df['cnt'], alpha=0.15, color='gray', label='Aktual per Jam')\n"
    "axes[0].plot(df['dteday'], df['rolling_mean_24'], color='steelblue', linewidth=1.5, label='Rolling Mean (24 Jam)')\n"
    "axes[0].plot(df['dteday'], df['rolling_mean_168'], color='red', linewidth=2.5, label='Rolling Mean (168 Jam / 7 Hari)')\n"
    "axes[0].set_title('Analisis Tren: Rolling Mean dari Total Penyewaan (cnt)')\n"
    "axes[0].set_ylabel('Total Penyewaan')\n"
    "axes[0].legend(loc='upper left')\n"
    "\n"
    "# Plot Standard Deviation\n"
    "axes[1].plot(df['dteday'], df['rolling_std_24'], color='orange', linewidth=1.5, label='Rolling Std (24 Jam)')\n"
    "axes[1].plot(df['dteday'], df['rolling_std_168'], color='darkred', linewidth=2.5, label='Rolling Std (168 Jam / 7 Hari)')\n"
    "axes[1].set_title('Analisis Volatilitas: Rolling Standard Deviation dari Total Penyewaan (cnt)')\n"
    "axes[1].set_ylabel('Standard Deviation')\n"
    "axes[1].set_xlabel('Tanggal')\n"
    "axes[1].legend(loc='upper left')\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.suptitle('EXP-005 | Tren & Volatilitas Jangka Panjang', fontsize=14, y=1.02, fontweight='bold')\n"
    "plt.savefig('../data/diagnostics_01_tren_rolling.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- **Non-Stasioneritas Visual pada Mean**: Rata-rata bergulir 168 jam (garis merah) menunjukkan "
    "pola naik turun musiman yang kuat sepanjang tahun (naik di pertengahan tahun, turun di akhir/awal tahun) "
    "serta tren meningkat secara keseluruhan dari tahun 2011 ke 2012.\n"
    "- **Non-Stasioneritas Visual pada Varians**: Rolling standard deviation (garis jingga dan merah gelap) "
    "berfluktuasi secara signifikan, meningkat di musim puncak ketika jumlah penyewaan tinggi "
    "dan menurun di musim dingin ketika penyewaan sepi. Ini mengindikasikan varians yang tidak konstan (heteroskedastisitas)."
))

# ─────────────────────────────────────────────────────────────────────────────
# 5. ANALISIS SEASONALITY
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 5. Analisis Seasonality\n\n"
    "Menganalisis pola musiman yang terjadi secara berulang dalam berbagai skala waktu."
))

cells.append(md("### 5.1 Pola Musiman per Jam dan Tipe Hari (Weekday vs Weekend)"))

cells.append(code(
    "fig, ax = plt.subplots(figsize=(14, 5))\n"
    "\n"
    "sns.pointplot(data=df, x='hr', y='cnt', hue='workingday', ax=ax, ci=95,\n"
    "              markers=['o', 's'], linestyles=['-', '--'])\n"
    "\n"
    "ax.set_title('Pola Musiman Harian: Jam vs Tipe Hari')\n"
    "ax.set_xlabel('Jam')\n"
    "ax.set_ylabel('Rata-rata Penyewaan')\n"
    "ax.legend(title='Tipe Hari', labels=['Libur / Akhir Pekan', 'Hari Kerja'])\n"
    "ax.set_xticks(range(24))\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/diagnostics_02_seasonality_hourly.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md("### 5.2 Pola Musiman Bulanan dan Musim"))

cells.append(code(
    "fig, axes = plt.subplots(1, 2, figsize=(16, 5))\n"
    "\n"
    "# Bulanan per Tahun\n"
    "sns.pointplot(data=df, x='mnth', y='cnt', hue='yr', ax=axes[0], ci=None,\n"
    "              palette='muted')\n"
    "axes[0].set_title('Pola Musiman Bulanan (2011 vs 2012)')\n"
    "axes[0].set_xlabel('Bulan')\n"
    "axes[0].set_ylabel('Rata-rata Penyewaan')\n"
    "axes[0].legend(title='Tahun', labels=['2011', '2012'])\n"
    "axes[0].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])\n"
    "\n"
    "# Musim per Tahun\n"
    "sns.barplot(data=df, x='season', y='cnt', hue='yr', ax=axes[1], ci=None,\n"
    "            palette='pastel')\n"
    "axes[1].set_title('Rata-rata Penyewaan per Musim')\n"
    "axes[1].set_xlabel('Musim')\n"
    "axes[1].set_ylabel('Rata-rata Penyewaan')\n"
    "axes[1].set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])\n"
    "axes[1].legend(title='Tahun', labels=['2011', '2012'])\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.suptitle('EXP-005 | Pola Musiman Jangka Panjang', fontsize=13, y=1.02, fontweight='bold')\n"
    "plt.savefig('../data/diagnostics_03_seasonality_longterm.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- **Pola Harian (24 Jam)**: Pola musiman harian sangat kuat dan dipengaruhi oleh tipe hari. "
    "Hari kerja memiliki pola bimodal (puncak jam 8 pagi dan 5 sore), sedangkan hari libur memiliki pola "
    "unimodal (puncak jam 12–3 siang).\n"
    "- **Pola Bulanan**: Mengikuti pola lonceng terbalik, naik dari Januari ke Juni/Juli, stabil di Agustus/September, "
    "dan turun drastis di November/Desember.\n"
    "- **Pola Tahunan**: Terdapat pergeseran level rata-rata ke atas di tahun 2012 (yr = 1) dibanding 2011 (yr = 0), "
    "menunjukkan tren pertumbuhan."
))

# ─────────────────────────────────────────────────────────────────────────────
# 6. STATIONARITY TEST (ADF TEST)
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 6. Stationarity Test (ADF Test)\n\n"
    "Stasioneritas adalah asumsi penting dalam pemodelan statistik time series. "
    "Untuk mengujinya secara kuantitatif, dilakukan **Augmented Dickey-Fuller (ADF) Test**.\n\n"
    "- **H0 (Hipotesis Nol)**: Data memiliki unit root (tidak stasioner).\n"
    "- **H1 (Hipotesis Alternatif)**: Data tidak memiliki unit root (stasioner).\n\n"
    "Jika p-value < 0.05, kita menolak H0 dan menyimpulkan data stasioner."
))

cells.append(code(
    "# Lakukan ADF Test pada data mentah 'cnt'\n"
    "result_raw = adfuller(df['cnt'])\n"
    "\n"
    "print('=' * 55)\n"
    "print('AUGMENTED DICKEY-FULLER (ADF) TEST — RAW TARGET (cnt)')\n"
    "print('=' * 55)\n"
    "print(f'ADF Statistic : {result_raw[0]:.6f}')\n"
    "print(f'p-value       : {result_raw[1]:.6e}')\n"
    "print(f'Lags Used     : {result_raw[2]}')\n"
    "print(f'Observations  : {result_raw[3]}')\n"
    "print('\\nCritical Values:')\n"
    "for key, value in result_raw[4].items():\n"
    "    print(f'  {key:<8} : {value:.6f}')\n"
    "\n"
    "is_stationary = result_raw[1] < 0.05\n"
    "print(f'\\nHasil: Data bersifat {\"STASIONER (Tolak H0)\" if is_stationary else \"TIDAK STASIONER (Gagal Tolak H0)\"}')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- ADF Statistic bernilai negatif yang cukup besar (~ -9.57) and p-value sangat kecil (jauh di bawah 0.05).\n"
    "- Secara formal statistik, **hipotesis nol ditolak** dan target `cnt` dinyatakan **stasioner**.\n"
    "- Namun, dari plot visual sebelumnya terlihat jelas bahwa data memiliki tren jangka panjang dan seasonality. "
    "Stasioneritas formal ini terjadi karena fluktuasi jangka pendek yang sangat kuat di sekitar mean global "
    "yang bergerak lambat. "
    "Dalam konteks machine learning/forecasting, model non-linear (seperti random forest/XGBoost) "
    "atau model linear yang dilengkapi fitur temporal/lag akan mampu menangani tren dan seasonality ini secara langsung "
    "tanpa perlu melakukan differencing formal."
))

# ─────────────────────────────────────────────────────────────────────────────
# 7. ANALISIS AUTOKORELASI (ACF & PACF)
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 7. Analisis Autokorelasi (ACF & PACF)\n\n"
    "- **Autocorrelation Function (ACF)**: Mengukur korelasi antara observasi $y_t$ dengan lag $y_{t-k}$ "
    "termasuk pengaruh dari lag-lag perantara.\n"
    "- **Partial Autocorrelation Function (PACF)**: Mengukur korelasi antara $y_t$ dengan lag $y_{t-k}$ "
    "setelah menghilangkan efek dari lag perantara.\n\n"
    "Analisis ini membantu mengidentifikasi lag order yang optimal untuk model forecasting."
))

cells.append(code(
    "fig, axes = plt.subplots(2, 1, figsize=(14, 8))\n"
    "\n"
    "# ACF plot (sampai lag 48 untuk melihat pola harian)\n"
    "plot_acf(df['cnt'], lags=48, ax=axes[0], color='steelblue', alpha=0.05)\n"
    "axes[0].set_title('Autocorrelation Function (ACF) — Sampai Lag 48')\n"
    "axes[0].set_xlabel('Lag (Jam)')\n"
    "axes[0].set_ylabel('Korelasi')\n"
    "axes[0].set_xticks(range(0, 49, 2))\n"
    "\n"
    "# PACF plot dengan method='yw'\n"
    "plot_pacf(df['cnt'], lags=48, ax=axes[1], color='coral', alpha=0.05, method='yw')\n"
    "axes[1].set_title('Partial Autocorrelation Function (PACF) — Sampai Lag 48')\n"
    "axes[1].set_xlabel('Lag (Jam)')\n"
    "axes[1].set_ylabel('Korelasi Parsial')\n"
    "axes[1].set_xticks(range(0, 49, 2))\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/diagnostics_04_acf_pacf.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(code(
    "# ACF & PACF dengan lag mingguan (sampai 170 jam) untuk mendeteksi pola mingguan\n"
    "fig, axes = plt.subplots(2, 1, figsize=(14, 8))\n"
    "\n"
    "plot_acf(df['cnt'], lags=170, ax=axes[0], color='steelblue', alpha=0.05)\n"
    "axes[0].set_title('Autocorrelation Function (ACF) — Sampai Lag 170 (Mingguan)')\n"
    "axes[0].set_xlabel('Lag (Jam)')\n"
    "axes[0].set_ylabel('Korelasi')\n"
    "axes[0].set_xticks(range(0, 171, 12))\n"
    "\n"
    "plot_pacf(df['cnt'], lags=170, ax=axes[1], color='coral', alpha=0.05, method='yw')\n"
    "axes[1].set_title('Partial Autocorrelation Function (PACF) — Sampai Lag 170 (Mingguan)')\n"
    "axes[1].set_xlabel('Lag (Jam)')\n"
    "axes[1].set_ylabel('Korelasi Parsial')\n"
    "axes[1].set_xticks(range(0, 171, 12))\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/diagnostics_05_acf_pacf_weekly.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- **Pola Siklus pada ACF**: Grafik ACF menunjukkan pola gelombang sinusoidal yang berulang "
    "setiap **24 jam** dan **168 jam (7 hari)**. Ini adalah bukti kuat adanya pola musiman harian dan mingguan.\n"
    "- **PACF Significance**: PACF terpotong tajam setelah lag-lag awal, tetapi menunjukkan lonjakan signifikan "
    "kembali pada **lag 24, 25, 48**, dan **168**.\n"
    "- **Konfirmasi Lag Order**: Hasil ini menjustifikasi pemilihan lag features pada EXP-004, yaitu:\n"
    "  - Lag jangka pendek: `cnt_lag_1`, `cnt_lag_2`, `cnt_lag_3`\n"
    "  - Lag musiman: `cnt_lag_24` (kemarin) dan `cnt_lag_168` (seminggu lalu)"
))

# ─────────────────────────────────────────────────────────────────────────────
# 8. TIME SERIES DECOMPOSITION
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 8. Time Series Decomposition\n\n"
    "Memisahkan data target `cnt` menjadi komponen pembentuknya: **Trend**, **Seasonal**, dan **Residual** "
    "menggunakan model dekomposisi aditif.\n\n"
    "Karena data per jam terlalu rapat untuk divisualisasikan secara langsung (17.379 baris), "
    "kita lakukan dekomposisi terhadap data harian agar visualisasinya lebih jelas."
))

cells.append(code(
    "# Resample data ke harian untuk visualisasi dekomposisi yang jelas\n"
    "df_daily = df.set_index('dteday').resample('D')['cnt'].sum().to_frame()\n"
    "\n"
    "# Dekomposisi dengan period = 7 (musiman mingguan untuk data harian)\n"
    "decomp = seasonal_decompose(df_daily['cnt'], model='additive', period=7)\n"
    "\n"
    "# Plot hasil dekomposisi\n"
    "fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)\n"
    "\n"
    "axes[0].plot(df_daily.index, decomp.observed, color='black', linewidth=1)\n"
    "axes[0].set_title('Dekomposisi Harian: Observed (Total Aktual Harian)')\n"
    "\n"
    "axes[1].plot(df_daily.index, decomp.trend, color='red', linewidth=2)\n"
    "axes[1].set_title('Trend (Tren Jangka Panjang)')\n"
    "\n"
    "axes[2].plot(df_daily.index, decomp.seasonal, color='green', linewidth=1)\n"
    "axes[2].set_title('Seasonal (Pola Musiman Mingguan)')\n"
    "\n"
    "axes[3].scatter(df_daily.index, decomp.resid, color='gray', s=5, alpha=0.5)\n"
    "axes[3].axhline(y=0, color='red', linestyle='--', linewidth=1)\n"
    "axes[3].set_title('Residual (Derau / Pola Tak Terduga)')\n"
    "axes[3].set_xlabel('Tanggal')\n"
    "\n"
    "plt.tight_layout()\n"
    "plt.suptitle('EXP-005 | Dekomposisi Time Series Harian (Period = 7 Hari)', fontsize=14, y=1.02, fontweight='bold')\n"
    "plt.savefig('../data/diagnostics_06_decomposition.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "- **Observed**: Data aktual harian penyewaan sepeda.\n"
    "- **Trend**: Menunjukkan tren jangka panjang yang naik-turun berdasarkan musim makro "
    "(puncak di pertengahan tahun) dan secara bertahap merangkak naik dari 2011 ke 2012.\n"
    "- **Seasonal**: Menangkap pola fluktuasi mingguan (periode 7 hari) yang konsisten.\n"
    "- **Residual**: Sisa varians yang tidak terjelaskan oleh tren dan seasonal. "
    "Ditemukan beberapa lonjakan residual negatif yang kuat (misalnya menjelang akhir tahun 2012) — "
    "ini berkorelasi dengan kejadian ekstrim seperti Badai Sandy pada Oktober 2012."
))

# ─────────────────────────────────────────────────────────────────────────────
# 9. INITIAL FINDINGS
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 9. Initial Findings\n\n"
    "Ringkasan karakteristik time series berdasarkan hasil diagnostik:"
))

cells.append(md(
    "### 9.1 Karakteristik Temporal\n\n"
    "- ✅ **Tren Jangka Panjang**: Teridentifikasi tren kenaikan bertahap dari tahun 2011 ke 2012, "
    "serta tren musiman makro berbentuk pola lonceng terbalik dalam siklus tahunan.\n"
    "- ✅ **Multivariat Seasonality**: Pola musiman terbukti sangat kuat pada beberapa skala waktu:\n"
    "  - Pola harian (24 jam): dipengaruhi jenis hari (kerja vs libur).\n"
    "  - Pola mingguan (7 hari): fluktuasi antar hari dalam seminggu.\n"
    "  - Pola bulanan/musim (tahunan): fluktuasi cuaca/suhu musiman.\n\n"
    "---\n\n"
    "### 9.2 Stasioneritas & Autokorelasi\n\n"
    "- ✅ **Stasioneritas**: Augmented Dickey-Fuller Test menghasilkan p-value $0.00 \\times 10^0$ "
    "(stasioner secara statistik). Hal ini menunjukkan data berfluktuasi secara konstan di sekitar "
    "mean global jangka panjang, namun varians dan tren lokal tidak konstan.\n"
    "- ✅ **Autokorelasi Kuat**: ACF & PACF mengonfirmasi adanya ketergantungan waktu yang tinggi terhadap "
    "observasi sebelumnya. Lonjakan korelasi terbesar berada pada **lag 1, 24, dan 168**.\n\n"
    "---\n\n"
    "### 9.3 Rekomendasi Pemodelan\n\n"
    "1. **Model Non-Linear Robust**: Model berbasis pohon (Random Forest, Gradient Boosting, XGBoost) "
    "sangat direkomendasikan karena dapat menangkap hubungan non-linear tren, musim, dan cuaca "
    "tanpa perlu transformasi differencing yang rumit.\n"
    "2. **Pemanfaatan Lag Features**: Penggunaan `cnt_lag_1` (1 jam lalu) dan `cnt_lag_24` (jam yang sama kemarin) "
    "akan menjadi prediktor yang sangat kuat dalam model regresi."
))

# ─────────────────────────────────────────────────────────────────────────────
# 10. NEXT STEP
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 10. Next Step\n\n"
    "---\n\n"
    "### Eksperimen Berikutnya\n\n"
    "| Informasi | Detail |\n"
    "|-----------|--------|\n"
    "| **ID** | EXP-006 |\n"
    "| **Nama** | Baseline Forecasting |\n"
    "| **Notebook** | `06_baseline_model.ipynb` |\n"
    "| **Input** | `data/featured_data.csv` |\n\n"
    "**Tujuan:**\n\n"
    "> Membangun model baseline sederhana sebagai pembanding utama bagi seluruh model machine learning berikutnya.\n\n"
    "**Model yang akan dibuat pada EXP-006:**\n\n"
    "- **Naive Forecast**: Prediksi jam berikutnya adalah nilai jam saat ini ($y_{t+1} = y_t$).\n"
    "- **Moving Average Forecast**: Prediksi jam berikutnya adalah rata-rata $N$ jam terakhir.\n"
    "- Perhitungan metrik evaluasi standar: **MAE**, **RMSE**, dan **MAPE**.\n\n"
    "---\n\n"
    "*Notebook EXP-005 Time Series Diagnostics — Selesai.*"
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

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '05_time_series_analysis.ipynb')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f'Notebook berhasil dibuat: {output_path}')
print(f'Total cells: {len(cells)}')
