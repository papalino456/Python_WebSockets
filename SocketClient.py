import socket
import numpy as np
import subprocess
while True:
    n = np.random.randint(low=1, high=10000)
    t = subprocess.getoutput("vcgencmd measure_temp")
    s = socket.socket()
    s.connect(("192.168.100.35", 1234))
    s.send(bytes("n={}".format(n), "utf-8"))
    res = s.recv(1024)
    print(res.decode("utf-8"))
    s.close()
