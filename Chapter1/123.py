from scapy.all import *

ping_one_reply = sr1(IP(dst='192.168.188.1')/ICMP(), timeout = 1, verbose=False)
ping_one_reply.show()

test