import socket
import colorama
import os
import sys
from colorama import Fore
from time import sleep
from sys import exit

os.system("cls & title paping made by mkay")

def tcpping(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip,port))
        print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] Connection to {ip} on {port} was established.")
    except:
        print(f"[{Fore.RED}ERROR{Fore.RESET}] Connection to host lost.")

ip = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] IP: ")
port = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] PORT: ")
while True:
    try:
        tcpping(ip,int(port))
        sleep(0.4)
    except KeyboardInterrupt:
        exit(0)

# tool developed by mkay