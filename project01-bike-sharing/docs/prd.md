# Product Requirements Document (PRD)

---

# Informasi Dokumen

| Informasi | Detail |
|------------|---------|
| Project ID | FL-001 |
| Nama Project | Bike Sharing Demand Forecasting |
| Kategori | Forecasting / Time Series Analysis |
| Domain | Data Science |
| Status | In Development |
| Versi | 1.0.0 |
| Tanggal Dibuat | Juli 2026 |
| Bahasa | Indonesia |
| Dataset | Bike Sharing Dataset (UCI Machine Learning Repository) |

---

# Riwayat Dokumen

| Versi | Tanggal | Perubahan | Penulis |
|--------|----------|-----------|----------|
| 1.0.0 | Juli 2026 | Dokumen awal | GAKUSEI Najib |

---

# Daftar Isi

1. Pendahuluan
2. Latar Belakang
3. Permasalahan
4. Tujuan Proyek
5. Ruang Lingkup
6. Sasaran Pembelajaran
7. Deliverables
8. Arsitektur Pengembangan
9. Standar Pengerjaan
10. Metodologi
11. Timeline
12. Future Development

---

# 1. Pendahuluan

## 1.1 Deskripsi Proyek

Bike Sharing Demand Forecasting merupakan proyek pembelajaran Data Science yang berfokus pada pembangunan sistem prediksi jumlah penyewaan sepeda berdasarkan data historis dan berbagai faktor pendukung seperti waktu, cuaca, musim, serta hari kerja.

Proyek ini tidak hanya bertujuan menghasilkan model dengan performa yang baik, tetapi juga membangun pemahaman menyeluruh mengenai proses pengembangan solusi forecasting secara end-to-end.

Seluruh proses akan mengikuti alur kerja yang umum digunakan dalam industri Data Science, mulai dari eksplorasi data hingga deployment model.

---

## 1.2 Latar Belakang

Forecasting merupakan salah satu bidang penting dalam Data Science karena hampir seluruh sektor industri membutuhkan kemampuan untuk memperkirakan kondisi di masa depan.

Beberapa contoh penerapan forecasting antara lain:

- Prediksi permintaan produk
- Prediksi konsumsi listrik
- Prediksi lalu lintas kendaraan
- Prediksi kualitas udara
- Prediksi jumlah pasien
- Prediksi permintaan transportasi

Bike Sharing Dataset dipilih sebagai proyek pertama karena memiliki karakteristik yang ideal untuk mempelajari forecasting, yaitu:

- Dataset bersih
- Ukuran dataset tidak terlalu besar
- Memiliki banyak fitur pendukung
- Memiliki pola musiman
- Memiliki pola harian
- Memiliki banyak referensi akademik

Dengan menggunakan dataset ini diharapkan proses pembelajaran dapat lebih fokus pada metodologi forecasting tanpa terbebani oleh kompleksitas data.

---

# 2. Permasalahan

Permasalahan utama yang ingin diselesaikan dalam proyek ini adalah:

> Bagaimana membangun model yang mampu memprediksi jumlah penyewaan sepeda pada periode waktu berikutnya berdasarkan data historis serta variabel pendukung yang tersedia.

Selain menghasilkan model prediksi, proyek ini juga berusaha menjawab beberapa pertanyaan analitis seperti:

- Faktor apa yang paling memengaruhi jumlah penyewaan?
- Bagaimana pola penyewaan pada hari kerja dibandingkan hari libur?
- Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan?
- Apakah terdapat pola musiman?
- Apakah terdapat pola harian?
- Seberapa baik model dapat melakukan prediksi dibandingkan baseline sederhana?

Jawaban atas pertanyaan tersebut akan diperoleh melalui proses Exploratory Data Analysis (EDA), Feature Engineering, dan Model Evaluation.

---

# 3. Tujuan Proyek

Proyek ini memiliki beberapa tujuan utama.

## 3.1 Tujuan Teknis

- Memahami alur kerja proyek forecasting.
- Melakukan eksplorasi terhadap dataset time series.
- Melakukan preprocessing data.
- Melakukan feature engineering.
- Membangun beberapa model forecasting.
- Melakukan evaluasi model.
- Membandingkan performa antar model.
- Menyusun dokumentasi proyek secara sistematis.

