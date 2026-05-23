"""Business logic SIAKAD Lite: file handler, mahasiswa, KRS, nilai, log."""
import json
import os

try:
    from models import Mahasiswa, MataKuliah, KRS, Nilai
except Exception:
    def _build_model_stub(name, fields):
        """Buat stub model sederhana dari daftar field."""
        class _Stub:
            """Stub entitas model jika models.py belum tersedia."""
            def __init__(self, *args): """Inisialisasi data model (stub)."""; [setattr(self, k, v) for k, v in zip(fields, args)]
            def to_dict(self): """Serialize model (stub)."""; return {k: getattr(self, k, None) for k in fields}
            @classmethod
            def from_dict(cls, data): """Deserialize model (stub)."""; return cls(*[data.get(k) for k in fields])
            def __str__(self): """Representasi string model (stub)."""; return f"{name}({', '.join(str(getattr(self, k, '')) for k in fields[:2])})"
        _Stub.__name__ = name
        return _Stub
    Mahasiswa = _build_model_stub("Mahasiswa", ["nim", "nama", "id_prodi", "angkatan"])
    MataKuliah = _build_model_stub("MataKuliah", ["kode", "nama", "sks", "semester", "tipe"])
    KRS = _build_model_stub("KRS", ["nim", "list_kode_mk"])
    Nilai = _build_model_stub("Nilai", ["nim", "kode_mk", "tugas", "uts", "uas", "nilai_akhir", "grade"])
try:
    from structures.hash_table import HashTable
    from structures.linked_list import SingleLL, DoubleLL, CircularLL
    from structures.stack_queue import Stack, Queue
    from structures.tree_graph import Tree, Graph
except Exception:
    class HashTable:
        """Stub HashTable jika structures belum tersedia."""
        def __init__(self): """Inisialisasi HashTable (stub)."""; self._data = {}
        def insert(self, key, value): """Insert data ke HashTable (stub)."""; self._data[key] = value
        def search(self, key): """Cari data di HashTable (stub)."""; return self._data.get(key)
    class SingleLL:
        """Stub Single Linked List jika structures belum tersedia."""
        def __init__(self): """Inisialisasi SingleLL (stub)."""; self._items = []
        def append(self, data): """Append data ke SingleLL (stub)."""; self._items.append(data)
        def display(self): """Display SingleLL (stub)."""; return list(self._items)
    class DoubleLL(SingleLL):
        """Stub Double Linked List jika structures belum tersedia."""
        def traverse_backward(self): """Traverse mundur DoubleLL (stub)."""; return list(reversed(self._items))
    class CircularLL(SingleLL): """Stub Circular Linked List jika structures belum tersedia."""; pass
    class Stack:
        """Stub Stack jika structures belum tersedia."""
        def __init__(self): """Inisialisasi Stack (stub)."""; self._items = []
        def push(self, item): """Push ke Stack (stub)."""; self._items.append(item)
        def display(self): """Display Stack (stub)."""; return list(reversed(self._items))
    class Queue:
        """Stub Queue jika structures belum tersedia."""
        def __init__(self): """Inisialisasi Queue (stub)."""; self._items = []
        def enqueue(self, item): """Enqueue ke Queue (stub)."""; self._items.append(item)
        def dequeue(self): """Dequeue dari Queue (stub)."""; return self._items.pop(0) if self._items else None
        def is_empty(self): """Cek Queue kosong (stub)."""; return not self._items
        def display(self): """Display Queue (stub)."""; return list(self._items)
    class Tree: """Stub Tree jika structures belum tersedia."""; pass
    class Graph:
        """Stub Graph jika structures belum tersedia."""
        def __init__(self): """Inisialisasi Graph (stub)."""; self._adj = {}
        def add_vertex(self, vertex): """Tambah vertex Graph (stub)."""; self._adj.setdefault(vertex, [])
        def add_edge(self, v1, v2): """Tambah edge Graph (stub)."""; self._adj.setdefault(v1, []).append(v2); self._adj.setdefault(v2, [])
        def get_neighbors(self, vertex): """Ambil neighbors Graph (stub)."""; return list(self._adj.get(vertex, []))
