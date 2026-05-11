# Pembagian Tugas — SIAKAD Lite

> **Internal Team Document**
> Capstone Project · Praktikum Algoritma Pemrograman & Struktur Data · UNRI · 3 Minggu · 3 Orang

Dokumen ini adalah panduan kerja tim selama 3 minggu ke depan. Setiap orang punya sprint dan ownership yang jelas — baca bagian kamu, pahami *done when*-nya, dan langsung eksekusi setelah repo siap.

Seluruh detail teknis (arsitektur, data flow, folder structure) ada di `SIAKAD-PRD.md` di repo. Dokumen ini fokus pada **siapa ngapain, kapan, dan batasannya apa**.

---

## Milestone Gate

| Gate | Waktu | Judul | Target |
|---|---|---|---|
| **Gate 1** | Akhir Week 1 | Foundation Berdiri | CRUD mahasiswa jalan end-to-end, semua Linked List bisa di-demo, models + JSON siap dipakai tim. |
| **Gate 2** | Akhir Week 2 | Semua Rubrik Ter-cover | 18 item rubrik kelompok ter-cover, KRS flow dan nilai flow jalan dari terminal. |
| **Gate 3** | Akhir Week 3 | Siap Demo & Ujian | Zero crash, docstring lengkap, tiap orang siap explain dan modifikasi kode bagiannya. |

---

## K — Ketua (Integrator · Algorithm · CLI)

**Role:** Sorting · Searching · Rekursif · Views · Final Integration

### Week 1 — Skeleton project berdiri, tim bisa mulai paralel

> **Outcome:** Repo siap, routing CLI jalan, CRUD mahasiswa bisa dipakai anggota untuk testing.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| K1-01 | Setup repo dan folder structure lengkap sesuai PRD | Semua folder dan `main.py` kosong sudah ada di repo |
| K1-02 | `menu_utama.py` — routing menu angka berjalan | Input 1–8 redirect ke sub-menu yang benar tanpa error |
| K1-03 | `menu_mahasiswa.py` — CRUD basic tersambung ke service | Tambah, lihat, edit, hapus mahasiswa berjalan via terminal |
| K1-04 | Integrasi awal: views → services → models → JSON | Data mahasiswa tersimpan dan ke-load dari file JSON |
| K1-05 | Briefing tim dan distribute PRD | Tiap anggota tahu file mana yang jadi tanggung jawabnya |

**Do · Don't · Constraint**

- ✅ **DO** Setup repo dan folder structure di hari pertama sebelum anggota mulai coding.
- ✅ **DO** Buat `main.py` dan `menu_utama.py` duluan sebagai anchor integrasi tim.
- ✅ **DO** Kerjakan views secara paralel — jangan tunggu Anggota 1 dan 2 selesai dulu.
- ❌ **DON'T** Jangan mulai coding services sebelum folder structure disepakati tim.
- ❌ **DON'T** Jangan masukkan business logic ke dalam views — views hanya untuk I/O terminal.
- ⚠️ **CONSTRAINT** Menu utama harus routing-only. Logic bisnis tidak boleh ada di layer views.

---

### Week 2 — Algorithm layer selesai, semua menu ter-cover

> **Outcome:** Sorting, searching, rekursif berjalan dan tersambung ke views.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| K2-01 | `sorting.py` — implementasi manual (bubble / insertion) | Mahasiswa bisa di-sort by nama dan by IPK via terminal |
| K2-02 | `searching.py` — linear search dan binary search | Cari mahasiswa by NIM (binary) dan nama (linear) berjalan |
| K2-03 | `nilai_service.py` — input nilai dan kalkulasi grade | Nilai masuk, grade (A/B/C) keluar otomatis berdasarkan bobot |
| K2-04 | `rekursif.py` — hitung IPK kumulatif secara rekursif | IPK terhitung benar dan bisa di-trace step rekursinya |
| K2-05 | `menu_nilai.py` + `menu_krs.py` tersambung ke service | Flow nilai dan KRS jalan end-to-end dari terminal |

**Do · Don't · Constraint**

