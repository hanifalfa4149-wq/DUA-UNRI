# SIAKAD Lite — Product Requirements Document (PRD)

> **Dokumen internal untuk alignment tim & context injection agentic coding**
> Version: 1.0 | Status: Active | Last Updated: Mei 2026

---

## 📌 Metadata Dokumen

| Field | Detail |
|---|---|
| **Nama Project** | SIAKAD Lite |
| **Tipe** | Capstone Project — Praktikum Algoritma Pemrograman & Struktur Data |
| **Platform** | CLI (Terminal-based), Python |
| **Tim** | Kelompok (struktur ketua + anggota) |
| **Institusi** | UNRI (Universitas Riau) |
| **Semester** | Aktif |

---

## 1. Overview

### 1.1 Deskripsi Produk

SIAKAD Lite adalah aplikasi simulasi sistem informasi akademik berbasis terminal (CLI) yang dibangun menggunakan Python, mencakup alur akademik dasar seperti manajemen mahasiswa, mata kuliah, KRS, dan penilaian — dengan seluruh fiturnya diimplementasikan langsung menggunakan struktur data dan algoritma seperti linked list, stack, queue, tree, graph, dan hash table.

### 1.2 Latar Belakang

Project ini merupakan capstone dari mata kuliah Algoritma Pemrograman dan Struktur Data. Tujuannya bukan sekadar membangun software fungsional, melainkan **mendemonstrasikan pemahaman mendalam** terhadap implementasi struktur data dan algoritma dalam konteks sistem nyata. SIAKAD dipilih sebagai domain karena relevan, familiar, dan memiliki kompleksitas yang cukup untuk mencakup seluruh materi perkuliahan.

### 1.3 Pendekatan Teknis

- **Bahasa**: Python 3.x
- **Interface**: CLI (Command Line Interface) — terminal-based
- **Storage**: File-based (JSON)
- **Paradigma**: OOP (Object-Oriented Programming)
- **Struktur Data**: Implementasi manual (bukan library bawaan Python)

---

## 2. Goals & Success Metrics

### 2.1 Primary Goal

Membangun sistem SIAKAD sederhana yang **fully functional di terminal**, di mana setiap fitur utama secara eksplisit menggunakan dan mendemonstrasikan implementasi struktur data serta algoritma yang telah dipelajari.

### 2.2 Success Metrics — Rubrik Penilaian Kelompok (Total: 100)

| No | Kriteria | Bobot | Target Implementasi |
|---|---|---|---|
| 1 | Program berjalan tanpa error dan warning | +5 | Semua module ditest, input validation ketat |
| 2 | Program berjalan benar di semua kondisi | +10 | Edge case handling, validasi tiap flow |
| 3 | Komentar dalam program | +5 | Docstring + inline comment di semua fungsi krusial |
| 4 | Kerapian program dan output | +5 | Menu CLI terstruktur, output formatted rapi |
| 5 | Kompleksitas proyek | +10 | 3 layer arsitektur: model, logic, struktur data |
| 6.1 | Sorting | +5 | Implementasi manual (bubble/merge/insertion) |
| 6.2 | File Handler | +5 | Read/write JSON untuk semua entitas |
| 6.3 | Searching | +5 | Linear search & binary search manual |
| 6.4 | Rekursif | +5 | Min. 1 fungsi rekursif meaningful |
| 6.5 | List, Tuple, Set, Dictionary | +5 | Digunakan dalam konteks yang tepat |
| 6.6 | Stack / Queue | +5 | Stack untuk log, Queue untuk antrian KRS |
| 6.7 | OOP | +5 | Class untuk semua entitas utama |
| 6.8 | Single Linked List | +5 | List mata kuliah per mahasiswa |
| 6.9 | Double Linked List | +5 | Navigasi riwayat nilai |
| 6.10 | Circular Linked List | +5 | Rotasi menu / carousel data |
| 7.1 | Tree | +5 | Hierarki Fakultas → Prodi → Mahasiswa |
| 7.2 | Graph | +5 | Prasyarat antar mata kuliah |
| 7.3 | Hash Table | +5 | Lookup NIM — implementasi manual |
| | **Total** | **100** | |

