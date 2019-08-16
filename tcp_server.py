import asyncio
import argparse

async  def on_connect(reader, writer):
    file = open('file1.txt', 'rb')
    data = file.read()
    print("Sending file to client")
    writer.write(data)
    await writer.drain()
    print("Client socket closing")
    writer.close()

def main(port):
    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(on_connect, '127.0.0.1', port, loop=loop)
    server = loop.run_until_complete(coroutine)
    loop.run_forever()

def valid_port(port):
    port = int(port)
    if port < 1024 or port >= 64000:
        raise argparse.ArgumentError()
    return port


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=valid_port)
    args = parser.parse_args()
    main(args.port)