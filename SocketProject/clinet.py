import socket

SERVER_IP = "10.25.54.180"
SERVER_PORT = 5678

#sent to clinet make into exe auto-py-to-exe

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT)) # we dont use bind we use the server adress we want the clinet top connect too
    data = s.recv(1024) # recives message number represents amount of bites that need to come in before moves on to next code
    print(data)

input() # program dosent clsoe out

# https://www.youtube.com/watch?v=oIQyPeBhs_4&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=2