try:
    from algoritma import bubble_sort, insertion_sort, linear_search, binary_search, hitung_ipk
except Exception:
    def bubble_sort(arr, key): """Stub bubble_sort jika algoritma.py belum tersedia."""; return arr
    def insertion_sort(arr, key): """Stub insertion_sort jika algoritma.py belum tersedia."""; return arr
    def linear_search(arr, keyword, field): """Stub linear_search jika algoritma.py belum tersedia."""; return None
    def binary_search(arr, nim): """Stub binary_search jika algoritma.py belum tersedia."""; return None
    def hitung_ipk(nilai_list, index=0, trace=False): """Stub hitung_ipk jika algoritma.py belum tersedia."""; return 0.0
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_DIR = os.path.join(_BASE_DIR, "data")
_mahasiswa_table = HashTable()
_krs_queue = Queue()
_log_stack = Stack()
_prasyarat_graph = Graph()
_krs_lists = {}
_nilai_lists = {}
def _ensure_data_dir(): """Pastikan folder data ada (tanpa DS khusus)."""; os.makedirs(_DATA_DIR, exist_ok=True)
def _data_path(filename): """Bangun path file data secara relative (tanpa DS khusus)."""; return os.path.join(_DATA_DIR, filename)
def _as_list(data): """Pastikan data berbentuk list (List)."""; return data if isinstance(data, list) else []
def _as_dict(data): """Pastikan data berbentuk dict (Dict)."""; return data if isinstance(data, dict) else {}
def _str(value): """Konversi nilai ke string aman (tanpa DS khusus)."""; return str(value) if value is not None else ""
def _require_all(*values): """Validasi semua input wajib terisi (tanpa DS khusus)."""; return all(values)
def load_data(filename):
    """Load JSON dari data/ (List/Dict sebagai struktur data Python)."""
    _ensure_data_dir()
    path = _data_path(filename)
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as file_handle:
            data = json.load(file_handle)
        return data if isinstance(data, (list, dict)) else []
    except Exception:
        return []
def save_data(filename, data):
    """Simpan JSON ke data/ (List/Dict sebagai struktur data Python)."""
    _ensure_data_dir()
    try:
        with open(_data_path(filename), "w", encoding="utf-8") as file_handle:
            json.dump(data, file_handle, ensure_ascii=True, indent=2)
        return True
    except Exception:
        return False
def _rebuild_mahasiswa_table():
    """Bangun ulang HashTable mahasiswa dari file (HashTable)."""
    global _mahasiswa_table
    _mahasiswa_table = HashTable()
    for item in _as_list(load_data("mahasiswa.json")):
        nim = item.get("nim") if isinstance(item, dict) else None
        if nim is not None:
            _mahasiswa_table.insert(_str(nim), item)
def _build_single_ll(items):
    """Bangun SingleLL dari list (SingleLL)."""
    linked = SingleLL()
    for item in items:
        linked.append(item)
    return linked
def _build_double_ll(items):
    """Bangun DoubleLL dari list (DoubleLL)."""
    linked = DoubleLL()
    for item in items:
        linked.append(item)
    return linked
def _grade_from_score(score):
    """Konversi nilai ke grade (tanpa DS khusus)."""
    if score >= 85:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "E"
def tambah_mahasiswa(nim, nama, id_prodi, angkatan):
    """Tambah mahasiswa baru dan simpan ke HashTable."""
    if not _require_all(nim, nama, id_prodi, angkatan):
        return False
    data = _as_list(load_data("mahasiswa.json"))
    nim_str = _str(nim)
    if any(isinstance(item, dict) and _str(item.get("nim")) == nim_str for item in data):
        return False
    entity = Mahasiswa(nim_str, nama, id_prodi, angkatan)
    payload = entity.to_dict() if hasattr(entity, "to_dict") else {"nim": nim_str, "nama": nama, "id_prodi": id_prodi, "angkatan": angkatan}
    data.append(payload)
    if not save_data("mahasiswa.json", data):
        return False
    _rebuild_mahasiswa_table()
    return payload
