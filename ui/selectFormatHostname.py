import pyfiglet

def bannerMikfiles():
      ascii_banner = pyfiglet.figlet_format("mikfiles")
      print(ascii_banner)

def selectFormat():
      print("""
Welcome to the mikfiles. The script will generate export or log file of MikroTik
Select the format hostname :""")                  
      print("\n\033[34m" + "(1)" + "\033[0m" + " ---> MikroTik-1_2023-11-20_10-00-12")
      print("\n\033[34m" + "(2)" + "\033[0m" + " ---> 192.168.1.1_2023-11-20_10-00-12")
      print("\n\033[34m" + "(q)" + "\033[0m" + " Exit the program")
      print("\nMeaning the format name is = hostname or ip address_date_clock\n")