import socket

s = socket.socket()
s.bind(("192.168.100.35", 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print("connection from {address} has been established")
    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))
    clientSocket.send(bytes("Hola desde el server!", "utf-8"))
    clientSocket.close()
    