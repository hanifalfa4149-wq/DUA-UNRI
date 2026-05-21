---
applyTo: "models.py"
---

# Instructions — models.py

## Aturan

- Semua class entitas ada di satu file ini: Mahasiswa, MataKuliah, KRS, Nilai
- Setiap class wajib punya: **init**, to_dict(), from_dict(), **str**()
- Tidak ada business logic — hanya definisi data dan serialisasi
- Tidak ada import dari structures/, services/, atau views/
- Gunakan type hint di **init**

## Struktur Minimal

```python
class NamaEntity:
    def __init__(self, ...): ...
    def to_dict(self) -> dict: ...
    @classmethod
    def from_dict(cls, data: dict): ...
    def __str__(self) -> str: ...
```
