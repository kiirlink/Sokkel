import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.100', 8888))
s.listen(1)

conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    
    if data == b'world':
        data = b'Exit' 
        conn.sendall(data)
        break

    data = b'Hello, ' + data 
    conn.sendall(data)

conn.close()
s.close()

