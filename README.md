# SIAKAD Lite 🎓

> **Capstone Project — Praktikum Algoritma Pemrograman & Struktur Data**
> Universitas Riau (UNRI) - Kelompok 2

SIAKAD Lite adalah aplikasi simulasi Sistem Informasi Akademik berbasis terminal (CLI) yang dibangun menggunakan Python. Proyek ini tidak hanya berfokus pada fungsionalitas sistem akademik dasar, tetapi juga mendemonstrasikan pemahaman mendalam tentang implementasi berbagai **Struktur Data dan Algoritma** secara manual (tanpa *library* bawaan) sesuai dengan rubrik penilaian praktikum.

## 🚀 Fitur Utama

- **Manajemen Mahasiswa**: CRUD data mahasiswa dengan pencarian cepat.
- **Manajemen Mata Kuliah**: CRUD data mata kuliah dan visualisasi prasyarat matkul.
- **Sistem KRS**: Pengajuan dan antrian pemrosesan KRS mahasiswa.
- **Penilaian & Kalkulasi IPK**: Input nilai dan perhitungan IPK mahasiswa secara otomatis.
- **Activity Log**: Pencatatan riwayat aktivitas operasional dalam sistem.
- **Struktur Akademik**: Representasi hierarki Fakultas → Prodi → Mahasiswa.

## 🧠 Implementasi Struktur Data (DS & Algo)

Sesuai dengan *Product Requirements Document* (PRD), proyek ini mengimplementasikan struktur data berikut dari awal di dalam direktori `structures/`:

- **Hash Table**: *Lookup* data mahasiswa berdasarkan NIM (O(1)).
- **Linked List** (Single, Double, Circular): Digunakan untuk list KRS mahasiswa, navigasi riwayat nilai, dan rotasi/carousel menu.
- **Stack**: Riwayat aksi/log aktivitas (LIFO).
- **Queue**: Antrian pengajuan KRS (FIFO).
- **Tree**: Hierarki struktur akademik institusi.
- **Graph**: Relasi dan penentuan prasyarat antar mata kuliah.
- **Algoritma**: Sorting manual (untuk mengurutkan mahasiswa/nilai), Searching (Linear & Binary), serta kalkulasi IPK rekursif.

## 📂 Struktur Direktori

```text
siakad_lite/
├── main.py                 # Entry point aplikasi
├── data/                   # File JSON untuk persistensi data (mahasiswa, matkul, dsb)
├── models/                 # Definisi Class entitas (Mahasiswa, MataKuliah, dll)
├── structures/             # Implementasi Struktur Data manual (Tree, Stack, Queue, dll)
├── services/               # Business logic & orkestrasi model dengan struktur data
└── views/                  # Antarmuka UI Terminal/CLI (Menu)
```

## 🛠️ Cara Menjalankan

1. Pastikan **Python 3.8+** telah terinstal di komputer Anda.
2. Clone repositori ini:
   ```bash
   git clone https://github.com/hanifalfa4149-wq/DUA-UNRI.git
   ```
3. Pindah ke direktori proyek dan jalankan aplikasi:
   ```bash
   cd DUA-UNRI
   python main.py
   ```

*(Catatan: Aplikasi ini berjalan sepenuhnya dengan standar library Python tanpa memerlukan instalasi dependensi eksternal via pip).*
