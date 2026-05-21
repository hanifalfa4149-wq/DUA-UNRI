# SIAKAD Lite — Product Requirements Document (PRD)

> Version: 2.0 | Status: Active | Last Updated: Mei 2026

---

## 1. Overview

SIAKAD Lite adalah simulasi sistem informasi akademik berbasis terminal (CLI) menggunakan Python,
mencakup alur akademik dasar — manajemen mahasiswa, mata kuliah, KRS, dan penilaian —
dengan seluruh fiturnya diimplementasikan langsung menggunakan struktur data dan algoritma
seperti linked list, stack, queue, tree, graph, dan hash table.

**Konteks:** Capstone project mata kuliah Algoritma Pemrograman dan Struktur Data — UNRI.
Fokus utama bukan hanya fungsionalitas, tapi demonstrasi eksplisit setiap struktur data
dan algoritma dalam konteks sistem nyata.

---

## 2. Tech Stack & Constraints

| Field | Detail |
|---|---|
| Language | Python 3.8+, pure stdlib |
| Interface | CLI terminal only |
| Storage | JSON file di folder data/ |
| Paradigma | OOP + implementasi struktur data manual |
| Entry point | `python main.py` tanpa setup tambahan |

**Hard Constraints:**
- DILARANG pakai `collections.deque`, `heapq`, `queue`, atau library DS apapun
- DILARANG pakai `sorted()` atau `.sort()` — sorting harus algoritma manual
- Semua struktur data di `structures/` implementasi class dari scratch
- Tidak ada dependency eksternal selain Python stdlib
- Tidak boleh hardcode path — gunakan `os.path` relative

---

## 3. Folder Structure

```
siakad_lite/
├── main.py              # Entry point, router utama (~30 baris)
├── models.py            # Semua class entitas (~80 baris)
├── algoritma.py         # Sorting, searching, rekursif (~60 baris)
├── services.py          # Semua business logic (~80 baris)
├── views.py             # Semua menu CLI (~80 baris)
├── data/
│   ├── mahasiswa.json
│   ├── matakuliah.json
│   ├── krs.json
│   └── nilai.json
└── structures/
    ├── linked_list.py   # Single, Double, Circular LL (~100 baris)
    ├── stack_queue.py   # Stack + Queue (~70 baris)
    ├── hash_table.py    # Hash Table separate chaining (~50 baris)
    └── tree_graph.py    # Tree + Graph (~80 baris)
```

**Total estimasi: ~630 baris**

---

## 4. Layer Rules

| Layer | Isi | Boleh Import Dari |
|---|---|---|
| `models.py` | Class entitas, serialisasi | — |
| `structures/` | Implementasi DS, generic | — |
| `algoritma.py` | Sorting, searching, rekursif | — |
| `services.py` | Business logic, orkestrasi | models, structures, algoritma |
| `views.py` | Menu CLI, I/O terminal | services |
| `main.py` | Entry point, router | views |

---

## 5. Fitur & User Flow

### 5.1 Manajemen Mahasiswa
- Tambah, lihat, edit, hapus data mahasiswa
- Cari mahasiswa by NIM (binary search) atau nama (linear search)
- Sort tampilan by nama atau IPK

### 5.2 Manajemen Mata Kuliah
- Tambah dan kelola data mata kuliah
- Definisi prasyarat antar mata kuliah via Graph

### 5.3 KRS
- Mahasiswa masuk antrian pengajuan (Queue)
- Diproses FIFO — hasil enroll disimpan ke Single Linked List
- Cek duplikasi matkul menggunakan Set

### 5.4 Penilaian & IPK
- Input nilai tugas, UTS, UAS per mahasiswa per matkul
- Kalkulasi grade dan IPK secara rekursif
- Navigasi riwayat nilai via Double Linked List

### 5.5 Struktur Akademik
- Tampilkan hierarki Fakultas → Prodi → Mahasiswa via Tree

### 5.6 Activity Log
- Semua aksi CRUD tercatat ke Stack
- Ditampilkan LIFO — aktivitas terbaru paling atas

---

## 6. Mapping Struktur Data ke Fitur

