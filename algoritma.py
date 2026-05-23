"""Algoritma sorting, searching, dan rekursif untuk SIAKAD Lite."""


def _get_value(item, key):
    """Ambil nilai field dari dict atau object secara aman."""
    if isinstance(item, dict):
        return item.get(key)
    return getattr(item, key, None)


def bubble_sort(arr, key):
    """Urutkan list secara in-place dengan bubble sort berdasarkan key."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            left = _get_value(arr[j], key)
            right = _get_value(arr[j + 1], key)
            if left is not None and right is not None and left > right:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr, key):
    """Urutkan list secara in-place dengan insertion sort berdasarkan key."""
    for i in range(1, len(arr)):
        current = arr[i]
        current_value = _get_value(current, key)
        j = i - 1
        while j >= 0:
            prev_value = _get_value(arr[j], key)
            if (
                prev_value is None
                or current_value is None
                or prev_value <= current_value
            ):
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def linear_search(arr, keyword, field):
    """Cari item secara linear berdasarkan field, case insensitive."""
    if keyword is None:
        return None
    target = str(keyword).lower()
    for item in arr:
        value = _get_value(item, field)
        if value is None:
            continue
        if str(value).lower() == target:
            return item
    return None


def binary_search(arr, nim):
    """Cari item by NIM pada list yang sudah terurut naik berdasarkan nim."""
    left = 0
    right = len(arr) - 1
    target = str(nim)
    while left <= right:
        mid = (left + right) // 2
        mid_value = _get_value(arr[mid], "nim")
        if mid_value is None:
            return None
        mid_str = str(mid_value)
        if mid_str == target:
            return arr[mid]
        if mid_str < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def hitung_ipk(nilai_list, index=0, trace=False):
    """Hitung IPK kumulatif secara rekursif dari list nilai."""
    if index >= len(nilai_list):
        return 0.0
    nilai = nilai_list[index]
    if trace:
        print(f"trace index={index} nilai={nilai}")
    return float(nilai) + hitung_ipk(nilai_list, index + 1, trace)


if __name__ == "__main__":
    demo = [
        {"nim": "22001", "nama": "Budi", "ipk": 3.1},
        {"nim": "22003", "nama": "Citra", "ipk": 3.6},
        {"nim": "22002", "nama": "Ani", "ipk": 3.4},
    ]
    bubble_sort(demo, "nim")
    insertion_sort(demo, "nama")
    linear_search(demo, "ani", "nama")
    binary_search(demo, "22002")
    hitung_ipk([3.0, 3.5, 3.8], trace=True)
