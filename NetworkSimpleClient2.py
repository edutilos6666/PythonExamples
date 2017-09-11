import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host , port))

s.send("First Message from {0} and {1}".format(host, port).encode("utf-8"))
print(s.recv(1024).decode("utf-8"))
s.close()