### 2.3 Success Metrics — Rubrik Penilaian Individu (Total: 100)

| No | Kriteria | Bobot | Cara Persiapan |
|---|---|---|---|
| 1 | Pemahaman Tiap Materi | +40 | Setiap anggota paham module yang dikerjakannya + bisa jelaskan struktur data yang dipakai |
| 2 | Kontribusi | +20 | Tracked via commit history + pembagian module yang jelas |
| 3 | Manipulasi Kode | +40 | Bisa modify/extend kode saat sesi ujian individu |

---

## 3. Scope

### 3.1 In Scope

- Manajemen data Mahasiswa (CRUD)
- Manajemen data Mata Kuliah (CRUD)
- Sistem KRS — pendaftaran dan antrian
- Sistem Penilaian — input nilai dan kalkulasi IPK
- Implementasi seluruh struktur data yang tercantum di rubrik
- Persistensi data via file JSON
- Activity log berbasis Stack
- Hierarki akademik berbasis Tree
- Graf prasyarat mata kuliah
- Hash Table untuk lookup cepat

### 3.2 Out of Scope

- GUI / web interface
- Autentikasi pengguna (login/logout)
- Integrasi database eksternal (SQL, dll)
- Integrasi PDDikti atau sistem eksternal
- Multi-user / concurrent access
- Fitur keuangan / pembayaran SPP

---

## 4. User & Roles

Karena ini CLI sederhana, sistem menggunakan **single-role admin** yang bisa mengakses semua menu.

| Role | Deskripsi | Akses |
|---|---|---|
| **Admin** | Pengguna utama (operator sistem) | Full access ke semua module |

> *Catatan: Role mahasiswa dan dosen tidak diimplementasikan sebagai login terpisah — data mereka dikelola oleh Admin.*

---

## 5. User Flow

### 5.1 Main Menu Flow

```
[START]
    │
    ▼
Menu Utama
    ├── 1. Manajemen Mahasiswa
    ├── 2. Manajemen Mata Kuliah
    ├── 3. KRS
    ├── 4. Penilaian & Nilai
    ├── 5. Laporan & Statistik
    ├── 6. Struktur Akademik (Tree)
    ├── 7. Prasyarat Matkul (Graph)
    ├── 8. Activity Log (Stack)
    └── 0. Keluar
```

### 5.2 Flow Manajemen Mahasiswa

```
Menu Mahasiswa
    ├── Tambah Mahasiswa      → input NIM, nama, prodi → simpan ke JSON → log ke Stack
    ├── Lihat Semua           → load JSON → tampil sebagai tabel
    ├── Cari Mahasiswa        → input keyword → searching (linear/binary) → tampil hasil
    ├── Sort Mahasiswa        → pilih kriteria (nama/IPK) → sorting manual → tampil
    ├── Edit Mahasiswa        → cari by NIM → update data → simpan
    ├── Hapus Mahasiswa       → cari by NIM → konfirmasi → hapus → simpan
    └── Kembali
```

### 5.3 Flow KRS

```
Menu KRS
    ├── Ajukan KRS            → input NIM → masuk antrian (Queue)
    ├── Proses Antrian KRS    → dequeue → pilih matkul → cek duplikat (Set)
    │                            → enroll → simpan ke Single Linked List mahasiswa
    ├── Lihat KRS Mahasiswa   → input NIM → tampil matkul yang diambil
    └── Kembali
```

### 5.4 Flow Penilaian

```
Menu Penilaian
    ├── Input Nilai           → pilih mahasiswa + matkul → input nilai → simpan
    ├── Hitung IPK            → load nilai → rekursif kalkulasi → tampil
    ├── Riwayat Nilai         → navigasi via Double Linked List (prev/next)
    ├── Sorting Nilai         → sort by nilai tertinggi → tampil ranking
    └── Kembali
```

