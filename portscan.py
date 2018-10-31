import argparse
import socket
import IPy
import time, threading
import queue

def portscan(ips, ports):
    ports = ports.split(",")
    ips=IPy.IP(ips)
    for ip in ips:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            port=int(port)
            ip=str(ip)
            result = s.connect_ex((ip, port))
            if result == 0:

                print("**"+ip+"   "+str(port) +"   open")
            else:
                print("**" + ip + "   " + str(port) + "   close")
            s.close()

def threadPool(thread_num):
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=portscan, args=(ips,ports))
        t.start()
        threads.append(t)


thread_num=3
parser = argparse.ArgumentParser()
parser.add_argument("-p", help="port", type=str)
parser.add_argument("-t", help="target", type=str)
args = parser.parse_args()
ports=args.p
ips=args.t



if __name__ == "__main__":
    lock = threading.Lock()
    threadPool(thread_num)