---

## 3.2 Tujuan Pembelajaran

Setelah proyek selesai diharapkan mampu:

- Memahami proses Data Analysis.
- Memahami proses Exploratory Data Analysis.
- Memahami proses Data Cleaning.
- Memahami Feature Engineering.
- Memahami Time Series Analysis.
- Memahami proses pembangunan model forecasting.
- Memahami evaluasi model forecasting.
- Memahami dokumentasi proyek Data Science.

---

## 3.3 Tujuan Portofolio

Proyek ini juga ditujukan sebagai portofolio yang menunjukkan kemampuan dalam:

- Data Analysis
- Data Visualization
- Feature Engineering
- Forecasting
- Machine Learning
- Dokumentasi teknis
- Pengembangan proyek secara terstruktur

---

# 4. Ruang Lingkup Proyek

Ruang lingkup proyek mencakup seluruh proses pengembangan model forecasting dari awal hingga akhir.

Tahapan yang termasuk dalam ruang lingkup proyek adalah:

- Memahami dataset.
- Melakukan Exploratory Data Analysis.
- Membersihkan data.
- Melakukan Feature Engineering.
- Menganalisis karakteristik time series.
- Membangun model baseline.
- Membangun model Machine Learning.
- Mengevaluasi model.
- Mendokumentasikan hasil eksperimen.
- Menyiapkan dashboard sederhana untuk visualisasi hasil prediksi.

---

Yang tidak termasuk dalam ruang lingkup proyek ini adalah:

- Pengumpulan data baru.
- Pengembangan sistem real-time.
- Integrasi IoT.
- Optimasi skala produksi.
- Deployment cloud production.

---

# 5. Deliverables

Pada akhir proyek diharapkan dihasilkan beberapa artefak berikut.

## Dokumentasi

- README.md
- PRD.md
- Data Dictionary
- Experiment Plan
- Model Report
- Roadmap

---

## Notebook

- Data Understanding
- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Modeling
- Evaluation

---

## Model

- Baseline Model
- Machine Learning Model
- Model terbaik

---

## Visualisasi

- Grafik eksplorasi data
- Grafik prediksi
- Grafik evaluasi
- Perbandingan model

---

## Dashboard

Dashboard sederhana yang mampu:

- Menampilkan hasil prediksi
- Menampilkan grafik historis
- Menampilkan performa model
- Menampilkan insight utama

---

# 6. Definisi Keberhasilan Proyek

Sebuah proyek dinyatakan selesai apabila seluruh kondisi berikut telah terpenuhi.

## Dokumentasi

- Seluruh dokumen telah selesai ditulis.
- Seluruh notebook memiliki penjelasan yang jelas.
- Seluruh eksperimen terdokumentasi.

---

## Data

- Dataset dipahami dengan baik.
- Tidak terdapat masalah kualitas data yang belum ditangani.

---

## Model

Minimal terdapat beberapa model yang berhasil dibandingkan.

Contoh:

- Naive Forecast
- Linear Regression
- Random Forest
- XGBoost

Model terbaik dipilih berdasarkan metrik evaluasi yang telah ditentukan.

---

## Visualisasi

Visualisasi mampu menjelaskan:

- distribusi data
- pola historis
- hasil prediksi
- performa model

---

## Dashboard

Dashboard mampu digunakan untuk menampilkan hasil forecasting secara interaktif.

---

**Catatan**

Dokumen ini merupakan acuan utama selama pengembangan proyek berlangsung. Seluruh perubahan terhadap ruang lingkup, tujuan, maupun metode pengembangan harus diperbarui pada dokumen ini agar dokumentasi tetap konsisten dan dapat dijadikan referensi pada tahap implementasi maupun evaluasi proyek.

---

# 7. Business Understanding

## 7.1 Gambaran Umum

Layanan Bike Sharing merupakan salah satu bentuk transportasi publik yang memungkinkan masyarakat menyewa sepeda dalam periode waktu tertentu.

