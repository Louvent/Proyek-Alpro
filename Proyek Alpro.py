"""
====================================================================
 PETA MATERI (cari tanda "[MATERI n]" di kode untuk melihat contohnya)
   [MATERI 1] Tipe data dan operator
   [MATERI 2] Predikat (fungsi yang mengembalikan True / False)
   [MATERI 3] Struktur pemilihan (if - elif - else)
   [MATERI 4] Struktur pengulangan (while dan for)
   [MATERI 5] Integrasi control flow (nested if, break, continue)
   [MATERI 6] String
   [MATERI 7] List
   [MATERI 8] Tuple
   [MATERI 9] Dictionary
   [MATERI 10] Fungsi (def)
   [MATERI 11] Searching (linear search dan binary search)
=====================================================================
"""

import random  # modul bawaan Python untuk membuat angka acak


# =====================================================================
# BAGIAN A - DATA GLOBAL
# =====================================================================

# [MATERI 8] TUPLE
# Tuple dipakai karena isinya TETAP (immutable): nama menu tidak boleh
# berubah saat program berjalan. Kalau pakai list, isinya bisa tidak
# sengaja terubah.
MENU_UTAMA = ("Main Game", "Lihat Leaderboard", "Cari Pemain", "Cara Bermain", "Keluar")

# [MATERI 9] DICTIONARY (di dalam dictionary ada dictionary lagi / nested)
# Dictionary dipakai karena data level punya "label" (nama, batas, nyawa)
# sehingga lebih mudah dibaca daripada list biasa.
# Nilai "batas" berupa TUPLE (min, max) karena sifatnya tetap.
LEVEL = {
    "1": {"nama": "Mudah", "batas": (1, 50), "nyawa": 10, "pengali": 1},
    "2": {"nama": "Sedang", "batas": (1, 100), "nyawa": 7, "pengali": 2},
    "3": {"nama": "Sulit", "batas": (1, 200), "nyawa": 9, "pengali": 3},
}

# [MATERI 7] LIST of DICTIONARY
# Leaderboard disimpan sebagai list karena jumlahnya bertambah terus
# (list itu mutable), dan tiap pemain berupa dictionary.
leaderboard = []


# =====================================================================
# BAGIAN B - PREDIKAT
# [MATERI 2] Predikat = fungsi yang HASILNYA hanya True atau False.
# Biasanya namanya diawali "apakah_" / "is_" supaya mudah dikenali.
# =====================================================================

def apakah_angka(teks):
    """Cek apakah teks isinya angka bulat positif saja.
    Memakai method string .isdigit() -> True kalau semua karakter digit."""
    return teks.isdigit()


def apakah_dalam_rentang(angka, batas_min, batas_max):
    """Cek apakah angka berada di antara batas_min dan batas_max.
    Memakai operator perbandingan yang dirantai (chained comparison),
    fitur khas Python: a <= x <= b."""
    return batas_min <= angka <= batas_max


def apakah_genap(angka):
    """Predikat dengan operator modulus (%). Genap jika sisa bagi 2 = 0."""
    return angka % 2 == 0


def apakah_prima(angka):
    """Predikat bilangan prima. Dipakai untuk memberi petunjuk tambahan."""
    if angka < 2:
        return False
    for pembagi in range(2, int(angka ** 0.5) + 1):  # ** = pangkat
        if angka % pembagi == 0:
            return False
    return True


# =====================================================================
# BAGIAN C - SEARCHING
# [MATERI 11] Dua algoritma pencarian dasar.
# =====================================================================

def linear_search(daftar, target):
    """LINEAR SEARCH: cek satu per satu dari awal sampai akhir.
    Cocok untuk data kecil / data TIDAK terurut.
    Mengembalikan index jika ketemu, -1 jika tidak ada.
    Kompleksitas: O(n)."""
    for index, nilai in enumerate(daftar):  # enumerate -> dapat index + nilai
        if nilai == target:
            return index
    return -1


