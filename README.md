ClinetServerConnection
A client-side socket program that connects to a server IP + port and sends or receives messages
The server socket program Uses `bind()`, `listen()`, `accept()’ Waits for a client to connect
ComputerCrash
CrashScript.py` Continuously launches itself
The script is a fork–bomb that overwhelms system resources.
DO NOT USE ON MAIN MACHINE. This is malicious behavior if used improperly.
Communication
ComEncrypter.py` Implements XOR encryption on text input by the user
Encrypts/decrypts messages
KeyLogger
KeyLogger.py uses a library like `pynput` to record every keystroke and writes them to KeyStrokes.txt.
PortScanning
main.py takes a target IP, loops through ports set by the user (1–1024 or similar), and uses `socket.connect_ex()` to test open ports
This is a basic port scanner, nmap-style tool
Ransomware
encryption.py file encrypts files with XOR text and replaces the original content at the bit level with scrambled garbage text
This simulates ransomware behavior. DO NOT USE ON MAIN MACHINE
decryption.py reverses the encryption and uses the same key
`serverRansomWare.py acts as a C2-style server that sends the encryption key and hostname to the attacker


* Client/server networking
* XOR encryption
* Port scanning
* Keylogging
* Ransomware simulation
* Process abuse/crash simulation

Use auto-py-to-exe for projects to run

