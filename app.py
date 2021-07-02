import socket
from flask import Flask

app = Flask(__name__)

s = socket.socket()
s.bind(("192.168.100.35", 1234))
s.listen(5)

def obtenerMensajes():
    clientSocket, address = s.accept()
    print("connection from {address} has been established")
    msg = clientSocket.recv(1024)
    decodedmsg = msg.decode("utf-8")
    print(decodedmsg)
    clientSocket.send(bytes("Hola desde el server!", "utf-8"))
    return decodedmsg


@app.route("/")
def home():
    mensaje = obtenerMensajes()
    return("<h1>hello world!</h1> " + mensaje)

if __name__ == "__main__":
    app.run


    
