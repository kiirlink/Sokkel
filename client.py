import socket

HOST = "192.168.1.100"
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

try:
    while True:
        message = input("Enter message: ")

        s.sendall(message.encode())

        data = s.recv(1024)
        print("Server:", data.decode())

        if data == b"Exit":
            break
finally:
    s.close()