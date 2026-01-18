iimport socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('example.com', 80))

http_запрос = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

client_socket.send(http_запрос.encode())

otvet = b''

while True:
    q = client_socket.recv(1024)
    if not q:
        break
    otvet += q

client_socket.close()
print(otvet.decode())
