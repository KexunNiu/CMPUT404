#Reference: https://drive.google.com/file/d/1Kvp7ZRIp2gseromIrwiWZpCXJsH3HkBn/view
#Wrote these after watching the video

import socket

def main():

    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    url = "www.google.com"
    payload = f'GET / HTTP/1.0\r\nHost: {url}\r\n\r\n'
    buffersize = 4068

    ip = socket.gethostbyname(url)
    skt.connect(('127.0.0.1',8001))

    skt.sendall(payload.encode())

    skt.shutdown(socket.SHUT_WR)

    output = b""

    while skt:
        temp = skt.recv(buffersize)
        if not temp:
            break
        output += temp
    
    print(output)

    skt.close()


if __name__=="__main__":
    main()
