#!/usr/bin/env python
 
import socket
import colorama
from colorama import Fore
text = """
███████╗███╗   ███╗███╗   ██╗███████╗████████╗    S
██╔════╝████╗ ████║████╗  ██║██╔════╝╚══██╔══╝    E
█████╗  ██╔████╔██║██╔██╗ ██║█████╗     ██║       R
██╔══╝  ██║╚██╔╝██║██║╚██╗██║██╔══╝     ██║       V
███████╗██║ ╚═╝ ██║██║ ╚████║███████╗   ██║       E
╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝       R
        2023-2024 All Rights Reserved © 
"""
txxt2 = """          
╔════════════════════════════════════════════════╗       
║   !WARNING! (SERVER IS VUNERABLE TO ATTACKS)   ║
║      Type Dev Menu/Setting to Access Them      ║
╚════════════════════════════════════════════════╝
              Type Continue If else
""" 
print(Fore.LIGHTCYAN_EX, text)
print(Fore.LIGHTRED_EX, txxt2)
opt = input(Fore.RED, "(main)<$")
if opt == 'Continue':
    print('[+]  Starting')
TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
('[+] Binded')
s.listen(1)
print('[+] Server Online Awaiting Connections')
conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    data2 = data.decode()
    if not data: break
    print (data2)
    conn.send(data)  # echo
conn.close()