# structures/stack_queue.py
# Anggota 1 — SIAKAD Lite Capstone Project
# Stack dan Queue


# ================================================================
#  STACK
#
#  Stack itu kayak tumpukan piring — piring yang terakhir kamu
#  taruh di atas, itu yang pertama kamu ambil.
#
#  Sifatnya: LIFO (Last In First Out)
#
#  Di SIAKAD, Stack dipakai untuk Activity Log:
#  aksi yang paling baru tampil paling atas.
#
#  Visualisasi:
#
#    TOP  →  [Submit KRS]  →  [Tambah MK]  →  [Login]  →  None
#            (paling baru)                    (paling lama)
#
#  Operasi utama:
#    push()  → O(1)  taruh di atas
#    pop()   → O(1)  ambil dari atas
#    peek()  → O(1)  lihat atas tanpa diambil
# ================================================================

class StackNode:
    """Satu kotak/node dalam tumpukan Stack."""

    def __init__(self, data):
        # data  → isi dari node ini
        # next  → pointer ke node di bawahnya
        self.data = data
        self.next = None


class Stack:
    """
    Stack — struktur data tumpukan dengan sifat LIFO.
    Dipakai untuk activity log di SIAKAD Lite.
    """

    def __init__(self):
        # top   → node paling atas, None kalau stack kosong
        # ukuran → hitung berapa elemen yang ada sekarang
        self.top = None
        self.ukuran = 0

    def push(self, data):
        """Masukkan data baru ke atas tumpukan."""
        node_baru = StackNode(data)

        # node baru menunjuk ke top yang lama
        # lalu top sekarang jadi node baru
        node_baru.next = self.top
        self.top = node_baru

        self.ukuran += 1

    def pop(self):
        """Ambil dan hapus data dari atas tumpukan. Return None kalau kosong."""
        if self.is_empty():
            print("  [Stack kosong, tidak ada yang bisa di-pop]")
            return None

        data_diambil = self.top.data  # simpan dulu sebelum dihapus
        self.top = self.top.next      # geser top ke node di bawahnya
        self.ukuran -= 1

        return data_diambil

    def peek(self):
        """Lihat data paling atas tanpa menghapusnya. Return None kalau kosong."""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """Return True kalau stack kosong, False kalau ada isinya."""
        return self.top is None

    def display(self):
        """Tampilkan semua isi stack dari atas ke bawah."""
        if self.is_empty():
            print("  [Stack kosong]")
            return

        # jalan dari top ke bawah, kumpulkan datanya
        node_sekarang = self.top
        isi = []
        while node_sekarang is not None:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next

        print("  TOP -> " + " -> ".join(isi) + " -> None")
        print(f"  Jumlah elemen: {self.ukuran}")


# ================================================================
#  QUEUE
#
#  Queue itu kayak antrian di kasir — siapa yang datang duluan,
#  dia yang dilayani duluan.
#
#  Sifatnya: FIFO (First In First Out)
#
#  Di SIAKAD, Queue dipakai untuk antrian KRS:
#  mahasiswa yang daftar duluan, diproses duluan.
#
#  Visualisasi:
#
#    FRONT  →  [Andi]  →  [Budi]  →  [Citra]  →  None
#              (duluan)                (belakangan)
#                                          ↑
#                                        REAR
#
#  Kita simpan FRONT dan REAR sekaligus supaya:
#    - ambil dari depan (dequeue) → O(1) lewat FRONT
#    - tambah ke belakang (enqueue) → O(1) lewat REAR
#      (kalau cuma simpan FRONT, enqueue harus jalan dulu ke ujung → O(n))
#
#  Operasi utama:
#    enqueue() → O(1)  masuk dari belakang (rear)
#    dequeue() → O(1)  keluar dari depan (front)
#    peek()    → O(1)  lihat depan tanpa diambil
# ================================================================

class QueueNode:
    """Satu kotak/node dalam antrian Queue."""

    def __init__(self, data):
        # data  → isi dari node ini
        # next  → pointer ke node berikutnya di antrian
        self.data = data
        self.next = None


