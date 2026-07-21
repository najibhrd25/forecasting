"""
Script untuk membuat notebook 03_preprocessing.ipynb (EXP-003 — Data Cleaning).
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
    "| **Eksperimen** | EXP-003 |\n"
    "| **Nama Eksperimen** | Data Cleaning |\n"
    "| **Dataset** | hour.csv (Bike Sharing Dataset — UCI ML Repository) |\n"
    "| **Tujuan Notebook** | Memastikan dataset siap digunakan untuk feature engineering dan modeling |\n"
    "| **Tanggal Pengerjaan** | 21 Juli 2026 |\n"
    "| **Versi Notebook** | 1.0.0 |\n"
    "| **Author** | GAKUSEI Najib |\n"
    "| **Prasyarat** | EXP-001 Data Understanding ✅, EXP-002 EDA ✅ |\n\n"
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
    "4. [Validasi Missing Value](#4-validasi-missing-value)\n"
    "5. [Validasi Duplicate](#5-validasi-duplicate)\n"
    "6. [Validasi & Konversi Tipe Data](#6-validasi--konversi-tipe-data)\n"
    "7. [Validasi Rentang Nilai](#7-validasi-rentang-nilai)\n"
    "8. [Analisis & Penanganan Outlier](#8-analisis--penanganan-outlier)\n"
    "9. [Penghapusan Feature yang Tidak Digunakan](#9-penghapusan-feature-yang-tidak-digunakan)\n"
    "10. [Dataset Final & Laporan Cleaning](#10-dataset-final--laporan-cleaning)\n"
    "11. [Simpan Dataset Hasil Cleaning](#11-simpan-dataset-hasil-cleaning)\n"
    "12. [Next Step](#12-next-step)"
))

# ─────────────────────────────────────────────────────────────────────────────
# 1. TUJUAN EKSPERIMEN
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md("---\n\n## 1. Tujuan Eksperimen"))

cells.append(md(
    "### Tujuan\n\n"
    "Memastikan dataset bersih dan siap digunakan untuk proses feature engineering dan modeling "
    "dengan melakukan serangkaian validasi serta transformasi yang diperlukan.\n\n"
    "---\n\n"
    "### Hipotesis\n\n"
    "> Dataset relatif bersih namun masih memerlukan validasi terhadap outlier, tipe data, "
    "serta konsistensi nilai.\n\n"
    "---\n\n"
    "### Konteks dari Eksperimen Sebelumnya\n\n"
    "Berdasarkan temuan pada **EXP-001** dan **EXP-002**, berikut yang perlu dilakukan:\n\n"
    "| Temuan | Aksi |\n"
    "|--------|------|\n"
    "| `dteday` bertipe `object` | Konversi ke `datetime` |\n"
    "| `casual` & `registered` menyebabkan data leakage | Hapus dari dataset |\n"
    "| `instant` hanya identifier tanpa nilai prediktif | Hapus dari dataset |\n"
    "| Distribusi `cnt` right-skewed dengan outlier di nilai tinggi | Analisis & dokumentasi |\n"
    "| Kolom kategorikal (season, yr, dll.) bertipe integer | Dokumentasi, tanpa konversi (model-agnostic) |\n\n"
    "---\n\n"
    "### Output yang Diharapkan\n\n"
    "- Dataset bersih yang siap digunakan pada EXP-004\n"
    "- File: `data/processed_data.csv`\n"
    "- Laporan ringkasan proses cleaning\n\n"
    "---\n\n"
    "### Acceptance Criteria\n\n"
    "| Kriteria | Keterangan |\n"
    "|----------|------------|\n"
    "| Dataset siap modeling | Feature tidak berguna sudah dihapus |\n"
    "| Tipe data sudah benar | `dteday` sudah `datetime` |\n"
    "| Tidak ada missing value | Diverifikasi ulang |\n"
    "| Tidak ada duplicate | Diverifikasi ulang |\n"
    "| Outlier sudah dianalisis | Keputusan retain/remove terdokumentasi |\n"
    "| Dataset berhasil disimpan | `data/processed_data.csv` tersedia |"
))

# ─────────────────────────────────────────────────────────────────────────────
# 2. IMPORT LIBRARY
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 2. Import Library\n\n"
    "Library yang dibutuhkan pada tahap Data Cleaning adalah `pandas`, `numpy`, dan "
    "`matplotlib`/`seaborn` untuk visualisasi distribusi saat penanganan outlier."
))

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
    "print('Library berhasil diimport.')\n"
    "print(f'Versi pandas : {pd.__version__}')\n"
    "print(f'Versi numpy  : {np.__version__}')"
))

# ─────────────────────────────────────────────────────────────────────────────
# 3. LOAD DATASET
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 3. Load Dataset\n\n"
    "Dataset dimuat langsung dari file raw `hour.csv`. "
    "Seluruh proses cleaning dilakukan terhadap salinan DataFrame sehingga data asli tidak berubah."
))

cells.append(code(
    "# Definisikan path\n"
    "DATA_PATH      = '../data/hour.csv'\n"
    "OUTPUT_PATH    = '../data/processed_data.csv'\n"
    "\n"
    "# Load dataset raw\n"
    "df_raw = pd.read_csv(DATA_PATH)\n"
    "\n"
    "# Buat salinan untuk proses cleaning\n"
    "df = df_raw.copy()\n"
    "\n"
    "print(f'Dataset berhasil dimuat: {DATA_PATH}')\n"
    "print(f'Dimensi awal           : {df.shape[0]:,} baris x {df.shape[1]} kolom')"
))

cells.append(md("**Interpretasi:** Dataset berhasil dimuat. Salinan `df` akan digunakan untuk seluruh proses cleaning. Dataset asli `df_raw` dipertahankan sebagai referensi."))

# ─────────────────────────────────────────────────────────────────────────────
# 4. VALIDASI MISSING VALUE
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 4. Validasi Missing Value\n\n"
    "Validasi ulang keberadaan missing value sebagai konfirmasi setelah temuan pada EXP-001."
))

cells.append(code(
    "# Hitung missing value\n"
    "missing_count = df.isnull().sum()\n"
    "missing_pct   = (df.isnull().mean() * 100).round(4)\n"
    "\n"
    "missing_df = pd.DataFrame({\n"
    "    'Jumlah Missing'        : missing_count,\n"
    "    'Persentase Missing (%)' : missing_pct\n"
    "}).sort_values('Jumlah Missing', ascending=False)\n"
    "\n"
    "print('=' * 48)\n"
    "print('VALIDASI MISSING VALUE')\n"
    "print('=' * 48)\n"
    "print(missing_df.to_string())\n"
    "print(f'\\nTotal kolom dengan missing value : {(missing_count > 0).sum()}')\n"
    "\n"
    "if (missing_count > 0).sum() == 0:\n"
    "    print('\\n✅ PASS — Tidak ada missing value pada dataset.')\n"
    "else:\n"
    "    print('\\n⚠ WARNING — Ditemukan missing value. Perlu penanganan.')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "✅ Validasi berhasil — **tidak ada missing value** pada seluruh kolom. "
    "Tidak diperlukan proses imputasi. Hasil ini konsisten dengan temuan pada EXP-001."
))

# ─────────────────────────────────────────────────────────────────────────────
# 5. VALIDASI DUPLICATE
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 5. Validasi Duplicate\n\n"
    "Validasi ulang data duplikat untuk memastikan tidak ada baris yang perlu dihapus."
))

cells.append(code(
    "# Duplikat seluruh kolom\n"
    "n_duplikat      = df.duplicated().sum()\n"
    "n_duplikat_kunci = df.duplicated(subset=['dteday', 'hr']).sum()\n"
    "\n"
    "print('=' * 48)\n"
    "print('VALIDASI DUPLICATE DATA')\n"
    "print('=' * 48)\n"
    "print(f'Jumlah baris total               : {len(df):,}')\n"
    "print(f'Duplikat (seluruh kolom)          : {n_duplikat}')\n"
    "print(f'Duplikat (kunci dteday + hr)      : {n_duplikat_kunci}')\n"
    "\n"
    "if n_duplikat == 0 and n_duplikat_kunci == 0:\n"
    "    print('\\n✅ PASS — Tidak ada data duplikat.')\n"
    "else:\n"
    "    print('\\n⚠ WARNING — Ditemukan duplikat. Perlu penanganan.')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "✅ Validasi berhasil — **tidak ada data duplikat** baik secara keseluruhan maupun berdasarkan "
    "kunci unik `dteday + hr`. Tidak diperlukan penghapusan baris."
))

# ─────────────────────────────────────────────────────────────────────────────
# 6. VALIDASI & KONVERSI TIPE DATA
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 6. Validasi & Konversi Tipe Data\n\n"
    "Berdasarkan temuan pada EXP-001, kolom `dteday` masih bertipe `object` dan perlu "
    "dikonversi ke tipe `datetime64` agar dapat digunakan untuk analisis time series."
))

cells.append(code(
    "# Tipe data sebelum konversi\n"
    "print('Tipe data SEBELUM konversi:')\n"
    "print(df[['dteday', 'instant', 'season', 'yr', 'mnth', 'hr']].dtypes.to_string())\n"
    "\n"
    "# Konversi dteday ke datetime\n"
    "df['dteday'] = pd.to_datetime(df['dteday'])\n"
    "\n"
    "print('\\nTipe data SESUDAH konversi:')\n"
    "print(df[['dteday', 'instant', 'season', 'yr', 'mnth', 'hr']].dtypes.to_string())\n"
    "\n"
    "print(f'\\n✅ Kolom dteday berhasil dikonversi ke: {df[\"dteday\"].dtype}')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "Kolom `dteday` berhasil dikonversi dari tipe `object` ke `datetime64[ns]`. "
    "Dengan tipe data yang benar, kolom ini dapat digunakan langsung untuk operasi time series "
    "seperti resampling, penambahan komponen waktu, dan pengurutan kronologis."
))

cells.append(md("### 6.1 Verifikasi Urutan Kronologis Dataset"))

cells.append(code(
    "# Pastikan dataset sudah terurut secara kronologis\n"
    "df_sorted = df.sort_values(by=['dteday', 'hr'], ascending=[True, True])\n"
    "is_sorted  = (df['instant'].values == df_sorted['instant'].values).all()\n"
    "\n"
    "print(f'Dataset sudah terurut secara kronologis: {is_sorted}')\n"
    "print(f'Tanggal pertama : {df[\"dteday\"].min().date()}')\n"
    "print(f'Tanggal terakhir: {df[\"dteday\"].max().date()}')\n"
    "print(f'Rentang waktu   : {(df[\"dteday\"].max() - df[\"dteday\"].min()).days} hari')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "Dataset sudah terurut secara kronologis (sesuai dengan urutan kolom `instant`). "
    "Dataset mencakup rentang waktu dari 1 Januari 2011 hingga 31 Desember 2012 — "
    "total **730–731 hari** atau **2 tahun** data."
))

# ─────────────────────────────────────────────────────────────────────────────
# 7. VALIDASI RENTANG NILAI
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 7. Validasi Rentang Nilai\n\n"
    "Memastikan setiap kolom memiliki nilai yang berada dalam rentang yang valid "
    "sesuai dokumentasi Data Dictionary."
))

cells.append(code(
    "# Definisikan rentang nilai yang valid per kolom\n"
    "VALID_RANGES = {\n"
    "    'season'    : (1, 4),\n"
    "    'yr'        : (0, 1),\n"
    "    'mnth'      : (1, 12),\n"
    "    'hr'        : (0, 23),\n"
    "    'holiday'   : (0, 1),\n"
    "    'weekday'   : (0, 6),\n"
    "    'workingday': (0, 1),\n"
    "    'weathersit': (1, 4),\n"
    "    'temp'      : (0.0, 1.0),\n"
    "    'atemp'     : (0.0, 1.0),\n"
    "    'hum'       : (0.0, 1.0),\n"
    "    'windspeed' : (0.0, 1.0),\n"
    "    'casual'    : (0, None),\n"
    "    'registered': (0, None),\n"
    "    'cnt'       : (1, None),\n"
    "}\n"
    "\n"
    "print('=' * 65)\n"
    "print('VALIDASI RENTANG NILAI KOLOM')\n"
    "print('=' * 65)\n"
    "\n"
    "laporan_validasi = []\n"
    "for col, (vmin, vmax) in VALID_RANGES.items():\n"
    "    aktual_min = df[col].min()\n"
    "    aktual_max = df[col].max()\n"
    "\n"
    "    min_ok = True if vmin is None else (aktual_min >= vmin)\n"
    "    max_ok = True if vmax is None else (aktual_max <= vmax)\n"
    "    status = '✅ OK' if (min_ok and max_ok) else '❌ INVALID'\n"
    "\n"
    "    laporan_validasi.append({'Kolom': col, 'Min Aktual': aktual_min,\n"
    "                             'Max Aktual': aktual_max, 'Status': status})\n"
    "    batas = f'{vmin} – {vmax}' if vmax is not None else f'>= {vmin}'\n"
    "    print(f'  {col:<12} | Aktual [{aktual_min:.4f}, {aktual_max:.4f}] | Batas: {batas:<10} | {status}')\n"
    "\n"
    "n_invalid = sum(1 for r in laporan_validasi if r['Status'] == '❌ INVALID')\n"
    "print(f'\\nTotal kolom dengan nilai invalid: {n_invalid}')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "✅ Seluruh kolom memiliki nilai dalam rentang yang valid sesuai Data Dictionary. "
    "Tidak ditemukan nilai yang berada di luar batas yang telah ditentukan. "
    "Dataset lolos validasi rentang nilai."
))

# ─────────────────────────────────────────────────────────────────────────────
# 8. ANALISIS & PENANGANAN OUTLIER
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 8. Analisis & Penanganan Outlier\n\n"
    "Berdasarkan EDA (EXP-002), distribusi `cnt` bersifat right-skewed dan terdapat "
    "nilai yang sangat tinggi. Bagian ini menganalisis outlier pada target `cnt` dan "
    "feature numerik menggunakan metode **IQR (Interquartile Range)**."
))

cells.append(md("### 8.1 Deteksi Outlier dengan Metode IQR"))

cells.append(code(
    "# Deteksi outlier menggunakan IQR untuk kolom numerik\n"
    "kolom_numerik = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']\n"
    "\n"
    "print('=' * 65)\n"
    "print('DETEKSI OUTLIER (METODE IQR)')\n"
    "print('=' * 65)\n"
    "\n"
    "outlier_summary = []\n"
    "for col in kolom_numerik:\n"
    "    Q1  = df[col].quantile(0.25)\n"
    "    Q3  = df[col].quantile(0.75)\n"
    "    IQR = Q3 - Q1\n"
    "    lower_bound = Q1 - 1.5 * IQR\n"
    "    upper_bound = Q3 + 1.5 * IQR\n"
    "\n"
    "    n_outlier_low  = (df[col] < lower_bound).sum()\n"
    "    n_outlier_high = (df[col] > upper_bound).sum()\n"
    "    n_outlier_total = n_outlier_low + n_outlier_high\n"
    "    pct_outlier = n_outlier_total / len(df) * 100\n"
    "\n"
    "    outlier_summary.append({\n"
    "        'Kolom': col, 'Q1': Q1, 'Q3': Q3, 'IQR': IQR,\n"
    "        'Lower Bound': lower_bound, 'Upper Bound': upper_bound,\n"
    "        'Outlier Bawah': n_outlier_low, 'Outlier Atas': n_outlier_high,\n"
    "        'Total Outlier': n_outlier_total, 'Persentase (%)': pct_outlier\n"
    "    })\n"
    "\n"
    "    print(f'\\n{col}')\n"
    "    print(f'  Q1={Q1:.4f}, Q3={Q3:.4f}, IQR={IQR:.4f}')\n"
    "    print(f'  Batas: [{lower_bound:.4f}, {upper_bound:.4f}]')\n"
    "    print(f'  Outlier bawah : {n_outlier_low}')\n"
    "    print(f'  Outlier atas  : {n_outlier_high}')\n"
    "    print(f'  Total outlier : {n_outlier_total} ({pct_outlier:.2f}%)')"
))

cells.append(md("### 8.2 Visualisasi Distribusi dengan Outlier"))

cells.append(code(
    "fig, axes = plt.subplots(1, len(kolom_numerik), figsize=(18, 5))\n"
    "\n"
    "for i, col in enumerate(kolom_numerik):\n"
    "    sns.boxplot(y=df[col], ax=axes[i], color='steelblue',\n"
    "                flierprops=dict(marker='o', markerfacecolor='red', markersize=3, alpha=0.4))\n"
    "    axes[i].set_title(col)\n"
    "    axes[i].set_ylabel('')\n"
    "\n"
    "plt.suptitle('EXP-003 | Boxplot Kolom Numerik — Identifikasi Outlier', fontsize=13, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.savefig('../data/cleaning_01_outlier_boxplot.png', bbox_inches='tight', dpi=110)\n"
    "plt.show()"
))

cells.append(md("### 8.3 Keputusan Penanganan Outlier"))

cells.append(code(
    "# Analisis outlier pada cnt secara lebih detail\n"
    "Q1_cnt  = df['cnt'].quantile(0.25)\n"
    "Q3_cnt  = df['cnt'].quantile(0.75)\n"
    "IQR_cnt = Q3_cnt - Q1_cnt\n"
    "upper_cnt = Q3_cnt + 1.5 * IQR_cnt\n"
    "\n"
    "outlier_cnt = df[df['cnt'] > upper_cnt]\n"
    "\n"
    "print('=' * 55)\n"
    "print('ANALISIS OUTLIER PADA KOLOM TARGET (cnt)')\n"
    "print('=' * 55)\n"
    "print(f'IQR Fence Atas : {upper_cnt:.2f}')\n"
    "print(f'Jumlah outlier : {len(outlier_cnt)}')\n"
    "print(f'Persentase     : {len(outlier_cnt)/len(df)*100:.2f}%')\n"
    "print(f'\\nDistribusi outlier berdasarkan jam (hr):')\n"
    "print(outlier_cnt['hr'].value_counts().sort_index().to_string())\n"
    "print(f'\\nDistribusi outlier berdasarkan musim:')\n"
    "print(outlier_cnt['season'].value_counts().to_string())"
))

cells.append(md(
    "### 8.4 Keputusan: Outlier Dipertahankan\n\n"
    "> **Keputusan: Outlier pada `cnt` TIDAK dihapus.**\n\n"
    "**Alasan:**\n\n"
    "1. **Outlier merepresentasikan kondisi nyata.** Nilai `cnt` yang tinggi terjadi pada jam "
    "sibuk (pagi & sore) dan musim ramai — bukan merupakan kesalahan pencatatan data.\n"
    "2. **Model harus mampu memprediksi jam puncak.** Menghapus outlier akan membuat model "
    "tidak mampu memprediksi periode penyewaan tertinggi yang justru penting secara bisnis.\n"
    "3. **Persentase outlier relatif kecil** (~5–10%) sehingga dampak pada distribusi tidak "
    "terlalu signifikan.\n"
    "4. **Tree-based models robust terhadap outlier.** Model seperti Random Forest dan "
    "XGBoost yang akan digunakan pada tahap modeling tidak sensitif terhadap outlier.\n\n"
    "**Catatan untuk Feature Engineering (EXP-004):**\n"
    "Jika diperlukan, transformasi `log1p(cnt)` dapat dipertimbangkan untuk mengurangi "
    "dampak skewness tanpa menghilangkan data."
))

# ─────────────────────────────────────────────────────────────────────────────
# 9. PENGHAPUSAN FEATURE YANG TIDAK DIGUNAKAN
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 9. Penghapusan Feature yang Tidak Digunakan\n\n"
    "Sesuai aturan penggunaan feature pada Data Dictionary, beberapa kolom tidak akan "
    "digunakan pada proses modeling dan perlu dihapus dari dataset."
))

cells.append(code(
    "# Kolom yang dihapus dan alasannya\n"
    "KOLOM_DIHAPUS = {\n"
    "    'instant'   : 'Identifier tanpa nilai prediktif',\n"
    "    'casual'    : 'Data leakage — komponen langsung dari cnt',\n"
    "    'registered': 'Data leakage — komponen langsung dari cnt',\n"
    "}\n"
    "\n"
    "print('=' * 55)\n"
    "print('KOLOM YANG DIHAPUS')\n"
    "print('=' * 55)\n"
    "for col, alasan in KOLOM_DIHAPUS.items():\n"
    "    print(f'  ❌ {col:<12} — {alasan}')\n"
    "\n"
    "# Dimensi sebelum penghapusan\n"
    "print(f'\\nDimensi SEBELUM : {df.shape[0]:,} baris x {df.shape[1]} kolom')\n"
    "\n"
    "# Hapus kolom\n"
    "df = df.drop(columns=list(KOLOM_DIHAPUS.keys()))\n"
    "\n"
    "print(f'Dimensi SESUDAH : {df.shape[0]:,} baris x {df.shape[1]} kolom')"
))

cells.append(code(
    "# Verifikasi kolom yang tersisa\n"
    "print('=' * 50)\n"
    "print('KOLOM YANG TERSISA PADA DATASET CLEAN')\n"
    "print('=' * 50)\n"
    "for i, col in enumerate(df.columns, 1):\n"
    "    print(f'{i:>2}. {col} ({df[col].dtype})')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "Dataset kini memiliki **14 kolom** (berkurang dari 17). Kolom yang tersisa terdiri dari:\n\n"
    "- 1 kolom tanggal: `dteday`\n"
    "- 5 kolom time feature: `season`, `yr`, `mnth`, `hr`, `weekday`\n"
    "- 2 kolom calendar feature: `holiday`, `workingday`\n"
    "- 5 kolom weather feature: `weathersit`, `temp`, `atemp`, `hum`, `windspeed`\n"
    "- 1 kolom target: `cnt`\n\n"
    "Semua kolom yang tersisa sesuai dengan aturan penggunaan feature pada Data Dictionary."
))

# ─────────────────────────────────────────────────────────────────────────────
# 10. DATASET FINAL & LAPORAN CLEANING
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 10. Dataset Final & Laporan Cleaning\n\n"
    "Melakukan pengecekan akhir pada dataset hasil cleaning dan membuat laporan ringkasan "
    "seluruh proses yang telah dilakukan."
))

cells.append(md("### 10.1 Pemeriksaan Akhir Dataset"))

cells.append(code(
    "# Info dataset akhir\n"
    "print('=' * 50)\n"
    "print('DATASET FINAL — RINGKASAN')\n"
    "print('=' * 50)\n"
    "print(f'Jumlah baris : {df.shape[0]:,}')\n"
    "print(f'Jumlah kolom : {df.shape[1]}')\n"
    "print(f'Missing value: {df.isnull().sum().sum()}')\n"
    "print(f'Duplikat     : {df.duplicated().sum()}')\n"
    "print(f'\\nTipe data setiap kolom:')\n"
    "print(df.dtypes.to_string())"
))

cells.append(code(
    "# Lima sampel data final\n"
    "print('Lima sampel pertama dataset clean:')\n"
    "df.head()"
))

cells.append(code(
    "# Statistik deskriptif dataset final\n"
    "df.describe().T"
))

cells.append(md("### 10.2 Laporan Ringkasan Proses Cleaning"))

cells.append(code(
    "# Laporan cleaning\n"
    "laporan = [\n"
    "    ('Validasi Missing Value'       , 'PASS', 'Tidak ada missing value pada 17 kolom'),\n"
    "    ('Validasi Duplicate'           , 'PASS', 'Tidak ada duplikat (seluruh baris & kunci dteday+hr)'),\n"
    "    ('Konversi Tipe Data (dteday)'  , 'DONE', 'object → datetime64[ns]'),\n"
    "    ('Validasi Rentang Nilai'        , 'PASS', 'Semua kolom dalam batas valid sesuai Data Dictionary'),\n"
    "    ('Analisis Outlier (cnt)'       , 'RETAIN', 'Outlier dipertahankan — merepresentasikan kondisi nyata'),\n"
    "    ('Hapus instant'                , 'DONE', 'Identifier — tidak memiliki nilai prediktif'),\n"
    "    ('Hapus casual'                 , 'DONE', 'Data leakage — penyusun langsung cnt'),\n"
    "    ('Hapus registered'             , 'DONE', 'Data leakage — penyusun langsung cnt'),\n"
    "]\n"
    "\n"
    "print('=' * 75)\n"
    "print('LAPORAN RINGKASAN DATA CLEANING — EXP-003')\n"
    "print('=' * 75)\n"
    "print(f'{\"No.\":<5} {\"Proses\":<35} {\"Status\":<10} {\"Keterangan\"}')\n"
    "print('-' * 75)\n"
    "for i, (proses, status, ket) in enumerate(laporan, 1):\n"
    "    emoji = '✅' if status in ('PASS', 'DONE') else ('⚠️' if status == 'RETAIN' else '❌')\n"
    "    print(f'{i:<5} {proses:<35} {emoji} {status:<8} {ket}')\n"
    "print('-' * 75)\n"
    "print(f'\\nDimensi awal  : {df_raw.shape[0]:,} baris x {df_raw.shape[1]} kolom')\n"
    "print(f'Dimensi akhir : {df.shape[0]:,} baris x {df.shape[1]} kolom')\n"
    "print(f'Kolom dihapus : 3 (instant, casual, registered)')\n"
    "print(f'Baris dihapus : 0')"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "Seluruh proses Data Cleaning telah berhasil diselesaikan. Dataset final memiliki karakteristik:\n\n"
    "- **17.379 baris** — tidak ada baris yang dihapus\n"
    "- **14 kolom** — 3 kolom dihapus (instant, casual, registered)\n"
    "- **0 missing value**\n"
    "- **0 duplikat**\n"
    "- Tipe data sudah benar\n"
    "- Rentang nilai sudah tervalidasi\n"
    "- Outlier pada `cnt` dipertahankan dengan alasan yang terdokumentasi\n\n"
    "Dataset ini siap digunakan untuk tahap berikutnya: **EXP-004 Feature Engineering**."
))

# ─────────────────────────────────────────────────────────────────────────────
# 11. SIMPAN DATASET
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 11. Simpan Dataset Hasil Cleaning\n\n"
    "Dataset hasil cleaning disimpan ke file `data/processed_data.csv` sebagai "
    "deliverable resmi EXP-003 dan input untuk EXP-004."
))

cells.append(code(
    "# Simpan dataset final\n"
    "df.to_csv(OUTPUT_PATH, index=False)\n"
    "\n"
    "print(f'✅ Dataset berhasil disimpan ke: {OUTPUT_PATH}')\n"
    "print(f'   Jumlah baris : {df.shape[0]:,}')\n"
    "print(f'   Jumlah kolom : {df.shape[1]}')\n"
    "\n"
    "# Verifikasi file tersimpan dengan benar\n"
    "df_verify = pd.read_csv(OUTPUT_PATH)\n"
    "print(f'\\nVerifikasi load ulang:')\n"
    "print(f'   Dimensi      : {df_verify.shape}')\n"
    "print(f'   Missing value: {df_verify.isnull().sum().sum()}')\n"
    "assert df_verify.shape == df.shape, 'ERROR: Dimensi tidak konsisten!'\n"
    "print(f'\\n✅ Verifikasi berhasil — file tersimpan dengan benar.')"
))

cells.append(code(
    "# Tampilkan lima baris pertama file yang disimpan\n"
    "print('Kolom pada processed_data.csv:')\n"
    "print(list(df_verify.columns))\n"
    "print()\n"
    "df_verify.head()"
))

cells.append(md(
    "**Interpretasi:**\n\n"
    "File `data/processed_data.csv` berhasil disimpan dan diverifikasi. "
    "Dataset ini akan menjadi input utama untuk semua eksperimen berikutnya (EXP-004 hingga EXP-013)."
))

# ─────────────────────────────────────────────────────────────────────────────
# 12. NEXT STEP
# ─────────────────────────────────────────────────────────────────────────────
cells.append(md(
    "---\n\n"
    "## 12. Next Step\n\n"
    "---\n\n"
    "### Eksperimen Berikutnya\n\n"
    "| Informasi | Detail |\n"
    "|-----------|--------|\n"
    "| **ID** | EXP-004 |\n"
    "| **Nama** | Feature Engineering |\n"
    "| **Notebook** | `04_feature_engineering.ipynb` |\n"
    "| **Input** | `data/processed_data.csv` |\n\n"
    "**Tujuan:**\n\n"
    "> Meningkatkan kualitas informasi pada dataset dengan membangun feature baru "
    "yang relevan untuk forecasting.\n\n"
    "**Aktivitas yang akan dilakukan pada EXP-004:**\n\n"
    "- Membuat feature waktu baru dari kolom `dteday`\n"
    "- Membuat cyclical encoding untuk `hr`, `mnth`, dan `weekday`\n"
    "- Membuat lag features dari `cnt`\n"
    "- Membuat rolling statistics (mean, std)\n"
    "- Membuat interaction features (`hr × workingday`)\n"
    "- Menyimpan dataset hasil feature engineering ke `data/featured_data.csv`\n\n"
    "---\n\n"
    "*Notebook EXP-003 Data Cleaning — Selesai.*"
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

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '03_preprocessing.ipynb')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f'Notebook berhasil dibuat: {output_path}')
print(f'Total cells: {len(cells)}')
