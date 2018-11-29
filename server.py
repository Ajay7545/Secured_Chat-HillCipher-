import socket


def TCPserver():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = socket.gethostname()
    port = 9999

    serversocket.bind((host, port))
    serversocket.listen(5)

    while True:
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        clientsocket.send(b'Hello World')

        while (1):
            message = clientsocket.recv(1024)
            print("Client: %s" % message.decode('ascii'))
            st = input('>')
            clientsocket.send(bytes(st, 'ascii'))
        clientsocket.close()


TCPserver()
