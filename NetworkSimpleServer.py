import socket

'''
bytes to string :  b"foo".decode("utf-8")
string to bytes : "foo".encode("utf-8")
'''

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host , port))


# wait for 5 ms after interrupt, socket to be closed
s.listen(5)

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    c.send(b"Thank you for connecting")
    c.close()
