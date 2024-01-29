import os
import readline
import sys


def BackOpt():
    print("[i] Select what you want :")
    print("\033[34m" + "(1)" + "\033[0m" + " Export/Generate Again")
    print("\033[34m" + "(2)" + "\033[0m" + " Back to Select Export File Menu")
    print("\033[34m" + "(3)" + "\033[0m" + " Back to Main Menu")
    print("\033[34m" + "(4)" + "\033[0m" + " Exit")

def selectionFile():
    os.system('clear')
    from ui import inputPrep
    if selection_format == "1":
        inputPrep.hostnameDefSelection()
    elif selection_format == "2":
        inputPrep.ipAddrDefSelection()
    else:
        print("unknown select")
    from ui import selectFileExport
    selectFileExport.selectFile()
    def selectFilesNum():
        try:
            selection_file = str(input("""[->] Select 1/2/3/4/b/q : """))
            if selection_file == "1": # export log file
                from modules import hostnameLog
                from modules import ipAddressLog
                if selection_format == "1": # [DONE] Execute hostname modules if selection format 1
                    from ui import inputPrep
                    inputPrep.hostnameDefSelection()
                    inputPrep.ExportFileDef.hostnameLogDef()
                    inputPrep.inputPrep()
                    hostnameLog.main()
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.hostnameDefSelection()
                                inputPrep.ExportFileDef.hostnameLogDef()
                                inputPrep.inputPrep()
                                hostnameLog.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "1": # back hostname format
                                    from ui import inputPrep
                                    inputPrep.hostnameDefSelection()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                elif selection_format == "2": # [DONE] Execute ip address modules if selection format 2
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrLogDef()
                    inputPrep.inputPrep()
                    ipAddressLog.main()
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.ipAddrDefSelection()
                                inputPrep.ExportFileDef.ipAddrLogDef()
                                inputPrep.inputPrep()
                                ipAddressLog.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "2": # back ip address format
                                    from ui import inputPrep
                                    inputPrep.ExportFileDef.ipAddrLogDef()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                else:
                    print("Unknown error")
                    sys.exit(0)
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
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.hostnameDefSelection()
                                inputPrep.ExportFileDef.hostnameFileConfDef()
                                inputPrep.inputPrep()
                                hostnameFileConf.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "1": # back hostname format
                                    from ui import inputPrep
                                    inputPrep.ExportFileDef.hostnameFileConfDef()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrFileConfDef()
                    inputPrep.inputPrep()
                    ipAddressFileConf.main()
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.ipAddrDefSelection()
                                inputPrep.ExportFileDef.ipAddrFileConfDef()
                                inputPrep.inputPrep()
                                ipAddressFileConf.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "2": # back ip address format
                                    from ui import inputPrep
                                    inputPrep.ExportFileDef.ipAddrFileConfDef()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                else:
                    print(f"\033[31m" + "[!]" + "\033[0m" + "Error")
                    sys.exit(0)
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
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.hostnameDefSelection()
                                inputPrep.ExportFileDef.hostnameExportBoth()
                                inputPrep.inputPrep()
                                hostnameExBoth.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "1": # back hostname format
                                    from ui import inputPrep
                                    inputPrep.ExportFileDef.hostnameExportBoth()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                elif selection_format == "2": # [DONE] Execute IP Address modules if selection format 1
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    inputPrep.ExportFileDef.ipAddrExportBoth()
                    inputPrep.inputPrep()
                    ipAddressExBoth.main()
                    # Back options
                    BackOpt()
                    def select_back():
                        try:
                            select = input("[->] : ")
                            if select == "1": # export again
                                from ui import inputPrep
                                inputPrep.hostnameDefSelection()
                                inputPrep.ExportFileDef.ipAddrExportBoth()
                                inputPrep.inputPrep()
                                ipAddressExBoth.main()
                                BackOpt(); select_back()
                            elif select == "2": # back to select file export
                                if selection_format == "2": # back ip address format
                                    from ui import inputPrep
                                    inputPrep.ExportFileDef.ipAddrExportBoth()
                                    selectionFile()
                            elif select == "3": # back to main menu
                                main()
                            elif select == "4": # exit
                                print("\n[i] Exit mikfiles ...")
                                sys.exit(0)
                            else:
                                print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                                select_back()
                        except ValueError:
                            print("\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
                            select_back()
                        except KeyboardInterrupt:
                            print("\n\n[i] Exit mikfiles ...")
                    select_back()
                else:
                    print(f"\033[31m" + "[!]" + "\033[0m" + "Error")
                    sys.exit(0)
            elif selection_file == "4":
                from modules import cronjob
                os.system('clear')
                cronjob.main()
                # Back options
                if selection_format == "1":
                    from ui import inputPrep
                    inputPrep.hostnameDefSelection()
                    selectionFile()
                elif selection_format == "2":
                    from ui import inputPrep
                    inputPrep.ipAddrDefSelection()
                    selectionFile()
                else:
                    print('error')
            elif selection_file == "b":
                print("[i] Back to the previous")
                main()
            elif selection_file == "q":
                print("\n[i] Exit mikfiles ...")
                sys.exit(0)
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectFilesNum()    
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectFilesNum()
        except KeyboardInterrupt:
            print("\n\n[i] Exit mikfiles ...")
            sys.exit(0)
    selectFilesNum()

def main():
    # select format name
    os.system('clear')
    from ui import selectFormatHostname
    selectFormatHostname.bannerMikfiles()
    selectFormatHostname.selectFormat()
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
                sys.exit(0)
            else:
                print("\n\033[31m"+"[!] Error. Select menu correctly !" + "\033[0m")
                selectionFormat()
        except ValueError:
            print("\n\033[31m"+"[!] Invalid value input. Repeat again !" + "\033[0m")
            selectionFormat()
        except KeyboardInterrupt:
            print("\n\n[i] Exit mikfiles ...")
            sys.exit(0)
    selectionFormat()

if __name__ == "__main__":
    main()
