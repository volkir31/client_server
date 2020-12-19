from socket import *
import sys
import time

host = 'localhost'
port = 7777
addr = (host, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('write to server: ')
    start_time = time.time()
    if not data:
        if input('do you want cancel session? y/n') == 'y':
            udp_socket.close()
            sys.exit(1)
            break
    data = str.encode(data)
    udp_socket.sendto(data, addr)
    data = bytes.decode(data)
    data = udp_socket.recvfrom(1024)
    ping_time = time.time() - start_time
    print(bytes.decode(data[0]), f'\ntime to response {ping_time}')
    if input('do you want cancel session? y/n') == 'y':
        udp_socket.close()
        break
