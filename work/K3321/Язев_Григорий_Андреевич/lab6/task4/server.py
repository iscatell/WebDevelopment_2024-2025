import socket
import threading

clients = []

def handle_client(client_socket, address):
    print(f"[+] Подключен: {address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break
    print(f"[-] Отключен: {address}")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                pass

def start_server():
    host = "localhost"
    port = 9090
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
