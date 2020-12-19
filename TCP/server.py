import socket

sock = socket.socket()
sock.bind(("", 14900))
while True:
    sock.listen(3)
    conn, addr = sock.accept()
    data = conn.recv(16384)
    user_data = bytes.decode(data)
    print("Data: " + user_data)
    conn.send(b"Hello!\n" + b"Your data: " + str.encode(user_data))