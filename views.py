"""Tampilan menu CLI untuk DUA UNRI."""

import services

# ---------------------------------------------------------------------------
# Helper tampilan & input
# ---------------------------------------------------------------------------

def garis():
    """Cetak garis pemisah."""
    print("=" * 40)


def sukses(pesan):
    """Cetak pesan sukses."""
    print(f"{pesan}")


def gagal(pesan):
    """Cetak pesan gagal."""
    print(f"{pesan}")


def tanya(prompt):
    """Minta input teks dari user."""
    return input(prompt).strip()


def tanya_angka(prompt):
    """Minta input angka bulat dari user, return None jika tidak valid."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        gagal("Input harus berupa angka")
        return None


def tanya_desimal(prompt):
    """Minta input angka desimal dari user, return None jika tidak valid."""
    try:
        return float(input(prompt).strip())
    except ValueError:
        gagal("Input harus berupa angka")
        return None


# ---------------------------------------------------------------------------
# Menu Mahasiswa
# ---------------------------------------------------------------------------

def menu_mahasiswa():
    """Menu untuk kelola data mahasiswa."""
    while True:
        garis()
        print("MENU MAHASISWA")
        print("1. Tambah mahasiswa")
        print("2. Lihat semua mahasiswa")
        print("3. Cari mahasiswa by NIM")
        print("4. Cari mahasiswa by nama")
        print("5. Urutkan mahasiswa")
        print("6. Hapus mahasiswa")
        print("7. Jelajahi data (Circular LL)")
        print("0. Kembali")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            return

        elif pilihan == 1:
            nim      = tanya("NIM       : ")
            nama     = tanya("Nama      : ")
            id_prodi = tanya("ID Prodi  : ")
            angkatan = tanya_angka("Angkatan  : ")
            if angkatan is None:
                continue
            hasil = services.tambah_mahasiswa(nim, nama, id_prodi, angkatan)
            if hasil:
                services.catat_log(f"Tambah mahasiswa {nim}")
                sukses("Mahasiswa berhasil ditambahkan")
            else:
                gagal("Gagal — NIM mungkin sudah terdaftar atau data tidak lengkap")

        elif pilihan == 2:
            data = services.lihat_semua_mahasiswa()
            if data:
                garis()
                for item in data:
                    print(item)
                services.catat_log("Lihat semua mahasiswa")
                sukses(f"{len(data)} mahasiswa ditampilkan")
            else:
                gagal("Belum ada data mahasiswa")

        elif pilihan == 3:
            nim  = tanya("NIM: ")
            data = services.cari_nim(nim)
            if data:
                print(data)
                services.catat_log(f"Cari NIM {nim}")
                sukses("Mahasiswa ditemukan")
            else:
                gagal("Mahasiswa tidak ditemukan")

        elif pilihan == 4:
            nama = tanya("Nama: ")
            data = services.cari_nama(nama)
            if data:
                print(data)
                services.catat_log(f"Cari nama {nama}")
                sukses("Mahasiswa ditemukan")
            else:
                gagal("Mahasiswa tidak ditemukan")

        elif pilihan == 5:
            print("Urutkan berdasarkan:")
            print("1. Nama")
            print("2. IPK")
            mode = tanya_angka("Pilih: ")
            if mode is None:
                continue
            key  = "nama" if mode == 1 else "ipk"
            data = services.sort_mahasiswa(key)
            if data:
                garis()
                for item in data:
                    print(item)
                services.catat_log(f"Sort mahasiswa by {key}")
                sukses("Data berhasil diurutkan")
            else:
                gagal("Tidak ada data untuk diurutkan")

        elif pilihan == 6:
            nim = tanya("NIM mahasiswa yang dihapus: ")
            if services.hapus_mahasiswa(nim):
                services.catat_log(f"Hapus mahasiswa {nim}")
                sukses("Mahasiswa berhasil dihapus")
            else:
                gagal("Mahasiswa tidak ditemukan")

        elif pilihan == 7:
            data = services.jelajahi_mahasiswa()
            if not data:
                gagal("Belum ada data mahasiswa")
                continue
            print("\nJelajahi data — Enter untuk lanjut, 'q' untuk keluar")
            garis()
            for item in data:
                print(item)
                cmd = tanya("").lower()
                if cmd == "q":
                    break
            services.catat_log("Jelajahi mahasiswa circular")
            sukses("Selesai menjelajahi data")

        else:
            gagal("Pilihan tidak tersedia")


# ---------------------------------------------------------------------------
# Menu Mata Kuliah
# ---------------------------------------------------------------------------

def menu_matkul():
    """Menu untuk kelola data mata kuliah."""
    while True:
        garis()
        print("MENU MATA KULIAH")
        print("1. Tambah mata kuliah")
        print("2. Lihat semua mata kuliah")
        print("3. Tambah prasyarat")
        print("4. Lihat prasyarat")
        print("0. Kembali")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            return

        elif pilihan == 1:
            kode     = tanya("Kode MK   : ")
            nama     = tanya("Nama MK   : ")
            sks      = tanya_angka("SKS       : ")
            semester = tanya_angka("Semester  : ")
            tipe     = tanya("Tipe (wajib/pilihan): ")
            if sks is None or semester is None:
                continue
            if services.tambah_matkul(kode, nama, sks, semester, tipe):
                services.catat_log(f"Tambah matkul {kode}")
                sukses("Mata kuliah berhasil ditambahkan")
            else:
                gagal("Gagal — kode mungkin sudah ada atau data tidak lengkap")

        elif pilihan == 2:
            data = services.lihat_semua_matkul()
            if data:
                garis()
                for item in data:
                    print(item)
                services.catat_log("Lihat semua matkul")
                sukses(f"{len(data)} mata kuliah ditampilkan")
            else:
                gagal("Belum ada data mata kuliah")

        elif pilihan == 3:
            kode_mk       = tanya("Kode MK          : ")
            kode_prasyarat = tanya("Kode prasyaratnya: ")
            if services.tambah_prasyarat(kode_mk, kode_prasyarat):
                services.catat_log(f"Tambah prasyarat {kode_mk}->{kode_prasyarat}")
                sukses("Prasyarat berhasil ditambahkan")
            else:
                gagal("Gagal — pastikan kode MK sudah terdaftar")

        elif pilihan == 4:
            kode_mk = tanya("Kode MK: ")
            data    = services.lihat_prasyarat(kode_mk)
            if data:
                print(f"Prasyarat {kode_mk}: {', '.join(data)}")
                services.catat_log(f"Lihat prasyarat {kode_mk}")
                sukses("Prasyarat ditampilkan")
            else:
                gagal("Tidak ada prasyarat untuk mata kuliah ini")

        else:
            gagal("Pilihan tidak tersedia")


# ---------------------------------------------------------------------------
# Menu KRS
# ---------------------------------------------------------------------------

def menu_krs():
    """Menu untuk kelola KRS mahasiswa."""
    while True:
        garis()
        print("MENU KRS")
        print("1. Ajukan KRS (masuk antrian)")
        print("2. Proses KRS (ambil dari antrian)")
        print("3. Lihat KRS mahasiswa")
        print("0. Kembali")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            return

        elif pilihan == 1:
            nim = tanya("NIM: ")
            if services.ajukan_krs(nim):
                services.catat_log(f"Ajukan KRS {nim}")
                sukses("KRS masuk antrian")
            else:
                gagal("Gagal — NIM tidak ditemukan atau belum terdaftar")

        elif pilihan == 2:
            nim = tanya("NIM yang diproses: ")
            raw = tanya("Kode MK yang diambil (pisah koma, contoh: MK001,MK002): ")
            list_kode = [k.strip() for k in raw.split(",") if k.strip()]
            if services.proses_krs(nim, list_kode):
                services.catat_log(f"Proses KRS {nim}")
                sukses("KRS berhasil diproses")
            else:
                gagal("Gagal — pastikan NIM sudah ada di antrian")

        elif pilihan == 3:
            nim  = tanya("NIM: ")
            data = services.lihat_krs(nim)
            if data:
                garis()
                print(f"KRS mahasiswa {nim}:")
                for kode in data:
                    print(f"  - {kode}")
                services.catat_log(f"Lihat KRS {nim}")
                sukses("KRS ditampilkan")
            else:
                gagal("KRS belum ada untuk mahasiswa ini")

        else:
            gagal("Pilihan tidak tersedia")


# ---------------------------------------------------------------------------
# Menu Nilai
# ---------------------------------------------------------------------------

def menu_nilai():
    """Menu untuk input dan lihat nilai mahasiswa."""
    while True:
        garis()
        print("MENU NILAI")
        print("1. Input nilai")
        print("2. Lihat nilai mahasiswa")
        print("3. Hitung IPK")
        print("0. Kembali")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            return

        elif pilihan == 1:
            nim     = tanya("NIM      : ")
            kode_mk = tanya("Kode MK  : ")
            tugas   = tanya_desimal("Tugas    : ")
            uts     = tanya_desimal("UTS      : ")
            uas     = tanya_desimal("UAS      : ")
            if None in (tugas, uts, uas):
                continue
            if services.input_nilai(nim, kode_mk, tugas, uts, uas):
                services.catat_log(f"Input nilai {nim} - {kode_mk}")
                sukses("Nilai berhasil disimpan")
            else:
                gagal("Gagal — pastikan nilai antara 0-100")

        elif pilihan == 2:
            nim  = tanya("NIM: ")
            data = services.lihat_nilai(nim)
            if data:
                garis()
                for item in data:
                    print(item)
                services.catat_log(f"Lihat nilai {nim}")
                sukses("Nilai ditampilkan")
            else:
                gagal("Belum ada nilai untuk mahasiswa ini")

        elif pilihan == 3:
            nim = tanya("NIM: ")
            ipk = services.hitung_ipk_mahasiswa(nim)
            if ipk is not None:
                garis()
                print(f"IPK mahasiswa {nim}: {ipk}")
                services.catat_log(f"Hitung IPK {nim}")
                sukses("IPK berhasil dihitung")
            else:
                gagal("Belum ada nilai untuk dihitung")

        else:
            gagal("Pilihan tidak tersedia")


# ---------------------------------------------------------------------------
# Menu Log
# ---------------------------------------------------------------------------

def menu_log():
    """Tampilkan riwayat aktivitas dari Stack."""
    garis()
    print("ACTIVITY LOG (terbaru di atas)")
    garis()
    data = services.tampil_log()
    if data:
        for item in data:
            print(f"  {item}")
        sukses(f"{len(data)} aktivitas tercatat")
    else:
        gagal("Log masih kosong")


# ---------------------------------------------------------------------------
# Menu Struktur Akademik
# ---------------------------------------------------------------------------

def menu_struktur_akademik():
    """Menu untuk kelola hierarki akademik via Tree."""
    while True:
        garis()
        print("MENU STRUKTUR AKADEMIK (Tree)")
        print("1. Tambah node (contoh: Fakultas -> Prodi)")
        print("2. Tampilkan hierarki")
        print("0. Kembali")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            return

        elif pilihan == 1:
            parent = tanya("Parent (contoh: UNRI atau FT): ")
            child  = tanya("Child  (contoh: FT atau Informatika): ")
            if services.tambah_node_tree(parent, child):
                services.catat_log(f"Tambah node {parent} -> {child}")
                sukses("Node berhasil ditambahkan")
            else:
                gagal("Gagal — pastikan parent sudah ada di Tree")

        elif pilihan == 2:
            garis()
            print("Hierarki Akademik:")
            services.tampil_tree()
            services.catat_log("Tampilkan struktur akademik")

        else:
            gagal("Pilihan tidak tersedia")


# ---------------------------------------------------------------------------
# Menu Utama
# ---------------------------------------------------------------------------

def menu_utama():
    """Menu utama — pintu masuk semua fitur DUA UNRI."""
    while True:
        garis()
        print("DUA UNRI — Sistem Informasi Akademik")
        print("1. Mahasiswa")
        print("2. Mata Kuliah")
        print("3. KRS")
        print("4. Nilai & IPK")
        print("5. Activity Log")
        print("6. Struktur Akademik")
        print("0. Keluar")

        pilihan = tanya_angka("Pilih menu: ")
        if pilihan is None:
            continue

        if pilihan == 0:
            sukses("Sampai jumpa!")
            return
        elif pilihan == 1:
            menu_mahasiswa()
        elif pilihan == 2:
            menu_matkul()
        elif pilihan == 3:
            menu_krs()
        elif pilihan == 4:
            menu_nilai()
        elif pilihan == 5:
            menu_log()
        elif pilihan == 6:
            menu_struktur_akademik()
        else:
            gagal("Pilihan tidak tersedia")


if __name__ == "__main__":
    menu_utama()