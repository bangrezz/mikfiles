# dev file
import re
import os
import shutil
import platform

# Fungsi untuk memeriksa sistem operasi dan file crontab
def cek_sistem_dan_file():
    # Mendeteksi sistem operasi user
    if platform.system() != 'Linux':
        print("Skrip ini hanya dapat dijalankan pada sistem operasi Linux.")
        return False

    # Mendeteksi file crontab
    if os.path.exists('/etc/crontab'):
        # Jika file backup belum ada, lakukan backup
        if not os.path.exists('/etc/crontab.bak'):
            shutil.copy2('/etc/crontab', '/etc/crontab.bak')
            print("File crontab telah dibackup.")
        # Menambahkan kalimat ke baris paling bawah file crontab
        with open('/etc/crontab', 'r') as file:
            if '# generated by mikfiles' in file.read():
                print("Kalimat sudah ada di file crontab.")
            else:
                # Menambahkan kalimat ke baris paling bawah file crontab jika belum ada
                with open('/etc/crontab', 'a') as file:
                    file.write("\n# generated by mikfiles\n")
                print("Kalimat telah ditambahkan ke baris paling bawah file crontab.")
    else:
        # Jika file crontab tidak ada, buat file baru
        with open('/etc/crontab', 'w') as file:
            file.write("# generated by mikfiles\n")
        print("File crontab baru telah dibuat.")

    return True

# Fungsi untuk menganalisis dan menjelaskan baris konfigurasi cron
def jelaskan_cron():
    konfigurasi_cron = []  # Daftar untuk menyimpan baris konfigurasi cron
    komentar_dan_non_cron = []  # Daftar untuk menyimpan komentar dan baris non-cron
    try:
        with open('/etc/crontab', 'r') as file:
            for line in file:
                if not line.strip().startswith('#') and line.strip():
                    konfigurasi_cron.append((line.strip(), "active"))  # Menambahkan baris konfigurasi cron ke daftar
                elif line.strip().startswith('#') and len(line.strip().split()) > 1:
                    konfigurasi_cron.append((line.strip(), "inactive"))
                else:
                    komentar_dan_non_cron.append(line.strip())
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    return konfigurasi_cron, komentar_dan_non_cron

def baca_crontab():
    konfigurasi_cron = []  # Daftar untuk menyimpan baris konfigurasi cron
    komentar_dan_non_cron = []  # Daftar untuk menyimpan komentar dan baris non-cron
    cron_pattern = re.compile(r'^\s*(\d+|\*)\s+(\d+|\*)\s+(\d+|\*)\s+(\d+|\*)\s+(\d+|\*)\s+.*$')
    format_cron_pattern = re.compile(r'^#\s*\*\s*\*\s*\*\s*\*\s*\*\s*user-name command to be executed$')
    try:
        with open('/etc/crontab', 'r') as file:
            for line in file:
                if format_cron_pattern.match(line):
                    komentar_dan_non_cron.append(line.strip())
                elif (cron_pattern.match(line) and not line.strip() == "* * * * *") or (line.strip().startswith('# ') and cron_pattern.match(line.strip()[2:]) and not line.strip()[2:] == "* * * * *"):
                    konfigurasi_cron.append(line.strip())  # Menambahkan baris konfigurasi cron ke daftar
                else:
                    komentar_dan_non_cron.append(line.strip())
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    return konfigurasi_cron, komentar_dan_non_cron