---

## 6. Data Flow & Proses

### 6.1 Layer Arsitektur

```
┌─────────────────────────────────────────┐
│              views/                      │  ← Input/output terminal, menu navigation
├─────────────────────────────────────────┤
│              services/                   │  ← Business logic, orchestrasi DS + model
├─────────────────────────────────────────┤
│   models/              structures/       │  ← OOP entities | DS implementations
├─────────────────────────────────────────┤
│              data/ (JSON)                │  ← Persistensi file
└─────────────────────────────────────────┘
```

### 6.2 Data Flow — Tambah Mahasiswa

```
User input (views)
    → MahasiswaService.tambah()
        → Mahasiswa(nim, nama, prodi) [models]
        → HashTable.insert(nim, mahasiswa) [structures]
        → Stack.push("ADD: {nim}") [log]
        → FileHandler.save("mahasiswa.json") [data]
    → Tampil konfirmasi (views)
```

### 6.3 Data Flow — Proses KRS

```
User input NIM (views)
    → KRSService.ajukan(nim)
        → Queue.enqueue(nim) [structures]

User trigger proses (views)
    → KRSService.proses()
        → nim = Queue.dequeue()
        → matkul_list = user input
        → Set untuk cek duplikat
        → mahasiswa.krs_list.append(matkul) [Single LL]
        → FileHandler.save("krs.json")
```

### 6.4 Mapping Struktur Data ke Fitur

| Struktur Data | Digunakan Di | Alasan Pemilihan |
|---|---|---|
| **Hash Table** | Lookup mahasiswa by NIM | O(1) average lookup, lebih cepat dari linear search |
| **Single Linked List** | List matkul per mahasiswa (KRS) | Dynamic insert, tidak perlu alokasi tetap |
| **Double Linked List** | Navigasi riwayat nilai | Perlu traversal dua arah (prev/next semester) |
| **Circular Linked List** | Rotasi tampilan menu/data | Loop tanpa end, cocok untuk carousel |
| **Stack** | Activity log / undo history | LIFO — aksi terakhir ditampilkan pertama |
| **Queue** | Antrian pengajuan KRS | FIFO — siapa duluan, diproses duluan |
| **Tree** | Hierarki Fakultas→Prodi→Mhs | Struktur hierarkis natural |
| **Graph** | Prasyarat antar mata kuliah | Relasi antar node yang non-linear |
| **Sorting** | Sort mahasiswa, sort nilai | Demonstrasi algoritma manual |
| **Searching** | Cari mahasiswa, cari matkul | Linear search & binary search |
| **Rekursif** | Hitung IPK kumulatif | Demonstrasi rekursi dalam kalkulasi |
| **List/Tuple/Set/Dict** | Struktur data native Python | Digunakan dalam konteks yang tepat |
| **OOP** | Semua entitas (Mahasiswa, Matkul, dll) | Encapsulation dan reusability |
| **File Handler** | Semua persistensi data | Read/write JSON untuk semua entitas |

---

## 7. Functional Requirements

### 7.1 Module Mahasiswa

| ID | Requirement |
|---|---|
| FR-MHS-01 | Sistem dapat menambah data mahasiswa (NIM, nama, prodi) |
| FR-MHS-02 | Sistem dapat menampilkan semua data mahasiswa |
| FR-MHS-03 | Sistem dapat mencari mahasiswa berdasarkan NIM atau nama |
| FR-MHS-04 | Sistem dapat mengurutkan mahasiswa berdasarkan nama atau IPK |
| FR-MHS-05 | Sistem dapat mengedit dan menghapus data mahasiswa |
| FR-MHS-06 | Data mahasiswa diindeks oleh Hash Table untuk lookup cepat |

### 7.2 Module Mata Kuliah

