
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufer_size_reserved = 1024
conn = None
addr = None

def create_socket_server_af_inet(socket_server_ip,socket_server_port):
    print("create_socket_server_af_inet ip:", socket_server_ip, "port:", socket_server_port)
    s.bind((socket_server_ip, socket_server_port))  # bind server
    s.listen(5)
    monitoring_received_message()


def monitoring_received_message():
    print("monitoring_received_message start ")
    while (True):
        conn, addr = s.accept()
        client_ip = addr[0]
        client_port = addr[1]
        message = conn.recv(bufer_size_reserved)
        print("new message from client:",message)
        
def send_message_to_client(msg_to_client):
    conn.send(msg_to_client.encode('utf-8'))