def tulis_crontab(konfigurasi_cron, komentar_dan_non_cron):
    try:
        with open('/etc/crontab', 'w') as file:
            for line in komentar_dan_non_cron:
                file.write(f"{line}\n")
            for konfigurasi in konfigurasi_cron:
                file.write(f"{konfigurasi}\n")
        print(f"\033[32m" + "[*]" + "\033[0m" + " File crontab berhasil diperbarui.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan menu dan memproses pilihan pengguna
def tampilkan_menu():
    print("\nMenu:")
    print("1. Add   2. Edit    3. Delete   4. Disable   5. Enable")
    pilihan = input("Masukkan pilihan Anda (1-5): ")
    return pilihan

# Fungsi untuk menambahkan baris konfigurasi cron
def tambahkan_cron(konfigurasi_cron):
    # Menerima input dari pengguna
    menit = input("Masukkan menit (0-59 atau *, tekan enter untuk *): ") or '*'
    jam = input("Masukkan jam (0-23 atau *, tekan enter untuk *): ") or '*'
    hari_dari_bulan = input("Masukkan hari dari bulan (1-31 atau *, tekan enter untuk *): ") or '*'
    bulan = input("Masukkan bulan (1-12 atau *, tekan enter untuk *): ") or '*'
    hari_dari_minggu = input("Masukkan hari dari minggu (0-7 dimana 0 dan 7 adalah Minggu, atau *, tekan enter untuk *): ") or '*'
    perintah = input("Masukkan perintah yang ingin dijalankan: ")

    # Membuat baris konfigurasi cron
    cron_baru = f"{menit} {jam} {hari_dari_bulan} {bulan} {hari_dari_minggu} {perintah}\n"

    try:
        with open('/etc/crontab', 'a') as file:
            file.write(cron_baru)
        konfigurasi_cron.append(cron_baru.strip())
        print(f"\033[32m" + "[*]" + "\033[0m" + " Konfigurasi cron berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#fungsi untuk edit baris konfigurasi cron
def edit_cron(konfigurasi_cron):
    nomor_konfigurasi = int(input("Masukkan nomor konfigurasi cron yang ingin Anda edit: "))
    if 1 <= nomor_konfigurasi <= len(konfigurasi_cron):
        parts = konfigurasi_cron[nomor_konfigurasi - 1].split()
        if len(parts) >= 6:
            menit_lama, jam_lama, hari_dari_bulan_lama, bulan_lama, hari_dari_minggu_lama, *perintah_lama = parts
            perintah_lama = ' '.join(perintah_lama)
        else:
            menit_lama = jam_lama = hari_dari_bulan_lama = bulan_lama = hari_dari_minggu_lama = '*'
            perintah_lama = ' '.join(parts)

        # Tambahkan kode berikut
        edit_file = input("Apakah Anda ingin mengedit file yang akan dieksekusi cron (y/n)? ")
        if edit_file.lower() == 'y':
            file_path = ' '.join(perintah_lama.split()[2:])  # Ambil path file dari perintah
            if os.path.isfile(file_path):
                with open(file_path, 'a') as file:
                    file.write("\nhello world\n")
                print("Kalimat 'hello world' telah ditambahkan ke baris akhir file.")

                # Tambahkan kode berikut untuk membaca variabel dari file
                with open(file_path, 'r') as file:
                    content = file.read()
                    username = re.search(r'username\s*=\s*str\(input\("Input Username : "\)\)', content)
                    password = re.search(r'password\s*=\s*str\(input\("Input Password : "\)\)', content)
                    port_input = re.search(r'port_input\s*=\s*input\("Masukkan port SSH \[Press Enter if default \(port 22\)\] : "\)', content)
                    

                    if username:
                        print(f"username: {username.group()}")
                    if password:
                        print(f"password: {password.group()}")
                    if port_input:
                        print(f"port: {port_input.group()}")

                # Tambahkan kode berikut untuk meminta pengguna apakah mereka ingin mengedit variabel
                edit_vars = input("Apakah Anda ingin mengedit variabel ini (y/n)? ")
                if edit_vars.lower() == 'y':
                    new_username = input(f"Masukkan nilai baru untuk username (tekan enter untuk tidak mengubah): ")
                    new_password = input(f"Masukkan nilai baru untuk password (tekan enter untuk tidak mengubah): ")
                    new_port_input = input(f"Masukkan nilai baru untuk port (tekan enter untuk tidak mengubah): ")

                    # Ganti nilai variabel dalam file
                    with open(file_path, 'r') as file:
                        content = file.read()
                    if new_username:
                        content = re.sub(r'(username\s*=\s*str\(input\("Input Username : "\)\))', f'username = "{new_username}"', content)
                    if new_password:
                        content = re.sub(r'(password\s*=\s*str\(input\("Input Password : "\)\))', f'password = "{new_password}"', content)
                    if new_port_input:
                        content = re.sub(r'port_input\s*=\s*input\("Masukkan port SSH \[Press Enter if default \(port 22\)\] : "\)', f'port_input = "{new_port_input}"', content)
                    with open(file_path, 'w') as file:
                        file.write(content)
                    print("Variabel telah berhasil diperbarui.")
            else:
                print("Perintah cron tidak berisi path file yang valid.")
        else:
            print("Perintah cron tidak berisi path file yang valid.")
        
        menit = input(f"Masukkan menit baru (0-59 atau *, tekan enter untuk tidak mengubah): ") or menit_lama
        jam = input(f"Masukkan jam baru (0-23 atau *, tekan enter untuk tidak mengubah): ") or jam_lama
        hari_dari_bulan = input(f"Masukkan hari dari bulan baru (1-31 atau *, tekan enter untuk tidak mengubah): ") or hari_dari_bulan_lama
        bulan = input(f"Masukkan bulan baru (1-12 atau *, tekan enter untuk tidak mengubah): ") or bulan_lama
        hari_dari_minggu = input(f"Masukkan hari dari minggu baru (0-7 dimana 0 dan 7 adalah Minggu, atau *, tekan enter untuk tidak mengubah): ") or hari_dari_minggu_lama
        perintah = input(f"Masukkan perintah baru yang ingin dijalankan (tekan enter untuk tidak mengubah): ") or perintah_lama
        konfigurasi_cron[nomor_konfigurasi - 1] = f"{menit} {jam} {hari_dari_bulan} {bulan} {hari_dari_minggu} {perintah}"
        with open('/etc/crontab', 'w') as file:
            for konfigurasi in konfigurasi_cron:
                file.write(f"{konfigurasi}\n")
        print(f"\033[32m" + "[*]" + "\033[0m" + " Konfigurasi cron berhasil diedit.")
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Nomor konfigurasi cron tidak valid.")

# Fungsi untuk menghapus baris konfigurasi cron
def hapus_cron(konfigurasi_cron):
    nomor_konfigurasi = int(input("Masukkan nomor konfigurasi cron yang ingin Anda hapus: "))
    if 1 <= nomor_konfigurasi <= len(konfigurasi_cron):
        del konfigurasi_cron[nomor_konfigurasi - 1]
        print(f"\033[32m" + "[*]" + "\033[0m" + " Konfigurasi cron berhasil dihapus.")
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Nomor konfigurasi cron tidak valid.")

def aktifkan_cron(konfigurasi_cron):
    nomor_konfigurasi = int(input("Masukkan nomor konfigurasi cron yang ingin Anda aktifkan: "))
    if 1 <= nomor_konfigurasi <= len(konfigurasi_cron):
        if konfigurasi_cron[nomor_konfigurasi - 1].startswith('# '):
            konfigurasi_cron[nomor_konfigurasi - 1] = konfigurasi_cron[nomor_konfigurasi - 1][2:]
            print(f"\033[32m" + "[*]" + "\033[0m" + " Konfigurasi cron berhasil diaktifkan.")
        else:
            print(f"\033[31m" + "[!]" + "\033[0m" + " Konfigurasi cron sudah aktif.")
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Nomor konfigurasi cron tidak valid.")

# Fungsi untuk menonaktifkan baris konfigurasi cron
def nonaktifkan_cron(konfigurasi_cron):
    nomor_konfigurasi = int(input("Masukkan nomor konfigurasi cron yang ingin Anda nonaktifkan: "))
    if 1 <= nomor_konfigurasi <= len(konfigurasi_cron):
        if konfigurasi_cron[nomor_konfigurasi - 1].startswith('# '):
            print(f"\033[31m" + "[!]" + "\033[0m" + " Konfigurasi cron sudah dinonaktifkan.")
        else:
            konfigurasi_cron[nomor_konfigurasi - 1] = '# ' + konfigurasi_cron[nomor_konfigurasi - 1]
            print(f"\033[32m" + "[*]" + "\033[0m" + " Konfigurasi cron berhasil dinonaktifkan.")
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Nomor konfigurasi cron tidak valid.")

def jelaskan_konfigurasi_cron(konfigurasi, status):
    bagian = konfigurasi.split()
    if len(bagian) >= 6:
        menit, jam, hari_dari_bulan, bulan, hari_dari_minggu, *perintah = bagian
        perintah = ' '.join(perintah)
        
        # Ganti '*' dengan '-'
        if menit == '*': menit = '-'
        if jam == '*': jam = '-'
        if hari_dari_bulan == '*': hari_dari_bulan = '-'
        if bulan == '*': bulan = '-'
        if hari_dari_minggu == '*': hari_dari_minggu = '-'
        
        print(f"[*] Status = {status}")
        print(f"[*] Time = Menit: {menit}, Jam: {jam}, Hari dari bulan: {hari_dari_bulan}, Bulan: {bulan}, Hari dari minggu: {hari_dari_minggu}")
        print(f"[*] Commands = {perintah}")
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Konfigurasi cron tidak valid.")

def main():
    # checking crontab file
    cek_sistem_dan_file()
    
    # reading crontab file
    konfigurasi_cron, komentar_dan_non_cron = baca_crontab()
    for i, konfigurasi in enumerate(konfigurasi_cron, start=1):
        print(f"\033[34m" + f"[{i}]" + "\033[0m" + f" Konfigurasi Cron Asli : {konfigurasi}")
        # Menentukan status berdasarkan apakah konfigurasi dimulai dengan '# '
        status = 'inactive' if konfigurasi.startswith('# ') else 'active'
        jelaskan_konfigurasi_cron(konfigurasi, status)
    pilihan = tampilkan_menu()
    print(f"Pilihan Anda: {pilihan}")
    if pilihan == '1':
        tambahkan_cron(konfigurasi_cron)
        tulis_crontab(konfigurasi_cron, komentar_dan_non_cron)
        konfigurasi_cron, komentar_dan_non_cron = baca_crontab()
    elif pilihan == '2':
        edit_cron(konfigurasi_cron)
        tulis_crontab(konfigurasi_cron, komentar_dan_non_cron)
    elif pilihan == '3':
        hapus_cron(konfigurasi_cron)
        tulis_crontab(konfigurasi_cron, komentar_dan_non_cron)
    elif pilihan == '4':
        nonaktifkan_cron(konfigurasi_cron)
        tulis_crontab(konfigurasi_cron, komentar_dan_non_cron)
    elif pilihan == '5':
        aktifkan_cron(konfigurasi_cron)
        tulis_crontab(konfigurasi_cron, komentar_dan_non_cron)
    else:
        print(f"\033[31m" + "[!]" + "\033[0m" + " Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()