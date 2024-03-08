import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost", 5558))

server.listen()
all_client = {}

def client_thread(client):
    message = client.recv(1024)
    for c in all_client:
        c.send(message)

while True:
    print("Connection is Successfully!")
    client , address = server.accept()
    print("Connection Esatablished!")
    name = client.recv().decode()
    all_client[client] = name
    thread = Thread(target=client_thread,args=(client,))
    thread.start()
