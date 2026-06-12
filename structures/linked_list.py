# structures/linked_list.py
# Anggota 1 — DUA UNRI Capstone Project
# Single Linked List, Double Linked List, Circular Linked List


# ================================================================
#  SINGLE LINKED LIST
#
#  Setiap node hanya tahu satu hal: siapa node BERIKUTNYA.
#  Tidak bisa balik — kalau sudah lewat, tidak bisa ke belakang.
#
#  Di DUA UNRI, Single LL dipakai untuk menyimpan daftar mata kuliah
#  per mahasiswa (KRS) — ukurannya tidak tetap, dinamis.
#
#  Visualisasi:
#
#    HEAD  →  [Hanif|next]  →  [Habib|next]  →  [Riva|next]  →  None
#             (pertama)                         (terakhir)
#
#  Operasi utama:
#    append()  →  O(n)  tambah di belakang (harus jalan dulu ke ujung)
#    delete()  →  O(n)  hapus node (harus cari dulu)
#    search()  →  O(n)  cari data (harus cek satu per satu)
# ================================================================

class SLLNode:
    """Satu kotak/node dalam Single Linked List."""

    def __init__(self, data):
        # data  → isi dari node ini
        # next  → pointer ke node berikutnya, None kalau ini yang terakhir
        self.data = data
        self.next = None


class SingleLL:
    """
    Single Linked List — rantai node satu arah.
    Dipakai untuk daftar mata kuliah per mahasiswa di DUA UNRI.
    """

    def __init__(self):
        # head → node pertama dalam list, None kalau list masih kosong
        self.head = None

    def append(self, data):
        """Tambah data baru di paling belakang list."""
        node_baru = SLLNode(data)

        # kalau list masih kosong, node baru langsung jadi head
        if self.head is None:
            self.head = node_baru
            return

        # kalau sudah ada isi, jalan terus sampai node paling akhir
        # node terakhir adalah node yang next-nya None
        node_sekarang = self.head
        while node_sekarang.next is not None:   # selama masih ada next, terus jalan
            node_sekarang = node_sekarang.next  # pindah ke node berikutnya

        # node_sekarang sekarang adalah node terakhir — sambungkan ke node baru
        node_sekarang.next = node_baru

    def delete(self, data):
        """Hapus node pertama yang datanya cocok. Return True kalau berhasil."""
        # list kosong — tidak ada yang bisa dihapus
        if self.head is None:
            return False

        # kasus khusus: node yang mau dihapus adalah head
        if self.head.data == data:
            self.head = self.head.next  # head pindah ke node kedua
            return True

        # kalau bukan head, kita butuh lacak node SEBELUMNYA (prev)
        # supaya bisa "bypass" node yang dihapus
        #
        #  sebelum hapus:  prev → target → selanjutnya
        #  sesudah hapus:  prev → selanjutnya   (target dilewati)
        #
        prev = self.head
        node_sekarang = self.head.next

        while node_sekarang is not None:
            if node_sekarang.data == data:
                prev.next = node_sekarang.next  # bypass / lompati node target
                return True
            prev = node_sekarang                # geser prev
            node_sekarang = node_sekarang.next  # geser node_sekarang

        return False  # data tidak ditemukan

    def search(self, data):
        """Cari data dalam list. Return True kalau ketemu, False kalau tidak."""
        node_sekarang = self.head
        while node_sekarang is not None:
            if node_sekarang.data == data:
                return True
            node_sekarang = node_sekarang.next
        return False

    def display(self):
        """Tampilkan semua isi list dari head ke belakang."""
        if self.head is None:
            print("  [Single LL kosong]")
            return

        node_sekarang = self.head
        isi = []
        while node_sekarang is not None:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next

        print("  " + " -> ".join(isi) + " -> None")


# ================================================================
#  DOUBLE LINKED LIST
#
#  Setiap node punya DUA pointer: ke node SEBELUMNYA (prev)
#  dan ke node BERIKUTNYA (next).
#  Beda dari Single LL — bisa jalan maju DAN mundur.
#
#  Di DUA UNRI, Double LL dipakai untuk navigasi riwayat nilai:
#  bisa scroll ke nilai sebelumnya (prev) atau berikutnya (next).
#
#  Visualisasi:
#
#    HEAD                                              TAIL
#     ↓                                                ↓
#    [prev=None|A|next]  ↔  [prev|B|next]  ↔  [prev|C|next=None]
#
#  Operasi utama:
#    append()           →  O(1)  tambah di belakang (langsung lewat tail)
#    delete()           →  O(n)  hapus node (harus cari dulu)
#    traverse_backward()→  O(n)  jalan dari tail ke head
# ================================================================

class DLLNode:
    """Satu kotak/node dalam Double Linked List."""

    def __init__(self, data):
        # data  → isi dari node ini
        # prev  → pointer ke node SEBELUMNYA
        # next  → pointer ke node BERIKUTNYA
        self.data = data
        self.prev = None
        self.next = None


