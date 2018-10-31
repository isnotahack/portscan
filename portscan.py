import argparse
import socket
import IPy
import threading
import queue

def portscan(q):
    while True:
        try:
            (ip, port) = q.get(block=False)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            port = int(port)
            ip = str(ip)
            result = s.connect_ex((ip, port))
            if result == 0:

                print("**" + ip + "   " + str(port) + "   open")
            else:
                print("**" + ip + "   " + str(port) + "   close")
            s.close()
            q.task_done()
        except queue.Empty:
             break

def threadPool(thread_num):
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=portscan, args=(q,))
        t.start()
        threads.append(t)



def scan(ips, ports):
    ports = ports.split(",")
    ips=IPy.IP(ips)
    for ip in ips:
        for port in ports:
            ip = str(ip)
            port = int(port)
            q.put((ip, port))




if __name__ == "__main__":
    lock = threading.Lock()
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="port", type=str)
    parser.add_argument("-t", help="target", type=str)
    parser.add_argument("-s", help="thread", type=int, default=10)
    args = parser.parse_args()
    thread_num=args.s
    ports = args.p
    ips = args.t
    q = queue.Queue()
    scan(ips, ports)
    threadPool(thread_num)
