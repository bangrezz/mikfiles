import re

# Fungsi untuk menganalisis dan menjelaskan baris konfigurasi cron
def jelaskan_cron(line):
    parts = line.split()
    if len(parts) >= 6:
        # Mengganti karakter '*' dengan '-' dalam bagian waktu
        waktu = ' '.join(part if part != '*' else '-' for part in parts[:5])
        # Menjelaskan waktu jadwal cron
        waktu_jelaskan = f"Menit: {parts[0].replace('*', '-')}, Jam: {parts[1].replace('*', '-')}, Hari dari bulan: {parts[2].replace('*', '-')}, Bulan: {parts[3].replace('*', '-')}, Hari dari minggu: {parts[4].replace('*', '-')}"
        # Menjelaskan perintah yang akan dijalankan
        perintah = ' '.join(parts[5:])
        return f"{waktu_jelaskan}, Perintah: {perintah}"
    else:
        return "Baris tidak valid atau tidak lengkap."

def main():
    try:
        with open('/etc/crontab', 'r') as file:
            for line in file:
                # Memeriksa apakah baris tidak dimulai dengan "#" dan bukan baris kosong
                if not line.strip().startswith('#') and line.strip():
                    # Mencetak baris konfigurasi dan penjelasannya dengan penggantian karakter '*'
                    print(line.strip())
                    print(jelaskan_cron(line.strip()))
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
