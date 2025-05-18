import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print("\n" + message)
        except:
            print("Отключение от сервера.")
            sock.close()
            break

def send_messages(sock, nickname):
    while True:
        message = input()
        full_message = f"{nickname}: {message}"
        sock.send(full_message.encode())

def start_client():
    host = "localhost"
    port = 9090
    nickname = input("Введите ваше имя: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    thread_recv = threading.Thread(target=receive_messages, args=(client_socket,))
    thread_recv.start()

    thread_send = threading.Thread(target=send_messages, args=(client_socket, nickname))
    thread_send.start()

if __name__ == "__main__":
    start_client()
