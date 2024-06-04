import fcntl
import socket
import struct

def send_frame(ifname, dstmac, eth_type, payload):
    # Open raw socket and bind it to network interface.
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((ifname, 0))

    # Get source interface's MAC address.
    info = fcntl.ioctl(s.fileno(),
                       0x8927,
                       struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    srcmac = ':'.join('%02x' % b for b in info[18:24])

    # Build Ethernet frame
    payload_bytes = payload.encode('utf-8')
    assert len(payload_bytes) <= 1500  # Ethernet MTU

    frame = human_mac_to_bytes(dstmac) + \
            human_mac_to_bytes(srcmac) + \
            eth_type + \
            payload_bytes

    # Send Ethernet frame
    return s.send(frame)

def human_mac_to_bytes(addr):
    print("kokot ",addr)
    return bytes.fromhex(addr.replace(':', ''))

def run():
  print("start")
  ifname = "eth1"
  dstmac = "00:0c:29:07:4a:7c"
  payload = "salut kali"
  ethtype = b'\x7A\x05'  # arbitrary, non-reserved
  print("start")
  send_frame(ifname, dstmac, ethtype, payload)
  
run()
