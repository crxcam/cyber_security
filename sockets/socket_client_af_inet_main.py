import socket_tools

bufer_size_reserved = 1024
socket_server_ip = "192.168.85.130"
socket_server_port = 4444

message_from_clients = ["bonjour de client", "je suis operationnel"]
message_to_client = ["bonjour de server", "tu est pret"]


def get_socket_client_af_inet():
    socket_client = socket_tools.get_socket_client_af_inet(
        socket_server_ip, socket_server_port)
    monitoring_received_message(socket_client)


def monitoring_received_message(socket_client):
    print("monitoring_received_message start ")
    while (True):
        message = socket_client.recv(bufer_size_reserved).decode('utf-8')
        if len(message) > 5:
            socket_tools.display_client_message(
        	    socket_client.get('client_name'), message, socket_client)
            socket_tools.send_message(socket_client)
            
