#Reference: https://drive.google.com/file/d/1Kvp7ZRIp2gseromIrwiWZpCXJsH3HkBn/view
#Wrote these after watching the video

import socket
from multiprocessing import Process

buffersize = 4068
payload = f'GET / HTTP/1.0\r\nHost: {url}\r\n\r\n'

def main():

    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    url = "www.google.com"
    
    ip = socket.gethostbyname(url)
    skt.connect((ip,80))

    skt.sendall(payload.encode('utf-8'))

    skt.shutdown(socket.SHUT_WR)

    output = b""

    while skt:
        temp = skt.recv(buffersize)
        if not temp:
            break
        output += temp

        p = Process(target = echo_handler,args=(skt))
        p.daemon = True
        p.start()
    
    print(output)

    skt.close()

def echo_handler(skt):
    skt.sendall(payload.encode('utf-8'))

    skt.shutdown(socket.SHUT_WR)

    output = b""

    while skt:
        temp = skt.recv(buffersize)
        if not temp:
            break
        output += temp
    
    print(output)


if __name__=="__main__":
    main()
