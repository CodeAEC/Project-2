import time
import os
from colorama import Fore, Style


# here is where magic happens :)
def system():
    while 1 == 1:
        print(Fore.YELLOW + "Welcome to Error System!", Style.RESET_ALL)
        print("select the tool you wanna use!")
        print("1. Nmap")
        print("other coming soon!")

    # here is where the user chosees which tool does he/she want to use
        usr_cmd = input("select (1, 2, 3): ")

        while usr_cmd == "1": 
            typ1 = str("")
            typ2 = str("")
            print("")

        
            print(Fore.YELLOW +"type target IP address: ", Style.RESET_ALL)

        # typing targets ip
            ip_addr = input("IP addr: ")
            print("")

        # selecting the scanning method
            print("1. -sV")
            print("2. -sS")

            scan_type = input("Select type a scan you wanna do (1, 2, 3): ")

            if scan_type == "1":
               typ1 += "-sV "
            elif scan_type == "2":
               typ1 == "-sS "

            question = input("Do you want to add more scanning types? (Y/n): ")
 
            # if the answer is Y/y (yes), you are able to add another scanning type
            if question == "Y" or question == "y":
                print("1. -sV")
                print("2. -sS")
                scan_type1 = input("Select the second type scan (1, 2): ")
                
                if scan_type1 == "1":
                    typ2 += "-sV "
                elif scan_type1 == "2":
                    typ2 += "-sS "

            # if the answer is N/n (No), it will break out of while loop and continue with command execute
            elif question == "N" or question == "n":
                break

            # executing the command 
            os.system("nmap " + typ1 + typ2 + ip_addr)
            break


        while usr_cmd == "2":
          print("i hope it works")




# log in logic part
while 1 == 1:
    print(Fore.RED + '=======|log in|========', Style.RESET_ALL)
    usr = input("username: ")
    pwd = input("password: ")
    
    # if user eneters usr and pwd correclty, it will sleep for 3 sec and break out of the loop
    if usr == "doni" and pwd == "2645":
        #time.sleep(3)
        break
    else:
        # if user types usr and pwd wrong, he will continue the loop
        time.sleep(3)
        print("wrong user and pass")

# after breaking out of the loop, the system function will be called!

os.system("clear")
system()