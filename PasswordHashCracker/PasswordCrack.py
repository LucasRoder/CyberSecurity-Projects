import hashlib

def hash_word(word):
    return hashlib.md5(word.encode()).hexdigest()

def crack_password(password):
    with open("wordlist.txt", "r") as file:
        wordlist = file.readlines()
    for word in wordlist:
        word = word.strip()
        hashed = hash_word(word)
        if password == hashed:
            print(f"Password found: {word}")
            return

    print("Password not found")


def main():
    password = input("Enter hash password: ").strip()
    crack_password(password)


if __name__ == "__main__":
    main()
