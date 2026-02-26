import random
msg = input("What is your message? ")
print(f"your message {msg}")

# will generate random key string and encrypt message with that
encryptionLevel = 128 // 8 #16 byte key

char_pool = "" # pool of potential key characters

for i in range(0x00, 0x255): # every askey character between 0 and 255
    char_pool += chr(i)


key = "" # encryption key

for i in range(encryptionLevel): # complete for level of encryption
    key += random.choice(char_pool)

#encryption works by taking binary for each char in mesage doing XOR encryption with message and key
#XOR encryption works by applying the XOR (exclusive OR) operation between each bit of the plaintext
# and a key used for encryption and decryption. If two bits are different, the result is 1; if they are
# the same, the result is 0.The key advantage is that applying XOR with the same key twice restores the
# original data, so the same operation is used for both encryption and decryption.

keyIndex = 0
maxKeyIndex = encryptionLevel-1
encryptedMsg = ""
for char in msg:
    encryptedChar = ord(char) ^ ord(key[keyIndex])
    # for every character make varible encrypted character take the integer asci value xor it with the key at key
    #index
    encryptedMsg += chr(encryptedChar) # adds char to message
    if keyIndex >= maxKeyIndex: # if at end of key index reset index
        keyIndex =0
    else:
        keyIndex += 1 # changes to next key index

print(f"Encrypted message: {encryptedMsg}")

keyIndex = 0
decryptedMsg = ""
for char in encryptedMsg: # uses same key in xor to decrypt
    decryptedChar = ord(char) ^ ord(key[keyIndex])
    decryptedMsg += chr(decryptedChar)
    if keyIndex >= maxKeyIndex:
        keyIndex =0
    else:
        keyIndex += 1
print(f"Decrypted message: {decryptedMsg}")






#https://www.youtube.com/watch?v=ZpMABSUwNj8&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=9