- ✅ **DO** Implement sorting dan searching di file terpisah — bukan inline di dalam service.
- ✅ **DO** Pastikan rekursif IPK bisa di-trace dan di-print step-nya — penting untuk ujian individu.
- ✅ **DO** Review output Anggota 1 dan 2 setiap akhir hari untuk deteksi integration issue lebih awal.
- ❌ **DON'T** Jangan pakai `sorted()` atau `.sort()` bawaan Python — harus implementasi algoritma manual.
- ❌ **DON'T** Jangan tunda koneksi views ke services sampai akhir week — sambungkan bertahap.
- ⚠️ **CONSTRAINT** Semua fungsi sorting dan searching harus bisa dipanggil isolated — testable tanpa UI.

---

### Week 3 — Program solid, siap jadi presenter utama

> **Outcome:** Zero crash, demo mulus, seluruh tim siap ujian individu.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| K3-01 | Full error handling semua menu (input invalid, data kosong) | Program tidak crash di kondisi apapun |
| K3-02 | Final integration test — semua flow dari awal ke akhir | Demo 10 menit jalan mulus tanpa bug |
| K3-03 | Copilot instructions files selesai (`.github/`) | `copilot-instructions.md` dan semua `.instructions.md` siap |
| K3-04 | Latihan presentasi dan dry run bersama tim | Bisa jelaskan arsitektur dan tiap DS dalam 5 menit |

**Do · Don't · Constraint**

- ✅ **DO** Prioritaskan error handling dulu sebelum polish komentar dan dokumentasi.
- ✅ **DO** Lakukan full dry run demo minimal 2x sebelum hari-H presentasi.
- ✅ **DO** Siapkan skenario "bagaimana kalau dosen tanya X" untuk tiap struktur data.
- ❌ **DON'T** Jangan tambah fitur baru di Week 3 — scope harus freeze dari Gate 2.
- ❌ **DON'T** Jangan jadi satu-satunya yang tahu alur integrasi — pastikan semua anggota paham flow-nya.
- ⚠️ **CONSTRAINT** Final demo harus bisa dijalankan dari `python main.py` tanpa setup tambahan apapun.

---

## Anggota 1 — Struktur Data Klasik

**Role:** Single LL · Double LL · Circular LL · Stack · Queue · KRS Service

### Week 1 — Semua Linked List bisa di-demo isolated

> **Outcome:** SingleLL, DoubleLL, CircularLL selesai dan bisa dijalankan mandiri.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A1-01 | `SingleLinkedList` — append, delete, search, display | Bisa simpan list matkul dan tampil di terminal |
| A1-02 | `DoubleLinkedList` — append, prev, next, display | Navigasi maju-mundur antar node berjalan benar |
| A1-03 | `CircularLinkedList` — append, traverse loop, display | Traverse tidak berhenti di akhir, kembali ke head |
| A1-04 | Unit test mandiri tiap LL di blok `__main__` | Jalankan `python linked_list.py` → semua demo jalan sendiri |

**Do · Don't · Constraint**

- ✅ **DO** Mulai dari `SingleLinkedList` dulu — ini yang paling fundamental dan yang lain mengikuti polanya.
- ✅ **DO** Buat blok `__main__` di `linked_list.py` untuk demo tiap LL secara isolated.
- ✅ **DO** Selesaikan ketiga LL di Week 1 sebelum masuk Stack dan Queue di Week 2.
- ❌ **DON'T** Jangan pakai `list` Python sebagai backing store — node harus benar-benar pointer antar objek.
- ❌ **DON'T** Jangan skip `CircularLinkedList` — implementasinya berbeda secara logika dari dua LL lainnya.
- ⚠️ **CONSTRAINT** Setiap LL wajib punya minimal: `append()`, `delete()`, `search()`, `display()`.

---

### Week 2 — Stack, Queue, dan KRS flow selesai tersambung

