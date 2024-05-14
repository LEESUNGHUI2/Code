from socket import *
import sys

BUFF_SIZE = 1024
PORT = 5555

message_boxes = {}

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', PORT))

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = data.decode()
    print('Received:', msg)
    
    if msg.startswith('send '):
        parts = msg.split(' ', 2)
        mboxID, message = parts[1], parts[2]
        if mboxID not in message_boxes:
            message_boxes[mboxID] = []
        message_boxes[mboxID].append(message)
        s_sock.sendto('OK'.encode(), addr)
    
    elif msg.startswith('receive '):
        parts = msg.split(' ')
        mboxID = parts[1]
        if mboxID in message_boxes and message_boxes[mboxID]:
            message = message_boxes[mboxID].pop(0)
            s_sock.sendto(message.encode(), addr)
        else:
            s_sock.sendto('No messages'.encode(), addr)
    
    elif msg == 'quit':
        break

s_sock.close()
sys.exit()
