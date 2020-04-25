# Caesar cipher
def encrypt(msg):
    shift = int(input("Please enter shift value: <1-25>: "))
    r = range(1, 26)
    if shift in r:
        cipher = ''
        for char in msg:
            if char.isalpha():                
                code = ord(char) + shift
                if char.islower():
                    if code > ord('z'):
                        code -= 26
                elif char.isupper():
                    if code > ord('Z'):
                        code -= 26
                
                cipher += chr(code)
            else:
                cipher += char
        print(cipher)
    else:
        print("Invalid Input!")


# Caesar cipher - decrypting a message
def decrypt(msg):
    shift = int(input("Please enter shift value: <1-25>: "))
    r = range(1, 26)
    if shift in r:
        text = ''
        for char in msg:
            if char.isalpha():
                code = ord(char) - shift
                if char.islower():
                    if code < ord('a'):
                        code += 26
                elif char.isupper():
                    if code < ord('A'):
                        code += 26
                    
                text += chr(code)
            else:
                text += char
        print(text)

caesar = None
while caesar != "q":
    caesar = input("Would you like to encrypt or decrypt? (q to quit) ")

    if caesar != "q":
        if caesar == "encrypt":
            msg = input("Please enter the message: ")
            encrypt(msg)

        elif caesar == "decrypt":
            msg = input("Please enter the message: ")
            decrypt(msg)

        else:
            print("Invalid Input!")


            
