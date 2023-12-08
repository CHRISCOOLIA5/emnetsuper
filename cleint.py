#!/usr/bin/env python
 
import socket
text = """
███████╗███╗   ███╗███╗   ██╗███████╗████████╗    
██╔════╝████╗ ████║████╗  ██║██╔════╝╚══██╔══╝    
█████╗  ██╔████╔██║██╔██╗ ██║█████╗     ██║       
██╔══╝  ██║╚██╔╝██║██║╚██╗██║██╔══╝     ██║       
███████╗██║ ╚═╝ ██║██║ ╚████║███████╗   ██║       
╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝       
                                                  
""" 
print(text)
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