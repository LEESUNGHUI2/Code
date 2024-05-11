from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

print("Listening on port 80...")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    if len(req) < 1:
        c.close()
        continue
    
    request_line = req[0]
    request_parts = request_line.split()

    if len(request_parts) < 3:
        c.close()
        continue
    
    filename = request_parts[1][1:]  
    filepath = './' + filename

    print(filename)
    if filename == "index.html":
        try:
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            print("성공")
        except FileNotFoundError:
            print("에러")
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    elif filename == "iot.png":
        try:
            f = open(filepath, 'rb')
            mimeType = 'image/png'
            
        except FileNotFoundError:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    elif filename == "favicon.ico":
        print(filename)
        try:
            f = open(filepath, 'rb')
            mimeType = 'image/x-icon'
        except FileNotFoundError:
            print("에러2)")
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    else:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.sendall(response.encode())
        c.close()
        continue

    response_headers = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
    c.sendall(response_headers.encode())

    if 'text' in mimeType:
        data = f.read()
        c.sendall(data.encode('utf-8'))
    else:
        data = f.read()
        c.sendall(data)

    c.close()