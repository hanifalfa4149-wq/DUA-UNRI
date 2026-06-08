# Pembagian Tugas — DUA UNRI

> Capstone Project · Praktikum Algoritma Pemrograman & Struktur Data · UNRI
> 2 Minggu · 3 Orang

---

## Cara Baca Dokumen Ini

Tiap orang punya section sendiri. Baca bagian kamu, pahami **done when**-nya,
dan langsung eksekusi. Detail teknis lengkap ada di `docs/DUA UNRI-PRD.md`.

---

## Milestone Gate

| Gate | Kapan | Kondisi Lulus |
|---|---|---|
| Gate 1 | Pertengahan Week 1 | Semua anggota selesai coding bagian masing-masing, push ke repo |
| Gate 2 | Akhir Week 1 | Ketua selesai QA, align, dan merge — program jalan end-to-end |
| Gate 3 | Akhir Week 2 | Semua orang paham full project, siap ujian individu |

---

## Ownership Per File

| File | PIC |
|---|---|
| `main.py` | Ketua |
| `views.py` | Ketua |
| `algoritma.py` | Ketua |
| `services.py` | Ketua |
| `structures/linked_list.py` | Anggota 1 |
| `structures/stack_queue.py` | Anggota 1 |
| `models.py` | Anggota 2 |
| `structures/hash_table.py` | Anggota 2 |
| `structures/tree_graph.py` | Anggota 2 |
| `data/*.json` | Anggota 2 (dummy data) |

---

## 👑 Ketua — Integrator · Algorithm · CLI

**File:** `algoritma.py`, `services.py`, `views.py`, `main.py`
**DS untuk ujian individu:** Sorting, Searching, Rekursif, Stack, Queue

### Week 1 — Coding + QA + Merge

| ID | Task | Done When |
|---|---|---|
| K1-01 | Setup repo dan folder structure, briefing tim | Semua folder + file placeholder ada, tim tahu ownership masing-masing |
| K1-02 | `algoritma.py` — sorting manual, searching, rekursif | Jalan isolated, demo di `__main__` berjalan |
| K1-03 | `services.py` — semua business logic dengan stub import | Semua fungsi utama jalan sesuai mapping DS di PRD |
| K1-04 | `views.py` — semua menu CLI tersambung ke services | Semua menu bisa diakses, output terminal rapi |
| K1-05 | `main.py` — entry point dan router | `python main.py` langsung masuk menu utama |
| K1-06 | Review, QA, dan merge semua branch anggota | Program jalan end-to-end tanpa error, semua DS tersambung |

### Week 2 — Pemahaman Full Project

| ID | Task | Done When |
|---|---|---|
| K2-01 | Pahami `structures/linked_list.py` milik Anggota 1 | Bisa jelaskan cara kerja Single, Double, Circular LL |
| K2-02 | Pahami `structures/stack_queue.py` milik Anggota 1 | Bisa jelaskan Stack dan Queue dan kenapa dipakai di sini |
| K2-03 | Pahami `models.py`, `hash_table.py`, `tree_graph.py` milik Anggota 2 | Bisa jelaskan OOP, Hash Table, Tree, Graph dalam konteks project ini |
| K2-04 | Latihan: jelaskan full project dari `main.py` sampai `structures/` | Bisa walkthrough alur program dari awal sampai akhir |
| K2-05 | Siap skenario ujian: modifikasi dan manipulasi kode any file | Bisa diminta ubah/extend bagian manapun on-the-spot |

### Do · Don't · Constraint
| | |
|---|---|
| ✅ | Setup repo di hari pertama sebelum anggota mulai coding |
| ✅ | Kerjakan `algoritma.py` duluan — paling independent, tidak butuh file lain |
| ✅ | Build `services.py` pakai stub import dulu, sambung saat merge |
| ❌ | Jangan pakai `sorted()` atau `.sort()` — harus algoritma manual |
| ❌ | Jangan taruh business logic di `views.py` |
| ❌ | Jangan skip review kode anggota — QA adalah tanggung jawab ketua |
| ⛔ | `python main.py` harus jalan tanpa setup tambahan apapun |

---

## 👤 Anggota 1 — Struktur Data Klasik

**File:** `structures/linked_list.py`, `structures/stack_queue.py`
**DS untuk ujian individu:** Single LL, Double LL, Circular LL, Stack, Queue

### Week 1 — Coding

| ID | Task | Done When |
|---|---|---|
| A1-01 | `SingleLinkedList` — append, delete, search, display | Bisa simpan list data dan tampil di terminal |
| A1-02 | `DoubleLinkedList` — append, prev, next, display, traverse_backward | Navigasi maju-mundur antar node berjalan benar |
| A1-03 | `CircularLinkedList` — append, traverse loop, display | Traverse tidak berhenti, kembali ke head |
| A1-04 | `Stack` — push, pop, peek, is_empty, display | Log aktivitas masuk dan tampil LIFO |
| A1-05 | `Queue` — enqueue, dequeue, peek, is_empty, display | Antrian masuk dan diproses FIFO |
| A1-06 | Demo isolated semua DS di blok `__main__` tiap file | `python structures/linked_list.py` dan `stack_queue.py` jalan sendiri |
| A1-07 | Docstring lengkap semua file, push ke repo | Setiap class dan method terdokumentasi, branch siap di-review ketua |

