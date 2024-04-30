import socket
import re
import operator

def calculate_expression(expression):
    try:
        pattern = r'(\d+)\s*([+\-*/])\s*(\d+)'
        match = re.match(pattern, expression)
        if match:
            operand1 = int(match.group(1))
            operator_symbol = match.group(2)
            operand2 = int(match.group(3))
            if operator_symbol == '+':
                return operand1 + operand2
            elif operator_symbol == '-':
                return operand1 - operand2
            elif operator_symbol == '*':
                return operand1 * operand2
            elif operator_symbol == '/':
                return round(operand1 / operand2, 1)
        else:
            return 'Invalid expression'
    except Exception as e:
        return str(e)

HOST = 'localhost'
PORT = 3333

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print('Server is listening...')

while True:
    client_socket, client_addr = server_socket.accept()
    print('Connection from', client_addr)
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        if data.lower() == 'q':
            break
        result = calculate_expression(data)
        client_socket.send(str(result).encode())
    client_socket.close()
