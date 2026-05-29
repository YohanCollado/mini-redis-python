import socket

HOST = "127.0.0.1"
PORT = 6379

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to Mini Redis")
    print("Type 'exit' to quit\n")

    while True:
        command = input("redis> ")

        if command.lower() == "exit":
            break;

        client.sendall(command.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")

        print(response)

    client.close()


if __name__ == "__main__":
    start_client()