Jumlah penyewaan sepeda tidak selalu konstan pada setiap waktu. Permintaan dapat berubah karena berbagai faktor seperti:

- Jam dalam sehari
- Hari kerja atau hari libur
- Musim
- Kondisi cuaca
- Suhu udara
- Kecepatan angin
- Tingkat kelembapan

Perubahan permintaan tersebut menyebabkan penyedia layanan perlu memperkirakan jumlah penyewaan yang akan terjadi pada periode berikutnya agar dapat melakukan perencanaan operasional secara lebih efektif.

Forecasting menjadi solusi yang dapat membantu proses tersebut dengan memanfaatkan data historis.

---

## 7.2 Business Problem

Tanpa adanya sistem forecasting, pengelola layanan memiliki beberapa kendala.

### Permasalahan Operasional

- Sulit menentukan jumlah sepeda yang harus tersedia.
- Sulit mengatur distribusi sepeda antar stasiun.
- Sulit mengantisipasi lonjakan permintaan.

### Permasalahan Efisiensi

- Terjadi kekurangan sepeda pada jam sibuk.
- Terjadi kelebihan sepeda pada jam sepi.
- Distribusi sumber daya menjadi tidak optimal.

### Permasalahan Analisis

Belum diketahui secara pasti faktor-faktor apa saja yang memiliki pengaruh paling besar terhadap jumlah penyewaan.

---

## 7.3 Business Objective

Melakukan prediksi jumlah penyewaan sepeda pada periode waktu berikutnya berdasarkan data historis serta variabel pendukung.

Selain menghasilkan prediksi, proyek ini juga bertujuan menghasilkan insight mengenai perilaku penyewaan sepeda.

---

## 7.4 Analytical Questions

Selama proses pengembangan, beberapa pertanyaan berikut harus dapat dijawab.

### Mengenai Data

- Bagaimana distribusi jumlah penyewaan?
- Bagaimana distribusi setiap fitur?
- Apakah terdapat missing value?
- Apakah terdapat outlier?
- Apakah terdapat data yang tidak konsisten?

---

### Mengenai Waktu

- Jam berapa penyewaan paling tinggi?
- Jam berapa penyewaan paling rendah?
- Apakah terdapat pola harian?
- Apakah terdapat pola mingguan?
- Apakah terdapat pola musiman?

---

### Mengenai Cuaca

- Apakah suhu memengaruhi jumlah penyewaan?
- Apakah kelembapan memengaruhi penyewaan?
- Bagaimana pengaruh hujan?
- Bagaimana pengaruh kecepatan angin?

---

### Mengenai Model

- Model apa yang memberikan hasil terbaik?
- Apakah Feature Engineering meningkatkan performa model?
- Bagaimana performa model dibandingkan baseline?

Seluruh pertanyaan tersebut harus dijawab melalui proses analisis data maupun evaluasi model.

---

# 8. Dataset Understanding

## 8.1 Dataset

Dataset yang digunakan merupakan Bike Sharing Dataset.

Dataset ini berisi informasi historis mengenai penyewaan sepeda beserta berbagai variabel pendukung yang memengaruhi jumlah penyewaan.

Dataset terdiri atas dua file utama.

- day.csv
- hour.csv

Pada proyek ini digunakan file:

> hour.csv

karena memiliki resolusi waktu yang lebih tinggi sehingga lebih sesuai untuk pembelajaran forecasting.

---

## 8.2 Target Prediksi

Target utama dalam proyek ini adalah:

```
cnt
```

Kolom tersebut merepresentasikan total jumlah sepeda yang disewa pada setiap jam.

Target inilah yang akan diprediksi oleh seluruh model.

---

## 8.3 Karakteristik Dataset

Dataset termasuk kategori:

- Multivariate Time Series
- Supervised Learning
- Regression Problem

Karakteristik utama dataset:

- Memiliki data historis
- Memiliki fitur numerik
- Memiliki fitur kategorikal
- Memiliki variabel cuaca
- Memiliki informasi waktu

Karakteristik tersebut membuat dataset sangat cocok digunakan untuk pembelajaran forecasting.

---

## 8.4 Asumsi Data

