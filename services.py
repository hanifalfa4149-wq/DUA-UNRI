"""Business logic DUA UNRI: file handler, mahasiswa, matkul, KRS, nilai, log."""

import json
import os

from models import Mahasiswa, MataKuliah, Nilai
from structures.hash_table import HashTable
from structures.linked_list import SingleLL, DoubleLL, CircularLL
from structures.stack_queue import Stack, Queue
from structures.tree_graph import Tree, Graph
from algoritma import bubble_sort, linear_search, hitung_ipk


# ---------------------------------------------------------------------------
# Inisialisasi struktur data global
# ---------------------------------------------------------------------------

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_DIR = os.path.join(_BASE_DIR, "data")

_mahasiswa_table = HashTable()   # lookup mahasiswa by NIM — HashTable
_krs_queue       = Queue()       # antrian pengajuan KRS — Queue
_log_stack       = Stack()       # riwayat aktivitas — Stack
_prasyarat_graph = Graph()       # relasi prasyarat antar matkul — Graph
_academic_tree   = Tree("UNRI")  # hierarki Fakultas -> Prodi -> Mahasiswa — Tree
_krs_lists       = {}            # { nim: SingleLL } daftar matkul per mahasiswa
_nilai_lists     = {}            # { nim: DoubleLL } riwayat nilai per mahasiswa


# ---------------------------------------------------------------------------
# File Handler — baca dan tulis data JSON
# ---------------------------------------------------------------------------

def buat_path(nama_file):
    """Buat path lengkap ke file JSON di folder data/."""
    os.makedirs(_DATA_DIR, exist_ok=True)
    return os.path.join(_DATA_DIR, nama_file)


def load_data(nama_file):
    """Baca data dari file JSON, return list atau dict kosong jika gagal."""
    path = buat_path(nama_file)
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, (list, dict)) else []
    except Exception:
        return []