> **Outcome:** Antrian KRS berjalan FIFO, log aktivitas berjalan LIFO, semua tersambung ke service.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A1-05 | `Stack` — push, pop, peek, is_empty, display | Log aktivitas masuk dan tampil secara LIFO |
| A1-06 | `Queue` — enqueue, dequeue, peek, is_empty, display | Antrian KRS masuk dan diproses secara FIFO |
| A1-07 | `log_service.py` — setiap aksi CRUD tercatat ke Stack | Setiap tambah/edit/hapus muncul di activity log |
| A1-08 | `krs_service.py` — ajukan KRS masuk Queue, proses dequeue, enroll ke Single LL | Flow KRS jalan dari antrian sampai matkul terdaftar di LL mahasiswa |

**Do · Don't · Constraint**

- ✅ **DO** Implement Stack dan Queue sebagai class terpisah di file yang berbeda.
- ✅ **DO** `krs_service.py` harus eksplisit menggunakan Queue untuk antrian dan Single LL untuk hasil enroll.
- ✅ **DO** Test KRS flow end-to-end sendiri sebelum diserahkan ke Ketua untuk integrasi.
- ❌ **DON'T** Jangan pakai `collections.deque` untuk Queue — harus implementasi class manual.
- ❌ **DON'T** Jangan campur logic KRS di dalam class Queue — Queue harus generic, logic ada di service.
- ⚠️ **CONSTRAINT** Stack untuk log harus menyimpan string aksi yang human-readable, bukan raw object.

---

### Week 3 — Siap ujian individu, bisa modifikasi kode on-the-spot

> **Outcome:** Docstring lengkap, Circular LL terpakai nyata, dan bisa whiteboard semua DS bagianmu.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A1-09 | Docstring dan komentar lengkap semua file milikmu | Setiap method ada docstring dan inline comment di bagian krusial |
| A1-10 | Circular LL dipakai di salah satu fitur nyata (bukan hanya demo) | Ada 1 fitur aktif yang menggunakan Circular LL, bukan hanya di `__main__` |
| A1-11 | Latihan: jelaskan Single LL, Double LL, Stack, Queue tanpa lihat kode | Bisa whiteboard struktur dan jelaskan operasinya |
| A1-12 | Skenario ujian: modifikasi method tambahan on-the-spot | Siap diminta tambah method baru saat ujian berlangsung |

**Do · Don't · Constraint**

- ✅ **DO** Cari satu fitur nyata untuk Circular LL — jangan biarkan hanya ada di blok demo.
- ✅ **DO** Latihan whiteboard: gambar node dan pointer setiap LL tanpa referensi kode.
- ✅ **DO** Siapkan jawaban untuk: *"kenapa pakai Linked List bukan list biasa?"*
- ❌ **DON'T** Jangan hafal kode — pahami alur logika tiap struktur data secara konseptual.
- ❌ **DON'T** Jangan biarkan docstring kosong sampai H-1 presentasi.
- ⚠️ **CONSTRAINT** Wajib bisa modifikasi salah satu method LL on-the-spot tanpa referensi — ini yang paling sering keluar di ujian individu.

---

## Anggota 2 — Foundation + Advanced DS

**Role:** OOP · File Handler · Hash Table · Tree · Graph · Matkul Service

### Week 1 — Foundation layer selesai, tim bisa pakai models dan JSON

> **Outcome:** Semua class model terdefinisi, data dummy tersedia, tim tidak terblokir.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A2-01 | `mahasiswa.py` — class Mahasiswa lengkap dengan atribut dan method | Objek Mahasiswa bisa dibuat, di-update, dan di-serialize ke dict |
| A2-02 | `matakuliah.py`, `krs.py`, `nilai.py` — semua class selesai | Semua entitas terdefinisi dan bisa di-import oleh services |
| A2-03 | File handler — read/write JSON untuk semua entitas | Load saat startup, save otomatis setiap ada perubahan |
| A2-04 | Data dummy JSON tersedia untuk testing tim | `mahasiswa.json` dan `matakuliah.json` berisi minimal 5 data dummy yang realistis |

**Do · Don't · Constraint**

