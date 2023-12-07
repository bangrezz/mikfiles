import paramiko
import ipaddress
import socket
import sys
import os
import datetime
import time
import re

os.system('')

def loginMikroTikdivNetwork(ip, username, password, port): # for multiple address and the address different network
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=3)
        print("\033[32m" + f"[+] Berhasil login ke {ip}" + "\033[0m")
        # ... (sisanya sama dengan skrip asli)

        # Get the hostname
        stdin, stdout, stderr = ssh.exec_command(":put [/system identity get name]")
        hostname = stdout.read().decode().strip()

        # Get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Define the log filename
        log_filename = f"{hostname}_{date_time}"

        # Export the log file
        command = f"/log print file={log_filename}"
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"[*] Eksekusi perintah '{command}' di {ip}:")
        print(stdout.read().decode())

        time.sleep(5)  # wait for 5 seconds

        # Buat objek SFTP
        sftp = ssh.open_sftp()

        # Pola regexp untuk mencocokkan nama file
        # \S+ cocok dengan satu atau lebih karakter non-whitespace
        pattern = r"\b\S+_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.txt\b"

        # Mendapatkan daftar semua file di direktori root
        files = sftp.listdir('/')

        # Mencari file yang cocok dengan pola
        for file in files:
            if re.match(pattern, file):
                # Lokasi file di komputer lokal (direktori tempat skrip dijalankan)
                local_file = os.path.join(os.getcwd(), file)

                # Mendownload file
                sftp.get('/' + file, local_file)

                # deleteBackupFile
                sftp.remove('/' + file)

        # Menutup koneksi
        sftp.close()

    except socket.timeout:
        print("\033[31m" + f"[!] Target {ip} tidak ada: Connection timed out." + "\033[0m") # the script will try next address if exists
        print("[*] Coba lagi menggunakan network atau IP address yang berbeda")
    except paramiko.AuthenticationException:
        print(f"[!] Gagal login ke {ip} authentication failed")
    except Exception as e:
        print(f"[*] Gagal login ke {ip}: {e}")
    finally:
        ssh.close()

def login_mikrotik(ip, username, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=10)
        print("\033[32m" + f"[+] Berhasil login ke {ip}" + "\033[0m")
        # ... (sisanya sama dengan skrip asli)

        # Get the hostname
        stdin, stdout, stderr = ssh.exec_command(":put [/system identity get name]")
        hostname = stdout.read().decode().strip()

        # Get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Define the log filename
        log_filename = f"{hostname}_{date_time}"

        # Export the log file
        command = f"/log print file={log_filename}"
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"[*] Eksekusi perintah '{command}' di {ip}:")
        print(stdout.read().decode())

        time.sleep(5)  # wait for 5 seconds

        # Buat objek SFTP
        sftp = ssh.open_sftp()

        # Pola regexp untuk mencocokkan nama file
        # \S+ cocok dengan satu atau lebih karakter non-whitespace
        pattern = r"\b\S+_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.txt\b"

        # Mendapatkan daftar semua file di direktori root
        files = sftp.listdir('/')

        # Mencari file yang cocok dengan pola
        for file in files:
            if re.match(pattern, file):
                # Lokasi file di komputer lokal (direktori tempat skrip dijalankan)
                local_file = os.path.join(os.getcwd(), file)

                # Mendownload file
                sftp.get('/' + file, local_file)

                # deleteBackupFile
                sftp.remove('/' + file)

        # Menutup koneksi
        sftp.close()

    except socket.timeout:
        print("\033[31m" + f"[!] Target {ip} tidak ada: Connection timed out." + "\033[0m")
        print("[*] Coba lagi menggunakan network atau IP address yang berbeda")
        sys.exit(1)
    except paramiko.AuthenticationException:
        print(f"[!] Gagal login ke {ip} authentication failed")
    except Exception as e:
        print(f"[*] Gagal login ke {ip}: {e}")
    finally:
        ssh.close()

def main():
    os.system('clear')
    username = str(input("Input Username : "))
    password = str(input("Input Password : "))
    port = 22  # Default port value

    def portInput():
        nonlocal port
        port_input = input("Masukkan port SSH [Press Enter if default (port 22)] : ")
        if port_input:
            try:
                port = int(port_input)
            except ValueError:
                print("\n [!] Port harus berupa angka.")
                portInput()
    portInput()

    def AddrInput():
        ip_input = input("""
            [*] Masukkan IP address dengan format dibawah (pisahkan dengan koma untuk IP yang berbeda, atau gunakan '-' untuk rentang IP, atau '/' untuk subnet):
                |
                v
            192.168.1.1
                or
            192.168.122.2,192.168.100.1,192.168.1.1
                or
            192.168.1.0/24
                or
            192.168.1.1-192.168.1.100

            : """)

        if ',' in ip_input:
            # Memisahkan input berdasarkan koma dan menghapus spasi
            ip_list = [ip.strip() for ip in ip_input.split(',')]
            for ip in ip_list:
                try:
                    ipaddress.IPv4Address(ip)  # Memvalidasi alamat IP
                    loginMikroTikdivNetwork(ip, username, password, port)
                except ipaddress.AddressValueError as ave:
                    print(f"Alamat IP tidak valid: {ave}")
                    AddrInput()
        else:
            try:
                if '-' in ip_input:
                    start_ip, end_ip = ip_input.split('-')
                    start_ip = ipaddress.IPv4Address(start_ip)
                    end_ip = ipaddress.IPv4Address(end_ip)

                    for ip_int in range(int(start_ip), int(end_ip) + 1):
                        ip = ipaddress.IPv4Address(ip_int)
                        login_mikrotik(str(ip), username, password, port)
                else:
                    ip_range = ipaddress.ip_network(ip_input, strict=False)
                    for ip in ip_range.hosts():
                        login_mikrotik(str(ip), username, password, port)
            except ValueError as ve:
                print(f"Input tidak valid: {ve}")
                AddrInput()
            except ipaddress.AddressValueError as ave:
                print(f"Alamat IP tidak valid: {ave}")
                AddrInput()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                print("wait 3s ... ")
                time.sleep(3)
                main()
    AddrInput()

if __name__ == "__main__":
    main()