| ID | Requirement |
|---|---|
| FR-MK-01 | Sistem dapat menambah data mata kuliah (kode, nama, SKS) |
| FR-MK-02 | Sistem dapat menampilkan semua mata kuliah |
| FR-MK-03 | Sistem dapat mencari mata kuliah berdasarkan kode atau nama |
| FR-MK-04 | Sistem dapat mendefinisikan prasyarat antar mata kuliah (Graph) |
| FR-MK-05 | Sistem dapat menampilkan graf prasyarat mata kuliah |

### 7.3 Module KRS

| ID | Requirement |
|---|---|
| FR-KRS-01 | Mahasiswa dapat dimasukkan ke antrian KRS (Queue) |
| FR-KRS-02 | Sistem memproses antrian KRS secara FIFO |
| FR-KRS-03 | Sistem mencegah duplikasi mata kuliah menggunakan Set |
| FR-KRS-04 | Daftar matkul per mahasiswa disimpan dalam Single Linked List |
| FR-KRS-05 | KRS dapat ditampilkan per mahasiswa |

### 7.4 Module Penilaian

| ID | Requirement |
|---|---|
| FR-NIL-01 | Admin dapat menginput nilai per mahasiswa per mata kuliah |
| FR-NIL-02 | Sistem menghitung IPK secara rekursif |
| FR-NIL-03 | Riwayat nilai dapat dinavigasi menggunakan Double Linked List |
| FR-NIL-04 | Nilai dapat diurutkan dari tertinggi ke terendah |

### 7.5 Module Struktur Akademik

| ID | Requirement |
|---|---|
| FR-TREE-01 | Sistem memiliki hierarki Fakultas → Prodi → Mahasiswa berbasis Tree |
| FR-TREE-02 | Tree dapat di-traverse dan ditampilkan di terminal |
| FR-CLL-01 | Circular Linked List digunakan untuk navigasi data secara loop |
| FR-LOG-01 | Setiap aksi CRUD dicatat ke activity log berbasis Stack |
| FR-LOG-02 | Log dapat ditampilkan (LIFO) |

### 7.6 File Handler

| ID | Requirement |
|---|---|
| FR-FILE-01 | Data mahasiswa, matkul, KRS, dan nilai disimpan ke file JSON |
| FR-FILE-02 | Data di-load dari file saat program dijalankan |
| FR-FILE-03 | Data disimpan ke file setiap ada perubahan |

---

## 8. Non-Functional Requirements

| ID | Kategori | Requirement |
|---|---|---|
| NFR-01 | **Reliability** | Program tidak crash untuk semua input valid maupun invalid |
| NFR-02 | **Readability** | Semua fungsi memiliki docstring dan komentar inline di bagian krusial |
| NFR-03 | **Maintainability** | Struktur folder terpisah per layer (models, structures, services, views) |
| NFR-04 | **Portability** | Berjalan di Python 3.8+ tanpa dependency eksternal (pure stdlib) |
| NFR-05 | **Usability** | Menu CLI jelas, ada instruksi singkat di tiap prompt |
| NFR-06 | **Traceability** | Setiap modul struktur data dapat di-demo secara isolated |
| NFR-07 | **Explainability** | Setiap pilihan struktur data terdokumentasi alasannya (untuk ujian individu) |

---

## 9. Folder Structure

