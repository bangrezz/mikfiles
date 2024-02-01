import paramiko
import ipaddress
import socket
import os
import datetime
import re

def login_mikrotik(ip, username, password, port, login_status):
    if login_status.get(ip, False):
        print("\033[32m" + "[i]" + "\033[0m" + f" {ip} already logged in, skipping...")
        return False

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=3)
        print("\033[32m" + "[i]" + "\033[0m" + f" Successfull login {ip}:{port}")

        login_status[ip] = True

        # Get the hostname
        stdin, stdout, stderr = ssh.exec_command(":put [/system identity get name]")
        hostname = stdout.read().decode().strip()

        # Get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Define the log filename
        global log_filename
        log_filename = f"{hostname}_{date_time}"

        # Export the log file
        command = f"/log print file={log_filename}"
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"[i] Execute command to " + "\033[32m" + f"{ip}:" + "\033[0m" + f"\n{command}")
        print("\033[32m" + "[i]" + "\033[0m" + " Result from MikroTik: ", stdout.read().decode(), end='',); print("\n")

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
        return True
    except socket.timeout:
        print("\033[31m" + "[!]" + "\033[0m" + f" Failed login to {ip}:{port}: Connection timed out.")
    except paramiko.AuthenticationException:
        print("\033[31m" + "[!]" + "\033[0m" + f" Failed login to {ip}:{port}: Authentication failed")
    except Exception as e:
        print("\033[31m" + "[!]" + "\033[0m" + f" Failed login to {ip}:{port}: {e}")
        return False
    finally:
        ssh.close()

def main():
    username = str(input("[+] Input Username : "))
    password = str(input("[+] Input Password : "))

    while True:
        ports_input = input("[+] Input SSH ports (comma separated) [Press Enter if default (port 22)] : ")
        ports = [port.strip() for port in ports_input.split(',')] if ports_input else ['22']
        if not all(port.isdigit() for port in ports):
            print(f"\033[31m" + "[!]" + "\033[0m" + "Invalid input. Input number only !")
        else:
            ports = [int(port) for port in ports]
            break

    login_status = {}

    while True:
        ip_input = input("[+] input IP Address : ")
        ip_entries = [ip.strip() for ip in ip_input.split(',')]
        if not all(validate_ip(ip) for ip in ip_entries):
            print(f"\033[31m" + "[!]" + "\033[0m" + "Invalid input. Please enter valid IP addresses !")
        else:
            break

    print("\n[i] Attempt to login :")
    for entry in ip_entries:
        if '-' in entry:
            start_ip, end_ip = entry.split('-')
            start_ip = ipaddress.IPv4Address(start_ip)
            end_ip = ipaddress.IPv4Address(end_ip)

            for ip_int in range(int(start_ip), int(end_ip) + 1):
                ip = ipaddress.IPv4Address(ip_int)
                for port in ports:
                    if login_mikrotik(str(ip), username, password, port, login_status):
                        break
        elif '/' in entry:
            ip_range = ipaddress.ip_network(entry, strict=False)
            for ip in ip_range.hosts():
                for port in ports:
                    if login_mikrotik(str(ip), username, password, port, login_status):
                        break
        else:
            try:
                ipaddress.IPv4Address(entry)  # Memvalidasi alamat IP
                for port in ports:
                    if login_mikrotik(entry, username, password, port, login_status):
                        break
            except ipaddress.AddressValueError as ave:
                print(f"\033[31m" + "[!]" + "\033[0m" + f" IP Address doesn't valid: {ave}")
    print("\n\033[32m" + "[i]" + "\033[0m" + " Finish attempting to login")
    # to counter failed connect to all ip for first time mikfiles usage
    try:
        print(f"[i] Your file format is : " + "\033[32m" + f"{log_filename}" + "\033[0m")
    except Exception:
        print("\033[31m" + "[!]" + "\033[0m" + " All device can't connect")

def validate_ip(ip):
    if '-' in ip:
        start_ip, end_ip = ip.split('-')
        return validate_single_ip(start_ip) and validate_single_ip(end_ip)
    elif '/' in ip:
        try:
            ipaddress.ip_network(ip, strict=False)
            return True
        except ValueError:
            return False
    else:
        return validate_single_ip(ip)

def validate_single_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False