def binary_search(daftar_urut, target):
    """BINARY SEARCH: syaratnya data HARUS terurut.
    Cara kerja: bandingkan dengan nilai tengah, buang separuh yang salah,
    ulangi. Jauh lebih cepat dari linear. Kompleksitas: O(log n).
    Mengembalikan TUPLE (index, jumlah_langkah)."""
    kiri = 0
    kanan = len(daftar_urut) - 1
    langkah = 0

    while kiri <= kanan:                 # [MATERI 4] while
        langkah += 1                     # operator assignment +=
        tengah = (kiri + kanan) // 2     # // = pembagian bulat
        if daftar_urut[tengah] == target:
            return tengah, langkah       # return banyak nilai (jadi tuple)
        elif daftar_urut[tengah] < target:
            kiri = tengah + 1            # buang separuh kiri
        else:
            kanan = tengah - 1           # buang separuh kanan

    return -1, langkah


def cari_pemain(nama_dicari):
    """Mencari pemain di leaderboard memakai linear search manual.
    Data berupa list of dictionary, jadi yang dibandingkan nilai kunci 'nama'.
    Pencarian tidak peka huruf besar/kecil (case-insensitive)."""
    nama_dicari = nama_dicari.strip().lower()    # [MATERI 6] method string
    hasil = []                                   # list penampung hasil
    for pemain in leaderboard:
        if nama_dicari in pemain["nama"].lower():  # operator 'in' pada string
            hasil.append(pemain)
    return hasil


# =====================================================================
# BAGIAN D - FUNGSI LOGIKA GAME
# [MATERI 10] Fungsi dengan parameter, nilai default, dan return.
# =====================================================================

def beri_petunjuk(rahasia, tebakan):
    """Memberi petunjuk dengan NESTED IF (if di dalam if).
    [MATERI 3 dan 5] Struktur pemilihan bertingkat.
    Mengembalikan string petunjuk."""
    selisih = abs(rahasia - tebakan)   # abs() = nilai mutlak (fungsi bawaan)

    if tebakan < rahasia:
        arah = "terlalu KECIL"
    else:
        arah = "terlalu BESAR"

    # Nested if: seberapa dekat tebakan dengan angka rahasia
    if selisih <= 5:
        if selisih <= 2:
            jarak = "SANGAT PANAS"
        else:
            jarak = "PANAS"
    elif selisih <= 15:
        jarak = "HANGAT"
    else:
        jarak = "DINGIN"

    # f-string: cara modern menyisipkan variabel ke dalam teks
    return f"Tebakanmu {arah} ({jarak})"


def beri_petunjuk_tambahan(rahasia, jumlah_tebakan):
    """Petunjuk ekstra yang keluar setelah beberapa kali salah.
    Memanfaatkan predikat apakah_genap() dan apakah_prima()."""
    if jumlah_tebakan == 3:
        jenis = "GENAP" if apakah_genap(rahasia) else "GANJIL"  # ternary
        return f"Hint: angka rahasia adalah bilangan {jenis}."
    if jumlah_tebakan == 5:
        status = "prima" if apakah_prima(rahasia) else "BUKAN prima"
        return f"Hint: angka rahasia {status}."
    return ""  # string kosong = tidak ada hint


def hitung_skor(nyawa_sisa, nyawa_awal, pengali, bonus_cepat=True):
    """Menghitung skor akhir. 'bonus_cepat' adalah PARAMETER DEFAULT.
    [MATERI 1] Memakai operator aritmatika: *, +, / dan fungsi round()."""
    skor_dasar = nyawa_sisa * 100 * pengali
    bonus = 0
    # operator logika 'and': dua syarat harus benar bersamaan
    if bonus_cepat and nyawa_sisa >= nyawa_awal / 2:
        bonus = 50 * pengali
    return round(skor_dasar + bonus)


def pilih_level():
    """Meminta pemain memilih level. Mengembalikan dictionary level terpilih.
    Memakai while True + validasi input (pengulangan sampai input benar)."""
    print("\nPilih level:")
    for kode, data in LEVEL.items():  # .items() -> pasangan (kunci, nilai)
        batas_min, batas_max = data["batas"]  # TUPLE UNPACKING
        print(f"  {kode}. {data['nama']:<7} | angka {batas_min}-{batas_max} "
              f"| nyawa {data['nyawa']}")

    while True:
        pilihan = input("Masukkan nomor level: ").strip()
        if pilihan in LEVEL:           # cek apakah kunci ada di dictionary
            return LEVEL[pilihan]
        print("Pilihan tidak valid, coba lagi.")