Selama proyek berlangsung digunakan beberapa asumsi berikut.

- Dataset dianggap valid.
- Timestamp dianggap benar.
- Tidak terdapat manipulasi data.
- Seluruh observasi dianggap independen terhadap kesalahan pencatatan.

Apabila ditemukan anomali selama proses eksplorasi maka asumsi tersebut dapat diperbarui.

---

# 9. Metodologi Pengembangan

Metodologi yang digunakan pada proyek ini mengacu pada pendekatan CRISP-DM (Cross Industry Standard Process for Data Mining).

Tahapan yang akan dilakukan meliputi:

```
Business Understanding

↓

Data Understanding

↓

Data Preparation

↓

Exploratory Data Analysis

↓

Feature Engineering

↓

Time Series Analysis

↓

Modeling

↓

Evaluation

↓

Interpretation

↓

Deployment
```

Setiap tahapan harus diselesaikan secara berurutan agar kualitas analisis tetap terjaga.

---

# 10. Standar Pengembangan

Selama proyek berlangsung seluruh proses harus mengikuti standar berikut.

## 10.1 Reproducibility

Seluruh notebook harus dapat dijalankan ulang tanpa menghasilkan error.

Notebook tidak boleh bergantung pada variabel yang berasal dari notebook lain.

---

## 10.2 Dokumentasi

Setiap notebook wajib memiliki:

- Judul
- Tujuan
- Input
- Output
- Kesimpulan

Setiap visualisasi wajib diberikan interpretasi.

Tidak diperbolehkan hanya menampilkan grafik tanpa penjelasan.

---

## 10.3 Eksperimen

Setiap eksperimen wajib memiliki:

- Tujuan
- Dataset
- Parameter
- Hasil
- Insight
- Kesimpulan

Tidak diperbolehkan melakukan eksperimen tanpa dokumentasi.

---

## 10.4 Visualisasi

Setiap visualisasi harus mampu menjawab pertanyaan analitis.

Visualisasi yang dibuat hanya untuk mempercantik notebook tidak diperbolehkan.

---

## 10.5 Versioning

Seluruh perubahan signifikan terhadap notebook maupun model harus dicatat pada dokumen Model Report atau Experiment Plan.

Dengan demikian seluruh perkembangan proyek dapat ditelusuri kembali.

---

# 11. Arsitektur Proyek

## 11.1 Gambaran Umum

Proyek ini dikembangkan menggunakan pendekatan modular.

Setiap tahapan pengembangan dipisahkan berdasarkan tanggung jawabnya sehingga proses analisis menjadi lebih terstruktur, mudah dipelihara, serta dapat direproduksi.

Alur utama proyek ditunjukkan sebagai berikut.

```
Dataset

↓

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

Model Training

↓

Model Evaluation

↓

Dashboard

↓

Deployment
```

Setiap tahapan menghasilkan artefak yang akan digunakan pada tahapan berikutnya.

Dengan pendekatan ini seluruh proses dapat dilacak kembali apabila terjadi perubahan maupun kesalahan pada salah satu tahap.

---

# 12. Struktur Proyek

Struktur direktori proyek ditetapkan sebagai berikut.

```text
project-bike-sharing/

│

├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── src/
│
├── reports/
│
├── dashboard/
│
├── models/
│
├── requirements.txt
│
└── README.md
```

Seluruh anggota proyek maupun AI Agent wajib mengikuti struktur ini.

Perubahan struktur direktori harus dilakukan secara konsisten pada seluruh dokumentasi.

---

# 13. Penjelasan Struktur Folder

## data/

Folder ini digunakan untuk menyimpan seluruh dataset.

Folder dibagi menjadi dua bagian.

### raw/

Berisi dataset asli.

Data pada folder ini **tidak boleh diubah**.

Dataset asli berfungsi sebagai sumber data utama apabila diperlukan proses preprocessing ulang.

---

### processed/

Berisi dataset hasil preprocessing.

Contoh:

- bike_clean.csv
- bike_feature.csv

Seluruh notebook setelah tahap preprocessing wajib menggunakan dataset pada folder ini.

---

## notebooks/

Berisi notebook utama proyek.

