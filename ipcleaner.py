import subprocess
from colorama import *
import time
init()


class AppCleaner:
    def __init__(self) -> None:
        pass
    
    #Loading process
    def loading(self, num):
        for arch in [
            Fore.YELLOW + "* 0 %", 
            Fore.YELLOW + "** 25 %", 
            Fore.YELLOW + "*** 50 %", 
            Fore.GREEN + "**** 75 %", 
            Fore.GREEN + "***** 99 %", 
            Fore.GREEN + "****** 100 %"]:
            time.sleep(1)
            print(Cursor.UP(1)+Cursor.FORWARD(num)+Fore.RED+str(arch))

    #Release and Renew IP
    def release_renew_Ip(self):
        print(Fore.YELLOW + "Release IP")
        self.loading(11)
        print(Fore.GREEN)
        subprocess.run(["ipconfig", "/release"],shell=True)
        time.sleep(3)
        subprocess.run(["cls"], shell=True)
        print(Fore.YELLOW + "Renew IP")
        self.loading(10)
        print(Style.RESET_ALL)
        time.sleep(3)
        print(Fore.GREEN)
        subprocess.run(["ipconfig", "/renew"],shell=True)
        time.sleep(3)
        subprocess.run("cls", shell=True)
        print(Fore.BLUE + "Done.")
        time.sleep(2)

    #Showing DNS and Flushing them
    def cleanDns(self):
        print( Fore.YELLOW + "DNS Loading")
        self.loading(12)
        print(Fore.GREEN)
        subprocess.run(["ipconfig", "/displaydns"],shell=True)
        time.sleep(3)
        subprocess.run(["cls"], shell=True)
        print(Fore.YELLOW + "Flushing Loading")
        self.loading(17)
        print(Fore.GREEN)
        subprocess.run(["ipconfig", "/flushdns"],shell=True)
        time.sleep(3)
        subprocess.run("cls", shell=True)
        print(Fore.BLUE + "Done.")
        time.sleep(2)


if __name__ == "__main__":
    app = AppCleaner()
    while True:
        subprocess.run(["cls"], shell=True)
        print(Fore.YELLOW + "Ip cleaner")
        value = input(Fore.BLUE + "\nChoose an Option:\n\n[1] Clean IP\n[2] Clean DNS\n[3] Close app\n\n_> " + Style.RESET_ALL)

        if value == "1":
            subprocess.run(["cls"], shell=True)
            app.release_renew_Ip()
        elif value == "2":
            subprocess.run(["cls"], shell=True)
            app.cleanDns()
        elif value == "3":
            subprocess.run(["cls"], shell=True)
            print(Fore.BLUE+Back.BLUE + "Good bye..!!")
            time.sleep(2)
            break
        else:
            time.sleep(1)
            subprocess.run(["cls"], shell=True)
            print(Fore.RED+Back.BLACK + "Try again..!!")
            time.sleep(4)