| Struktur Data | Fitur | Alasan |
|---|---|---|
| Hash Table | Lookup mahasiswa by NIM | O(1) average, NIM unik |
| Single LL | List matkul per mahasiswa (KRS) | Dynamic insert, ukuran tidak tetap |
| Double LL | Navigasi riwayat nilai | Traversal dua arah (prev/next) |
| Circular LL | Navigasi carousel di views | Loop tanpa end |
| Stack | Activity log | LIFO — aksi terbaru tampil duluan |
| Queue | Antrian KRS | FIFO — siapa duluan diproses duluan |
| Tree | Hierarki Fakultas → Prodi → Mhs | Struktur hierarkis natural |
| Graph | Prasyarat antar matkul | Relasi non-linear antar node |
| Sorting | Sort mahasiswa by nama/IPK | Demonstrasi algoritma manual |
| Searching | Cari by nama / by NIM | Linear untuk nama, binary untuk NIM |
| Rekursif | Kalkulasi IPK kumulatif | Akumulasi nilai lintas semester |

---

## 7. Success Metrics — Rubrik Penilaian

### Kelompok (Total: 100)

| No | Kriteria | Bobot | Implementasi |
|---|---|---|---|
| 1 | Program jalan tanpa error dan warning | +5 | Input validation di `services.py` |
| 2 | Berjalan benar di semua kondisi | +10 | Edge case handling tiap fungsi |
| 3 | Komentar dalam program | +5 | Docstring tiap fungsi + inline comment |
| 4 | Kerapian program dan output | +5 | Output formatted, menu konsisten |
| 5 | Kompleksitas proyek | +10 | Multi-layer, semua DS terimplementasi |
| 6.1 | Sorting | +5 | `algoritma.py` — bubble/insertion sort manual |
| 6.2 | File Handler | +5 | Read/write JSON semua entitas di `services.py` |
| 6.3 | Searching | +5 | `algoritma.py` — linear + binary search |
| 6.4 | Rekursif | +5 | `algoritma.py` — hitung IPK rekursif |
| 6.5 | List, Tuple, Set, Dictionary | +5 | Dipakai di `models.py` dan `services.py` |
| 6.6 | Stack / Queue | +5 | `structures/stack_queue.py` |
| 6.7 | OOP | +5 | `models.py` — semua class entitas |
| 6.8 | Single Linked List | +5 | `structures/linked_list.py` |
| 6.9 | Double Linked List | +5 | `structures/linked_list.py` |
| 6.10 | Circular Linked List | +5 | `structures/linked_list.py` |
| 7.1 | Tree | +5 | `structures/tree_graph.py` |
| 7.2 | Graph | +5 | `structures/tree_graph.py` |
| 7.3 | Hash Table | +5 | `structures/hash_table.py` |
| | **Total** | **100** | |

### Individu (Total: 100)

| No | Kriteria | Bobot | Persiapan |
|---|---|---|---|
| 1 | Pemahaman tiap materi | +40 | Kuasai file ownership + bisa jelaskan DS yang dipakai |
| 2 | Kontribusi | +20 | Tracked via commit history |
| 3 | Manipulasi kode | +40 | Latihan modifikasi on-the-spot tanpa referensi |

---

## 8. Pembagian Ownership Tim

| Anggota | File Utama | DS yang Dikuasai |
|---|---|---|
| Ketua | `main.py`, `views.py`, `algoritma.py`, `services.py` (sorting/searching) | Sorting, Searching, Rekursif, Views |
| Anggota 1 | `structures/linked_list.py`, `structures/stack_queue.py` | Single LL, Double LL, Circular LL, Stack, Queue |
| Anggota 2 | `models.py`, `structures/hash_table.py`, `structures/tree_graph.py` | OOP, File Handler, Hash Table, Tree, Graph |

---

## 9. Glossary

| Term | Definisi |
|---|---|
| CLI | Command Line Interface — antarmuka berbasis terminal |
| CRUD | Create, Read, Update, Delete |
| KRS | Kartu Rencana Studi |
| IPK | Indeks Prestasi Kumulatif |
| DS | Data Structure / Struktur Data |
| LIFO | Last In First Out — sifat Stack |
| FIFO | First In First Out — sifat Queue |
| Separate Chaining | Teknik resolve collision di Hash Table menggunakan linked list per bucket |

---

> Living document — update sesuai perkembangan implementasi.
> Gunakan sebagai context injection saat bekerja dengan GitHub Copilot.