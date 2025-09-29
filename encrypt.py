import re

#Ceaser Cipher -  changes the the letters with the key
def ceaserCipher(text, key) -> str:
    result = []
    for i in range (len(text)):
        char = text[i]
        if (char.isupper()):
            result.append(chr((ord(char) + key - 65) % 26 + 65))
        elif (char.islower()):
            result.append(chr((ord(char) + key - 97) % 26 + 97))
        else:
            result.append(char)
    return ''.join(result)

#Substitution Cipher -  changes the vawols into ASCII and add the number in key
def substitutionCipher(text, key) -> str:
    result =[]
    vowels = set('aeiouAEIOU')
    for i in range(len(text)):
        char = text[i]
        if char in vowels:
            result.append(f"*{ord(char) + key}*")
        else: 
            result.append(char)
    return ''.join(result)
        
#Runs the encryption by steps
def encrypt(text, key) -> str:
    encrypt1 = ceaserCipher(text, key)
    encrypt2 = substitutionCipher(encrypt1, key)
    return encrypt2

#decryption to the substitution cipher    
def decryptSubstitution(text, key) ->str:
    result = []
    i = 0
    while i < len(text):
        if text[i] == "*":  
            j = text.find("*", i + 1)
            if j != -1:
                num_str = text[i+1:j] 
                if num_str.isdigit():
                    num_minus_key = int(num_str) - key
                    result.append(chr(num_minus_key))
                i = j + 1
                continue
        result.append(text[i])
        i += 1
    return ''.join(result)

    
def decrypt(text, key):
    decrypted_text1 = decryptSubstitution(text, key)
    #uses same function as encodying but changes key to negative number 
    decrypted_text2 = ceaserCipher(decrypted_text1, -key)
    return decrypted_text2

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                file.write(encrypt(line, key))
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                file.write(decrypt(line, key))
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    
    choice = int(input("Enter your choice: "))
    input_file = input("Enter the input file name: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 1:
        output_file = "encrypted.txt"
        encrypt_file(input_file, output_file, key)
        print(f"Encrypted output saved as {output_file}")

    elif choice == 2:
        output_file = "decrypted.txt"
        decrypt_file(input_file, output_file, key)
        print(f"Decrypted output saved as {output_file}")
    else:
        print("Invalid choice.")