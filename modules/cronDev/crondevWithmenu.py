import re
import os

# Fungsi untuk menganalisis dan menjelaskan baris konfigurasi cron
def jelaskan_cron():
    try:
        with open('/etc/crontab', 'r') as file:
            # Menambahkan variabel penghitung
            counter = 1
            for line in file:
                # Memeriksa apakah baris tidak dimulai dengan "#" dan bukan baris kosong
                if not line.strip().startswith('#') and line.strip():
                    # Menampilkan konfigurasi cron asli
                    print(f"Konfigurasi Cron Asli {counter}: {line.strip()}")
                    parts = line.split()
                    if len(parts) >= 6:
                        # Mengganti karakter '*' dengan '-' dalam bagian waktu
                        waktu = ' '.join(part if part != '*' else '-' for part in parts[:5])
                        # Menjelaskan waktu jadwal cron
                        waktu_jelaskan = f"Menit: {parts[0].replace('*', '-')}, Jam: {parts[1].replace('*', '-')}, Hari dari bulan: {parts[2].replace('*', '-')}, Bulan: {parts[3].replace('*', '-')}, Hari dari minggu: {parts[4].replace('*', '-')}"
                        # Menjelaskan perintah yang akan dijalankan
                        perintah = ' '.join(parts[5:])
                        print(f"{counter}. {waktu_jelaskan}, Perintah: {perintah}")
                        # Meningkatkan penghitung
                        counter += 1
                    else:
                        print("Baris tidak valid atau tidak lengkap.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan menu dan memproses pilihan pengguna
def tampilkan_menu():
    print("\nMenu:")
    print("1. Add   2. Edit    3. Delete   4. Disable")
    pilihan = input("Masukkan pilihan Anda (1-4): ")
    return pilihan

# Fungsi untuk menambahkan baris konfigurasi cron
def tambahkan_cron():
    # Menerima input dari pengguna
    menit = input("Masukkan menit (0-59 atau *): ")
    jam = input("Masukkan jam (0-23 atau *): ")
    hari_dari_bulan = input("Masukkan hari dari bulan (1-31 atau *): ")
    bulan = input("Masukkan bulan (1-12 atau *): ")
    hari_dari_minggu = input("Masukkan hari dari minggu (0-7 dimana 0 dan 7 adalah Minggu, atau *): ")
    perintah = input("Masukkan perintah yang ingin dijalankan: ")

    # Membuat baris konfigurasi cron
    cron_baru = f"{menit} {jam} {hari_dari_bulan} {bulan} {hari_dari_minggu} {perintah}\n"

    try:
        with open('/etc/crontab', 'a') as file:
            file.write(cron_baru)
        print("Konfigurasi cron berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk mengedit baris konfigurasi cron
def edit_cron():
    # Implementasi fungsi ini tergantung pada kebutuhan spesifik Anda
    pass

# Fungsi untuk menghapus baris konfigurasi cron
def hapus_cron():
    # Implementasi fungsi ini tergantung pada kebutuhan spesifik Anda
    pass

# Fungsi untuk menonaktifkan baris konfigurasi cron
def nonaktifkan_cron():
    # Implementasi fungsi ini tergantung pada kebutuhan spesifik Anda
    pass

def main():
    # Menampilkan penjelasan baris konfigurasi cron
    jelaskan_cron()
    # Menampilkan menu
    pilihan = tampilkan_menu()
    if pilihan == '1':
        tambahkan_cron()
    elif pilihan == '2':
        edit_cron()
    elif pilihan == '3':
        hapus_cron()
    elif pilihan == '4':
        nonaktifkan_cron()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()