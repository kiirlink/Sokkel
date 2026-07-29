import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.100', 8888))

data = input('Enter your name: ')
data = data.encode('utf-8')

s.sendall(data)

data = s.recv(1024)
s.close()

print('Received data:', data.decode('utf-8'))