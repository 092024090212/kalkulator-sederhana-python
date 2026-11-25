# Kalkulator Sederhana (4 Operasi Bilangan) — Python

Repositori ini berisi program kalkulator berbasis teks (*Command-Line Interface*) yang mendukung 4 operasi aritmatika dasar menggunakan bahasa pemrograman Python. Proyek ini dibuat sebagai dokumentasi pembelajaran dasar pemrograman untuk mendukung fondasi pengembangan karier di bidang **Network Engineering** (*network automation*).

**Penulis:** Panji Widagdo  
**Universitas:** Jakarta Global University  
**Fokus Minat:** Network Engineer

## Fitur Utama

1. **Penjumlahan (`+`)** — Menjumlahkan dua bilangan bulat maupun desimal.
2. **Pengurangan (`-`)** — Menghitung selisih antara dua bilangan.
3. **Perkalian (`*`)** — Mengalikan dua bilangan secara akurat.
4. **Pembagian (`/`)** — Membagi dua bilangan dilengkapi penanganan kesalahan pembagian dengan nol (`ZeroDivisionError`).
5. **Validasi Input** — Mencegah program berhenti mendadak jika pengguna memasukkan karakter selain angka (`ValueError`).

## Teknologi yang Digunakan

- **Python 3** (hanya menggunakan *standard library*, tanpa perlu instalasi paket tambahan).

## Cara Menjalankan Program

1. Pastikan **Python 3** sudah terpasang di perangkat Anda.
2. Unduh atau *clone* repositori ini:
   ```bash
   git clone https://github.com/username-anda/kalkulator-sederhana-python.git
   cd kalkulator-sederhana-python
   ```
3. Jalankan program melalui terminal/Command Prompt:
   ```bash
   python kalkulator_sederhana.py
   ```
4. Pilih nomor operasi (`1`–`4`), masukkan dua angka, lalu lihat hasil perhitungannya. Pilih `5` untuk keluar.

## Contoh Output

```text
========================================
   KALKULATOR SEDERHANA (4 OPERASI)
========================================
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian   (*)
4. Pembagian   (/)
5. Keluar
========================================
Pilih operasi (1/2/3/4/5): 4
Masukkan angka pertama : 25
Masukkan angka kedua   : 4

Hasil: 25 / 4 = 6.25
```

## Pembelajaran Utama

- Menyusun struktur kode secara modular dengan memisahkan setiap operasi ke dalam fungsi tersendiri.
- Menerapkan *error handling* (`try-except` dan `raise`) untuk menjaga keandalan program saat menerima input tak terduga.
- Mendokumentasikan proyek pemrograman secara rapi di GitHub agar mudah dibaca dan diuji oleh orang lain.