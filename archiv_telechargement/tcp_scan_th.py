import threading
import time
import socket
import threading
import collections
from datetime import datetime
'''section 1'''
net = input("Enter the Network Address ")
st1 = int(input("Enter the starting Number  "))
en1 = int(input("Enter the last Number "))
en1 = en1+1
dic = collections.OrderedDict()
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
t1 = datetime.now()
'''section 2'''


class myThread (threading.Thread):
    def __init__(self, st, en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en

    def run(self):
        run1(self.st, self.en)


'''section 3'''


def scan(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr, 22))
    if result == 0:
        sock.close()
        return 1
    else:
        sock.close()


def run1(st1, en1):
    for ip in range(st1, en1):
        addr = net2+str(ip)
        if scan(addr):
            dic[ip] = addr


'''section 4'''
total_ip = en1-st1
tn = 20  # number of ip handled by one thread
total_thread = total_ip/tn
total_thread = total_thread+1
threads = []
try:
    for i in range(input(total_thread)):
        # print "i is ",i
        en = st1+tn
        if (en > en1):
            en = en1
        thread = myThread(st1, en)
        thread.start()
        threads.append(thread)
        st1 = en
except:
    print("Error: unable to start thread")
print("Number of Threads active:", threading.active_count())
for t in threads:
    t.join()
print("Exiting Main Thread")
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print(dict[key], "-->" "Live")
t2 = datetime.now()
total = t2-t1
print("scanning complete in ", total)
