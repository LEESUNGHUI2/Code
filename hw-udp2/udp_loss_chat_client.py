from socket import *
import random
import time


port = 3333
BUFF_SIZE = 1024

s_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    data = 0
    while data <= 5:
        resp = str(data) + ' ' + msg
        s_sock.sendto(resp.encode(), ('localhost', port))
        #타임아웃 2초
        s_sock.settimeout(2)

        try:
            data, addr = s_sock.recvfrom(BUFF_SIZE)
        except timeout:
            data = data + 1
            continue
        else:
            break
    s_sock.settimeout(None)
    while True:
        data, addr = s_sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            s_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
