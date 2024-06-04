import socket
import select

socks = []  # 소켓 리스트
BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)
socks.append(s_sock)  # 소켓 리스트에 서버 소켓을 추가

print('Server Started')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    r_sock, _, _ = select.select(socks, [], [])

    for s in r_sock:
        # 수신(읽기 가능한) 소켓 리스트 검사
        if s == s_sock:  # 새로운 클라이언트의 연결 요청 이벤트 발생
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            # 기존 클라이언트의 데이터 수신 이벤트 발생
            try:
                data = s.recv(BUFFER)
                if not data:
                    raise ConnectionResetError
                print('Received:', data.decode())
                # 모든 클라이언트에게 메시지 브로드캐스트
                for client in socks:
                    if client != s_sock and client != s:
                        try:
                            client.send(data)
                        except:
                            client.close()
                            socks.remove(client)
            except:
                print('Client disconnected')
                s.close()
                socks.remove(s)
