# Data Dictionary

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-001 |
| Nama Project | Bike Sharing Demand Forecasting |
| Dokumen | Data Dictionary |
| Versi | 1.0.0 |
| Bahasa | Indonesia |
| Dataset | hour.csv |
| Jumlah Record | 17.379 baris |
| Jumlah Kolom | 17 kolom |

---

# Tujuan Dokumen

Dokumen ini disusun sebagai referensi utama untuk memahami struktur dataset yang digunakan pada proyek **FL-001 Bike Sharing Demand Forecasting**.

Seluruh informasi mengenai fitur, tipe data, hubungan antar fitur, rekomendasi penggunaan fitur, serta catatan khusus dijelaskan pada dokumen ini.

Dokumen ini bersifat **living document**, sehingga dapat diperbarui apabila selama proses eksplorasi ditemukan karakteristik baru dari dataset.

---

# Ringkasan Dataset

## Deskripsi

Dataset Bike Sharing berisi data historis penyewaan sepeda yang dikumpulkan dari sistem Capital Bikeshare.

Setiap baris merepresentasikan kondisi penyewaan sepeda pada satu jam tertentu beserta informasi waktu, cuaca, dan jumlah penyewaan.

Dataset ini termasuk kategori **Multivariate Time Series Regression Dataset**.

---

## Statistik Dataset

| Informasi | Nilai |
|------------|---------|
| Jumlah Record | 17.379 |
| Jumlah Kolom | 17 |
| Target Prediksi | cnt |
| Missing Value | Tidak ada |
| Tipe Masalah | Regression |
| Jenis Dataset | Multivariate Time Series |

---

# Struktur Dataset

Dataset terdiri atas beberapa kelompok fitur.

## 1. Identifier

Fitur yang hanya digunakan sebagai identitas data.

- instant

---

## 2. Time Features

Fitur yang menjelaskan informasi waktu.

- dteday
- yr
- mnth
- hr
- weekday
- season

---

## 3. Calendar Features

Fitur yang berkaitan dengan kalender.

- holiday
- workingday

---

## 4. Weather Features

Fitur yang menggambarkan kondisi cuaca.

- weathersit
- temp
- atemp
- hum
- windspeed

---

## 5. User Features

Jumlah pengguna berdasarkan kategori.

- casual
- registered

---

## 6. Target

Target yang akan diprediksi.

- cnt

---

# Hubungan Antar Kolom

Hubungan penting pada dataset.

```

casual

+

registered

↓

cnt

```

Artinya:

```
cnt = casual + registered
```

Hubungan ini sangat penting karena menunjukkan bahwa kolom **casual** dan **registered** merupakan penyusun langsung target prediksi.

Kedua fitur tersebut **tidak boleh digunakan sebagai feature input** saat proses modeling karena akan menyebabkan **Data Leakage**.

---

# Klasifikasi Feature

| Kelompok | Jumlah |
|-----------|---------|
| Identifier | 1 |
| Time Feature | 6 |
| Calendar Feature | 2 |
| Weather Feature | 5 |
| User Feature | 2 |
| Target | 1 |

---

# Aturan Penggunaan Feature

Selama proyek berlangsung digunakan aturan berikut.

| Jenis Feature | Digunakan |
|---------------|-----------|
| Identifier | Tidak |
| Time Feature | Ya |
| Calendar Feature | Ya |
| Weather Feature | Ya |
| User Feature | Tidak |
| Target | Sebagai label |

Alasan:

- Identifier tidak memiliki informasi prediktif.
- User Feature menyebabkan data leakage.
- Time Feature memiliki hubungan langsung dengan pola permintaan.
- Weather Feature memiliki pengaruh terhadap jumlah penyewaan.

---

# Penjelasan Detail Setiap Kolom

## 1. instant

| Informasi | Detail |
|------------|---------|
| Nama Kolom | instant |
| Nama Lengkap | Record Index |
| Tipe Data | Integer |
| Jenis Feature | Identifier |
| Contoh Nilai | 1, 2, 3, ... |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ❌ Tidak |
| Feature Engineering | ❌ Tidak |

### Deskripsi

Kolom ini merupakan nomor urut setiap record pada dataset.

Nilai pada kolom ini hanya berfungsi sebagai identitas data dan tidak memiliki hubungan langsung dengan jumlah penyewaan sepeda.

