
import socket

def get_socket_server_af_inet(socket_server_ip,socket_server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("create_socket_server_af_inet ip:", socket_server_ip, "port:", socket_server_port)
    s.bind((socket_server_ip, socket_server_port)) 
    s.listen(5)
    return s

def get_socket_client_af_inet(socket_server_ip,socket_server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket_client_af_ine start ip ip_socket_server",
          socket_server_ip, socket_server_port)
    s.connect((socket_server_ip, socket_server_port))  # connexion
    return s


def send_message(conn):
    print("Ecriver votre reponse:")
    reponse = input()
    conn.send(reponse.encode('utf-8'))

def display_client_message(client_name,message):
    print('Reponse de ',client_name,":",message.decode('utf-8'))
