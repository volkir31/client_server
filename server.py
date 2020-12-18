from socket import *
import datetime
import time

host = 'localhost'
port = 7777
addr = (host, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)
while True:
    print('wait data...')
    conn, addr = udp_socket.recvfrom(1024)
    print('client addr: ', addr, 'message:', conn)
    data = datetime.datetime.now()
    time.sleep(1)
    if bytes.decode(conn).upper() == 'DATE':
        out_data = str(data.date())
    elif bytes.decode(conn).upper() == 'TIME':
        out_data = str(data.time())
    else:
        out_data = 'Invalid Request'
    udp_socket.sendto(str.encode(out_data), addr)
udp_socket.close()
