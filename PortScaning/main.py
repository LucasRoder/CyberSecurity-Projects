import socket
import threading
import queue


IP_ADDRESS = "10.23.173.239" # VM IP
q = queue.Queue() # list for port numbers
PORT_START_RANGE = 1
PORT_END_RANGE = 150

for i in range(PORT_START_RANGE, PORT_END_RANGE): #makes q of ports
    q.put(i)


def scan():
    while not q.empty(): # continues till q is empty
        port = q.get()# grabs first port we put in q and removes it from q

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # opens socket
            try:
                s.connect((IP_ADDRESS, port)) # tries to connect to port
                print(f"Port {port} connected")
            except:
               pass# if connection unsucsesful skips

        q.task_done()





for i in range(30):
    t = threading.Thread(target= scan, daemon=True)
    t.start()
# we use threads becuase smallest process withing program will be fastest
# thread object assigned to scan function target key word what you want thread to do
# daemon set to true means when main program closses all threds close
# t.start() starts job

q.join() # dont run until task done
print(f"finished scanning ports from {PORT_START_RANGE} to {PORT_END_RANGE} ports")


# https://www.youtube.com/watch?v=oIQyPeBhs_4&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=2