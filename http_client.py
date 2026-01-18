import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('example.com', 80))

http_запрос = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

client_socket.send(http_запрос.encode())

полный_ответ = b''

while True:
    порция = client_socket.recv(1024)
    if not порция:
        break
    полный_ответ += порция

client_socket.close()
print(полный_ответ.decode())