import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)


print("listening on port {0} and host {1}".format(port , host))

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    print("data = {0}".format(c.recv(1024).decode("utf-8")))
    c.send(b"Thanks for connecting, bye!")
    c.close()