class Queue:
    """
    Queue — struktur data antrian dengan sifat FIFO.
    Dipakai untuk antrian pengajuan KRS di SIAKAD Lite.
    """

    def __init__(self):
        # front → node paling depan (yang akan keluar duluan)
        # rear  → node paling belakang (tempat masuk yang baru)
        # ukuran → hitung berapa elemen yang ada sekarang
        self.front = None
        self.rear = None
        self.ukuran = 0

    def enqueue(self, data):
        """Masukkan data baru ke belakang antrian."""
        node_baru = QueueNode(data)

        # kalau antrian masih kosong, node baru jadi satu-satunya elemen
        # sekaligus jadi front dan rear
        if self.rear is None:
            self.front = node_baru
            self.rear = node_baru
            self.ukuran += 1
            return

        # kalau sudah ada isi, sambungkan ke belakang rear yang lama
        self.rear.next = node_baru  # rear lama tunjuk ke node baru
        self.rear = node_baru       # update rear ke node baru
        self.ukuran += 1

    def dequeue(self):
        """Ambil dan hapus data dari depan antrian. Return None kalau kosong."""
        if self.is_empty():
            print("  [Queue kosong, tidak ada yang bisa di-dequeue]")
            return None

        data_diambil = self.front.data      # simpan dulu sebelum dihapus
        self.front = self.front.next        # geser front ke node berikutnya

        # kalau antrian jadi kosong setelah dequeue, reset rear juga
        # (biar tidak ada pointer menggantung)
        if self.front is None:
            self.rear = None

        self.ukuran -= 1
        return data_diambil

    def peek(self):
        """Lihat data paling depan tanpa menghapusnya. Return None kalau kosong."""
        if self.is_empty():
            return None
        return self.front.data

    def is_empty(self):
        """Return True kalau queue kosong, False kalau ada isinya."""
        return self.front is None

    def display(self):
        """Tampilkan semua isi queue dari depan ke belakang."""
        if self.is_empty():
            print("  [Queue kosong]")
            return

        # jalan dari front ke rear, kumpulkan datanya
        node_sekarang = self.front
        isi = []
        while node_sekarang is not None:
            isi.append(str(node_sekarang.data))
            node_sekarang = node_sekarang.next

        print("  FRONT -> " + " -> ".join(isi) + " -> None")
        print(f"  REAR: '{self.rear.data}' | Jumlah elemen: {self.ukuran}")


# ================================================================
#  DEMO — jalankan file ini langsung: python structures/stack_queue.py
# ================================================================

if __name__ == "__main__":

    # ------------------------------------------------------------
    #  DEMO STACK
    # ------------------------------------------------------------
    print("=" * 55)
    print("  DEMO STACK — Activity Log (LIFO)")
    print("=" * 55)

    stack = Stack()

    print("\n[1] Push 3 aksi ke log:")
    stack.push("Login: Andi")
    stack.push("Tambah MK: Algoritma")
    stack.push("Submit KRS")
    stack.display()

    print(f"\n[2] Peek — aksi terbaru: '{stack.peek()}'")

    print("\n[3] Pop — ambil aksi paling atas:")
    aksi = stack.pop()
    print(f"    Di-pop: '{aksi}'")
    stack.display()

    print("\n[4] Push aksi baru:")
    stack.push("Edit Profil")
    stack.display()

    print("\n[5] Pop semua sampai kosong:")
    while not stack.is_empty():
        print(f"    Pop: '{stack.pop()}'")
    stack.display()

    print("\n[6] Pop dari stack yang sudah kosong:")
    stack.pop()

    # ------------------------------------------------------------
    #  DEMO QUEUE
    # ------------------------------------------------------------
    print("\n" + "=" * 55)
    print("  DEMO QUEUE — Antrian KRS (FIFO)")
    print("=" * 55)

    queue = Queue()

    print("\n[1] Enqueue 4 mahasiswa ke antrian KRS:")
    queue.enqueue("2110101001 - Andi")
    queue.enqueue("2110101002 - Budi")
    queue.enqueue("2110101003 - Citra")
    queue.enqueue("2110101004 - Dian")
    queue.display()

    print(f"\n[2] Peek — giliran pertama: '{queue.peek()}'")

    print("\n[3] Dequeue — proses mahasiswa paling depan:")
    mahasiswa = queue.dequeue()
    print(f"    Diproses: '{mahasiswa}'")
    queue.display()

    print("\n[4] Enqueue mahasiswa baru (daftar belakangan):")
    queue.enqueue("2110101005 - Eka")
    queue.display()

    print("\n[5] Proses semua antrian sampai habis:")
    while not queue.is_empty():
        print(f"    Proses: '{queue.dequeue()}'")
    queue.display()

    print("\n[6] Dequeue dari queue yang sudah kosong:")
    queue.dequeue()

    print("\nDemo selesai.")
