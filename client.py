import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host, port))

while(1):
    tm = s.recv(1024)
    message = tm.decode('ascii')
    if message is "":
        break
    print("server: %s" % message)
    st=input('>')
    s.send(bytes(st,'ascii'))
s.close()
