import sys
import socket
from thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print('ERROR NEED IP AND PORT')
    exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])

s.bind((ip, port))

num_conex = 100

s.listen(num_conex)

clients = []


def client_thread(conn, addr):
    conn.send('Welcome to Xat')

    while True:
        try:
            msg = conn.recv(2048)
            if msg:
                msg_send = 'IP: ' + addr[0] + ' : ' + msg
                print(msg_send)
                broadcast(msg_send, conn)


def broadcast(msg, conn):
    for client in clients:
        if clients != conn:
            try:
                client.send(msg)
            except:
                client.close()
                remove(client)

def remove(conn):
    if conn in clients:
        clients.remove(conn)


while True:
    conn, addr = s.accept()

    clients.append(conn)

    print(addr[0] + " connected succesful")

