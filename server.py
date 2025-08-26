import socket
import os
import tqdm
import subprocess

path = os.getcwd()
SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 9999))

def handle_upload(c, client_address):
    try:
        data, _ = c.recvfrom(4096)
        filename, size = data.decode().split(SPACE)
        filename = os.path.basename(filename)
        file = open(str(filename), 'wb')
        terminated = False
        upload_bar = tqdm.tqdm(range(int(size)), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        while not terminated:
            data, _ = c.recvfrom(4096)
            if not data:
                terminated = True
                break
            file.write(data)
            upload_bar.update(len(data))
        file.close()
    except Exception as e:
        print("Error:", e)

def handle_ls(c, client_address):
    try:
        data = os.listdir(path)
        data = ' '.join(data)
        c.sendto(bytes(data, "utf-8"), client_address)
    except Exception as e:
        print("Error:", e)

def handle_cmd(c, client_address):
    try:
        data, _ = c.recvfrom(4096)
        command = data.decode("utf-8")
        subprocess.run(command, shell=True)
    except Exception as e:
        print("Error:", e)

def handle_download(c, client_address):
    try:
        data, _ = c.recvfrom(4096)
        filename = data.decode("utf-8").strip()
        size = os.path.getsize(filename)
        c.sendto(f"{filename}{SPACE}{size}".encode(), client_address)
        upload_bar = tqdm.tqdm(range(int(size)), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        filename = filename.replace(" ", "")
        with open(filename, "rb") as file:
            terminated = False
            while not terminated:
                data = file.read(4096)
                if not data:
                    terminated = True
                    break
                c.sendto(data, client_address)
                upload_bar.update(len(data))
    except Exception as e:
        print("Error:", e)

print("Server waiting....")
while True:
    try:
        data, client_address = s.recvfrom(1024)
        msg = data.decode("utf-8")
        if msg == "upload":
            handle_upload(s, client_address)
        elif msg == "ls":
            handle_ls(s, client_address)
        elif msg == "cmd":
            handle_cmd(s, client_address)
        elif msg == "download":
            handle_download(s, client_address)
    except Exception as e:
        print("Error:", e)
