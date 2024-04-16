import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
# 본인의 이름을 문자열로 전송
sock.send(b'LEE SUNG HUI ')


# 본인의 학번을 수신 후 출력
msg2 = sock.recv(1024)
c = int.from_bytes(msg2, 'big')
print(c)
sock.close()
