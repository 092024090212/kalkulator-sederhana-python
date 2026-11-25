"""
Program Kalkulator Sederhana - 4 Operasi Bilangan
Penulis      : Panji Widagdo
Universitas  : Jakarta Global University
Minat Bidang : Network Engineer
"""


def tambah(a: float, b: float) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b


def kurang(a: float, b: float) -> float:
    """Mengembalikan hasil pengurangan a - b."""
    return a - b


def kali(a: float, b: float) -> float:
    """Mengembalikan hasil perkalian a * b."""
    return a * b


def bagi(a: float, b: float) -> float:
    """Mengembalikan hasil pembagian a / b dengan validasi nol."""
    if b == 0:
        raise ZeroDivisionError("Pembagian dengan angka nol tidak diperbolehkan.")
    return a / b


def input_angka(pesan: str) -> float:
    """Meminta input angka dari pengguna hingga valid."""
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka (contoh: 10 atau 3.5).")


def format_hasil(nilai: float) -> str:
    """Menampilkan bilangan bulat tanpa .0 agar hasil lebih rapi."""
    return str(int(nilai)) if nilai.is_integer() else f"{nilai:.4f}".rstrip("0").rstrip(".")


def tampilkan_menu() -> None:
    """Menampilkan daftar menu operasi kalkulator."""
    print("\n========================================")
    print("   KALKULATOR SEDERHANA (4 OPERASI)     ")
    print("========================================")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian   (*)")
    print("4. Pembagian   (/)")
    print("5. Keluar")
    print("========================================")


def main() -> None:
    operasi = {
        "1": ("+", tambah),
        "2": ("-", kurang),
        "3": ("*", kali),
        "4": ("/", bagi),
    }

    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1/2/3/4/5): ").strip()

        if pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator ini.")
            break

        if pilihan not in operasi:
            print("Pilihan tidak tersedia. Silakan pilih angka 1 sampai 5.")
            continue

        angka1 = input_angka("Masukkan angka pertama : ")
        angka2 = input_angka("Masukkan angka kedua   : ")
        simbol, fungsi = operasi[pilihan]

        try:
            hasil = fungsi(angka1, angka2)
            print(
                f"\nHasil: {format_hasil(angka1)} {simbol} {format_hasil(angka2)} "
                f"= {format_hasil(hasil)}"
            )
        except ZeroDivisionError as err:
            print(f"\nError: {err}")


if __name__ == "__main__":
    main()