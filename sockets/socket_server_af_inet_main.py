
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server_ip = "192.168.85.130"
import time
socket_server_port = 4444


def get_socket_server():
    socket_server = socket_tools.get_socket_server_af_inet(
        socket_server_ip, socket_server_port)
    monitoring_received_message(socket_server)


def monitoring_received_message(socket_server):
    print("monitoring_received_message from clients... ")
    while (True):
        conn, addr = socket_server.accept()
        client_ip = addr[0]
        message = conn.recv(1024)
        handle_message_from_client(client_ip,message,conn)
        conn.close()


def handle_message_from_client(client_ip,message,conn):
    for socket_client in socket_clients:
        if socket_client.get('ip') == client_ip:
            socket_tools.display_client_message(socket_client.get('client_name'),message,conn)
            socket_tools.send_message_client(conn)
            #print("new message from client:",socket_client.get('client_name'),"message:",message)


get_socket_server()
