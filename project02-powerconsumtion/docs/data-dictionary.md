# Data Dictionary

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-002 |
| Nama Project | Power Consumption Demand Forecasting |
| Dokumen | Data Dictionary |
| Versi | 1.0.0 |
| Bahasa | Indonesia |

---

# Deskripsi Dataset

Dataset ini berisi data konsumsi daya listrik dari 3 zona, diukur setiap 10 menit selama tahun 2017. Dataset juga mencakup variabel cuaca sebagai fitur pendukung.

---

# 1. Format Dataset

- **Format**: CSV (Comma-Separated Values)
- **Delimiter**: Koma (,)
- **Encoding**: UTF-8
- **Jumlah Baris**: 52.417 (tidak termasuk header)
- **Jumlah Kolom**: 9

---

# 2. Deskripsi Kolom

## 2.1 Kolom Waktu

| Nama Kolom | Tipe Data | Deskripsi | Contoh |
|------------|-----------|-----------|--------|
| Datetime | Datetime (string) | Timestamp pengukuran dalam format MM/DD/YYYY HH:MM | "1/1/2017 0:00" |

**Keterangan:**
- Format waktu: bulan/hari/tahun jam:menit
- Interval pengukuran: 10 menit
- Periode data: 1 Januari 2017 - 30 Desember 2017

---

## 2.2 Kolom Fitur Cuaca

| Nama Kolom | Tipe Data | Deskripsi | Satuan | Rentang Nilai |
|------------|-----------|-----------|--------|----------------|
| Temperature | Float | Suhu udara | °C | ~4.7 - ~36 |
| Humidity | Float | Kelembaban udara | % | ~13 - ~99 |
| WindSpeed | Float | Kecepatan angin | m/s | ~0.05 - ~9.4 |
| GeneralDiffuseFlows | Float | Diffuse flow umum (radiasi) | W/m² | ~0.02 - ~316 |
| DiffuseFlows | Float | Diffuse flow spesifik | W/m² | ~0.01 - ~280 |

**Keterangan:**
- Diffuse flow: radiasi matahari yang tersebar (bukan sinar langsung)
- Temperature dan Humidity memiliki korelasi kuat dengan konsumsi daya

---

## 2.3 Kolom Target (Konsumsi Daya)

| Nama Kolom | Tipe Data | Deskripsi | Satuan | Rentang Nilai |
|------------|-----------|-----------|--------|----------------|
| PowerConsumption_Zone1 | Float | Konsumsi daya zona 1 | kWh | ~13.000 - ~71.000 |
| PowerConsumption_Zone2 | Float | Konsumsi daya zona 2 | kWh | ~6.000 - ~41.000 |
| PowerConsumption_Zone3 | Float | Konsumsi daya zona 3 | kWh | ~8.000 - ~34.000 |

**Keterangan:**
- Setiap zona merupakan area geografis yang berbeda
- Konsumsi daya diukur dalam satuan kWh (kilowatt-hour)
- Zona 1 memiliki konsumsi daya tertinggi, diikuti Zona 3, lalu Zona 2

---

# 3. Statistik Deskriptif

| Kolom | Mean | Std | Min | Max |
|-------|------|-----|-----|-----|
| Temperature | ~17.8 | ~7.3 | ~4.7 | ~36 |
| Humidity | ~68.3 | ~15.5 | ~13 | ~99 |
| WindSpeed | ~2.0 | ~1.7 | ~0.05 | ~9.4 |
| GeneralDiffuseFlows | ~17.4 | ~29.6 | ~0.02 | ~316 |
| DiffuseFlows | ~17.7 | ~27.2 | ~0.01 | ~280 |
| PowerConsumption_Zone1 | ~33.1 | ~12.0 | ~13.0 | ~71.0 |
| PowerConsumption_Zone2 | ~21.7 | ~7.6 | ~6.0 | ~41.0 |
| PowerConsumption_Zone3 | ~18.2 | ~5.8 | ~8.0 | ~34.0 |

---

# 4. Missing Values

Tidak terdapat missing values pada dataset.

---

# 5. Duplicate Data

Tidak terdapat data duplikat berdasarkan kombinasi Datetime.

---

# 6. Catatan Penting

1. **Interval Waktu**: Data diukur setiap 10 menit, sehingga 144 observasi per hari
2. **Multi-target**: Terdapat 3 target yang bisa dimodelkan (Zone 1, 2, 3)
3. **Korelasi antar zona**: Konsumsi daya di ketiga zona memiliki korelasi tinggi
4. **Pola harian**: Konsumsi daya menunjukkan pola harian yang jelas (naik siang, turun malam)
5. **Pola musiman**: Terdapat variasi konsumsi berdasarkan musim (terkait suhu)
