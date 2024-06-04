import socket_tools

bufer_size_reserved = 1024
socket_server_ip = "192.168.85.130"
socket_server_port = 4444

def get_socket_client_af_inet():
    socket = socket_tools.get_socket_client_af_inet(
        socket_server_ip, socket_server_port,"login","password")
    monitoring_received_message(socket)


def monitoring_received_message(socket):
    print("monitoring_received_message from server... ")
    while (True):
        message = socket.recv(bufer_size_reserved).decode('utf-8')
        socket_tools.handle_message("client",message,socket)

get_socket_client_af_inet()