def lihat_semua_mahasiswa(): """Lihat semua mahasiswa dari file (List)."""; return _as_list(load_data("mahasiswa.json"))
def cari_nim(nim):
    """Cari mahasiswa by NIM lewat HashTable."""
    if not nim:
        return None
    _rebuild_mahasiswa_table()
    return _mahasiswa_table.search(_str(nim))
def cari_nama(keyword): """Cari mahasiswa by nama dengan linear search (List + linear_search)."""; return None if not keyword else linear_search(_as_list(load_data("mahasiswa.json")), keyword, "nama")
def sort_mahasiswa(key): """Sort mahasiswa dengan bubble sort (List + bubble_sort)."""; return bubble_sort(_as_list(load_data("mahasiswa.json")), key) if key else []
def hapus_mahasiswa(nim):
    """Hapus mahasiswa dari file dan HashTable."""
    if not nim:
        return False
    data = _as_list(load_data("mahasiswa.json"))
    nim_str = _str(nim)
    new_data = [item for item in data if _str(item.get("nim")) != nim_str]
    if len(new_data) == len(data):
        return False
    if not save_data("mahasiswa.json", new_data):
        return False
    _rebuild_mahasiswa_table()
    return True
def tambah_matkul(kode, nama, sks, semester, tipe):
    """Tambah mata kuliah baru (List)."""
    if not _require_all(kode, nama, tipe) or sks is None or semester is None:
        return False
    data = _as_list(load_data("matakuliah.json"))
    kode_str = _str(kode)
    if any(isinstance(item, dict) and _str(item.get("kode")) == kode_str for item in data):
        return False
    entity = MataKuliah(kode_str, nama, sks, semester, tipe)
    payload = entity.to_dict() if hasattr(entity, "to_dict") else {"kode": kode_str, "nama": nama, "sks": sks, "semester": semester, "tipe": tipe}
    data.append(payload)
    return payload if save_data("matakuliah.json", data) else False
def lihat_semua_matkul(): """Lihat semua mata kuliah dari file (List)."""; return _as_list(load_data("matakuliah.json"))
def tambah_prasyarat(kode_mk, kode_prasyarat):
    """Tambah prasyarat mata kuliah pada Graph."""
    if not _require_all(kode_mk, kode_prasyarat):
        return False
    data = _as_list(load_data("matakuliah.json"))
    kode_mk = _str(kode_mk)
    kode_prasyarat = _str(kode_prasyarat)
    updated = False
    for item in data:
        if _str(item.get("kode")) == kode_mk:
            prasyarat = item.get("prasyarat", [])
            if kode_prasyarat not in prasyarat:
                prasyarat.append(kode_prasyarat)
                item["prasyarat"] = prasyarat
            updated = True
            break
    if not updated:
        return False
    _prasyarat_graph.add_vertex(kode_mk)
    _prasyarat_graph.add_vertex(kode_prasyarat)
    _prasyarat_graph.add_edge(kode_mk, kode_prasyarat)
    return save_data("matakuliah.json", data)
def lihat_prasyarat(kode_mk):
    """Lihat prasyarat dari Graph atau file (Graph)."""
    if not kode_mk:
        return []
    kode_mk = _str(kode_mk)
    neighbors = _prasyarat_graph.get_neighbors(kode_mk)
    if neighbors:
        return neighbors
    for item in _as_list(load_data("matakuliah.json")):
        if _str(item.get("kode")) == kode_mk:
            return item.get("prasyarat", [])
    return []
