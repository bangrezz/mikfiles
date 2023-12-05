import os
import time

os.system('')

def selectionFile():
    os.system('clear')
    from ui import inputPrep
    if selection_format == "1":
        inputPrep.hostnameDefSelection()
    elif selection_format == "2":
        inputPrep.ipAddrDefSelection()
    else:
        print("unknown")
    from ui import selectFileExport
    selectFileExport.selectFile()
    selection_file = str(input("Select 1/2/3/b/e : "))
    if selection_file == "1": # export log file
        from modules import hostnameLog
        from modules import ipAddressLog
        if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
            hostnameLog.main()
        elif selection_format == "2": # [DONE] Execute ip address modules if selection format 2
            ipAddressLog.main()
        else:
            print("error")
            os.system('exit')
    elif selection_file == "2": # export file config and backup
        """
         # Untuk ekspor file config, harus membuat regexp baru lagi, 
         # kemudian harus memisahkan file hostname log dengan hostname file config
        atau bisa dengan membuatkan function didalam file hostname.py untuk ekspor log atau file config
        """
        print("Export file configuration and backup file")
        from modules import hostnameFileConf
        from modules import ipAddressFileConf
        if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
            hostnameFileConf.main()
        elif selection_format == "2": # [DONE] Execute hostname modules if selection format 1
            ipAddressFileConf.main()
        else:
            print("error")
            os.system('exit')
    elif selection_file == "3":
        print("Export both coming soon")
        print("Back to the previous. Wait 3s...")
        time.sleep(3)
        main()
    elif selection_file == "b":
        print("Back to the previous")
        main()
    elif selection_file == "q":
        print("\nExit mikfiles")
        os.system('exit')

def main():
    # select format name
    os.system('clear')
    from ui import selectFormatHostname
    selectFormatHostname.selectFormat()

    global selection_format
    selection_format = str(input("Select 1/2/q : "))
    if selection_format == "1":
        selectionFile()
    elif selection_format == "2":
        selectionFile()
    elif selection_format == "q":
        print("\nExit mikfiles")
        os.system('exit')
    else:
        print("\nError. Type again, wait 3s...")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
