"""Modul demonstrasi kode bersih untuk pengujian quality gate."""


def hitung_operasi(angka_pertama, angka_kedua):
    """Menjumlahkan dua buah bilangan.

    Args:
        angka_pertama (int): Bilangan pertama.
        angka_kedua (int): Bilangan kedua.

    Returns:
        int: Hasil penjumlahan.
    """
    hasil = angka_pertama + angka_kedua
    print(f"Hasil: {hasil}")
    return hasil


def main():
    """Fungsi utama program."""
    hitung_operasi(1, 2)


if __name__ == "__main__":
    main()
