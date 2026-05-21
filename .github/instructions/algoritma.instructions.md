---
applyTo: "algoritma.py"
---

# Instructions — algoritma.py

## Aturan

- Satu file berisi semua algoritma: sorting, searching, rekursif
- Tidak ada I/O (print/input) di file ini — murni fungsi
- Tidak ada import dari models/, services/, atau views/
- Semua fungsi harus bisa dipanggil isolated

## Fungsi Wajib

### Sorting (manual — dilarang sorted() atau .sort())

- bubble_sort(arr, key) atau insertion_sort(arr, key)
- Parameter key untuk tentukan field yang di-sort

### Searching

- linear_search(arr, keyword, field) → untuk search by nama
- binary_search(arr, nim) → hanya untuk data yang sudah terurut by NIM

### Rekursif

- hitung_ipk(nilai_list, index) → rekursif, bukan loop
- Harus bisa di-trace step-nya (tambahkan print opsional)
