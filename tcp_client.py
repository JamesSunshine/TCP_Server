import socket
import argparse

def tcp_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(100)
    file = open("file2.txt", 'wb')
    file.write(data)

def valid_port(port):
    port = int(port)
    if port < 1024 or port >= 64000:
        raise argparse.ArgumentError()
    return port

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port", type=valid_port)
    args = parser.parse_args()
    tcp_client(args.host, args.port)
