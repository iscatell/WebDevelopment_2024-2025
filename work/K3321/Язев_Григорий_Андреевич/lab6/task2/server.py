import socket

def server_Pifagor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 9090))

    while True:
        message,client_address = server_socket.recvfrom(1024)
        a,b = message.decode().strip().split(',')
        a = float(a)
        b = float(b)
        c = (a**2 + b**2)** 0.5
        response = f"Гипотенуза = {c}"
        server_socket.sendto(response.encode(),client_address)
        
if __name__ == '__main__':
    server_Pifagor()