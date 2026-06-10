"""Algoritma sorting, searching, dan rekursif untuk DUA UNRI."""


def ambil_nilai(item, key):
    """Ambil nilai dari dict atau object berdasarkan key secara aman."""
    if isinstance(item, dict):
        return item.get(key)
    return getattr(item, key, None)


def bubble_sort(arr, key):
    """Urutkan list dengan bubble sort berdasarkan key — Sorting."""
    n = len(arr)
    for i in range(n):
        ada_pertukaran = False
        for j in range(0, n - i - 1):
            kiri = ambil_nilai(arr[j], key)
            kanan = ambil_nilai(arr[j + 1], key)
            if kiri is not None and kanan is not None and kiri > kanan:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ada_pertukaran = True
        # Kalau tidak ada pertukaran, data sudah terurut — berhenti lebih awal
        if not ada_pertukaran:
            break
    return arr


def insertion_sort(arr, key):
    """Urutkan list dengan insertion sort berdasarkan key — Sorting."""
    for i in range(1, len(arr)):
        item_sekarang = arr[i]
        nilai_sekarang = ambil_nilai(item_sekarang, key)
        j = i - 1
        # Geser item ke kanan selama nilainya lebih besar dari item_sekarang
        while j >= 0:
            nilai_sebelum = ambil_nilai(arr[j], key)
            if (
                nilai_sebelum is None
                or nilai_sekarang is None
                or nilai_sebelum <= nilai_sekarang
            ):
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_sekarang
    return arr


def linear_search(arr, keyword, field):
    """Cari item satu per satu berdasarkan field, tidak case sensitive — Searching."""
    if keyword is None:
        return None
    target = str(keyword).lower()
    for item in arr:
        nilai = ambil_nilai(item, field)
        if nilai is None:
            continue
        if str(nilai).lower() == target:
            return item
    return None


def binary_search(arr, nim):
    """Cari mahasiswa by NIM di list yang sudah terurut — Searching."""
    kiri = 0
    kanan = len(arr) - 1
    target = str(nim)
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nilai_tengah = ambil_nilai(arr[tengah], "nim")
        if nilai_tengah is None:
            return None
        nilai_tengah = str(nilai_tengah)
        if nilai_tengah == target:
            return arr[tengah]  # Ketemu
        if nilai_tengah < target:
            kiri = tengah + 1  # Cari di sebelah kanan
        else:
            kanan = tengah - 1  # Cari di sebelah kiri
    return None


def hitung_ipk(nilai_list, index=0, trace=False):
    """Jumlahkan semua nilai secara rekursif — Rekursif."""
    # Base case: kalau index sudah melewati akhir list, kembalikan 0
    if index >= len(nilai_list):
        return 0.0
    nilai = nilai_list[index]
    if trace:
        print(f"  rekursif ke-{index}: nilai={nilai}")
    # Rekursif: nilai sekarang + jumlah nilai berikutnya
    return float(nilai) + hitung_ipk(nilai_list, index + 1, trace)


# ---------------------------------------------------------------------------
# Demo isolated — jalankan: python algoritma.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    data = [
        {"nim": "22001", "nama": "Hanif", "ipk": 3.1},
        {"nim": "22003", "nama": "Habib", "ipk": 3.6},
        {"nim": "22002", "nama": "Riva", "ipk": 3.4},
    ]

    print("=== Bubble Sort by NIM ===")
    hasil = bubble_sort(data.copy(), "nim")
    for item in hasil:
        print(f"  {item['nim']} - {item['nama']}")

    print("\n=== Insertion Sort by Nama ===")
    hasil = insertion_sort(data.copy(), "nama")
    for item in hasil:
        print(f"  {item['nama']}")

    print("\n=== Linear Search nama 'ani' ===")
    print(f"  hasil: {linear_search(data, 'ani', 'nama')}")

    print("\n=== Binary Search NIM '22002' ===")
    terurut = bubble_sort(data.copy(), "nim")
    print(f"  hasil: {binary_search(terurut, '22002')}")

    print("\n=== Rekursif hitung_ipk [3.0, 3.5, 3.8] ===")
    total = hitung_ipk([3.0, 3.5, 3.8], trace=True)
    print(f"  total: {total} | rata-rata: {round(total / 3, 2)}")
