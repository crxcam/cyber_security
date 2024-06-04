
import socket
import time
import socket_tools


class socket_client:
    def __init__(self, client_name, ip):
        self._client_name = client_name
        self._ip = ip

    @property
    def client_name(self):
        return self._client_name

    @property
    def ip(self):
        return self._ip


socket_clients = []
socket_clients.append(socket_client("kali", "192.168.85.130"))

socket_server_ip = "192.168.85.130"
socket_server_port = 4444


def get_socket_server():
    socket = socket_tools.get_socket_server_af_inet(
        socket_server_ip, socket_server_port)
    monitoring_received_message(socket)


def monitoring_received_message(socket):
    print("monitoring_received_message from clients... ")
    while (True):
        conn, addr = socket.accept()
        client_ip = addr[0]
        message = conn.recv(1024)
        socket_tools.handle_message("server",message,socket)
        conn.close()

get_socket_server()
