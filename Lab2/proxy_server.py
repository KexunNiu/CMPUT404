#Reference: https://drive.google.com/file/d/1Kvp7ZRIp2gseromIrwiWZpCXJsH3HkBn/view
#Wrote these after watching the video

import socket

HOST = ""
PORT = 8001

def main():
    host = 'www.google.com'
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_skt:

        proxy_skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        proxy_skt.bind((HOST, PORT))

        proxy_skt.listen(2)

        while True:
            connection,addr = proxy_skt.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_skt_end:
                ip = socket.gethostbyname(host)

                proxy_skt_end.connect((ip,port))

                data = connection.recv(4068)
                print(f"",data)

                proxy_skt_end.sendall(data)

                proxy_skt_end.shutdown(socket.SHUT_WR)
                data2 = proxy_skt_end.recv(1024)
                print(f"",data2)
                connection.send(data2)

            connection.close()

main()