- ✅ **DO** Selesaikan semua `models/` di awal — ini yang paling dibutuhkan tim lain untuk mulai.
- ✅ **DO** Buat data dummy JSON yang realistis — minimal 5 mahasiswa, 4 matkul, 2 prodi.
- ✅ **DO** File handler harus punya method `load()` dan `save()` yang generic — bisa dipakai semua entitas.
- ❌ **DON'T** Jangan hardcode path file — gunakan `os.path` yang relative terhadap root project.
- ❌ **DON'T** Jangan tunggu models sempurna sebelum dibagikan ke tim — draft yang jalan lebih penting dari yang sempurna.
- ⚠️ **CONSTRAINT** Semua class di `models/` wajib punya method `to_dict()` dan `from_dict()` untuk serialisasi JSON.

---

### Week 2 — Advanced DS selesai dan tersambung ke fitur nyata

> **Outcome:** Hash Table, Tree, dan Graph bisa di-demo dan aktif dipakai di service.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A2-05 | `hash_table.py` — implementasi manual dengan separate chaining | Lookup NIM berjalan, collision handled, demo di `__main__` jalan |
| A2-06 | `tree.py` — hierarki Fakultas → Prodi → Mahasiswa | Tree bisa di-traverse dan ditampilkan di terminal |
| A2-07 | `graph.py` — directed graph prasyarat mata kuliah | Bisa tambah edge, cek prasyarat, tampilkan adjacency list |
| A2-08 | `matkul_service.py` — CRUD matkul dan integrasi graph prasyarat | Tambah matkul dan definisi prasyarat berjalan dari terminal |

**Do · Don't · Constraint**

- ✅ **DO** Hash Table pakai separate chaining — lebih mudah diimplementasikan dan dijelaskan saat ujian.
- ✅ **DO** Tree cukup simple — insert node dan traverse pre-order sudah cukup untuk kebutuhan kita.
- ✅ **DO** Graph pakai adjacency list berbasis dictionary — paling natural untuk relasi prasyarat matkul.
- ❌ **DON'T** Jangan pakai `dict` Python langsung sebagai Hash Table — harus ada class `HashTable` dengan fungsi hash manual.
- ❌ **DON'T** Jangan buat Tree dan Graph terlalu kompleks — cukup cover kebutuhan fitur yang ada di PRD.
- ⚠️ **CONSTRAINT** Hash Table harus bisa demonstrasikan collision dan cara resolve-nya — ini yang paling sering ditanya dosen.

---

### Week 3 — Siap ujian individu, bisa jelaskan OOP dan 3 advanced DS

> **Outcome:** Docstring lengkap, Hash Table aktif dipakai, siap explain semua DS bagianmu.

**Backlog**

| ID | Task | Done When |
|---|---|---|
| A2-09 | Docstring dan komentar lengkap semua file milikmu | Setiap class dan method terdokumentasi dengan jelas |
| A2-10 | Hash Table aktif dipakai untuk lookup mahasiswa by NIM | Setiap search by NIM melewati Hash Table, bukan linear scan biasa |
| A2-11 | Latihan: jelaskan OOP, Hash Table, Tree, Graph tanpa lihat kode | Bisa gambar struktur dan jelaskan time complexity-nya |
| A2-12 | Skenario ujian: modifikasi graph (tambah node/edge) on-the-spot | Siap diminta extend fitur prasyarat saat ujian berlangsung |

**Do · Don't · Constraint**

- ✅ **DO** Pastikan Hash Table aktif dipakai untuk lookup NIM — bukan hanya ada di blok demo.
- ✅ **DO** Latihan jelaskan OOP: apa itu encapsulation, dalam konteks class yang kita buat.
- ✅ **DO** Siapkan jawaban untuk: *"kenapa pakai Hash Table?"* dan *"apa bedanya Tree sama Graph?"*
- ❌ **DON'T** Jangan anggap OOP dan File Handler "gampang jadi tidak perlu dilatih" — tetap sering ditanyain.
- ❌ **DON'T** Jangan biarkan Tree hanya jadi display statis — harus bisa insert node baru saat dijalankan.
- ⚠️ **CONSTRAINT** Hash Table, Tree, dan Graph harus bisa di-demo isolated via `__main__` block masing-masing file — wajib untuk ujian individu.

---

*SIAKAD Lite · Capstone Project Praktikum Algoritma & Struktur Data · UNRI*
*Internal document — untuk alignment tim dan eksekusi langsung.*
