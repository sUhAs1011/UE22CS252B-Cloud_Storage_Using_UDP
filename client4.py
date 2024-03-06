import socket
import tqdm
import os
from tkinter import *
from tkinter import filedialog
import time

path = os.getcwd()

def socket_connect():
    global s
    ip = "localhost"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return (s, (ip, port))

s, server_address = socket_connect()

SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

print("You are successfully connected with the server Use command upload to upload files in cloud. Use command ls to list files in server. Use command download <filename.ext> to download files")
print("Eg: download test.png. Use cmd commands by cmd <command>. Eg: cmd mkdir Documents")
print("For more info watch the video on Programming Py")

while True:
    task1 = input(str("Server: ") + ">> ")
    task = task1.split()
    
    if task1 == 'upload':
        try:
            data = filedialog.askopenfile(initialdir="/")
            filename = str(data.name)
            size = os.path.getsize(filename)
            s.sendto(bytes("upload", "utf-8"), server_address)
            s.sendto(f"{filename}{SPACE}{size}".encode(), server_address)
            
            with open(filename, "rb") as file:
                terminated = False
                while not terminated:
                    data = file.read(4096)
                    if not data:
                        s.sendto(b'', server_address)  # Send an empty packet to signify end of file
                        terminated = True
                    else:
                        s.sendto(data, server_address)
                        time.sleep(0.01)  # Add slight delay for UDP packets
        except Exception as e:
            print("Error:", e)

    if task1 == 'ls':
        try:
            s.sendto(bytes("ls", "utf-8"), server_address)
            data, _ = s.recvfrom(4096)
            print(str(data.decode('utf-8')))
        except Exception as e:
            print("Error:", e)

    if len(task) > 1:
        if task[0] == "cmd":
            try:
                s.sendto(bytes("cmd", "utf-8"), server_address)
                task = task1.split('cmd')
                task[1] = task[1].lstrip(' ')
                s.sendto(bytes(str(task[1]), "utf-8"), server_address)
            except Exception as e:
                print("Error:", e)

        if task[0] == "download":
            try:
                s.sendto(bytes("download", "utf-8"), server_address)
                task[1] = task[1].lstrip(' ')
                s.sendto(bytes(str(task[1]), "utf-8"), server_address)
                
                data, _ = s.recvfrom(4096)
                filename, size = data.decode().split(SPACE)
                filename = os.path.basename(filename)
                
                with open(filename, 'wb') as file:
                    terminated = False
                    while not terminated:
                        data, _ = s.recvfrom(4096)
                        if not data:
                            terminated = True
                            break
                        file.write(data)
            except Exception as e:
                print("Error:", e)
