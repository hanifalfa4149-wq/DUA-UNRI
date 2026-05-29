"""
Tree dan Graph untuk SIAKAD Lite.

Tree  : hierarki Fakultas -> Prodi -> Mahasiswa, traversal pre-order.
Graph : directed adjacency list untuk relasi prasyarat antar mata kuliah.
"""


# ===========================================================================
# TREE
# ===========================================================================

class _TreeNode:
    """
    Node untuk Tree hierarki akademik.

    Attributes:
        data     : Data yang disimpan di node (nama fakultas/prodi/mahasiswa).
        children : List node anak (bisa banyak — general tree, bukan binary).
    """

    def __init__(self, data):
        """Inisialisasi TreeNode dengan data dan list children kosong."""
        self.data = data
        self.children = []  # list Python sebagai container anak node


class Tree:
    """
    General Tree untuk merepresentasikan hierarki akademik.

    Dipakai di SIAKAD Lite untuk menampilkan struktur:
        Fakultas -> Prodi -> Mahasiswa
    Struktur ini bersifat hierarkis natural sehingga Tree adalah
    pilihan yang tepat dibanding DS linear seperti LL atau Stack.

    Traversal menggunakan pre-order (root -> children secara rekursif)
    sehingga hierarki tampil dari atas ke bawah secara intuitif.

    Time Complexity:
        insert (add_child) : O(1) — langsung append ke children parent
        search             : O(n) — harus kunjungi semua node worst case
        display (pre-order): O(n) — kunjungi setiap node tepat satu kali

    Attributes:
        root (_TreeNode): Node root Tree (biasanya nama Fakultas).
    """

    def __init__(self, root_data):
        """Inisialisasi Tree dengan satu root node."""
        self.root = _TreeNode(root_data)

    def _find(self, node: _TreeNode, target) -> "_TreeNode | None":
        """Cari node dengan data tertentu secara rekursif (pre-order)."""
        if node is None:
            return None
        if node.data == target:
            return node
        for child in node.children:
            result = self._find(child, target)
            if result is not None:
                return result
        return None

    def insert(self, parent_data, child_data) -> bool:
        """
        Tambahkan child node di bawah parent node yang dicari by data.

        Args:
            parent_data : Data node parent yang jadi tempat insert.
            child_data  : Data node baru yang akan ditambahkan.

        Returns:
            True jika parent ditemukan dan child berhasil ditambah,
            False jika parent tidak ditemukan.
        """
        parent_node = self._find(self.root, parent_data)
        if parent_node is None:
            return False
        parent_node.children.append(_TreeNode(child_data))
        return True

    def search(self, target) -> bool:
        """
        Cari apakah data tertentu ada di Tree — O(n).

        Args:
            target: Data yang dicari.

        Returns:
            True jika ditemukan, False jika tidak.
        """
        return self._find(self.root, target) is not None

    def _display_recursive(self, node: _TreeNode, level: int) -> None:
        """Cetak node secara pre-order dengan indentasi sesuai level (rekursif)."""
        if node is None:
            return
        indent = "  " * level
        prefix = "+-" if level > 0 else ""
        print(f"{indent}{prefix}{node.data}")
        for child in node.children:
            self._display_recursive(child, level + 1)

    def display(self) -> None:
        """Tampilkan seluruh hierarki Tree secara pre-order dengan indentasi."""
        if self.root is None:
            print("Tree kosong.")
            return
        self._display_recursive(self.root, 0)

    def get_children(self, parent_data) -> list:
        """
        Ambil list data anak langsung dari sebuah node.

        Args:
            parent_data: Data node parent.

        Returns:
            List data children, atau list kosong jika tidak ditemukan.
        """
        node = self._find(self.root, parent_data)
        if node is None:
            return []
        return [child.data for child in node.children]


# ===========================================================================
# GRAPH
# ===========================================================================