def tampilkan_riwayat(riwayat):
    """Menampilkan riwayat tebakan memakai for + enumerate + slicing."""
    if len(riwayat) == 0:
        return
    # [MATERI 7] join() menggabungkan list menjadi satu string.
    # str(x) mengubah angka (int) ke string, dibuat dengan list comprehension.
    teks = ", ".join([str(x) for x in riwayat])
    print(f"  Riwayat tebakan : {teks}")
    if len(riwayat) > 3:
        # slicing negatif: ambil 3 elemen terakhir
        print(f"  3 tebakan terakhir: {riwayat[-3:]}")


# =====================================================================
# BAGIAN E - GAME UTAMA
# =====================================================================

def main_game():
    """Satu ronde permainan. Menggabungkan hampir semua materi."""
    level = pilih_level()

    # [MATERI 8] Tuple unpacking dari nilai dictionary
    batas_min, batas_max = level["batas"]
    nyawa_awal = level["nyawa"]
    nyawa = nyawa_awal                       # variabel int (bisa berubah)
    rahasia = random.randint(batas_min, batas_max)

    riwayat = []        # [MATERI 7] list kosong untuk menyimpan tebakan
    menang = False      # [MATERI 1] tipe data bool sebagai penanda status

    print(f"\nAku memilih angka antara {batas_min} dan {batas_max}.")
    print(f"Kamu punya {nyawa} nyawa. Selamat bermain!")

    # [MATERI 4] WHILE: ulangi selama nyawa masih ada dan belum menang
    while nyawa > 0 and not menang:
        print(f"\n--- Nyawa: {'♥ ' * nyawa}({nyawa}) ---")
        masukan = input("Tebakanmu: ").strip()

        # ---- Validasi input (nested if + continue) ----
        # [MATERI 5] 'continue' = lompati sisa kode, langsung ulang loop
        if not apakah_angka(masukan):
            print("Masukkan harus berupa angka bulat positif!")
            continue                          # nyawa TIDAK berkurang

        tebakan = int(masukan)                # konversi tipe: str -> int

        if not apakah_dalam_rentang(tebakan, batas_min, batas_max):
            print(f"Angka harus di antara {batas_min} dan {batas_max}!")
            continue

        # ---- Cek tebakan duplikat memakai LINEAR SEARCH ----
        if linear_search(riwayat, tebakan) != -1:
            print("Kamu sudah menebak angka itu. Coba angka lain!")
            continue

        riwayat.append(tebakan)               # tambah elemen ke list

        # ---- Pemilihan: benar atau salah ----
        if tebakan == rahasia:
            menang = True
        else:
            nyawa -= 1                        # operator assignment -=
            print(beri_petunjuk(rahasia, tebakan))
            hint = beri_petunjuk_tambahan(rahasia, len(riwayat))
            if hint != "":
                print(hint)
            tampilkan_riwayat(riwayat)

    # ---- Hasil akhir ----
    print("\n" + "=" * 45)       # string * int = diulang
    if menang:
        skor = hitung_skor(nyawa, nyawa_awal, level["pengali"])
        print(f"SELAMAT! Angkanya memang {rahasia}.")
        print(f"Kamu menebak dalam {len(riwayat)} percobaan. Skor: {skor}")
        simpan_ke_leaderboard(skor, level["nama"], len(riwayat))
    else:
        print(f"Nyawa habis! Angka rahasianya adalah {rahasia}.")

    tampilkan_analisis_binary(rahasia, batas_min, batas_max, len(riwayat))
    print("=" * 45)


def tampilkan_analisis_binary(rahasia, batas_min, batas_max, tebakan_pemain):
    """Membandingkan jumlah tebakan pemain dengan strategi BINARY SEARCH.
    list(range(...)) membuat list terurut berisi semua kemungkinan angka."""
    semua_angka = list(range(batas_min, batas_max + 1))
    _, langkah = binary_search(semua_angka, rahasia)   # '_' = abaikan nilai
    print("\n[Analisis Binary Search]")
    print(f"  Dengan strategi 'tebak tengah', angka ini ketemu dalam {langkah} langkah.")
    print(f"  Kamu memakai {tebakan_pemain} tebakan.")
    if tebakan_pemain <= langkah:
        print("  Hebat! Kamu seefisien (atau lebih dari) algoritma.")
    else:
        print("  Tips: selalu tebak angka TENGAH dari rentang yang tersisa.")