Notebook digunakan untuk proses eksplorasi, analisis, eksperimen, serta dokumentasi.

Notebook bukan merupakan tempat penyimpanan fungsi yang digunakan berulang kali.

---

## src/

Folder src digunakan untuk menyimpan seluruh source code yang dapat digunakan kembali.

Contoh:

- preprocessing
- visualisasi
- feature engineering
- evaluasi
- utilities

Seluruh fungsi yang digunakan lebih dari satu kali sebaiknya dipindahkan ke folder ini.

---

## models/

Folder ini digunakan untuk menyimpan model yang telah selesai dilatih.

Contoh isi folder:

- linear_regression.pkl
- random_forest.pkl
- xgboost.json

Model pada folder ini akan digunakan kembali pada proses evaluasi maupun deployment.

---

## reports/

Berisi hasil analisis.

Contohnya:

- gambar
- tabel
- confusion matrix
- grafik
- hasil evaluasi

Folder ini bertujuan memisahkan hasil analisis dengan source code.

---

## dashboard/

Berisi source code dashboard.

Dashboard merupakan aplikasi sederhana yang digunakan untuk menampilkan hasil forecasting.

Dashboard tidak melakukan proses training model.

Dashboard hanya menggunakan model yang telah tersedia.

---

# 14. Standar Notebook

Seluruh notebook wajib mengikuti struktur berikut.

```
Judul

↓

Tujuan

↓

Import Library

↓

Load Dataset

↓

Proses Analisis

↓

Insight

↓

Kesimpulan
```

Notebook tidak diperbolehkan langsung berisi kode tanpa penjelasan.

---

## 14.1 Tujuan Notebook

Setiap notebook hanya memiliki **satu tujuan utama**.

Contoh.

Notebook EDA.

Tujuan:

Memahami karakteristik dataset.

Notebook Preprocessing.

Tujuan:

Membersihkan data serta menghasilkan dataset siap modeling.

Notebook Modeling.

Tujuan:

Melatih dan membandingkan beberapa model forecasting.

Dengan demikian setiap notebook memiliki tanggung jawab yang jelas.

---

## 14.2 Standar Penulisan

Notebook harus mudah dibaca oleh orang lain.

Beberapa aturan yang harus dipenuhi.

- Menggunakan Markdown sebagai penjelasan.
- Memberikan komentar pada proses penting.
- Menjelaskan alasan setiap keputusan.
- Menjelaskan hasil setiap visualisasi.

Notebook yang hanya berisi kode dianggap belum memenuhi standar dokumentasi proyek.

---

# 15. Pipeline Data

Pipeline data yang digunakan pada proyek ini adalah sebagai berikut.

```
Raw Dataset

↓

Validasi Dataset

↓

Exploratory Data Analysis

↓

Data Cleaning

↓

Feature Engineering

↓

Processed Dataset
```

Output utama dari pipeline ini adalah dataset siap digunakan untuk proses modeling.

Dataset hasil preprocessing disimpan pada folder:

```
data/processed/
```

Seluruh proses modeling wajib menggunakan dataset tersebut.
---

# 16. Pipeline Modeling

Tahapan modeling merupakan proses pembangunan model forecasting berdasarkan dataset hasil preprocessing.

Model dibangun secara bertahap, dimulai dari model paling sederhana hingga model yang lebih kompleks.

Pendekatan bertahap ini bertujuan agar performa setiap model dapat dibandingkan secara objektif.

Pipeline modeling ditetapkan sebagai berikut.

```
Processed Dataset

↓

Train-Test Split

↓

Baseline Model

↓

Machine Learning Model

↓

Hyperparameter Tuning

↓

Model Evaluation

↓

Model Comparison

↓

Best Model

↓

Model Saving
```

Seluruh model yang telah selesai dilatih wajib disimpan pada folder:

```
models/
```

---

## 16.1 Filosofi Pengembangan Model

Model tidak dibangun untuk memperoleh akurasi tertinggi semata.

Setiap model harus mampu menjawab pertanyaan berikut.

