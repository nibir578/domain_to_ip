import socket
import pyfiglet #banar packeg
from termcolor import *
print(colored("**************Domain_To_Ip_Converter*****************",'green'))
banar = colored(pyfiglet.figlet_format("Domain_To_Ip"),'green')
print(banar)
print(colored("                                     Created_by_King37         ",'red'))
domain=input("Please,Enter Your Domain: ")
ip=socket.gethostbyname(domain)
print("Ip For {} : {}".format(domain,ip))
