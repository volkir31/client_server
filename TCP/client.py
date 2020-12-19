import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 14900))
while True:
    data = input('Write message: ')
    conn.send(str.encode(data))
    tmp = conn.recv(1024)
    print(bytes.decode(tmp))
    if input('do u want close session? y/n \t') == 'y':
        conn.close()
        break
