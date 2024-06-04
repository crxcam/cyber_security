
import socket
import time
import socket_server_af_inet


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server_ip= "192.168.85.130"
socket_server_port =4444

message_from_clients=["bonjour de client","je suis operationnel"]
message_to_client=["bonjour de server","tu est pret"]


def run_socket_server():
    socket_server_af_inet.create_socket_server_af_inet(socket_server_ip,socket_server_port)


def send_message_to_client():
    time.sleep(3)
    socket_server_af_inet.send_message_to_client("bonjour de server")
    time.sleep(3)
    socket_server_af_inet.send_message_to_client("tu est pret")


run_socket_server()