import os

LEADERBOARD_FILE = "leaderboard.txt"

def load_leaderboard():
    """Membaca data dari file teks leaderboard.txt."""
    leaderboard = []
    if not os.path.exists(LEADERBOARD_FILE):
        return leaderboard
        
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Format baris di file: Nama,TotalPercobaan,Level
                    parts = line.split(",")
                    if len(parts) == 3:
                        name, attempts, level = parts
                        leaderboard.append({
                            "name": name,
                            "attempts": int(attempts),
                            "level": level
                        })
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat membaca file: {e}")
        
    return leaderboard

def save_leaderboard(leaderboard):
    """Menyimpan kembali daftar leaderboard ke file teks."""
    try:
        with open(LEADERBOARD_FILE, "w") as file:
            for entry in leaderboard:
                line = f"{entry['name']},{entry['attempts']},{entry['level']}\n"
                file.write(line)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan file: {e}")

def update_leaderboard(player_name, attempts, level_name):
    """Menambahkan skor baru, mengurutkannya, dan membatasi 5 besar."""
    leaderboard = load_leaderboard()
    
    # Masukkan data pemain yang baru menang
    leaderboard.append({
        "name": player_name,
        "attempts": attempts,
        "level": level_name
    })
    
    # Urutkan berdasarkan jumlah percobaan paling sedikit (ascending)
    leaderboard.sort(key=lambda x: x["attempts"])
    
    # Ambil 5 skor terbaik saja
    leaderboard = leaderboard[:5]
    
    save_leaderboard(leaderboard)
    print(f"🏆 Hebat! Skor {player_name} berhasil masuk leaderboard!")

def display_leaderboard():
    """Menampilkan tabel leaderboard ke terminal."""
    leaderboard = load_leaderboard()
    
    print("\n==================================================")
    print("                  🏆 DAFTAR LEADERBOARD 🏆               ")
    print("==================================================")
    if not leaderboard:
        print("Belum ada data di leaderboard. Jadilah yang pertama!")
    else:
        print(f"{'Peringkat':<10} {'Nama Penebak':<15} {'Level':<12} {'Percobaan':<10}")
        print("-" * 50)
        for idx, entry in enumerate(leaderboard, start=1):
            print(f"{idx:<10} {entry['name']:<15} {entry['level']:<12} {entry['attempts']:<10}")
    print("==================================================")
    input("\nTekan Enter untuk kembali ke menu utama...")

def main_game():
    print("\n==========================================")
    print("      🎮 PERMAINAN TEBAK ANGKA 🎮          ")
    print("==========================================")

    # 1. Pemilihan Level Kesulitan
    print("\nPilih Tingkat Kesulitan:")
    print("1. Mudah  (Rentang 1 - 50,  Nyawa: 8)")
    print("2. Sedang (Rentang 1 - 100, Nyawa: 6)")
    print("3. Sulit  (Rentang 1 - 200, Nyawa: 5)")

    pilihan_level = input("\Pilih level (1-3): ")

    if pilihan_level == "1":
        nama_level = "Mudah"
        batas_maks = 50
        nyawa = 8
    elif pilihan_level == "2":
        nama_level = "Sedang"
        batas_maks = 100
        nyawa = 6
    elif pilihan_level == "3":
        nama_level = "Sulit"
        batas_maks = 200
        nyawa = 5
    else:
        print(
            "⚠️ Pilihan salah, otomatis ke Level Sedang (1-100, Nyawa: 6)."
        )
        nama_level = "Sedang"
        batas_maks = 100
        nyawa = 6

    # 2. Pemain 1 Memasukkan Angka Rahasia
    print(f"\n--- LEVEL: {nama_level.upper()} ---")
    pembuat_angka = input("Nama Pemain 1 (Pembuat Angka): ")
    penebak = input("Nama Pemain 2 (Penebak Angka): ")

    # Loop penentu angka rahasia sampai inputnya benar di dalam rentang
    while True:
        try:
            angka_rahasia = int(
                input(
                    f"\n[{pembuat_angka}] Masukkan angka rahasia (1-{batas_maks}): "
                )
            )
            if 1 <= angka_rahasia <= batas_maks:
                break
            print(f"⚠️ Angka harus di dalam rentang 1 sampai {batas_maks}!")
        except ValueError:
            print("❌ Input harus berupa angka bulat!")

    # Menyembunyikan angka dari layar
    print("\n" * 30)
    print(f"Giliran {penebak} untuk menebak!")
    print(
        f"Level: {nama_level} | Rentang: 1 - {batas_maks} | Nyawa: {nyawa}"
    )

    # 3. Perulangan Tebakan Pemain 2
    riwayat_tebakan = []
    status_menang = False

    while nyawa > 0:
        print(f"\nNyawa Tersisa: {'❤️ ' * nyawa} ({nyawa})")
        if riwayat_tebakan:
            print(f"Riwayat Tebakan: {riwayat_tebakan}")

        try:
            tebakan = int(input(f"Tebakanmu (1-{batas_maks}): "))
        except ValueError:
            print("❌ Input harus berupa angka!")
            continue

        if tebakan < 1 or tebakan > batas_maks:
            print(f"⚠️ Tebak angka antara 1 sampai {batas_maks} saja!")
            continue

        riwayat_tebakan.append(tebakan)

        if tebakan == angka_rahasia:
            status_menang = True
            break
        elif tebakan < angka_rahasia:
            print("📈 Terlalu RENDAH! Coba angka lebih besar.")
        else:
            print("📉 Terlalu TINGGI! Coba angka lebih kecil.")

        nyawa -= 1

    # 4. Pengumuman Hasil
    print("\n" + "-" * 40)
    if status_menang:
        print(f"🎉 SELAMAT {penebak.upper()}! Tebakan kamu BENAR!")
        print(f"Angka rahasianya memang: {angka_rahasia}")
        total_percobaan = len(riwayat_tebakan)
        print(f"Total Percobaan: {total_percobaan} kali")
        
        # Panggil fungsi update leaderboard jika pemain menang
        update_leaderboard(penebak, total_percobaan, nama_level)
    else:
        print(f"💥 GAME OVER, {penebak}! Nyawa kamu sudah habis.")
        print(f"Angka rahasia yang dibuat {pembuat_angka} adalah: {angka_rahasia}")
    print("-" * 40)

    input("\nTekan Enter untuk kembali ke menu utama...")
    
def main():
    while True:
        print("\n==========================================")
        print("      🎯 GAME TEBAK ANGKA TERMINAL 🎯      ")
        print("==========================================")
        print("1. Mulai Permainan")
        print("2. Lihat Leaderboard")
        print("3. Keluar")

        try:
            pilih = int(input("Pilih Menu (1-3): "))
            if pilih == 1:
                main_game()
            elif pilih == 2:
                display_leaderboard()
            elif pilih == 3:
                print("\nTerima kasih sudah bermain! Semangat Alpro-nya! ✨")
                break
            else:
                print("⚠️ Pilihan menu tidak valid.")
        except ValueError:
            print("❌ Masukkan angka menu 1, 2, atau 3!")


if __name__ == "__main__":
    main()