class DoubleLL:
    """
    Double Linked List — rantai node dua arah.
    Dipakai untuk navigasi riwayat nilai di DUA UNRI.
    """

    def __init__(self):
        # head → node pertama
        # tail → node terakhir (disimpan agar append bisa O(1))
        self.head = None
        self.tail = None

    def append(self, data):
        """Tambah data baru di paling belakang list."""
        node_baru = DLLNode(data)

        # list masih kosong — node baru jadi head sekaligus tail
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            return

        # sambungkan node baru ke tail yang lama
        # sebelum: ... → [tail_lama] → None
        # sesudah: ... → [tail_lama] ↔ [node_baru] → None
        node_baru.prev = self.tail      # node baru lihat ke belakang (tail lama)
        self.tail.next = node_baru      # tail lama lihat ke depan (node baru)
        self.tail = node_baru           # update tail ke node baru

    def delete(self, data):
        """Hapus node pertama yang datanya cocok. Return True kalau berhasil."""
        node_sekarang = self.head

        while node_sekarang is not None:
            if node_sekarang.data == data:

                # sambungkan prev dan next dari node yang dihapus
                # supaya rantai tidak putus
                if node_sekarang.prev is not None:
                    node_sekarang.prev.next = node_sekarang.next
                else:
                    # node ini adalah head — geser head ke node berikutnya
                    self.head = node_sekarang.next

                if node_sekarang.next is not None:
                    node_sekarang.next.prev = node_sekarang.prev
                else:
                    # node ini adalah tail — geser tail ke node sebelumnya
                    self.tail = node_sekarang.prev

                return True

            node_sekarang = node_sekarang.next

        return False  # data tidak ditemukan

    def display(self):
        """Tampilkan list dari head ke tail (maju)."""
        if self.head is None:
            print("  [Double LL kosong]")
            return

        node_sekarang = self.head
        isi = []
        while node_sekarang is not None:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next

        print("  None ← " + " ↔ ".join(isi) + " → None")

    def traverse_backward(self):
        """Tampilkan list dari tail ke head (mundur)."""
        if self.tail is None:
            print("  [Double LL kosong]")
            return

        node_sekarang = self.tail
        isi = []
        while node_sekarang is not None:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.prev  # jalan mundur lewat prev

        print("  None ← " + " ↔ ".join(isi) + " → None  [MUNDUR]")


# ================================================================
#  CIRCULAR LINKED LIST
#
#  Sama seperti Single LL, tapi node TERAKHIR tidak menunjuk ke None —
#  melainkan menunjuk kembali ke HEAD. Membentuk lingkaran.
#
#  Di DUA UNRI, Circular LL dipakai untuk navigasi carousel di views:
#  menu terus berputar dan tidak ada ujungnya.
#
#  Visualisasi:
#
#    HEAD
#     ↓
#    [Senin] → [Selasa] → [Rabu] → [Kamis]
#       ↑_________________________________|
#                  (kembali ke head)
#
#  Operasi utama:
#    append()       →  O(n)  tambah di belakang (harus cari tail dulu)
#    delete()       →  O(n)  hapus node (harus jaga lingkaran tetap utuh)
#    traverse_loop()→  O(n)  keliling sebanyak n langkah
# ================================================================

class CLLNode:
    """Satu kotak/node dalam Circular Linked List."""

    def __init__(self, data):
        # data  → isi dari node ini
        # next  → pointer ke node berikutnya (node terakhir → kembali ke head)
        self.data = data
        self.next = None


class CircularLL:
    """
    Circular Linked List — rantai node yang membentuk lingkaran.
    Dipakai untuk navigasi carousel menu di DUA UNRI.
    """

    def __init__(self):
        # head → node pertama, None kalau list kosong
        self.head = None

    def append(self, data):
        """Tambah data baru di belakang list (lingkaran tetap terjaga)."""
        node_baru = CLLNode(data)

        # list masih kosong — node baru tunjuk ke dirinya sendiri (circular!)
        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
            return

        # cari node terakhir — yaitu node yang next-nya sudah kembali ke head
        node_sekarang = self.head
        while node_sekarang.next != self.head:  # belum satu putaran penuh
            node_sekarang = node_sekarang.next

        # sambungkan: tail lama → node baru → head
        node_sekarang.next = node_baru  # tail lama tunjuk ke node baru
        node_baru.next = self.head      # node baru tunjuk kembali ke head (tutup lingkaran)

    def delete(self, data):
        """Hapus node pertama yang datanya cocok. Jaga lingkaran tetap utuh."""
        if self.head is None:
            return False

        # kasus: node yang dihapus adalah head
        if self.head.data == data:

            # kalau cuma ada 1 node — hapus semuanya
            if self.head.next == self.head:
                self.head = None
                return True

            # kalau lebih dari 1 node:
            # cari tail dulu (node yang next-nya head)
            # lalu sambungkan tail ke head baru
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            self.head = self.head.next  # geser head ke node kedua
            tail.next = self.head       # tail sekarang tunjuk ke head baru
            return True

        # kasus: node ada di tengah atau tail
        # lacak prev supaya bisa bypass node target
        prev = self.head
        node_sekarang = self.head.next

        while node_sekarang != self.head:   # berhenti kalau sudah satu putaran
            if node_sekarang.data == data:
                prev.next = node_sekarang.next  # bypass node target
                return True
            prev = node_sekarang
            node_sekarang = node_sekarang.next

        return False  # tidak ditemukan

    def display(self):
        """Tampilkan semua node dalam satu putaran penuh."""
        if self.head is None:
            print("  [Circular LL kosong]")
            return

        node_sekarang = self.head
        isi = []
        while True:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next
            if node_sekarang == self.head:  # sudah satu putaran penuh, berhenti
                break

        print("  HEAD: " + " -> ".join(isi) + f" -> (kembali ke '{self.head.data}')")

    def traverse_loop(self, steps=None):
        """
        Keliling list sebanyak `steps` langkah.
        Kalau steps tidak diisi, default satu putaran penuh.
        """
        if self.head is None:
            print("  [Circular LL kosong]")
            return

        # hitung panjang list kalau steps tidak diberikan
        if steps is None:
            steps = self._panjang()

        node_sekarang = self.head
        isi = []
        for _ in range(steps):
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next  # terus berputar, tidak pernah None

        print("  " + " -> ".join(isi) + f" -> (kembali ke '{self.head.data}'...)")

    def _panjang(self):
        """Helper — hitung jumlah node dalam list."""
        if self.head is None:
            return 0

        jumlah = 1
        node_sekarang = self.head.next
        while node_sekarang != self.head:
            jumlah += 1
            node_sekarang = node_sekarang.next
        return jumlah


