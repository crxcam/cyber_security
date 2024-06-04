
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufer_size_reserved = 1024

def create_socket_client_af_inet(socket_server_ip,socket_server_port):
    print("socket_client_af_ine start ip ip_socket_server",
          socket_server_ip, socket_server_port)
    s.connect((socket_server_ip, socket_server_port))  # connexion
    monitoring_received_message()


def monitoring_received_message():
    print("monitoring_received_message start ")
    while(True):
        message = s.recv(bufer_size_reserved)
        print("new message from server:",message)

def send_message_to_server(message_to_server):
    s.send(message_to_server.encode('utf-8'))