# =====================================================================
# BAGIAN F - LEADERBOARD (LIST + DICTIONARY + SORTING)
# =====================================================================

def simpan_ke_leaderboard(skor, nama_level, percobaan):
    """Meminta nama pemain, lalu menyimpan datanya sebagai dictionary."""
    nama = input("Masukkan namamu untuk leaderboard: ").strip()

    if nama == "":                  # string kosong dianggap False-ish
        nama = "Anonim"
    nama = nama.title()             # [MATERI 6] 'andhika' -> 'Andhika'
    nama = nama[:15]                # slicing: batasi maksimal 15 karakter

    # Membuat dictionary baru lalu memasukkannya ke list
    data_pemain = {
        "nama": nama,
        "skor": skor,
        "level": nama_level,
        "percobaan": percobaan,
    }
    leaderboard.append(data_pemain)
    print(f"Skor {nama} tersimpan!")


def tampilkan_leaderboard():
    """Menampilkan 5 skor tertinggi.
    sorted(..., key=lambda ...) mengurutkan list of dictionary berdasarkan skor.
    reverse=True -> dari terbesar ke terkecil."""
    if not leaderboard:             # list kosong dianggap False
        print("\nLeaderboard masih kosong. Ayo main dulu!")
        return

    urut = sorted(leaderboard, key=lambda p: p["skor"], reverse=True)

    print("\n=========== LEADERBOARD (Top 5) ===========")
    print(f"{'No':<4}{'Nama':<16}{'Level':<9}{'Skor':>6}")
    print("-" * 37)
    for nomor, pemain in enumerate(urut[:5], start=1):  # slicing top 5
        print(f"{nomor:<4}{pemain['nama']:<16}{pemain['level']:<9}{pemain['skor']:>6}")

    # Statistik sederhana memakai fungsi bawaan sum(), len(), max()
    semua_skor = [p["skor"] for p in leaderboard]   # list comprehension
    rata = sum(semua_skor) / len(semua_skor)
    print("-" * 37)
    print(f"Rata-rata skor: {rata:.1f} | Tertinggi: {max(semua_skor)}")


def menu_cari_pemain():
    """Menu pencarian pemain di leaderboard (memakai searching)."""
    nama = input("Masukkan nama yang dicari: ")
    hasil = cari_pemain(nama)
    if len(hasil) == 0:
        print("Pemain tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} data:")
        for p in hasil:
            print(f"  - {p['nama']} | {p['level']} | skor {p['skor']} "
                  f"| {p['percobaan']} percobaan")


def cara_bermain():
    """Menampilkan aturan. Memakai triple-quote string (multi-baris)."""
    print("""
============== CARA BERMAIN ==============
1. Komputer memilih angka rahasia secara acak.
2. Tebak angka tersebut sebelum nyawamu habis.
3. Setiap tebakan salah mengurangi 1 nyawa
   dan memberi petunjuk (kecil/besar & panas/dingin).
4. Input salah atau tebakan ganda TIDAK mengurangi nyawa.
5. Makin sedikit nyawa terpakai, makin tinggi skor.
==========================================""")


# =====================================================================
# BAGIAN G - PROGRAM UTAMA
# =====================================================================

def tampilkan_menu():
    """Menampilkan menu dari TUPLE MENU_UTAMA dengan nomor otomatis."""
    print("\n########## GAME TEBAK ANGKA ##########")
    for nomor, isi in enumerate(MENU_UTAMA, start=1):
        print(f"  {nomor}. {isi}")


def main():
    """Fungsi utama: loop menu sampai pemain memilih Keluar.
    [MATERI 3 dan 4] while True + if/elif/else sebagai 'saklar' menu."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            main_game()
        elif pilihan == "2":
            tampilkan_leaderboard()
        elif pilihan == "3":
            menu_cari_pemain()
        elif pilihan == "4":
            cara_bermain()
        elif pilihan == "5":
            print("Terima kasih sudah bermain. Sampai jumpa!")
            break                       # keluar dari while True
        else:
            print("Menu tidak tersedia, pilih 1-5.")


# Blok ini memastikan main() hanya jalan kalau file DIJALANKAN langsung,
# bukan saat di-import dari file lain. Ini kebiasaan baik di Python.
if __name__ == "__main__":
    main()