class _GraphNode:
    """
    Node dalam adjacency list Graph.

    Dipakai sebagai elemen linked list di tiap slot adjacency list,
    menghindari penggunaan list Python sebagai DS utama relasi antar vertex.

    Attributes:
        vertex : Label vertex tujuan edge.
        next   : Pointer ke node berikutnya dalam linked list neighbors.
    """

    def __init__(self, vertex):
        """Inisialisasi GraphNode dengan vertex dan next=None."""
        self.vertex = vertex
        self.next = None


class Graph:
    """
    Directed Graph dengan adjacency list untuk relasi prasyarat mata kuliah.

    Dipakai di SIAKAD Lite karena relasi prasyarat bersifat non-linear
    dan directed: MK003 -> MK001 berarti MK003 membutuhkan MK001,
    tapi tidak sebaliknya. Graph menangkap relasi ini secara natural.

    Implementasi adjacency list: setiap vertex memetakan ke linked list
    (_GraphNode) berisi semua vertex tetangga (neighbors/prasyarat).

    Time Complexity:
        add_vertex    : O(1)
        add_edge      : O(1) — prepend ke linked list neighbors
        get_neighbors : O(k) — k = jumlah tetangga vertex
        display       : O(V + E) — kunjungi semua vertex dan edge

    Attributes:
        _adj (dict) : Dict { vertex: _GraphNode head } sebagai adjacency list.
                      Dict Python hanya sebagai lookup vertex -> head node,
                      relasi antar vertex direpresentasikan linked list _GraphNode.
    """

    def __init__(self):
        """Inisialisasi Graph kosong tanpa vertex maupun edge."""
        # Dict hanya sebagai map vertex -> head linked list neighbors
        self._adj: dict = {}

    def add_vertex(self, vertex) -> None:
        """
        Tambahkan vertex baru ke Graph jika belum ada.

        Args:
            vertex: Label vertex baru (kode matkul).
        """
        if vertex not in self._adj:
            self._adj[vertex] = None  # head linked list neighbors = None (kosong)

    def add_edge(self, from_vertex, to_vertex) -> None:
        """
        Tambahkan directed edge dari from_vertex ke to_vertex.

        Artinya: from_vertex membutuhkan to_vertex sebagai prasyarat.
        Kedua vertex otomatis ditambahkan jika belum ada.
        Edge baru disisipkan di depan linked list neighbors (prepend O(1)).

        Args:
            from_vertex : Vertex sumber (kode matkul yang punya prasyarat).
            to_vertex   : Vertex tujuan (kode matkul yang jadi prasyarat).
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        # Cek duplikasi edge sebelum insert
        current = self._adj[from_vertex]
        while current is not None:
            if current.vertex == to_vertex:
                return  # Edge sudah ada, skip
            current = current.next

        # Prepend ke linked list neighbors from_vertex
        new_node = _GraphNode(to_vertex)
        new_node.next = self._adj[from_vertex]
        self._adj[from_vertex] = new_node

    def get_neighbors(self, vertex) -> list:
        """
        Ambil semua tetangga (prasyarat) dari sebuah vertex — O(k).

        Args:
            vertex: Vertex yang dicari neighbornya (kode matkul).

        Returns:
            List vertex tetangga, atau list kosong jika vertex tidak ada.
        """
        if vertex not in self._adj:
            return []
        neighbors = []
        current = self._adj[vertex]
        while current is not None:
            neighbors.append(current.vertex)
            current = current.next
        return neighbors

    def display(self) -> None:
        """Tampilkan seluruh adjacency list Graph vertex per vertex."""
        if not self._adj:
            print("Graph kosong.")
            return
        print(f"Graph (directed, {len(self._adj)} vertex):")
        for vertex, head in self._adj.items():
            neighbors = []
            current = head
            while current is not None:
                neighbors.append(current.vertex)
                current = current.next
            arrow = " -> ".join(neighbors) if neighbors else "(tidak ada prasyarat)"
            print(f"  {vertex} : {arrow}")

    def has_edge(self, from_vertex, to_vertex) -> bool:
        """
        Cek apakah directed edge dari from_vertex ke to_vertex ada.

        Args:
            from_vertex: Vertex sumber.
            to_vertex  : Vertex tujuan.

        Returns:
            True jika edge ada, False jika tidak.
        """
        if from_vertex not in self._adj:
            return False
        current = self._adj[from_vertex]
        while current is not None:
            if current.vertex == to_vertex:
                return True
            current = current.next
        return False


# ---------------------------------------------------------------------------
# Demo isolated — jalankan: python structures/tree_graph.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("DEMO tree_graph.py")
    print("=" * 50)

    # -----------------------------------------------------------------------
    # TREE — Hierarki Fakultas -> Prodi -> Mahasiswa
    # -----------------------------------------------------------------------
    print("\n[Tree — Hierarki Akademik]")

    tree = Tree("UNRI")
    tree.insert("UNRI", "FMIPA")
    tree.insert("UNRI", "Teknik")
    tree.insert("FMIPA", "Informatika")
    tree.insert("FMIPA", "Matematika")
    tree.insert("Teknik", "Teknik Sipil")
    tree.insert("Informatika", "Andi Pratama")
    tree.insert("Informatika", "Budi Santoso")
    tree.insert("Informatika", "Citra Dewi")
    tree.insert("Matematika", "Dian Rahmawati")
    tree.insert("Teknik Sipil", "Eko Prasetyo")

    print("\nStruktur Hierarki (pre-order):")
    tree.display()

    print("\n[Search di Tree]")
    print(f"  search('Informatika') -> {tree.search('Informatika')}")
    print(f"  search('Budi Santoso') -> {tree.search('Budi Santoso')}")
    print(f"  search('Kedokteran')   -> {tree.search('Kedokteran')}")

    print("\n[get_children]")
    print(f"  children('FMIPA')       -> {tree.get_children('FMIPA')}")
    print(f"  children('Informatika') -> {tree.get_children('Informatika')}")

    print("\n[Insert ke parent tidak ada]")
    print(f"  insert('TIDAK_ADA', 'X') -> {tree.insert('TIDAK_ADA', 'X')}")

    # -----------------------------------------------------------------------
    # GRAPH — Prasyarat Mata Kuliah (directed)
    # -----------------------------------------------------------------------
    print("\n" + "-" * 50)
    print("[Graph — Prasyarat Mata Kuliah]")

    g = Graph()

    # Tambah vertex
    for mk in ["MK001", "MK002", "MK003", "MK004"]:
        g.add_vertex(mk)

    # Tambah edge directed: MK -> prasyarat
    # MK003 butuh MK001 dan MK002
    g.add_edge("MK003", "MK001")
    g.add_edge("MK003", "MK002")
    # MK004 butuh MK001
    g.add_edge("MK004", "MK001")

    print("\nAdjacency list:")
    g.display()

    print("\n[get_neighbors]")
    print(f"  get_neighbors('MK003') -> {g.get_neighbors('MK003')}")
    print(f"  get_neighbors('MK001') -> {g.get_neighbors('MK001')} (tidak punya prasyarat)")
    print(f"  get_neighbors('MK999') -> {g.get_neighbors('MK999')} (tidak ada)")

    print("\n[has_edge]")
    print(f"  has_edge('MK003', 'MK001') -> {g.has_edge('MK003', 'MK001')}")
    print(f"  has_edge('MK001', 'MK003') -> {g.has_edge('MK001', 'MK003')} (directed, bukan sebaliknya)")
    print(f"  has_edge('MK004', 'MK002') -> {g.has_edge('MK004', 'MK002')}")

    print("\n[Duplikasi edge dicegah]")
    g.add_edge("MK003", "MK001")  # tambah lagi edge yang sama
    neighbors = g.get_neighbors("MK003")
    mk001_count = neighbors.count("MK001")
    print(f"  MK001 muncul {mk001_count}x di neighbors MK003 (harusnya 1) -> {'OK ✓' if mk001_count == 1 else 'FAIL'}")

    print("\n" + "=" * 50)
    print("Semua demo selesai tanpa error.")