- Mengapa model ini dipilih?
- Apa kelebihan model ini?
- Apa kekurangan model ini?
- Dalam kondisi apa model bekerja dengan baik?
- Dalam kondisi apa model gagal melakukan prediksi?

Pendekatan ini bertujuan membangun pemahaman terhadap model, bukan sekadar memperoleh nilai evaluasi terbaik.

---

## 16.2 Urutan Pengembangan Model

Pengembangan model dilakukan secara bertahap.

Tahap pertama.

Model baseline.

Contoh:

- Naive Forecast
- Moving Average

Tahap kedua.

Model Machine Learning.

Contoh:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

Tahap ketiga.

Model Deep Learning (Opsional)

Contoh:

- LSTM
- GRU

Model Deep Learning hanya dikembangkan apabila model Machine Learning belum memberikan performa yang memadai.

---

# 17. Pipeline Evaluasi

Evaluasi dilakukan setelah seluruh model selesai dibangun.

Pipeline evaluasi ditetapkan sebagai berikut.

```
Prediction

↓

Evaluation Metrics

↓

Visual Comparison

↓

Residual Analysis

↓

Model Comparison

↓

Best Model Selection
```

Evaluasi tidak hanya dilakukan berdasarkan angka.

Visualisasi hasil prediksi juga harus digunakan untuk melihat perilaku model.

---

## 17.1 Metrik Evaluasi

Minimal metrik yang digunakan adalah.

- MAE
- RMSE
- MAPE

Apabila diperlukan dapat ditambahkan metrik lain yang sesuai.

Seluruh model wajib menggunakan metrik evaluasi yang sama.

Dengan demikian hasil evaluasi dapat dibandingkan secara adil.

---

## 17.2 Analisis Error

Selain menghitung metrik evaluasi, proyek juga harus melakukan analisis terhadap error prediksi.

Hal-hal yang perlu dianalisis antara lain.

- Kapan error terbesar terjadi.
- Faktor apa yang menyebabkan error tinggi.
- Apakah model gagal pada jam tertentu.
- Apakah model gagal pada kondisi cuaca tertentu.

Analisis error bertujuan memahami keterbatasan model.

---

# 18. Standar Eksperimen

Seluruh eksperimen harus mengikuti format yang sama.

Minimal terdiri dari.

- Nama eksperimen
- Tujuan
- Dataset yang digunakan
- Model yang digunakan
- Parameter
- Hasil
- Insight
- Kesimpulan

Eksperimen tanpa dokumentasi dianggap tidak valid.

---

## Contoh Format

```
Nama Eksperimen

Tujuan

Dataset

Model

Parameter

Evaluation

Insight

Kesimpulan
```

---

# 19. Acceptance Criteria

Setiap tahapan proyek memiliki indikator keberhasilan.

## 19.1 Data Understanding

Selesai apabila.

- Dataset berhasil dimuat.
- Struktur dataset dipahami.
- Seluruh fitur telah diidentifikasi.
- Target prediksi telah ditentukan.

---

## 19.2 Exploratory Data Analysis

Selesai apabila.

- Distribusi data dianalisis.
- Missing value dianalisis.
- Outlier dianalisis.
- Korelasi dianalisis.
- Insight dituliskan.

---

## 19.3 Data Cleaning

Selesai apabila.

- Dataset bebas dari masalah kualitas data yang signifikan.
- Dataset hasil preprocessing berhasil disimpan.

---

## 19.4 Feature Engineering

Selesai apabila.

- Seluruh fitur baru telah dibuat.
- Alasan pembuatan fitur dijelaskan.
- Dataset hasil feature engineering berhasil disimpan.

---

## 19.5 Modeling

Selesai apabila.

- Minimal dua model berhasil dilatih.
- Seluruh model berhasil menghasilkan prediksi.
- Model berhasil disimpan.

---

## 19.6 Evaluation

Selesai apabila.

- Seluruh model dibandingkan.
- Grafik evaluasi dibuat.
- Model terbaik dipilih.

---

## 19.7 Dashboard

Selesai apabila dashboard mampu.

- Menampilkan grafik historis.
- Menampilkan hasil prediksi.
- Menampilkan informasi model.
- Menampilkan insight utama.

---