### Week 2 — Pemahaman Full Project

| ID | Task | Done When |
|---|---|---|
| A2-01 | Pahami `models.py` milik Anggota 2 | Bisa jelaskan class Mahasiswa, MataKuliah, KRS, Nilai dan serialisasinya |
| A2-02 | Pahami `hash_table.py` dan `tree_graph.py` milik Anggota 2 | Bisa jelaskan cara kerja Hash Table, Tree, dan Graph |
| A2-03 | Pahami `algoritma.py`, `services.py`, `views.py` milik Ketua | Bisa jelaskan sorting, searching, rekursif, dan alur business logic |
| A2-04 | Latihan: jelaskan kenapa tiap DS dipilih untuk fitur tertentu | Bisa jawab "kenapa Queue untuk KRS, bukan Stack?" dan sejenisnya |
| A2-05 | Siap skenario ujian: modifikasi method on-the-spot | Bisa diminta tambah method baru di LL atau Stack tanpa referensi |

### Do · Don't · Constraint
| | |
|---|---|
| ✅ | Mulai dari `SingleLinkedList` dulu — yang lain ikuti polanya |
| ✅ | Node harus class terpisah dengan pointer — bukan list Python |
| ✅ | Push ke repo segera setelah selesai — ketua butuh ini untuk merge |
| ❌ | Jangan pakai `collections.deque` untuk Queue |
| ❌ | Jangan campur domain logic di dalam class DS |
| ❌ | Jangan hafal kode — pahami logika tiap struktur data |
| ⛔ | Setiap DS wajib bisa di-demo isolated via `__main__` block |

---

## 👤 Anggota 2 — Foundation + Advanced DS

**File:** `models.py`, `structures/hash_table.py`, `structures/tree_graph.py`, `data/*.json`
**DS untuk ujian individu:** OOP, File Handler, Hash Table, Tree, Graph

### Week 1 — Coding

| ID | Task | Done When |
|---|---|---|
| A2-01 | `models.py` — class Mahasiswa, MataKuliah, KRS, Nilai | Semua class punya `to_dict()`, `from_dict()`, `__str__()` |
| A2-02 | Data dummy JSON semua entitas | Minimal 5 mahasiswa, 4 matkul, data realistis siap untuk testing |
| A2-03 | `hash_table.py` — separate chaining, fungsi hash manual | Lookup NIM berjalan, collision handled, demo di `__main__` jalan |
| A2-04 | `tree_graph.py` — Tree hierarki + Graph prasyarat | Tree bisa traverse, Graph tampilkan adjacency list, demo jalan |
| A2-05 | Docstring lengkap semua file, push ke repo | Setiap class dan method terdokumentasi, branch siap di-review ketua |

### Week 2 — Pemahaman Full Project

| ID | Task | Done When |
|---|---|---|
| A2-01 | Pahami `structures/linked_list.py` milik Anggota 1 | Bisa jelaskan Single, Double, Circular LL dan perbedaannya |
| A2-02 | Pahami `structures/stack_queue.py` milik Anggota 1 | Bisa jelaskan Stack dan Queue, LIFO vs FIFO |
| A2-03 | Pahami `algoritma.py`, `services.py`, `views.py` milik Ketua | Bisa jelaskan alur dari input user sampai data tersimpan ke JSON |
| A2-04 | Latihan: jelaskan OOP dalam konteks project — bukan teori | Bisa jawab "kenapa pakai class, bukan dict biasa?" |
| A2-05 | Siap skenario ujian: modifikasi Hash Table atau Tree on-the-spot | Bisa extend fitur Graph (tambah node/edge) tanpa referensi |

### Do · Don't · Constraint
| | |
|---|---|
| ✅ | Selesaikan `models.py` secepat mungkin — ketua butuh ini untuk stub |
| ✅ | Buat data dummy realistis — tim butuh ini untuk testing integrasi |
| ✅ | Hash Table pakai separate chaining — lebih mudah diimplementasi dan dijelaskan |
| ❌ | Jangan pakai `dict` Python langsung sebagai Hash Table |
| ❌ | Jangan hardcode path file — pakai `os.path` relative |
| ❌ | Jangan skip `__main__` block demo di semua file structures |
| ⛔ | Semua class di `models.py` wajib punya `to_dict()` dan `from_dict()` |

---

## Constraint Global — Berlaku Untuk Semua

- DILARANG pakai library struktur data eksternal (`collections.deque`, `heapq`, dll)
- DILARANG pakai `sorted()` atau `.sort()` — harus algoritma manual
- Setiap fungsi dan class wajib punya docstring minimal satu baris
- Tidak ada dependency eksternal selain Python stdlib
- Entry point program: `python main.py`
- Push ke repo setelah selesai coding — jangan tunggu sempurna

---

> Baca `docs/DUA UNRI-PRD.md` untuk detail teknis lengkap.
