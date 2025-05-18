import socket

def client_Pifagor():
    a = input("Введите катет a: ")
    b = input("Введите катет b: ")
    message = f'{a},{b}'
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(), ("localhost", 9090))

    response, _ = client_socket.recvfrom(1024)

    print(response.decode())

if __name__ == '__main__':
    client_Pifagor()