# 20. Milestone Proyek

Pengembangan proyek dibagi menjadi beberapa sprint.

| Sprint | Fokus |
|---------|------|
| Sprint 1 | Project Setup |
| Sprint 2 | Data Understanding |
| Sprint 3 | Exploratory Data Analysis |
| Sprint 4 | Data Cleaning |
| Sprint 5 | Feature Engineering |
| Sprint 6 | Time Series Analysis |
| Sprint 7 | Modeling |
| Sprint 8 | Evaluation |
| Sprint 9 | Dashboard |
| Sprint 10 | Final Documentation |

Setiap sprint harus menghasilkan deliverable yang dapat digunakan pada sprint berikutnya.

---

# 21. Engineering Principles

Seluruh proses pengembangan proyek ForecastLab harus mengikuti prinsip-prinsip berikut.

Prinsip ini bertujuan menjaga kualitas analisis, meningkatkan reproducibility, serta memastikan seluruh keputusan teknis memiliki dasar yang jelas.

---

## 21.1 Data Driven Decision

Seluruh keputusan harus didasarkan pada data.

Tidak diperbolehkan mengambil keputusan berdasarkan asumsi pribadi tanpa didukung hasil analisis.

Contoh:

✓ Menghapus outlier karena telah dianalisis.

✗ Menghapus outlier hanya karena terlihat aneh.

---

## 21.2 Explain Before Predict

Sebelum membangun model, dataset harus dipahami terlebih dahulu.

Tahapan berikut wajib dilakukan sebelum modeling.

- Memahami karakteristik dataset.
- Mengetahui distribusi data.
- Mengetahui hubungan antar fitur.
- Menemukan pola data.
- Menemukan potensi masalah data.

Modeling tanpa memahami data dianggap belum memenuhi standar proyek.

---

## 21.3 Simple First

Pengembangan model dilakukan dari model paling sederhana menuju model yang lebih kompleks.

Urutan pengembangan yang disarankan.

Naive Forecast

↓

Moving Average

↓

Linear Regression

↓

Random Forest

↓

Gradient Boosting

↓

XGBoost

↓

Deep Learning

Pendekatan ini bertujuan memastikan peningkatan performa benar-benar berasal dari kompleksitas model, bukan sekadar penggunaan algoritma yang lebih canggih.

---

## 21.4 Reproducibility

Seluruh eksperimen harus dapat dijalankan ulang.

Notebook tidak boleh bergantung pada state notebook sebelumnya.

Dataset yang digunakan harus jelas.

Parameter model harus dicatat.

Random seed harus ditentukan apabila memungkinkan.

---

## 21.5 Documentation First

Seluruh proses penting wajib didokumentasikan.

Minimal meliputi.

- alasan keputusan
- perubahan preprocessing
- perubahan fitur
- perubahan parameter
- hasil eksperimen

Dokumentasi merupakan bagian dari deliverable proyek.

---

## 21.6 One Notebook One Responsibility

Setiap notebook hanya memiliki satu tujuan utama.

Contoh.

01_data_understanding.ipynb

↓

Memahami dataset.

02_preprocessing.ipynb

↓

Membersihkan data.

03_modeling.ipynb

↓

Melatih model.

Notebook tidak diperbolehkan memiliki terlalu banyak tanggung jawab.

---

## 21.7 Every Visualization Must Answer a Question

Visualisasi tidak dibuat hanya untuk mempercantik notebook.

Setiap visualisasi harus mampu menjawab pertanyaan analitis.

Contoh.

Jam berapa penyewaan tertinggi?

Bagaimana pengaruh suhu?

Bagaimana distribusi target?

Apabila visualisasi tidak memberikan insight baru maka visualisasi tersebut sebaiknya tidak dibuat.

---

## 21.8 Every Model Must Be Explainable

Setiap model harus dijelaskan.

Minimal meliputi.

- alasan pemilihan
- kelebihan
- kekurangan
- performa
- interpretasi hasil

Model bukan sekadar menghasilkan angka evaluasi.

---

# 22. Coding Convention

Seluruh source code harus mengikuti standar berikut.

---

## Penamaan File

