# DUA UNRI 🎓

> **Capstone Project — Praktikum Algoritma Pemrograman & Struktur Data**
> Universitas Riau (UNRI) - Kelompok 2

DUA UNRI adalah aplikasi simulasi Sistem Informasi Akademik berbasis terminal (CLI) yang dibangun menggunakan Python. Proyek ini tidak hanya berfokus pada fungsionalitas sistem akademik dasar, tetapi juga mendemonstrasikan pemahaman mendalam tentang implementasi berbagai **Struktur Data dan Algoritma** secara manual (tanpa *library* eksternal) sesuai dengan rubrik penilaian praktikum.

---

## 🚀 Fitur Utama

- **Manajemen Mahasiswa**: CRUD data mahasiswa dengan pencarian (Linear/Binary) dan pengurutan (Sorting).
- **Manajemen Mata Kuliah**: CRUD data mata kuliah dan visualisasi prasyarat matkul menggunakan graf.
- **Sistem KRS**: Pengajuan KRS, antrian pemrosesan KRS, dan validasi duplikasi.
- **Penilaian & Kalkulasi IPK**: Input nilai, histori nilai, dan perhitungan IPK mahasiswa secara otomatis menggunakan rekursi.
- **Activity Log**: Pencatatan riwayat aktivitas operasional dalam sistem (Undo/History).
- **Struktur Akademik**: Representasi hierarki Fakultas → Prodi → Mahasiswa.

---

## 📖 Instruksi Penggunaan (Panduan Menu)

Karena aplikasi ini berbasis CLI (Terminal), navigasi dilakukan dengan memasukkan angka sesuai menu yang ditampilkan. Sistem menggunakan **single-role admin** yang memiliki akses ke seluruh fitur.

### 1. Menu Utama
Saat aplikasi dijalankan, Anda akan disambut dengan daftar menu berikut:
- `1` Manajemen Mahasiswa
- `2` Manajemen Mata Kuliah
- `3` KRS (Kartu Rencana Studi)
- `4` Penilaian & Nilai
- `5` Laporan & Statistik
- `6` Struktur Akademik (Fakultas/Prodi - Tree)
- `7` Prasyarat Matkul (Graph)
- `8` Activity Log (Aktivitas Terakhir - Stack)
- `0` Keluar

### 2. Skenario Penggunaan Umum
- **Menambahkan Mahasiswa Baru**: 
  Pilih menu `1` (Manajemen Mahasiswa) ➔ Pilih `Tambah Mahasiswa` ➔ Masukkan NIM, Nama, dan Prodi. *(Data akan disimpan menggunakan Hash Table dan aksi ini dicatat di Activity Log).*
- **Mendaftarkan KRS Mahasiswa**: 
  1. Pengajuan: Pilih menu `3` (KRS) ➔ `Ajukan KRS` ➔ Masukkan NIM. Mahasiswa akan masuk ke dalam **Antrian (Queue)**.
  2. Pemrosesan: Pilih `Proses Antrian KRS` (Dequeue). Sistem akan mengeluarkan antrian teratas, lalu Anda bisa memilih mata kuliah untuk di-enroll. *(Sistem mengecek duplikasi menggunakan Set dan menyimpan daftar matkul ke dalam Single Linked List).*
- **Menginput Nilai & Melihat IPK**: 
  Pilih menu `4` (Penilaian) ➔ `Input Nilai` ➔ Pilih mahasiswa & matkul ➔ Masukkan nilai. Untuk melihat hasil, pilih `Hitung IPK` *(dihitung otomatis menggunakan fungsi Rekursif)*. Histori nilai dari semester ke semester dapat dinavigasikan menggunakan *Double Linked List*.
- **Melihat Riwayat Operasi (Log)**: 
  Pilih menu `8` (Activity Log) untuk melihat urutan aktivitas terakhir yang Anda lakukan dalam sistem (disajikan dari yang paling baru menggunakan prinsip LIFO - *Stack*).

---

## 🧠 Implementasi Struktur Data (DS & Algo)

Sesuai dengan *Product Requirements Document* (PRD), proyek ini mengimplementasikan struktur data berikut dari awal di dalam direktori `structures/`:

- **Hash Table**: *Lookup* cepat data mahasiswa berdasarkan NIM (O(1)).
- **Linked List** (Single, Double, Circular): Digunakan untuk daftar matkul KRS (Single), navigasi riwayat nilai (Double), dan rotasi menu/carousel (Circular).
- **Stack**: Riwayat aksi / *activity log* (LIFO).
- **Queue**: Antrian pengajuan KRS (FIFO).
- **Tree**: Hierarki struktur akademik (Fakultas → Prodi → Mahasiswa).
- **Graph**: Relasi dan penentuan prasyarat antar mata kuliah.
- **Algoritma**: Sorting manual (untuk mengurutkan nama/IPK), Searching (Linear & Binary search untuk lookup data), dan Rekursif (kalkulasi IPK kumulatif).

---

## 📂 Struktur Direktori

Arsitektur aplikasi dibagi menjadi 4 layer utama (*MVC-like pattern*):

```text
dua_unri/
├── main.py                 # Entry point aplikasi (Jalankan file ini)
├── data/                   # File persistensi berformat JSON (mahasiswa, matkul, krs, nilai)
├── models/                 # Definisi Class entitas/OOP (Mahasiswa, MataKuliah, dll)
├── structures/             # Implementasi Struktur Data manual (Tree, Stack, Queue, dll)
├── services/               # Business logic & orkestrasi (CRUD, logika proses)
└── views/                  # Antarmuka CLI & routing navigasi terminal
```

---

## 🛠️ Cara Menjalankan Aplikasi

**Prasyarat**: Pastikan **Python 3.8+** telah terinstal di perangkat Anda. Proyek ini dibangun murni menggunakan *Standard Library Python*, sehingga tidak memerlukan penginstalan dependensi eksternal via PIP.

1. **Clone repositori**:
   ```bash
   git clone https://github.com/hanifalfa4149-wq/DUA-UNRI.git
   ```
2. **Pindah ke direktori proyek**:
   ```bash
   cd DUA-UNRI
   ```
3. **Jalankan aplikasi utama**:
   ```bash
   python main.py
   ```
4. **Mulai Navigasi**: Ikuti instruksi di layar terminal dengan menginputkan angka menu. Setiap perubahan data akan otomatis tersimpan dalam format JSON di dalam folder `data/`.