# ================================================================
#  DEMO — jalankan file ini langsung: python structures/linked_list.py
# ================================================================

if __name__ == "__main__":

    # ------------------------------------------------------------
    #  DEMO SINGLE LINKED LIST
    # ------------------------------------------------------------
    print("=" * 55)
    print("  DEMO SINGLE LINKED LIST")
    print("=" * 55)

    sll = SingleLL()

    print("\n[1] Append: Andi, Budi, Citra, Dian")
    sll.append("Andi")
    sll.append("Budi")
    sll.append("Citra")
    sll.append("Dian")
    sll.display()

    print("\n[2] Search:")
    print(f"    'Citra' ada? → {sll.search('Citra')}")
    print(f"    'Zara'  ada? → {sll.search('Zara')}")

    print("\n[3] Delete 'Budi' (node tengah):")
    sll.delete("Budi")
    sll.display()

    print("\n[4] Delete 'Andi' (head):")
    sll.delete("Andi")
    sll.display()

    print("\n[5] Delete 'Dian' (tail) — sisa Citra:")
    sll.delete("Dian")
    sll.display()

    print("\n[6] Delete 'Citra' — list jadi kosong:")
    sll.delete("Citra")
    sll.display()

    print("\n[7] Delete dari list kosong:")
    hasil = sll.delete("Siapapun")
    print(f"    Return: {hasil}")

    # ------------------------------------------------------------
    #  DEMO DOUBLE LINKED LIST
    # ------------------------------------------------------------
    print("\n" + "=" * 55)
    print("  DEMO DOUBLE LINKED LIST")
    print("=" * 55)

    dll = DoubleLL()

    print("\n[1] Append: X, Y, Z")
    dll.append("X")
    dll.append("Y")
    dll.append("Z")
    print("    Maju   :", end=" ")
    dll.display()
    print("    Mundur :", end=" ")
    dll.traverse_backward()

    print("\n[2] Delete 'Y' (tengah):")
    dll.delete("Y")
    print("    Maju   :", end=" ")
    dll.display()
    print("    Mundur :", end=" ")
    dll.traverse_backward()

    print("\n[3] Delete 'X' (head):")
    dll.delete("X")
    print("    Maju   :", end=" ")
    dll.display()
    print("    Mundur :", end=" ")
    dll.traverse_backward()

    print("\n[4] Delete 'Z' (tail) — list jadi kosong:")
    dll.delete("Z")
    print("    Maju   :", end=" ")
    dll.display()

    # ------------------------------------------------------------
    #  DEMO CIRCULAR LINKED LIST
    # ------------------------------------------------------------
    print("\n" + "=" * 55)
    print("  DEMO CIRCULAR LINKED LIST")
    print("=" * 55)

    cll = CircularLL()

    print("\n[1] Append: Senin, Selasa, Rabu, Kamis")
    cll.append("Senin")
    cll.append("Selasa")
    cll.append("Rabu")
    cll.append("Kamis")
    cll.display()

    print("\n[2] Traverse satu putaran penuh (4 langkah):")
    cll.traverse_loop()

    print("\n[3] Traverse 7 langkah — buktikan melingkar:")
    cll.traverse_loop(steps=7)

    print("\n[4] Delete 'Selasa':")
    cll.delete("Selasa")
    cll.display()

    print("\n[5] Delete 'Senin' (head):")
    cll.delete("Senin")
    cll.display()

    print("\nDemo selesai.")