```
siakad_lite/
│
├── main.py                       # Entry point — jalankan ini
│
├── data/                         # Persistensi file (File Handler)
│   ├── mahasiswa.json
│   ├── matakuliah.json
│   ├── krs.json
│   └── nilai.json
│
├── models/                       # OOP — definisi class & atribut
│   ├── mahasiswa.py              # class Mahasiswa
│   ├── matakuliah.py             # class MataKuliah
│   ├── krs.py                    # class KRS
│   └── nilai.py                  # class Nilai
│
├── structures/                   # Implementasi struktur data (manual, no library)
│   ├── linked_list.py            # Single, Double, Circular Linked List
│   ├── stack.py                  # Stack — activity log
│   ├── queue.py                  # Queue — antrian KRS
│   ├── tree.py                   # Tree — hierarki akademik
│   ├── graph.py                  # Graph — prasyarat matkul
│   └── hash_table.py             # Hash Table — lookup NIM
│
├── services/                     # Business logic — orkestrasi models + structures
│   ├── mahasiswa_service.py      # CRUD, searching, sorting mahasiswa
│   ├── matkul_service.py         # CRUD matkul, graph prasyarat
│   ├── krs_service.py            # Enroll, queue, cek duplikat
│   ├── nilai_service.py          # Input nilai, hitung IPK rekursif
│   └── log_service.py            # Stack-based activity log
│
└── views/                        # Terminal UI — menu & I/O
    ├── menu_utama.py             # Router menu utama
    ├── menu_mahasiswa.py         # Sub-menu mahasiswa
    ├── menu_matkul.py            # Sub-menu mata kuliah
    ├── menu_krs.py               # Sub-menu KRS
    └── menu_nilai.py             # Sub-menu nilai & IPK
```

---

## 10. Pembagian Tugas Tim (Saran)

> Pembagian ini memastikan setiap anggota punya ownership yang jelas untuk keperluan ujian individu.

| Area | File Utama | Struktur Data Terkait |
|---|---|---|
| **Ketua / Lead** | `main.py`, `views/menu_utama.py`, koordinasi | Semua (oversight) |
| **Anggota 1** | `models/`, `structures/linked_list.py` | Single LL, Double LL, Circular LL, OOP |
| **Anggota 2** | `structures/stack.py`, `structures/queue.py`, `services/log_service.py`, `services/krs_service.py` | Stack, Queue |
| **Anggota 3** | `services/mahasiswa_service.py`, `services/nilai_service.py` | Sorting, Searching, Rekursif |
| **Anggota 4** | `structures/tree.py`, `structures/graph.py`, `structures/hash_table.py` | Tree, Graph, Hash Table |
| **Semua** | `data/` (File Handler), komentar kode | File Handler, List/Tuple/Set/Dict |

---

## 11. Constraints & Assumptions

- Tidak menggunakan library struktur data eksternal (tidak boleh `from collections import deque` untuk Queue, dll) — semua implementasi manual
- Data bersifat persistent antar sesi melalui file JSON
- Input dari user diasumsikan via keyboard (stdin)
- Tidak ada concurrent access — single process, single user
- Struktur data harus bisa di-demo secara isolated saat ujian individu

---

## 12. Glossary

| Term | Definisi |
|---|---|
| **CLI** | Command Line Interface — antarmuka berbasis terminal/teks |
| **CRUD** | Create, Read, Update, Delete |
| **KRS** | Kartu Rencana Studi — form pendaftaran mata kuliah per semester |
| **IPK** | Indeks Prestasi Kumulatif |
| **OOP** | Object-Oriented Programming |
| **DS** | Data Structure / Struktur Data |
| **Single LL** | Single Linked List |
| **Double LL** | Double Linked List |
| **Circular LL** | Circular Linked List |
| **Hash Table** | Struktur data yang menggunakan fungsi hash untuk mapping key→value |
| **Stack** | Struktur data LIFO (Last In First Out) |
| **Queue** | Struktur data FIFO (First In First Out) |
| **Tree** | Struktur data hierarkis non-linear |
| **Graph** | Struktur data berupa node + edge, bisa directed/undirected |
| **Rekursif** | Fungsi yang memanggil dirinya sendiri |
| **Agentic Coding** | Pendekatan coding menggunakan AI agent (Copilot, Claude) secara autonomous |

---

> *Dokumen ini bersifat living document — update sesuai perkembangan implementasi.*
> *Gunakan sebagai context injection saat bekerja dengan GitHub Copilot Agent Mode atau Claude.*