def save_data(nama_file, data):
    """Simpan data ke file JSON, return True jika berhasil."""
    try:
        with open(buat_path(nama_file), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Helper internal
# ---------------------------------------------------------------------------

def pastikan_list(data):
    """Pastikan data bertipe list, kalau bukan return list kosong."""
    return data if isinstance(data, list) else []


def pastikan_dict(data):
    """Pastikan data bertipe dict, kalau bukan return dict kosong."""
    return data if isinstance(data, dict) else {}


def konversi_grade(nilai):
    """Konversi nilai angka ke grade huruf A-E."""
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 60:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def bangun_ulang_hash_table():
    """Baca semua mahasiswa dari file, masukkan ke HashTable (HashTable)."""
    global _mahasiswa_table
    _mahasiswa_table = HashTable()
    semua = pastikan_list(load_data("mahasiswa.json"))
    for item in semua:
        if isinstance(item, dict) and item.get("nim"):
            _mahasiswa_table.insert(str(item["nim"]), item)


# ---------------------------------------------------------------------------
# Manajemen Mahasiswa
# ---------------------------------------------------------------------------

def tambah_mahasiswa(nim, nama, id_prodi, angkatan):
    """Tambah mahasiswa baru ke file JSON dan HashTable."""
    if not all([nim, nama, id_prodi, angkatan]):
        return False

    data = pastikan_list(load_data("mahasiswa.json"))
    nim  = str(nim)

    # Cek duplikasi NIM
    nim_sudah_ada = any(str(i.get("nim")) == nim for i in data if isinstance(i, dict))
    if nim_sudah_ada:
        return False

    mahasiswa_baru = Mahasiswa(nim, nama, id_prodi, angkatan)
    data.append(mahasiswa_baru.to_dict())

    if not save_data("mahasiswa.json", data):
        return False

    bangun_ulang_hash_table()
    return mahasiswa_baru.to_dict()


def lihat_semua_mahasiswa():
    """Ambil semua data mahasiswa dari file JSON (List)."""
    return pastikan_list(load_data("mahasiswa.json"))


def cari_nim(nim):
    """Cari mahasiswa berdasarkan NIM menggunakan HashTable."""
    if not nim:
        return None
    bangun_ulang_hash_table()
    return _mahasiswa_table.search(str(nim))


def cari_nama(keyword):
    """Cari mahasiswa berdasarkan nama menggunakan linear search (Searching)."""
    if not keyword:
        return None
    semua = pastikan_list(load_data("mahasiswa.json"))
    return linear_search(semua, keyword, "nama")


def sort_mahasiswa(key):
    """Urutkan daftar mahasiswa berdasarkan key menggunakan bubble sort (Sorting)."""
    if not key:
        return []
    semua = pastikan_list(load_data("mahasiswa.json"))
    return bubble_sort(semua, key)


def hapus_mahasiswa(nim):
    """Hapus mahasiswa dari file JSON dan HashTable."""
    if not nim:
        return False

    nim  = str(nim)
    data = pastikan_list(load_data("mahasiswa.json"))

    # Filter — ambil semua kecuali yang NIM-nya sama
    data_baru = [i for i in data if str(i.get("nim")) != nim]

    # Kalau panjangnya sama berarti NIM tidak ditemukan
    if len(data_baru) == len(data):
        return False

    if not save_data("mahasiswa.json", data_baru):
        return False

    bangun_ulang_hash_table()
    return True


def jelajahi_mahasiswa():
    """Masukkan semua mahasiswa ke CircularLL untuk navigasi loop (CircularLL)."""
    semua = pastikan_list(load_data("mahasiswa.json"))
    if not semua:
        return []

    linked = CircularLL()
    for item in semua:
        linked.append(item)

    return linked.display()


# ---------------------------------------------------------------------------
# Manajemen Mata Kuliah
# ---------------------------------------------------------------------------

def tambah_matkul(kode, nama, sks, semester, tipe):
    """Tambah mata kuliah baru ke file JSON (List)."""
    if not all([kode, nama, tipe]) or sks is None or semester is None:
        return False

    data = pastikan_list(load_data("matakuliah.json"))
    kode = str(kode)

    # Cek duplikasi kode
    kode_sudah_ada = any(str(i.get("kode")) == kode for i in data if isinstance(i, dict))
    if kode_sudah_ada:
        return False

    matkul_baru = MataKuliah(kode, nama, sks, semester, tipe)
    data.append(matkul_baru.to_dict())

    if not save_data("matakuliah.json", data):
        return False

    return matkul_baru.to_dict()


def lihat_semua_matkul():
    """Ambil semua mata kuliah dari file JSON (List)."""
    return pastikan_list(load_data("matakuliah.json"))


def tambah_prasyarat(kode_mk, kode_prasyarat):
    """Tambah relasi prasyarat antar matkul ke Graph dan file JSON (Graph)."""
    if not all([kode_mk, kode_prasyarat]):
        return False

    kode_mk        = str(kode_mk)
    kode_prasyarat = str(kode_prasyarat)
    data           = pastikan_list(load_data("matakuliah.json"))
    ditemukan      = False

    for item in data:
        if str(item.get("kode")) == kode_mk:
            prasyarat = item.get("prasyarat", [])
            if kode_prasyarat not in prasyarat:
                prasyarat.append(kode_prasyarat)
                item["prasyarat"] = prasyarat
            ditemukan = True
            break

    if not ditemukan:
        return False

    # Tambahkan ke Graph juga agar bisa di-query via get_neighbors
    _prasyarat_graph.add_vertex(kode_mk)
    _prasyarat_graph.add_vertex(kode_prasyarat)
    _prasyarat_graph.add_edge(kode_mk, kode_prasyarat)

    return save_data("matakuliah.json", data)


def lihat_prasyarat(kode_mk):
    """Ambil daftar prasyarat sebuah matkul dari Graph (Graph)."""
    if not kode_mk:
        return []

    kode_mk   = str(kode_mk)
    neighbors = _prasyarat_graph.get_neighbors(kode_mk)

    # Kalau sudah ada di Graph, pakai itu
    if neighbors:
        return neighbors

    # Fallback: baca dari file JSON
    for item in pastikan_list(load_data("matakuliah.json")):
        if str(item.get("kode")) == kode_mk:
            return item.get("prasyarat", [])

    return []


# ---------------------------------------------------------------------------
# Struktur Akademik — Tree
# ---------------------------------------------------------------------------

def tambah_node_tree(parent, child):
    """Tambah node baru ke Tree hierarki akademik (Tree)."""
    if not all([parent, child]):
        return False
    return bool(_academic_tree.insert(str(parent), str(child)))


def tampil_tree():
    """Tampilkan hierarki Tree akademik ke terminal (Tree)."""
    _academic_tree.display()


# ---------------------------------------------------------------------------
# KRS
# ---------------------------------------------------------------------------

def ajukan_krs(nim):
    """Masukkan NIM mahasiswa ke antrian KRS (Queue)."""
    if not nim or not cari_nim(nim):
        return False
    _krs_queue.enqueue(str(nim))
    return True


def proses_krs(nim, list_kode_mk):
    """Ambil NIM dari antrian, simpan daftar matkul ke SingleLL (Queue + SingleLL)."""
    if not all([nim, list_kode_mk]) or _krs_queue.is_empty():
        return False

    nim        = str(nim)
    nim_antrian = str(_krs_queue.dequeue())

    # Pastikan yang diproses sesuai antrian
    if nim_antrian != nim:
        return False

    # Masukkan tiap kode matkul ke SingleLL
    linked = SingleLL()
    for kode in list_kode_mk:
        linked.append(str(kode))

    _krs_lists[nim] = linked

    # Simpan ke file juga
    data      = pastikan_dict(load_data("krs.json"))
    data[nim] = [str(k) for k in list_kode_mk]

    return save_data("krs.json", data)


def lihat_krs(nim):
    """Tampilkan daftar matkul mahasiswa dari SingleLL (SingleLL)."""
    if not nim:
        return []

    nim       = str(nim)
    kode_list = pastikan_dict(load_data("krs.json")).get(nim, [])

    # Bangun SingleLL dari data file
    linked = SingleLL()
    for kode in kode_list:
        linked.append(kode)

    _krs_lists[nim] = linked
    return linked.display() or kode_list


# ---------------------------------------------------------------------------
# Penilaian
# ---------------------------------------------------------------------------

def input_nilai(nim, kode_mk, tugas, uts, uas):
    """Input nilai mahasiswa, hitung nilai akhir, simpan ke file dan DoubleLL (DoubleLL)."""
    if not all([nim, kode_mk]):
        return False

    # Validasi tipe dan range nilai
    try:
        tugas = float(tugas)
        uts   = float(uts)
        uas   = float(uas)
    except (TypeError, ValueError):
        return False

    if not all(0 <= v <= 100 for v in [tugas, uts, uas]):
        return False

    # Hitung nilai akhir dengan bobot tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = round(tugas * 0.3 + uts * 0.3 + uas * 0.4, 2)
    grade       = konversi_grade(nilai_akhir)

    # Buat objek Nilai dan simpan ke file
    nilai_baru = Nilai(str(nim), str(kode_mk), tugas, uts, uas, nilai_akhir, grade)
    payload    = nilai_baru.to_dict()

    data       = pastikan_dict(load_data("nilai.json"))
    nim        = str(nim)
    nilai_list = data.get(nim, [])
    nilai_list.append(payload)
    data[nim]  = nilai_list

    if not save_data("nilai.json", data):
        return False

    # Masukkan semua nilai ke DoubleLL untuk navigasi prev/next
    linked = DoubleLL()
    for item in nilai_list:
        linked.append(item)
    _nilai_lists[nim] = linked

    return payload


def lihat_nilai(nim):
    """Tampilkan riwayat nilai mahasiswa dari DoubleLL (DoubleLL)."""
    if not nim:
        return []

    nim        = str(nim)
    nilai_list = pastikan_dict(load_data("nilai.json")).get(nim, [])

    # Bangun DoubleLL dari data file
    linked = DoubleLL()
    for item in nilai_list:
        linked.append(item)

    _nilai_lists[nim] = linked
    return linked.display() or nilai_list


def hitung_ipk_mahasiswa(nim):
    """Hitung IPK mahasiswa secara rekursif dari daftar nilai akhir (Rekursif)."""
    if not nim:
        return None

    nilai_list = pastikan_dict(load_data("nilai.json")).get(str(nim), [])
    if not nilai_list:
        return None

    # Ambil semua nilai_akhir, hitung total secara rekursif
    daftar_nilai_akhir = [i.get("nilai_akhir", 0) for i in nilai_list if isinstance(i, dict)]
    if not daftar_nilai_akhir:
        return None

    # Catatan: menggunakan rata-rata sederhana, bukan weighted by SKS
    total = hitung_ipk(daftar_nilai_akhir, 0)
    return round(total / len(daftar_nilai_akhir), 2)


# ---------------------------------------------------------------------------
# Activity Log
# ---------------------------------------------------------------------------

def catat_log(aksi):
    """Catat aktivitas ke Stack log (Stack)."""
    if not aksi:
        return False
    _log_stack.push(aksi)
    return True


def tampil_log():
    """Tampilkan semua log aktivitas dari Stack, terbaru di atas (Stack)."""
    return _log_stack.display() or []