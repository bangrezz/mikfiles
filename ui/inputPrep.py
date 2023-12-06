import os
cls = os.system('clear')

class ExportFileDef:
    def hostnameLogDef():
        print("[->] Export Log File with Hostname format")
    def ipAddrLogDef():
        print("[->] Export Log File with IP Address format")
    def hostnameFileConfDef():
        print("[->] Export File Configuration and Backup file with Hostname format")
    def ipAddrFileConfDef():
        print("[->] Export File Configuration and Backup file with IP Address format")
    def hostnameExportBoth():
        print("[->] Export Log, Config, Backup Configuration Files with hostname format")
    def ipAddrExportBoth():
        print("[->] Export Log, Config, Backup Configuration Files with hostname format")

def hostnameDefSelection():
    cls
    print("[->] Export with Hostname format")
def ipAddrDefSelection():
    cls
    print("[->] Export with IP address format")

def inputPrep():
    print("""
        [*] Input range IP Address with format in below
             
        192.168.1.1 [single IP Address]
            or
        192.168.1.0/24
            or
        192.168.1.1-192.168.1.100 (no space between '-')


        """)