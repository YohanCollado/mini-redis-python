import socket

HOST = "127.0.0.1" # local host
PORT = 6379 # redis default port

store = {} # our db so far

# we create something like redis, a giant in memory key value store
# stores value in memory for faster access

def handle_command(command): # brain of the server
    parts = command.strip().split() 
    # strip removes extra space or lines
    # splits the input by spaces between parts (command, value)
    # split is a tokenization or parsing

    if not parts: 
        return "ERROR: empty command"

    cmd = parts[0].upper()
    
    if cmd == "SET": # modifies db
        if len(parts) < 3:
            return "ERROR: SET needs key and value"
            # has to be 3, we need SET key value
            
        key = parts[1]
        value = " ".join(parts[2:])
        store[key] = value # modifies RAM

        return "OK"

    elif cmd == "GET": # reads from db
        if len(parts) != 2:
            return "ERROR: GET needs a key"

        key = parts[1]

        if key in store:
            return store[key]
        else:
            return "NULL"
    elif cmd == "DEL":
        if len(parts) != 2:
            return "ERROR: DEL needs key"
            
        key = parts[1]

        if key in store:
            del store[key]
            return "DELETED"
        else: 
            return "NULL"

    elif cmd == "PING": # health check for our kvs
        return "PONG"
        
    else:
        return "ERROR: unknown command"
        
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # creates a TCP socket
    # AF_INET = IPv4 networking
    # SOCK_STREAM = TCP connection

    server.bind((HOST, PORT))
    server.listen()

    print(f"Mini Redis is running on {HOST}:{PORT}")

    while True:
        connection, address = server.accept()
        print(f"Connected by {address}")

        with connection:
            while True:
                data = connection.recv(1024)

                if not data:
                    break

                command = data.decode("utf-8")
                response = handle_command(command)

                connection.sendall((response + "\n").encode("utf-8"))

if __name__ == "__main__":
    start_server()