import socket
import struct
import threading

def main():
    ip = "localhost"
    port = 49999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(1)
    print(f'[*] Listening on {ip}:{port}')

    client, address = server.accept()
    print(f' [*] Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle, args =(client,))
    client_handler.start()

def handle(client):
    while True:
        try:
            rcv = client.recv(8)
            msg = struct.unpack('d',rcv)
            print(msg)
        except:
            print(" [*] Closing connection.")
            client.close()
            break   

if __name__=='__main__':
    main()
