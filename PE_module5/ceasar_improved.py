# Ceasar Cipher
# Encrypt, Decrypt or Brute Force

# setting max shift value + 1
MAX_SHIFT = 26


# get the message from user
def getMsg():
    msg = input("Enter your message: ")
    return msg


# ask user if they want to either encrypt or decrypt
def getMode():
    while True:
        mode = (input("""
Would you like to encrypt or decrypt or brute forced? """).lower())
        if mode in "encrypt e decrypt d brute b".split():
            return mode
        else:
            print("""
Invalid input.
Please enter either 'encrypt' or 'e' or 'decrypt' or 'd' or 'brute' or 'b'.
""")


# get shift value from user
def getShift():
    shift = 0
    shift = int(input("Please enter shift value: <1-25>: "))
    if shift in range(1, MAX_SHIFT):
        return shift


def ceasar(mode, msg, shift):
    if mode[0] == "d":
        shift = -shift

    text = ""

    for char in msg:
        if char.isalpha():
            code = ord(char) + shift

            if char.islower():
                if code < ord('a'):
                    code += 26
                elif code > ord('z'):
                    code -= 26
            elif char.isupper():
                if code < ord('A'):
                    code += 26
                elif code > ord('Z'):
                    code -= 26

            text += chr(code)
        else:
            text += char
    return text


while __name__ == "__main__":
    msg = getMsg()
    mode = getMode()

    if not mode[0] in "brute b".split():
        shift = getShift()

    print(f"Your message has been translated to the following:")

    if not mode[0] in "brute b".split():
        print(ceasar(mode, msg, shift))
    else:
        for shift in range(1, MAX_SHIFT):
            print(shift, ceasar("d", msg, shift))
