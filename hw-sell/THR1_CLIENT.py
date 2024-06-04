import socket
import threading

def handler(sock):
    while True:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())


# 서버 주소 및 포트 설정
svr_addr = ('localhost', 2500)

# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

# 사용자 ID 입력 및 서버로 전송
my_id = input('ID를 입력하세요: ')
sock.sendall(('[' + my_id + ']').encode())

# 메시지 수신 스레드 시작
th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()


while True:
    msg = '[' + my_id + '] ' + input()
    sock.sendall(msg.encode())
    # if msg == '[quit]':
    #     break

sock.close()
