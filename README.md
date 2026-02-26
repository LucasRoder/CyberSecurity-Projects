1. ClinetServerConnection
A client-side socket program which connects to a server IP + port and sends or receives messages
The server socket program Uses `bind()`, `listen()`, `accept()’ Waits for a client to connect

2. ComputerCrash
CrashScript.py` Continuously launches itself
The script is fork bomb–style script that overwhelms system resources.
DO NOT USE ON MAIN MACHINE. This is malicious behavior if used improperly.

4. Communication
ComEncrypter.py` Implements XOR encryption on text input by the user
Encrypts/decrypts messages
5. KeyLogger
KeyLogger.py uses a library like `pynput` to record every keystroke and writes them to KeyStrokes.txt`
6. PortScanning
main.py takes a target IP, loops through ports set by the user (1–1024 or similar), and uses `socket.connect_ex()` to test open ports
This is a basic port scanner nmap-style tool
7. Ransomware
encryption.py file encrypts files with XOR text and replaces original content at the bit level with scrambled garbage text
This simulates ransomware behavior. DO NOT USE ON MAIN MACHINE
decryption.py reverses the encryption uses the same key
`serverRansomWare.py acts as a C2-style server sends encryption key and hostname to attacker


* Client/server networking
* XOR encryption
* Port scanning
* Keylogging
* Ransomware simulation
* Process abuse / crash simulation

Use auto-py-to-exe for projects to run