### Catatan

Karena hanya merupakan identifier, kolom ini akan dihapus sebelum proses modeling.

---

## 2. dteday

| Informasi | Detail |
|------------|---------|
| Nama Kolom | dteday |
| Nama Lengkap | Date |
| Tipe Data | Date |
| Jenis Feature | Time Feature |
| Contoh Nilai | 2011-01-01 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | ✅ Ya |

### Deskripsi

Tanggal lengkap dari setiap observasi.

Kolom ini merupakan dasar seluruh analisis time series karena menunjukkan urutan waktu setiap data.

### Potensi Feature Engineering

Dari kolom ini dapat dibuat berbagai fitur baru seperti:

- minggu ke-
- kuartal
- akhir pekan
- awal bulan
- akhir bulan
- musim
- hari dalam tahun

### Catatan

Kolom ini merupakan salah satu feature terpenting dalam proyek forecasting.

---

## 3. season

| Informasi | Detail |
|------------|---------|
| Nama Kolom | season |
| Nama Lengkap | Season |
| Tipe Data | Integer |
| Jenis Feature | Categorical |
| Contoh Nilai | 1–4 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional |

### Mapping

| Nilai | Arti |
|--------|------|
| 1 | Spring |
| 2 | Summer |
| 3 | Fall |
| 4 | Winter |

### Deskripsi

Menunjukkan musim ketika observasi dilakukan.

Musim diperkirakan memiliki pengaruh terhadap tingkat penyewaan sepeda.

### Catatan

Perlu diperlakukan sebagai data kategorikal, bukan numerik kontinu.

---

## 4. yr

| Informasi | Detail |
|------------|---------|
| Nama Kolom | yr |
| Nama Lengkap | Year |
| Tipe Data | Integer |
| Jenis Feature | Time Feature |
| Contoh Nilai | 0, 1 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |

### Mapping

| Nilai | Tahun |
|--------|--------|
| 0 | 2011 |
| 1 | 2012 |

### Deskripsi

Menunjukkan tahun pencatatan data.

Feature ini memungkinkan model mempelajari perubahan tren antar tahun.

---

## 5. mnth

| Informasi | Detail |
|------------|---------|
| Nama Kolom | mnth |
| Nama Lengkap | Month |
| Tipe Data | Integer |
| Jenis Feature | Time Feature |
| Contoh Nilai | 1–12 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |

### Deskripsi

Menunjukkan bulan pada saat data dicatat.

Feature ini penting untuk mendeteksi pola musiman.

---

## 6. hr

| Informasi | Detail |
|------------|---------|
| Nama Kolom | hr |
| Nama Lengkap | Hour |
| Tipe Data | Integer |
| Jenis Feature | Time Feature |
| Contoh Nilai | 0–23 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |

### Deskripsi

Jam ketika observasi dilakukan.

Merupakan salah satu feature terpenting karena jumlah penyewaan berubah sangat signifikan berdasarkan jam.

### Insight yang Diharapkan

Pada tahap EDA nantinya akan dianalisis:

- Jam tersibuk
- Jam tersepi
- Jam pulang kerja
- Jam berangkat kerja

---

## 7. holiday

| Informasi | Detail |
|------------|---------|
| Nama Kolom | holiday |
| Nama Lengkap | Holiday |
| Tipe Data | Integer |
| Jenis Feature | Binary |
| Contoh Nilai | 0,1 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |

### Mapping

| Nilai | Arti |
|--------|------|
| 0 | Bukan Hari Libur |
| 1 | Hari Libur |

### Deskripsi

Menunjukkan apakah hari tersebut merupakan hari libur nasional.

Hari libur diperkirakan memengaruhi pola penggunaan sepeda.

---

## 8. weekday

| Informasi | Detail |
|------------|---------|
| Nama Kolom | weekday |
| Nama Lengkap | Day of Week |
| Tipe Data | Integer |
| Jenis Feature | Time Feature |
| Contoh Nilai | 0–6 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |

### Mapping

| Nilai | Hari |
|--------|------|
| 0 | Minggu |
| 1 | Senin |
| 2 | Selasa |
| 3 | Rabu |
| 4 | Kamis |
| 5 | Jumat |
| 6 | Sabtu |

