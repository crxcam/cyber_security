import os
import platform
from datetime import datetime
net = input("Enter the Network Address : ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(input("Enter the Starting Number : "))
en1 = int(input("Enter the Last Number : "))
en1 = en1+1
oper = platform.system()

if (oper == "Windows"):
    ping1 = "ping -n 1 "
elif (oper == "Linux"):
    ping1 = "ping -c 3 "
else:
    ping1 = "ping -c 1 "
t1 = datetime.now()
print("Scanning in Progress ... ")
for ip in range(st1, en1):
    # print ip, "IP\n"
    addr = net2+str(ip)
    comm = ping1+addr
    response = os.popen(comm)

    for line in response.readlines():
        # print line, "Line\n"
        if (line.count("ttl")):
            # print oper, " OS\n"
            break
    if (line.count("ttl")) > 0:
        print(addr, "--> Active host ")

t2 = datetime.now()
total = t2-t1
print("scanning complete in ", total)