Gunakan snake_case.

Contoh.

```
feature_engineering.py

train_model.py

evaluation.py
```

---

## Penamaan Notebook

Gunakan format.

```
01_data_understanding.ipynb

02_eda.ipynb

03_preprocessing.ipynb

04_feature_engineering.ipynb

05_modeling.ipynb

06_evaluation.ipynb
```

---

## Penamaan Variabel

Gunakan nama yang deskriptif.

Contoh.

```
bike_data

processed_data

prediction_result

evaluation_metrics
```

Hindari penggunaan nama seperti.

```
x

abc

temp1

data123
```

---

## Komentar

Komentar hanya digunakan untuk menjelaskan proses yang kompleks.

Komentar tidak digunakan untuk menjelaskan kode yang sudah jelas.

---

## Markdown

Setiap notebook wajib menggunakan Markdown.

Markdown minimal menjelaskan.

- tujuan
- proses
- hasil
- insight

---

# 23. Git Workflow

Seluruh perubahan proyek dikelola menggunakan Git.

Struktur branch yang disarankan.

```
main

↓

develop

↓

feature/*
```

Contoh.

```
feature/eda

feature/preprocessing

feature/modeling

feature/dashboard
```

Commit message disarankan menggunakan format.

```
feat:

fix:

docs:

refactor:

experiment:
```

Contoh.

```
feat: menambahkan feature engineering

docs: memperbarui PRD

experiment: random forest baseline
```

---

# 24. Future Improvement

Setelah proyek selesai, beberapa pengembangan berikut dapat dilakukan.

## Pengembangan Dataset

- Menggunakan dataset yang lebih besar.
- Menggunakan data multi tahun.
- Menggunakan data real-time.

---

## Pengembangan Model

- Hyperparameter Tuning.
- Ensemble Learning.
- LSTM.
- GRU.
- Transformer.

---

## Pengembangan Dashboard

- Dashboard interaktif.
- Upload dataset.
- Live prediction.
- Monitoring model.

---

## Pengembangan Deployment

- REST API.
- Docker.
- Cloud Deployment.
- CI/CD Pipeline.

---

# 25. Checklist Penyelesaian Proyek

## Dokumentasi

- [ ] README selesai
- [ ] PRD selesai
- [ ] Data Dictionary selesai
- [ ] Experiment Plan selesai
- [ ] Model Report selesai

---

## Data

- [ ] Dataset dipahami
- [ ] Missing value dianalisis
- [ ] Outlier dianalisis
- [ ] Dataset dibersihkan

---

## Feature Engineering

- [ ] Fitur baru dibuat
- [ ] Dataset diproses
- [ ] Dataset disimpan

---

## Modeling

- [ ] Baseline selesai
- [ ] Machine Learning selesai
- [ ] Model terbaik dipilih

---

## Evaluation

- [ ] Seluruh metrik dihitung
- [ ] Grafik evaluasi dibuat
- [ ] Insight ditulis

---

## Dashboard

- [ ] Dashboard selesai
- [ ] Model berhasil digunakan
- [ ] Visualisasi lengkap

---

## Dokumentasi Akhir

- [ ] Seluruh notebook lengkap
- [ ] Seluruh gambar tersimpan
- [ ] Repository siap dipublikasikan

---

# Penutup

Dokumen Product Requirements Document (PRD) ini menjadi acuan utama dalam pelaksanaan proyek **FL-001 Bike Sharing Demand Forecasting**.

Seluruh tahapan pengembangan, mulai dari analisis data hingga deployment, harus mengacu pada standar, ruang lingkup, dan prinsip yang telah ditetapkan pada dokumen ini.

Apabila terjadi perubahan kebutuhan selama proses pengembangan, pembaruan harus dilakukan pada dokumen ini agar tetap menjadi sumber referensi yang konsisten bagi seluruh proses implementasi maupun dokumentasi proyek.

Dengan adanya PRD ini diharapkan proyek tidak hanya menghasilkan model forecasting yang baik, tetapi juga menghasilkan proses kerja yang sistematis, terdokumentasi, dapat direproduksi, dan siap dijadikan portofolio profesional.