### Deskripsi

Menunjukkan hari dalam satu minggu.

Digunakan untuk menganalisis perbedaan perilaku pengguna antara weekday dan weekend.

---

## 9. workingday

| Informasi | Detail |
|------------|---------|
| Nama Kolom | workingday |
| Nama Lengkap | Working Day |
| Tipe Data | Integer |
| Jenis Feature | Binary |
| Contoh Nilai | 0, 1 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | ❌ Tidak |

### Mapping

| Nilai | Arti |
|--------|------|
| 0 | Hari Libur / Akhir Pekan |
| 1 | Hari Kerja |

### Deskripsi

Menunjukkan apakah suatu tanggal merupakan hari kerja normal.

Feature ini digunakan untuk membedakan perilaku penyewaan antara hari kerja dan hari libur.

### Insight yang Diharapkan

- Apakah jumlah penyewaan lebih tinggi pada hari kerja?
- Apakah terdapat perbedaan pola jam sibuk?
- Apakah pengguna casual lebih aktif pada hari libur?

### Catatan

Feature ini berpotensi memiliki hubungan yang kuat dengan `hr` dan `weekday`.

---

## 10. weathersit

| Informasi | Detail |
|------------|---------|
| Nama Kolom | weathersit |
| Nama Lengkap | Weather Situation |
| Tipe Data | Integer |
| Jenis Feature | Categorical |
| Contoh Nilai | 1–4 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional (Encoding) |

### Mapping

| Nilai | Kondisi Cuaca |
|--------|---------------|
| 1 | Cerah / Sedikit Berawan |
| 2 | Berkabut / Mendung |
| 3 | Hujan Ringan / Salju Ringan |
| 4 | Hujan Lebat / Salju Lebat / Kabut Tebal |

### Deskripsi

Menggambarkan kondisi cuaca pada saat observasi dilakukan.

### Insight yang Diharapkan

- Bagaimana pengaruh cuaca terhadap jumlah penyewaan?
- Kondisi cuaca apa yang menghasilkan penyewaan tertinggi?
- Seberapa besar penurunan penyewaan saat hujan?

### Catatan

Kemungkinan besar memiliki korelasi negatif terhadap jumlah penyewaan.

---

## 11. temp

| Informasi | Detail |
|------------|---------|
| Nama Kolom | temp |
| Nama Lengkap | Normalized Temperature |
| Tipe Data | Float |
| Jenis Feature | Numerical |
| Contoh Nilai | 0.24 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional |

### Deskripsi

Suhu udara yang telah dinormalisasi ke rentang tertentu oleh penyedia dataset.

Nilai ini **bukan suhu dalam derajat Celcius**.

### Insight yang Diharapkan

- Apakah suhu berkorelasi positif terhadap jumlah penyewaan?
- Pada rentang suhu berapa permintaan paling tinggi?
- Apakah terdapat titik jenuh ketika suhu terlalu tinggi?

### Catatan

Interpretasi hasil perlu memperhatikan bahwa data telah dinormalisasi.

---

## 12. atemp

| Informasi | Detail |
|------------|---------|
| Nama Kolom | atemp |
| Nama Lengkap | Normalized Feeling Temperature |
| Tipe Data | Float |
| Jenis Feature | Numerical |
| Contoh Nilai | 0.28 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional |

### Deskripsi

Temperatur yang dirasakan manusia (apparent temperature).

Nilai ini memperhitungkan kondisi lingkungan sehingga berbeda dengan suhu aktual.

### Insight yang Diharapkan

- Apakah atemp lebih berpengaruh dibanding temp?
- Apakah pengguna lebih sensitif terhadap suhu yang dirasakan?
- Seberapa tinggi korelasi antara temp dan atemp?

### Catatan

Kemungkinan terjadi multikolinearitas dengan feature `temp`.

---

## 13. hum

| Informasi | Detail |
|------------|---------|
| Nama Kolom | hum |
| Nama Lengkap | Humidity |
| Tipe Data | Float |
| Jenis Feature | Numerical |
| Contoh Nilai | 0.81 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional |

### Deskripsi

Tingkat kelembapan udara yang telah dinormalisasi.

### Insight yang Diharapkan

