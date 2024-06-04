import sys
import fcntl
import socket
import struct


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufer_size_reserved = 1024

def create_socket_client_af_inet(ip_socket_server,port):
    buffer_size = 1024
    print("socket_client_af_ine start...")
    s.connect((ip_socket_server, port))  # connexion
    print("socket_client_af_ine send data to server")
    s.send(b"{user:'toto'}")  # send data to server
    data_from_server = s.recv(buffer_size)
    buffer_size = bytearray(data_from_server)
    print("socket_client_af_ine: message from server content:", data_from_server)
    print("socket_client_af_ine: message from server size :", len(buffer_size))
    #s.close()

create_socket_client_af_inet("debian",4444)



