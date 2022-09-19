#Reference: https://drive.google.com/file/d/1Kvp7ZRIp2gseromIrwiWZpCXJsH3HkBn/view
#Wrote these after watching the video

import socket
import time

HOST = ""
PORT = 8001

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:

        skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        skt.bind((HOST, PORT))

        skt.listen(2)

        print("Listening")

        while True:
            connection,addr = skt.accept()
            print(addr," connected")
            
            data = connection.recv(1024)

            time.sleep(1)
            connection.sendall(data)
            connection.close()



if __name__=="__main__":
    main()
