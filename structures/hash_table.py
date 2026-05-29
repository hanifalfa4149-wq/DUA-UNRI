"""
Hash Table dengan separate chaining untuk SIAKAD Lite.

Implementasi manual tanpa dict Python sebagai storage utama.
Collision diselesaikan dengan linked list per bucket (separate chaining).
Fungsi hash manual berbasis nilai ASCII karakter key.
"""


class _Node:
    """
    Node untuk chain di tiap bucket Hash Table.

    Attributes:
        key   : Key unik (NIM string).
        value : Value yang disimpan (dict data mahasiswa).
        next  : Pointer ke node berikutnya dalam chain.
    """

    def __init__(self, key, value):
        """Inisialisasi node dengan key, value, dan next=None."""
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    Hash Table dengan separate chaining untuk lookup data mahasiswa by NIM.

    Dipakai di SIAKAD Lite karena NIM bersifat unik sehingga cocok sebagai key,
    dan Hash Table memberikan lookup O(1) average — jauh lebih cepat dari
    linear search O(n) saat data mahasiswa banyak.

    Collision resolution: separate chaining — tiap bucket adalah linked list
    (_Node) sehingga beberapa key yang hash ke bucket sama tetap tersimpan semua.

    Time Complexity:
        insert  : O(1) average, O(n) worst case (semua key collision satu bucket)
        search  : O(1) average, O(n) worst case
        delete  : O(1) average, O(n) worst case

    Attributes:
        _capacity (int)  : Jumlah bucket (default 16).
        _buckets  (list) : Array bucket, tiap slot head _Node atau None.
        _size     (int)  : Jumlah total key-value yang tersimpan.
    """

    def __init__(self, capacity: int = 16):
        """Inisialisasi Hash Table dengan sejumlah bucket kosong."""
        self._capacity = capacity
        # List Python dipakai hanya sebagai array fixed-size,
        # bukan sebagai pengganti Hash Table
        self._buckets = [None] * self._capacity
        self._size = 0

    def _hash(self, key: str) -> int:
        """
        Fungsi hash manual berbasis nilai ASCII karakter key.

        Polynomial rolling hash: h = (h * 31 + ord(c)) % capacity
        untuk setiap karakter c dalam key.

        Returns:
            int: indeks bucket (0 sampai capacity-1).
        """
        h = 0
        for char in str(key):
            h = (h * 31 + ord(char)) % self._capacity
        return h

    def insert(self, key, value) -> None:
        """
        Sisipkan atau update pasangan key-value ke Hash Table.

        Jika key sudah ada, value diperbarui (update in-place).
        Jika belum ada, node baru disisipkan di depan chain — O(1).

        Args:
            key   : Key unik, biasanya NIM string.
            value : Data yang disimpan, biasanya dict mahasiswa.
        """
        index = self._hash(key)
        current = self._buckets[index]

        # Cek apakah key sudah ada di chain — jika iya, update value
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Key belum ada — sisipkan node baru di depan chain (prepend O(1))
        new_node = _Node(key, value)
        new_node.next = self._buckets[index]
        self._buckets[index] = new_node
        self._size += 1

    def search(self, key):
        """
        Cari value berdasarkan key — O(1) average.

        Args:
            key: Key yang dicari (NIM string).

        Returns:
            Value jika ditemukan, None jika tidak ada.
        """
        index = self._hash(key)
        current = self._buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key) -> bool:
        """
        Hapus pasangan key-value dari Hash Table — O(1) average.

        Args:
            key: Key yang akan dihapus.

        Returns:
            True jika berhasil, False jika key tidak ditemukan.
        """
        index = self._hash(key)
        current = self._buckets[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self._buckets[index] = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return True
            prev = current
            current = current.next

        return False

    def display(self) -> None:
        """Tampilkan isi seluruh Hash Table bucket per bucket (hanya yang tidak kosong)."""
        print(f"HashTable (capacity={self._capacity}, size={self._size})")
        for i, head in enumerate(self._buckets):
            if head is None:
                continue
            chain = []
            current = head
            while current is not None:
                chain.append(f"{current.key}:{current.value}")
                current = current.next
            print(f"  Bucket[{i:02d}] -> " + " -> ".join(chain))

    def get_all(self) -> list:
        """Ambil semua pasangan key-value sebagai list of tuple (key, value)."""
        result = []
        for head in self._buckets:
            current = head
            while current is not None:
                result.append((current.key, current.value))
                current = current.next
        return result


# ---------------------------------------------------------------------------
# Demo isolated — jalankan: python structures/hash_table.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("DEMO hash_table.py")
    print("=" * 50)

    ht = HashTable(capacity=8)  # Kapasitas kecil untuk mudah trigger collision

    # --- Insert ---
    print("\n[Insert 5 mahasiswa]")
    data = [
        ("2201001", {"nim": "2201001", "nama": "Andi Pratama",   "id_prodi": "TIF", "angkatan": 2022}),
        ("2201002", {"nim": "2201002", "nama": "Budi Santoso",   "id_prodi": "TIF", "angkatan": 2022}),
        ("2201003", {"nim": "2201003", "nama": "Citra Dewi",     "id_prodi": "TIF", "angkatan": 2022}),
        ("2201004", {"nim": "2201004", "nama": "Dian Rahmawati", "id_prodi": "SIF", "angkatan": 2022}),
        ("2301001", {"nim": "2301001", "nama": "Eko Prasetyo",   "id_prodi": "TIF", "angkatan": 2023}),
    ]
    for key, val in data:
        ht.insert(key, val)
        print(f"  insert({key}) -> bucket[{ht._hash(key)}]")

    print()
    ht.display()

    # --- Search hit ---
    print("\n[Search — hit]")
    result = ht.search("2201003")
    print(f"  search('2201003') -> {result}")

    # --- Search miss ---
    print("\n[Search — miss]")
    print(f"  search('9999999') -> {ht.search('9999999')}")

    # --- Update ---
    print("\n[Update key yang sudah ada]")
    ht.insert("2201001", {"nim": "2201001", "nama": "Andi UPDATED", "id_prodi": "TIF", "angkatan": 2022})
    print(f"  search('2201001') -> {ht.search('2201001')}")

    # --- Delete ---
    print("\n[Delete]")
    print(f"  delete('2201002')  -> {ht.delete('2201002')}")
    print(f"  search('2201002')  -> {ht.search('2201002')}")
    print(f"  delete('9999999')  -> {ht.delete('9999999')}")

    # --- Collision test eksplisit ---
    print("\n[Collision test — capacity=4, 8 key]")
    ht2 = HashTable(capacity=4)
    keys = ["2201001", "2201002", "2201003", "2201004", "2301001", "2302001", "2303001", "2304001"]
    for k in keys:
        ht2.insert(k, {"nim": k})
    for i, head in enumerate(ht2._buckets):
        count, chain = 0, []
        cur = head
        while cur:
            count += 1
            chain.append(cur.key)
            cur = cur.next
        if count > 0:
            status = "CHAIN ✓" if count > 1 else "single"
            print(f"  Bucket[{i}] ({status}): {' -> '.join(chain)}")
    all_ok = all(ht2.search(k) is not None for k in keys)
    print(f"  Search semua {len(keys)} key setelah collision: {'OK ✓' if all_ok else 'FAIL'}")

    print("\n" + "=" * 50)
    print("Semua demo selesai tanpa error.")