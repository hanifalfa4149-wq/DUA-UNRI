"""
Entitas model SIAKAD Lite: Mahasiswa, MataKuliah, KRS, Nilai.

Setiap class mengimplementasikan:
- __init__  : inisialisasi atribut (dengan type hint)
- to_dict   : serialisasi ke dict (untuk JSON)
- from_dict : deserialisasi dari dict (classmethod)
- __str__   : representasi string untuk display CLI
"""

from typing import List, Optional


class Mahasiswa:
    """
    Representasi data mahasiswa.

    Attributes:
        nim      (str): Nomor Induk Mahasiswa, bersifat unik.
        nama     (str): Nama lengkap mahasiswa.
        id_prodi (str): Kode/ID program studi.
        angkatan (int): Tahun angkatan masuk.
    """

    def __init__(self, nim: str, nama: str, id_prodi: str, angkatan: int) -> None:
        """Inisialisasi objek Mahasiswa dengan atribut dasar."""
        self.nim: str = str(nim)
        self.nama: str = str(nama)
        self.id_prodi: str = str(id_prodi)
        self.angkatan: int = int(angkatan)

    def to_dict(self) -> dict:
        """Serialisasi Mahasiswa ke dict untuk penyimpanan JSON."""
        return {
            "nim": self.nim,
            "nama": self.nama,
            "id_prodi": self.id_prodi,
            "angkatan": self.angkatan,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Mahasiswa":
        """Buat instance Mahasiswa dari dict hasil load JSON."""
        return cls(
            nim=data.get("nim", ""),
            nama=data.get("nama", ""),
            id_prodi=data.get("id_prodi", ""),
            angkatan=data.get("angkatan", 0),
        )

    def __str__(self) -> str:
        """Representasi string ringkas Mahasiswa untuk display CLI."""
        return (
            f"[{self.nim}] {self.nama} | Prodi: {self.id_prodi} | Angkatan: {self.angkatan}"
        )


class MataKuliah:
    """
    Representasi data mata kuliah.

    Attributes:
        kode      (str)  : Kode unik mata kuliah.
        nama      (str)  : Nama mata kuliah.
        sks       (int)  : Jumlah SKS.
        semester  (int)  : Semester mata kuliah ditawarkan.
        tipe      (str)  : Tipe mata kuliah, contoh: 'wajib' atau 'pilihan'.
        prasyarat (list) : List kode mata kuliah yang menjadi prasyarat.
                           Default list kosong, diisi via tambah_prasyarat.
    """

    def __init__(
        self,
        kode: str,
        nama: str,
        sks: int,
        semester: int,
        tipe: str,
        prasyarat: Optional[List[str]] = None,
    ) -> None:
        """Inisialisasi objek MataKuliah. prasyarat opsional, default list kosong."""
        self.kode: str = str(kode)
        self.nama: str = str(nama)
        self.sks: int = int(sks)
        self.semester: int = int(semester)
        self.tipe: str = str(tipe)
        # Gunakan list baru jika prasyarat tidak diberikan (hindari mutable default arg)
        self.prasyarat: List[str] = list(prasyarat) if prasyarat is not None else []

    def to_dict(self) -> dict:
        """Serialisasi MataKuliah ke dict untuk penyimpanan JSON."""
        return {
            "kode": self.kode,
            "nama": self.nama,
            "sks": self.sks,
            "semester": self.semester,
            "tipe": self.tipe,
            "prasyarat": self.prasyarat,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MataKuliah":
        """Buat instance MataKuliah dari dict hasil load JSON."""
        return cls(
            kode=data.get("kode", ""),
            nama=data.get("nama", ""),
            sks=data.get("sks", 0),
            semester=data.get("semester", 0),
            tipe=data.get("tipe", ""),
            prasyarat=data.get("prasyarat", []),
        )

    def __str__(self) -> str:
        """Representasi string ringkas MataKuliah untuk display CLI."""
        prasyarat_str = ", ".join(self.prasyarat) if self.prasyarat else "-"
        return (
            f"[{self.kode}] {self.nama} | {self.sks} SKS | "
            f"Sem {self.semester} | {self.tipe} | Prasyarat: {prasyarat_str}"
        )


class KRS:
    """
    Representasi KRS (Kartu Rencana Studi) seorang mahasiswa.

    Attributes:
        nim          (str) : NIM mahasiswa pemilik KRS.
        list_kode_mk (list): List kode mata kuliah yang diambil.
    """

    def __init__(self, nim: str, list_kode_mk: Optional[List[str]] = None) -> None:
        """Inisialisasi objek KRS. list_kode_mk opsional, default list kosong."""
        self.nim: str = str(nim)
        # Salin list agar tidak berbagi referensi dengan pemanggil
        self.list_kode_mk: List[str] = list(list_kode_mk) if list_kode_mk is not None else []

    def to_dict(self) -> dict:
        """
        Serialisasi KRS ke dict.

        Catatan: services.py menyimpan krs.json sebagai dict { nim: [kode_mk] },
        sehingga to_dict mengembalikan representasi flat yang sama.
        """
        return {
            "nim": self.nim,
            "list_kode_mk": self.list_kode_mk,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "KRS":
        """Buat instance KRS dari dict hasil load JSON."""
        return cls(
            nim=data.get("nim", ""),
            list_kode_mk=data.get("list_kode_mk", []),
        )

    def __str__(self) -> str:
        """Representasi string KRS untuk display CLI."""
        mk_str = ", ".join(self.list_kode_mk) if self.list_kode_mk else "-"
        return f"KRS [{self.nim}] -> {mk_str}"


class Nilai:
    """
    Representasi nilai seorang mahasiswa untuk satu mata kuliah.

    Attributes:
        nim         (str)  : NIM mahasiswa.
        kode_mk     (str)  : Kode mata kuliah.
        tugas       (float): Nilai tugas (0-100).
        uts         (float): Nilai UTS (0-100).
        uas         (float): Nilai UAS (0-100).
        nilai_akhir (float): Nilai akhir hasil kalkulasi (dihitung di services).
        grade       (str)  : Grade huruf hasil konversi nilai akhir.
    """

    def __init__(
        self,
        nim: str,
        kode_mk: str,
        tugas: float,
        uts: float,
        uas: float,
        nilai_akhir: float,
        grade: str,
    ) -> None:
        """Inisialisasi objek Nilai dengan semua komponen penilaian."""
        self.nim: str = str(nim)
        self.kode_mk: str = str(kode_mk)
        self.tugas: float = float(tugas)
        self.uts: float = float(uts)
        self.uas: float = float(uas)
        self.nilai_akhir: float = float(nilai_akhir)
        self.grade: str = str(grade)

    def to_dict(self) -> dict:
        """Serialisasi Nilai ke dict untuk penyimpanan JSON."""
        return {
            "nim": self.nim,
            "kode_mk": self.kode_mk,
            "tugas": self.tugas,
            "uts": self.uts,
            "uas": self.uas,
            "nilai_akhir": self.nilai_akhir,
            "grade": self.grade,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Nilai":
        """Buat instance Nilai dari dict hasil load JSON."""
        return cls(
            nim=data.get("nim", ""),
            kode_mk=data.get("kode_mk", ""),
            tugas=data.get("tugas", 0.0),
            uts=data.get("uts", 0.0),
            uas=data.get("uas", 0.0),
            nilai_akhir=data.get("nilai_akhir", 0.0),
            grade=data.get("grade", "E"),
        )

    def __str__(self) -> str:
        """Representasi string Nilai untuk display CLI."""
        return (
            f"[{self.nim}] {self.kode_mk} | "
            f"Tugas: {self.tugas} UTS: {self.uts} UAS: {self.uas} | "
            f"Akhir: {self.nilai_akhir} ({self.grade})"
        )


# ---------------------------------------------------------------------------
# Demo isolated — jalankan: python models.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("DEMO models.py")
    print("=" * 50)

    # --- Mahasiswa ---
    print("\n[Mahasiswa]")
    mhs = Mahasiswa("2201001", "Andi Pratama", "TIF", 2022)
    print(mhs)
    d = mhs.to_dict()
    print("to_dict :", d)
    mhs2 = Mahasiswa.from_dict(d)
    print("from_dict:", mhs2)

    # --- MataKuliah ---
    print("\n[MataKuliah]")
    mk = MataKuliah("MK001", "Algoritma & Struktur Data", 3, 3, "wajib")
    print(mk)
    d = mk.to_dict()
    print("to_dict :", d)
    mk2 = MataKuliah.from_dict(d)
    print("from_dict:", mk2)

    mk_adv = MataKuliah("MK003", "Basis Data Lanjut", 3, 5, "wajib", ["MK001", "MK002"])
    print("dengan prasyarat:", mk_adv)

    # --- KRS ---
    print("\n[KRS]")
    krs = KRS("2201001", ["MK001", "MK002", "MK003"])
    print(krs)
    d = krs.to_dict()
    print("to_dict :", d)
    krs2 = KRS.from_dict(d)
    print("from_dict:", krs2)
    print("KRS kosong:", KRS("2201002"))

    # --- Nilai ---
    print("\n[Nilai]")
    nilai = Nilai("2201001", "MK001", 85.0, 78.0, 90.0, 84.9, "B")
    print(nilai)
    d = nilai.to_dict()
    print("to_dict :", d)
    nilai2 = Nilai.from_dict(d)
    print("from_dict:", nilai2)

    print("\n" + "=" * 50)
    print("Semua demo selesai tanpa error.")