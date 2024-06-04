import sys
import fcntl
import socket
import struct


def transform_human_mac_to_bytes(addr):
    return bytes.fromhex(addr.replace(':', ''))


def get_local_mac_address(s, ifname):
    info = fcntl.ioctl(s.fileno(),
                       0x8927,
                       struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])


def build_socket_af_packet(ifname):
    # Open raw socket and bind it to network interface.
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((ifname, 0))


def build_frame_socket_af_packet(payload, eth_type, dstmac, srcmac):
    # Build Ethernet frame
    payload_bytes = payload.encode('utf-8')
    assert len(payload_bytes) <= 1500  # Ethernet MTU
    frame = transform_human_mac_to_bytes(dstmac) + \
        transform_human_mac_to_bytes(srcmac) + \
        eth_type + \
        payload_bytes
    return frame


def create_socket_client_af_inet(ip_socket_server,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


def create_socket_server_af_packet(ifname):
    print("create_socket_server_af_packet ip:", ip, "port:", port)
    bufer_size_reserved = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ifname, 0))
    s.listen(2)

    while (True):
        conn, addr = s.accept()
        client_ip = addr[0]
        client_port = addr[1]
        client_message_content = conn.recv(bufer_size_reserved)
        client_message_size = bytearray(client_message_content)
        print("server_af_packet : new client connexion uncomming ip:",
              client_ip, "port:", client_port)
        print("server_af_packet : message client content  :",
              client_message_content)
        # print("Socket server : message client size :", len(client_message_size))
        print("server_af_packet : send data to client")
        conn.send(b"server_af_packet Thank you for connecting")
        # print("Socket server : connexion closed")
        # conn.close()


def create_socket_server_af_inet(ip, port):
    print("create_socket_server_af_inet ip:", ip, "port:", port)
    bufer_size_reserved = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))  # bind server
    s.listen(2)

    while (True):
        conn, addr = s.accept()
        client_ip = addr[0]
        client_port = addr[1]
        client_message_content = conn.recv(bufer_size_reserved)
        client_message_size = bytearray(client_message_content)
        print("socket_server_af_inet : new client connexion uncomming ip:",
              client_ip, "port:", client_port)
        print("socket_server_af_inet : message client content  :",
              client_message_content)
        # print("Socket server : message client size :", len(client_message_size))
        print("socket_server_af_inet : send data to client")
        conn.send(b"Thank you for connecting")
        # print("Socket server : connexion closed")
        # conn.close()


def run():
    print("start")
    ifname = "eth1"
    payload = "salut kali"
    eth_type = b'\x7A\x05'  # arbitrary, non-reserved
    print("build_socket_af_packet")
    s = build_socket_af_packet(ifname)
    mac_destination = "00:0c:29:07:4a:7c"
    print("get_local_mac_address")
    mac_source = get_local_mac_address(s, ifname)
    print("build_frame_socket_af_packet")
    frame = build_frame_socket_af_packet(
        payload, eth_type, mac_destination, mac_source)
    print("build_frame_socket_af_packet")
    s.send(frame)


run()
