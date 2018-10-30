import requests
import IPy
import sys
import socket

ip = sys.argv[1]
port = sys.argv[2]

def portscan(ip, port):
    ip=str(ip)
    port = port.split(",")
    for x in port:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        x=int(x)
        result = s.connect_ex((ip, x))
        if result == 0:

            print("**"+ip+"   "+str(x) +"   open")
        else:
            print("**" + ip + "   " + str(x) + "   close")
        s.close()


portscan(ip, port)
