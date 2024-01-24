import paramiko
import ipaddress
import socket
import os
import datetime
import time
import re

def login_mikrotik(ip, username, password, port, login_status):
    if login_status.get(ip, False):
        print("\033[32m" + f"[i] {ip} already logged in, skipping..." + "\033[0m")
        return False

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=3)
        print("\033[32m" + f"[i] Successfull {ip}:{port}" + "\033[0m")

        login_status[ip] = True

        # Get the hostname
        stdin, stdout, stderr = ssh.exec_command(":put [/system identity get name]")
        hostname = stdout.read().decode().strip()

        # Get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Define the log filename
        log_filename = f"{ip}_{date_time}"

        # Export the log file
        command = f"/log print file={log_filename}"
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"[i] Execute command '{command}' di {ip}:")
        print(stdout.read().decode())

        time.sleep(5)  # wait for 5 seconds

        # Buat objek SFTP
        sftp = ssh.open_sftp()

        # Pola regexp untuk mencocokkan nama file
        # \S+ cocok dengan satu atau lebih karakter non-whitespace
        pattern = rf"{ip}_\d{{4}}-\d{{2}}-\d{{2}}_\d{{2}}-\d{{2}}-\d{{2}}\.txt"

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
        print("\033[31m" + f"[!] Target {ip}:{port} none: Connection timed out." + "\033[0m")
        print("[i] Maybe devices is off or filtered by firewall devices")
    except paramiko.AuthenticationException:
        print(f"\033[31m" + "[!]" + "\033[0m" + f" Failed login to {ip}:{port} authentication failed")
    except Exception as e:
        print(f"\033[31m" + "[!]" + "\033[0m" + f" Failed login to {ip}:{port}: {e}")
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
            print("Invalid input. Please enter numbers only.")
        else:
            ports = [int(port) for port in ports]
            break

    login_status = {}

    while True:
        ip_input = input("[+] input IP Address : ")
        ip_entries = [ip.strip() for ip in ip_input.split(',')]
        if not all(validate_ip(ip) for ip in ip_entries):
            print("Invalid input. Please enter valid IP addresses.")
        else:
            break

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