---
applyTo: "structures/**"
---

# Instructions — structures/

## Aturan Keras

- DILARANG import collections, heapq, queue, atau library DS apapun
- Node harus class terpisah dengan pointer (next, prev, dll) — bukan list Python
- Setiap DS harus generic — tidak ada domain logic (mahasiswa, matkul, dll)
- Wajib ada blok **main** untuk demo isolated di setiap file

## Method Wajib Per File

### linked_list.py — 3 class: SingleLL, DoubleLL, CircularLL

- Minimal: append(), delete(), search(), display()
- DoubleLL tambahan: traverse_backward()
- CircularLL: tail.next harus selalu menunjuk ke head

### stack_queue.py — 2 class: Stack, Queue

- Stack: push(), pop(), peek(), is_empty(), display()
- Queue: enqueue(), dequeue(), peek(), is_empty(), display()
- DILARANG pakai collections.deque

### hash_table.py — class HashTable

- Separate chaining untuk collision resolution
- insert(), search(), delete(), display()
- Fungsi hash manual — bukan hash() bawaan Python

### tree_graph.py — 2 class: Tree, Graph

- Tree: insert(), search(), display() dengan traverse pre-order
- Graph: adjacency list, add_vertex(), add_edge(), get_neighbors(), display()
- Graph directed untuk relasi prasyarat matkul

## Docstring

Setiap class wajib docstring yang menyebut: apa DS ini, kenapa dipakai, time complexity operasi utama.
