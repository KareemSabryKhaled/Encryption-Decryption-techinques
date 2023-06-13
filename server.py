import socket
import threading
from elgamal import*
from AES import *
from RSA2 import*
from des import*
from AES import*

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print(host)
port = 9999

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# set the server to listen for incoming connections
server_socket.listen(2)
print("Server is listening for incoming connections...")
# function to handle a client connection

def handle_client(client_socket, addr):
    global_var = 0
    while True:
        # receive messages from client
        data = client_socket.recv(1024).decode()
        if not data:
            break

        global_var = global_var +1
        if global_var % 2 == 0:
            print('Data for me:' , data)
            print('data: ' , data[-1])
            if data[-1] == '1':
                print('algamal')
                cipher= encryption_elgamal(data[0: (len(data)-1)])
            elif data[-1] == '2':
                print('RSA',data[0: (len(data)-1)],data[-1])
                cipher= cipherRSA(data[0: (len(data)-1)])
                print(cipher)
                   # RSA2(data[0: (len(data)-1)])
            elif data[-1] == '3':
                cipher=encrypt(data[0:(len(data)-1)])
                print('DES')
            elif data[-1] == '4':
                cipher = AESCallEncrypt(data[0:(len(data)-1)])

                print('AES')
        else:
            print('Data for me:', data)
            print('data: ', data[-1])
            if data[-1] == '1':
                print('algamal')
                cipher = decryption_elgamal(data[0: (len(data) - 1)])
            elif data[-1] == '2':
                print('RSA', data[0: (len(data) - 1)], data[-1])
                cipher = decipherRSA(data[0: (len(data) - 1)])
                print(cipher)
                # RSA2(data[0: (len(data)-1)])
            elif data[-1] == '3':
                cipher = decrypt(data[0:(len(data) - 1)])
                print('DES')
            elif data[-1] == '4':
                cipher = AESCallDecrypt(data[0:(len(data) - 1)])

                print('AES')
        # send messages to the other client
        other_client_socket = [c for c in clients if c != client_socket][0]
        print('Cipher: ', cipher)
        cipher = cipher + data[-1]
        other_client_socket.send(cipher.encode())
        break

    # close the connection
    print(f"Client {addr} has disconnected")
    client_socket.close()
    clients.remove(client_socket)

# keep track of connected clients
clients = []

# wait for incoming connections
while True:
    # accept incoming connection
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f"New client connected: {addr}")

    # handle client connection in a new thread
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()

