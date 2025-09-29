def ceaserCipher(text, key):
    result = []
    for i in range (len(text)):
        char = text[i]
        if (char.isalpha()):
            result.append(chr((ord(char) + key-65) % 26 + 65))
        else:
            result.append(chr((ord(char) + s - 97) % 26 + 97))
    return ''.join(result)

def substitutionCipher(text, key):
    result =[]
    vowels = set('aeiouAEIOU')
    for i in range(len(text)):
        char = text[i]
        if char in vowels:
            result.append(str(ord(char) + key))
        else: 
            result.append[char]
    return ''.join(result)
        

def encrypt(text, key):
    encrypt1 = ceaserCipher(text, key)
    encrypt2 = substitutionCipher(encrypt1, key)
    encrypted_text = ''  
    return encrypted_text
    

def decrypt(text, key):
    decrypted_text = ''.join([chr(ord(char) - key) for char in text])
    return decrypted_text

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
    output_file = input("Enter the output file name: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 1:
        encrypt_file(input_file, output_file, key)
    elif choice == 2:
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid choice.")