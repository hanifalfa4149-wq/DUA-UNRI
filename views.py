"""Menu CLI untuk SIAKAD Lite."""

from services import (
    tambah_mahasiswa,
    lihat_semua_mahasiswa,
    cari_nim,
    cari_nama,
    sort_mahasiswa,
    hapus_mahasiswa,
    tambah_matkul,
    lihat_semua_matkul,
    tambah_prasyarat,
    lihat_prasyarat,
    ajukan_krs,
    proses_krs,
    lihat_krs,
    input_nilai,
    lihat_nilai,
    hitung_ipk_mahasiswa,
    catat_log,
    tampil_log,
)


def _header(title):
    """Cetak header menu."""
    print("=" * 40)
    print(title)


def _ok(msg):
    """Cetak pesan sukses."""
    print(f"✓ {msg}")


def _fail(msg):
    """Cetak pesan gagal."""
    print(f"✗ {msg}")


def _read_str(prompt):
    """Baca input string dengan strip."""
    return input(prompt).strip()


def _read_int(prompt):
    """Baca input angka int dengan validasi."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        _fail("Input angka tidak valid")
        return None


def _read_float(prompt):
    """Baca input angka float dengan validasi."""
    try:
        return float(input(prompt).strip())
    except ValueError:
        _fail("Input angka tidak valid")
        return None


def menu_mahasiswa():
    """Menu manajemen mahasiswa."""
    while True:
        _header("Menu Mahasiswa")
        print(
            "1. Tambah\n2. Lihat Semua\n3. Cari NIM\n4. Cari Nama\n5. Sort\n6. Hapus\n0. Kembali"
        )
        pilihan = _read_int("Pilih: ")
        if pilihan is None:
            continue
        if pilihan == 0:
            return
        if pilihan == 1:
            nim = _read_str("NIM: ")
            nama = _read_str("Nama: ")
            id_prodi = _read_str("ID Prodi: ")
            angkatan = _read_int("Angkatan: ")
            if angkatan is None:
                continue
            if tambah_mahasiswa(nim, nama, id_prodi, angkatan):
                catat_log(f"Tambah mahasiswa {nim}")
                _ok("Mahasiswa ditambahkan")
            else:
                _fail("Gagal menambah mahasiswa")
        elif pilihan == 2:
            data = lihat_semua_mahasiswa()
            if data:
                for item in data:
                    print(item)
                catat_log("Lihat semua mahasiswa")
                _ok("Data ditampilkan")
            else:
                _fail("Data mahasiswa kosong")
        elif pilihan == 3:
            nim = _read_str("NIM: ")
            data = cari_nim(nim)
            if data:
                print(data)
                catat_log(f"Cari mahasiswa NIM {nim}")
                _ok("Data ditemukan")
            else:
                _fail("Data tidak ditemukan")
        elif pilihan == 4:
            keyword = _read_str("Nama: ")
            data = cari_nama(keyword)
            if data:
                print(data)
                catat_log(f"Cari mahasiswa nama {keyword}")
                _ok("Data ditemukan")
            else:
                _fail("Data tidak ditemukan")
        elif pilihan == 5:
            mode = _read_int("Sort 1=Nama, 2=IPK: ")
            if mode is None:
                continue
            key = "nama" if mode == 1 else "ipk"
            data = sort_mahasiswa(key)
            if data:
                for item in data:
                    print(item)
                catat_log(f"Sort mahasiswa by {key}")
                _ok("Data diurutkan")
            else:
                _fail("Gagal sort data")
        elif pilihan == 6:
            nim = _read_str("NIM: ")
            if hapus_mahasiswa(nim):
                catat_log(f"Hapus mahasiswa {nim}")
                _ok("Mahasiswa dihapus")
            else:
                _fail("Gagal menghapus mahasiswa")
        else:
            _fail("Menu tidak valid")


def menu_matkul():
    """Menu manajemen mata kuliah."""
    while True:
        _header("Menu Mata Kuliah")
        print(
            "1. Tambah\n2. Lihat Semua\n3. Tambah Prasyarat\n4. Lihat Prasyarat\n0. Kembali"
        )
        pilihan = _read_int("Pilih: ")
        if pilihan is None:
            continue
        if pilihan == 0:
            return
        if pilihan == 1:
            kode = _read_str("Kode: ")
            nama = _read_str("Nama: ")
            sks = _read_int("SKS: ")
            semester = _read_int("Semester: ")
            tipe = _read_str("Tipe: ")
            if sks is None or semester is None:
                continue
            if tambah_matkul(kode, nama, sks, semester, tipe):
                catat_log(f"Tambah matkul {kode}")
                _ok("Mata kuliah ditambahkan")
            else:
                _fail("Gagal menambah mata kuliah")
        elif pilihan == 2:
            data = lihat_semua_matkul()
            if data:
                for item in data:
                    print(item)
                catat_log("Lihat semua matkul")
                _ok("Data ditampilkan")
            else:
                _fail("Data mata kuliah kosong")
        elif pilihan == 3:
            kode_mk = _read_str("Kode MK: ")
            kode_prasyarat = _read_str("Kode Prasyarat: ")
            if tambah_prasyarat(kode_mk, kode_prasyarat):
                catat_log(f"Tambah prasyarat {kode_mk}->{kode_prasyarat}")
                _ok("Prasyarat ditambahkan")
            else:
                _fail("Gagal menambah prasyarat")
        elif pilihan == 4:
            kode_mk = _read_str("Kode MK: ")
            data = lihat_prasyarat(kode_mk)
            if data:
                print(", ".join(data))
                catat_log(f"Lihat prasyarat {kode_mk}")
                _ok("Prasyarat ditampilkan")
            else:
                _fail("Prasyarat tidak ditemukan")
        else:
            _fail("Menu tidak valid")


def menu_krs():
    """Menu KRS."""
    while True:
        _header("Menu KRS")
        print("1. Ajukan KRS\n2. Proses KRS\n3. Lihat KRS\n0. Kembali")
        pilihan = _read_int("Pilih: ")
        if pilihan is None:
            continue
        if pilihan == 0:
            return
        if pilihan == 1:
            nim = _read_str("NIM: ")
            if ajukan_krs(nim):
                catat_log(f"Ajukan KRS {nim}")
                _ok("KRS diajukan")
            else:
                _fail("Gagal ajukan KRS")
        elif pilihan == 2:
            nim = _read_str("NIM: ")
            raw = _read_str("Kode MK (pisahkan koma): ")
            list_kode = [item.strip() for item in raw.split(",") if item.strip()]
            if proses_krs(nim, list_kode):
                catat_log(f"Proses KRS {nim}")
                _ok("KRS diproses")
            else:
                _fail("Gagal proses KRS")
        elif pilihan == 3:
            nim = _read_str("NIM: ")
            data = lihat_krs(nim)
            if data:
                for item in data:
                    print(item)
                catat_log(f"Lihat KRS {nim}")
                _ok("KRS ditampilkan")
            else:
                _fail("KRS tidak ditemukan")
        else:
            _fail("Menu tidak valid")


def menu_nilai():
    """Menu penilaian dan IPK."""
    while True:
        _header("Menu Nilai")
        print("1. Input Nilai\n2. Lihat Nilai\n3. Hitung IPK\n0. Kembali")
        pilihan = _read_int("Pilih: ")
        if pilihan is None:
            continue
        if pilihan == 0:
            return
        if pilihan == 1:
            nim = _read_str("NIM: ")
            kode_mk = _read_str("Kode MK: ")
            tugas = _read_float("Tugas: ")
            uts = _read_float("UTS: ")
            uas = _read_float("UAS: ")
            if None in (tugas, uts, uas):
                continue
            if input_nilai(nim, kode_mk, tugas, uts, uas):
                catat_log(f"Input nilai {nim}-{kode_mk}")
                _ok("Nilai disimpan")
            else:
                _fail("Gagal simpan nilai")
        elif pilihan == 2:
            nim = _read_str("NIM: ")
            data = lihat_nilai(nim)
            if data:
                for item in data:
                    print(item)
                catat_log(f"Lihat nilai {nim}")
                _ok("Nilai ditampilkan")
            else:
                _fail("Nilai tidak ditemukan")
        elif pilihan == 3:
            nim = _read_str("NIM: ")
            ipk = hitung_ipk_mahasiswa(nim)
            if ipk is not None:
                print(f"IPK: {ipk}")
                catat_log(f"Hitung IPK {nim}")
                _ok("IPK dihitung")
            else:
                _fail("Gagal hitung IPK")
        else:
            _fail("Menu tidak valid")


def menu_log():
    """Menu aktivitas log."""
    _header("Activity Log")
    data = tampil_log()
    if data:
        for item in data:
            print(item)
        _ok("Log ditampilkan")
    else:
        _fail("Log kosong")


def menu_utama():
    """Menu utama aplikasi."""
    while True:
        _header("SIAKAD Lite")
        print("1. Mahasiswa\n2. Mata Kuliah\n3. KRS\n4. Nilai\n5. Log\n0. Keluar")
        pilihan = _read_int("Pilih: ")
        if pilihan is None:
            continue
        if pilihan == 0:
            _ok("Keluar")
            return
        if pilihan == 1:
            menu_mahasiswa()
        elif pilihan == 2:
            menu_matkul()
        elif pilihan == 3:
            menu_krs()
        elif pilihan == 4:
            menu_nilai()
        elif pilihan == 5:
            menu_log()
        else:
            _fail("Menu tidak valid")


if __name__ == "__main__":
    menu_utama()
