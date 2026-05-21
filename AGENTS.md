# AGENTS.md — SIAKAD Lite

Untuk semua AI agent yang bekerja di repo ini.

## Baca Dulu Sebelum Apapun
1. .github/copilot-instructions.md  ← instruksi lengkap
2. docs/SIAKAD-PRD.md               ← context fitur dan rubrik
3. .github/instructions/            ← rules per file/folder

## Ringkasan
- Python CLI — jalankan dengan: python main.py
- DILARANG pakai library DS eksternal — semua implementasi manual
- Satu file per turn, bottom-up: models → structures → algoritma → services → views → main

## Verify Jalan
python main.py
python structures/linked_list.py
python structures/hash_table.py
python structures/tree_graph.py
python structures/stack_queue.py