# Skrip Python3 untuk menampilkan isi baris konfigurasi dari file /etc/crontab
# tanpa menampilkan baris yang memiliki "#" di paling kiri

def main():
    try:
        with open('/etc/crontab', 'r') as file:
            for line in file:
                # Memeriksa apakah baris tidak dimulai dengan "#"
                if not line.strip().startswith('#'):
                    print(line.strip())
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