def ajukan_krs(nim):
    """Ajukan KRS ke antrian (Queue)."""
    if not nim or not cari_nim(nim):
        return False
    _krs_queue.enqueue(_str(nim))
    return True
def proses_krs(nim, list_kode_mk):
    """Proses antrian KRS dan simpan ke SingleLL (Queue + SingleLL)."""
    if not _require_all(nim, list_kode_mk) or _krs_queue.is_empty():
        return False
    queued_nim = _krs_queue.dequeue()
    if _str(queued_nim) != _str(nim):
        return False
    kode_list = [_str(kode) for kode in list_kode_mk]
    linked = _build_single_ll(kode_list)
    _krs_lists[_str(nim)] = linked
    data = _as_dict(load_data("krs.json"))
    data[_str(nim)] = kode_list
    return save_data("krs.json", data)
def lihat_krs(nim):
    """Lihat KRS mahasiswa dari SingleLL (SingleLL)."""
    if not nim:
        return []
    data = _as_dict(load_data("krs.json"))
    list_kode = data.get(_str(nim), [])
    linked = _build_single_ll(list_kode)
    _krs_lists[_str(nim)] = linked
    displayed = linked.display()
    return displayed if displayed is not None else list_kode
def input_nilai(nim, kode_mk, tugas, uts, uas):
    """Input nilai dan simpan ke DoubleLL (DoubleLL)."""
    if not _require_all(nim, kode_mk):
        return False
    try:
        tugas_val, uts_val, uas_val = float(tugas), float(uts), float(uas)
    except Exception:
        return False
    if not (0 <= tugas_val <= 100 and 0 <= uts_val <= 100 and 0 <= uas_val <= 100):
        return False
    nilai_akhir = round((tugas_val * 0.3) + (uts_val * 0.3) + (uas_val * 0.4), 2)
    grade = _grade_from_score(nilai_akhir)
    entity = Nilai(_str(nim), _str(kode_mk), tugas_val, uts_val, uas_val, nilai_akhir, grade)
    payload = entity.to_dict() if hasattr(entity, "to_dict") else {"nim": _str(nim), "kode_mk": _str(kode_mk), "tugas": tugas_val, "uts": uts_val, "uas": uas_val, "nilai_akhir": nilai_akhir, "grade": grade}
    data = _as_dict(load_data("nilai.json"))
    nilai_list = data.get(_str(nim), [])
    nilai_list.append(payload)
    data[_str(nim)] = nilai_list
    if not save_data("nilai.json", data):
        return False
    linked = _build_double_ll(nilai_list)
    _nilai_lists[_str(nim)] = linked
    return payload
def lihat_nilai(nim):
    """Lihat semua nilai mahasiswa dari DoubleLL (DoubleLL)."""
    if not nim:
        return []
    data = _as_dict(load_data("nilai.json"))
    nilai_list = data.get(_str(nim), [])
    linked = _build_double_ll(nilai_list)
    _nilai_lists[_str(nim)] = linked
    displayed = linked.display()
    return displayed if displayed is not None else nilai_list
def hitung_ipk_mahasiswa(nim):
    """Hitung IPK mahasiswa secara rekursif (DoubleLL + hitung_ipk)."""
    if not nim:
        return None
    data = _as_dict(load_data("nilai.json"))
    nilai_list = data.get(_str(nim), [])
    if not nilai_list:
        return None
    akhir = [item.get("nilai_akhir", 0) for item in nilai_list if isinstance(item, dict)]
    if not akhir:
        return None
    # catatan: menggunakan rata-rata sederhana, bukan weighted by SKS
    total = hitung_ipk(akhir, 0, False)
    return round(total / len(akhir), 2)
def catat_log(aksi): """Catat aksi ke Stack log (Stack)."""; return False if not aksi else (_log_stack.push(aksi) or True)
def tampil_log(): """Tampilkan log aktivitas dari Stack (Stack)."""; return _log_stack.display() or []