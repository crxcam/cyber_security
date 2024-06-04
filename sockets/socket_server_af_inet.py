import sys
import fcntl
import socket
import struct


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufer_size_reserved = 1024

def create_socket_server_af_inet(ip, port):
    print("create_socket_server_af_inet ip:", ip, "port:", port)
    bufer_size_reserved = 1024
    s.bind((ip, port))  # bind server
    s.listen(5)
    monitoring_received_message()


def monitoring_received_message():
    print("monitoring_received_message start ")
    while (True):
        conn, addr = s.accept()
        client_ip = addr[0]
        client_port = addr[1]
        client_message_content = conn.recv(bufer_size_reserved)
        print("socket_server_af_inet : new client connexion uncomming ip:",
            client_ip, "port:", client_port)
        print("socket_server_af_inet : message client content  :",
            client_message_content)

def send_message_to_client(ip,port):
    conn, addr = s.accept()




