---
applyTo: "services.py"
---

# Instructions — services.py

## Aturan
- Satu file berisi semua business logic
- Tidak ada I/O terminal — hanya parameter dan return value
- Semua akses file JSON dilakukan di sini (bukan di views)
- Setiap fungsi docstring wajib sebut struktur data yang dipakai

## Fungsi Wajib dan DS yang Dipakai
- tambah_mahasiswa()     → HashTable.insert()
- cari_mahasiswa_nim()   → HashTable.search()
- cari_mahasiswa_nama()  → linear_search() dari algoritma.py
- sort_mahasiswa()       → bubble_sort() dari algoritma.py
- ajukan_krs()           → Queue.enqueue()
- proses_krs()           → Queue.dequeue() → SingleLL.append()
- input_nilai()          → DoubleLL.append()
- hitung_ipk()           → hitung_ipk() rekursif dari algoritma.py
- catat_log()            → Stack.push()
- tampil_log()           → Stack.display()

## Error Handling
- Return None jika data tidak ditemukan
- Return False jika operasi gagal
- Validasi input sebelum proses — jangan biarkan data kotor masuk ke DS