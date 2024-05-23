import socket
import threading
import time

port = 2500
BUFSIZE = 1024
clients = [] 

class ClientThread(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr

    def run(self):
        while True:
            try:
                data = self.sock.recv(BUFSIZE)
                if not data:
                    break
                message = data.decode()
                print(time.asctime() + " " + str(self.addr) + ': ' + message)

                if 'quit' in message:
                    self.remove_client()
                    print(self.addr, 'exited')
                    break

                self.broadcast(message)

            except ConnectionResetError:
                break

        self.remove_client()
        self.sock.close()

    def broadcast(self, message):
        for client in clients:
            if client != self.sock:
                try:
                    client.sendall(message.encode())
                except:
                    pass

    def remove_client(self):
        if self.sock in clients:
            clients.remove(self.sock)

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', port))
    server_sock.listen(5)
    print('Server Started on port', port)

    while True:
        conn, addr = server_sock.accept()
        clients.append(conn)
        print('New client', addr)
        client_thread = ClientThread(conn, addr)
        client_thread.start()

if __name__ == '__main__':
    main()
