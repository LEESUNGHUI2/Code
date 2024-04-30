import socket

HOST = 'localhost'
PORT = 3333

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print('Connected to server')

while True:
    expression = input('Enter: ')
    if expression.lower() == 'q':
        client_socket.send('q'.encode())
        break
    client_socket.send(expression.encode())
    result = client_socket.recv(1024).decode()
    print('Result:', result)

client_socket.close()
