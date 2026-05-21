# SIAKAD Lite — Copilot Instructions

## Project Overview

SIAKAD Lite adalah simulasi sistem informasi akademik berbasis CLI (terminal), Python.
Capstone project mata kuliah Algoritma Pemrograman dan Struktur Data — UNRI.
Fokus: demonstrasi eksplisit struktur data dan algoritma di setiap fitur.

## Folder Structure

siakad_lite/
├── main.py
├── models.py
├── algoritma.py
├── services.py
├── views.py
├── data/
└── structures/
├── linked_list.py
├── stack_queue.py
├── hash_table.py
└── tree_graph.py

## Layer Rules

- models.py → class entitas only, wajib to_dict() dan from_dict()
- structures/ → implementasi DS manual, generic, tidak ada domain logic
- algoritma.py → sorting manual, searching, rekursif — tidak ada I/O
- services.py → semua business logic, orkestrasi DS + models + algoritma
- views.py → I/O terminal dan menu only, tidak ada logic
- main.py → entry point, router ke views

## Hard Constraints — Tidak Boleh Dilanggar

- DILARANG: collections.deque, heapq, queue, atau library DS apapun
- DILARANG: sorted() atau .sort() — sorting harus algoritma manual
- Semua DS di structures/ harus implementasi class dari scratch
- Tidak ada dependency eksternal selain Python stdlib
- Tidak boleh hardcode path — gunakan os.path relative
- Setiap fungsi wajib punya docstring (satu baris cukup)
- Validasi input di services.py, bukan di views.py
- Entry point: python main.py tanpa setup tambahan

## Mapping Struktur Data ke Fitur

- Hash Table → lookup mahasiswa by NIM
- Single LL → list matkul per mahasiswa
- Double LL → navigasi riwayat nilai
- Circular LL → navigasi carousel di views
- Stack → activity log (LIFO)
- Queue → antrian KRS (FIFO)
- Tree → hierarki Fakultas → Prodi → Mahasiswa
- Graph → prasyarat antar mata kuliah
- Sorting → sort mahasiswa by nama/IPK
- Searching → linear by nama, binary by NIM
- Rekursif → kalkulasi IPK kumulatif

## Cara Kerja

Satu file per turn. Setiap file yang dibuat harus:

1. Lengkap dan langsung bisa dijalankan
2. Ada docstring satu baris per fungsi
3. Untuk structures/ — sertakan blok **main** demo isolated
4. Kalau butuh file yang belum ada, gunakan stub/pass dulu
