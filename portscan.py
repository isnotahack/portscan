import requests
import IPy
import sys
import socket

ip = sys.argv[1]
port = sys.argv[2]


def portscan(ip, port):
    ip=str(ip)
    port=int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:

        print("**"+ip+"   "+str(port) +"   open")
    else:
        print("** close")
    return

portscan(ip, port)
