from views import menu_utama


def _banner():
    """Tampilkan banner aplikasi."""
    print("=" * 40)
    print("DUA UNRI — CLI Akademik")
    print("=" * 40)


if __name__ == "__main__":
    _banner()
    menu_utama()
