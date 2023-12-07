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
    def selectFilesNum():
        try:
            selection_file = str(input("Select 1/2/3/b/q : "))
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
                print("Export file configuration and backup file")
                from modules import hostnameFileConf
                from modules import ipAddressFileConf
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    hostnameFileConf.main()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    ipAddressFileConf.main()
                else:
                    print("error")
                    os.system('exit')
            elif selection_file == "3": # Export both
                print("Export both")
                from modules import HostnameExBoth
                from modules import ipAddressExBoth
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    HostnameExBoth.main()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    ipAddressExBoth.main()
                else:
                    print("error")
                    os.system('exit')
            elif selection_file == "b":
                print("Back to the previous")
                main()
            elif selection_file == "q":
                print("\nExit mikfiles")
                os.system('exit')
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectFilesNum()    
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectFilesNum()
        except KeyboardInterrupt:
            print("\nExit mikfiles ...")
            os.system('exit')
    selectFilesNum()

def main():
    # select format name
    os.system('clear')
    from ui import selectFormatHostname
    selectFormatHostname.selectFormat()
    #global selection_format
    def selectionFormat():
        try:
            global selection_format
            selection_format = str(input("Select 1/2/q : "))
            if selection_format == "1":
                selectionFile()
            elif selection_format == "2":
                selectionFile()
            elif selection_format == "q":
                print("\nExit mikfiles ...")
                os.system('exit')
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectionFormat()
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectionFormat()
        except KeyboardInterrupt:
            print("Exit mikfiles ...")
            os.system('exit')
    selectionFormat()

if __name__ == "__main__":
    main()
