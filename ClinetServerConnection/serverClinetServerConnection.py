import socket # socket module

SERVER_IP = "10.25.54.180"

SERVER_PORT = 5678
# acsses socket module like acssesing a file socket function takes 2 parameters socket you create and what protocol (TCP/UDp) you are using
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT)) # binds socket to server
    print("Waiting for connection...")
    s.listen(1) # recives one connection
    conn, addr = s.accept()
    # once connection comes in object is returned that represents connection between server and clinet and varible that stores connected clinet adress
    print("Connection address:", addr)
    with conn:
        while True: # sends and recives data
            conn.send(b"hello world") # must be sent in binary b in python converts to binary
            break

# https://www.youtube.com/watch?v=oIQyPeBhs_4&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=2


