import os
import readline

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
            selection_file = str(input("""[->] Select 1/2/3/4/b/q 
: """))
            if selection_file == "1": # export log file
                from modules import hostnameLog
                from modules import ipAddressLog
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    from ui import inputPrep
                    inputPrep.hostnameDefSelection()
                    inputPrep.ExportFileDef.hostnameLogDef()
                    inputPrep.inputPrep()
                    hostnameLog.main()
                elif selection_format == "2": # [DONE] Execute ip address modules if selection format 2
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrLogDef()
                    inputPrep.inputPrep()
                    ipAddressLog.main()
                else:
                    print("error")
                    os.system('exit')
            elif selection_file == "2": # export file config and backup
                print("Export file configuration and backup file")
                from modules import hostnameFileConf
                from modules import ipAddressFileConf
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    from ui import inputPrep
                    inputPrep.hostnameDefSelection()
                    inputPrep.ExportFileDef.hostnameFileConfDef()
                    inputPrep.inputPrep()
                    hostnameFileConf.main()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrFileConfDef()
                    inputPrep.inputPrep()
                    ipAddressFileConf.main()
                else:
                    print(f"\033[31m" + "[!]" + "\033[0m" + "Error")
                    os.system('exit')
            elif selection_file == "3": # Export both
                print("Export both")
                from modules import hostnameExBoth
                from modules import ipAddressExBoth
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    from ui import inputPrep
                    inputPrep.hostnameDefSelection()
                    inputPrep.ExportFileDef.hostnameExportBoth()
                    inputPrep.inputPrep()
                    hostnameExBoth.main()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrExportBoth()
                    inputPrep.inputPrep()
                    ipAddressExBoth.main()
                else:
                    print(f"\033[31m" + "[!]" + "\033[0m" + "Error")
                    os.system('exit')
            elif selection_file == "4": # cron with hostname
                from modules import cronjob
                os.system('clear')
                cronjob.main()
            elif selection_file == "b":
                print("Back to the previous")
                main()
            elif selection_file == "q":
                print("\n[i] Exit mikfiles")
                os.system('exit')
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectFilesNum()    
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectFilesNum()
        except KeyboardInterrupt:
            print("\n\n[i] Exit mikfiles ...")
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
            selection_format = str(input("[->] Select 1/2/q : "))
            if selection_format == "1":
                selectionFile()
            elif selection_format == "2":
                selectionFile()
            elif selection_format == "q":
                print("\n[i] Exit mikfiles ...")
                os.system('exit')
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectionFormat()
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectionFormat()
        except KeyboardInterrupt:
            print("\n\n[i] Exit mikfiles ...")
            os.system('exit')
    selectionFormat()

if __name__ == "__main__":
    main()
