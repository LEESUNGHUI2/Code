from socket import *

BUFF_SIZE = 1024
PORT = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', PORT))

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    c_sock.send(msg.encode())
    
    if msg == 'quit':
        break
    
    data, addr = c_sock.recvfrom(BUFF_SIZE)
    print('<- ', data.decode())

c_sock.close()