- Apakah kelembapan tinggi menurunkan jumlah penyewaan?
- Bagaimana distribusi kelembapan sepanjang tahun?
- Apakah terdapat hubungan dengan musim?

### Catatan

Perlu dianalisis bersama `temp` dan `weathersit`.

---

## 14. windspeed

| Informasi | Detail |
|------------|---------|
| Nama Kolom | windspeed |
| Nama Lengkap | Wind Speed |
| Tipe Data | Float |
| Jenis Feature | Numerical |
| Contoh Nilai | 0.16 |
| Missing Value | Tidak Ada |
| Digunakan pada Model | ✅ Ya |
| Feature Engineering | Opsional |

### Deskripsi

Kecepatan angin yang telah dinormalisasi.

### Insight yang Diharapkan

- Apakah angin kencang menurunkan jumlah penyewaan?
- Apakah pengaruhnya signifikan dibandingkan suhu?
- Bagaimana distribusi kecepatan angin?

### Catatan

Feature ini kemungkinan memiliki pengaruh lebih kecil dibanding suhu atau cuaca.

---

## 15. casual

| Informasi | Detail |
|------------|---------|
| Nama Kolom | casual |
| Nama Lengkap | Casual Users |
| Tipe Data | Integer |
| Jenis Feature | User Feature |
| Digunakan pada Model | ❌ Tidak |

### Deskripsi

Jumlah pengguna yang tidak terdaftar yang menyewa sepeda pada jam tersebut.

### Insight yang Diharapkan

- Berapa proporsi pengguna casual?
- Apakah pengguna casual lebih aktif saat akhir pekan?
- Bagaimana pengaruh cuaca terhadap pengguna casual?

### Catatan

⚠ **Tidak boleh digunakan sebagai feature input.**

Karena:

```
cnt = casual + registered
```

Menggunakan feature ini akan menyebabkan **Data Leakage**.

---

## 16. registered

| Informasi | Detail |
|------------|---------|
| Nama Kolom | registered |
| Nama Lengkap | Registered Users |
| Tipe Data | Integer |
| Jenis Feature | User Feature |
| Digunakan pada Model | ❌ Tidak |

### Deskripsi

Jumlah pengguna terdaftar pada jam tersebut.

### Insight yang Diharapkan

- Apakah pengguna terdaftar lebih aktif pada hari kerja?
- Berapa kontribusi registered terhadap total penyewaan?

### Catatan

⚠ **Tidak digunakan sebagai feature model** karena merupakan bagian langsung dari target.

---

## 17. cnt

| Informasi | Detail |
|------------|---------|
| Nama Kolom | cnt |
| Nama Lengkap | Total Bike Rentals |
| Tipe Data | Integer |
| Jenis Feature | Target |
| Digunakan pada Model | 🎯 Target Prediksi |

### Deskripsi

Jumlah total penyewaan sepeda pada setiap jam.

Kolom ini merupakan target utama yang akan diprediksi oleh seluruh model forecasting.

### Insight yang Diharapkan

EDA terhadap target minimal mencakup:

- Distribusi data
- Tren historis
- Pola harian
- Pola mingguan
- Pola musiman
- Outlier
- Jam sibuk
- Jam sepi

### Catatan

Target memiliki hubungan:

```
cnt = casual + registered
```

Sehingga kedua feature tersebut tidak boleh digunakan sebagai variabel prediktor.

---

# Kesimpulan Data Dictionary

Berdasarkan hasil identifikasi, dataset terdiri dari **17 fitur** yang dapat dikelompokkan menjadi enam kategori utama:

- Identifier
- Time Features
- Calendar Features
- Weather Features
- User Features
- Target

Untuk proses pemodelan forecasting, feature yang direkomendasikan adalah seluruh **Time Features**, **Calendar Features**, dan **Weather Features**.

Feature `instant`, `casual`, dan `registered` tidak digunakan sebagai input model karena masing-masing merupakan identifier dan sumber potensi **data leakage**.

Dokumen ini akan menjadi referensi utama selama proses Data Understanding, Exploratory Data Analysis (EDA), Feature Engineering, hingga Modeling. Apabila ditemukan insight baru selama eksperimen berlangsung, Data Dictionary ini harus diperbarui agar tetap mencerminkan kondisi dataset secara akurat.