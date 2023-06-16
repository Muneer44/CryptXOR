import random
import time
import os
import subprocess
ENCRYPTION_KEY_SIZE = 128 // 8  # Size of encryption key (bytes).


def read_file(fname):
    if not os.path.isfile(fname):  # Handle error
        raise FileNotFoundError(f"\nError: file '{fname}' not found")
    with open(fname, "r", encoding="utf-8") as f:
        return f.read()


def option_menu():
    # Print the main menu options
    print("Menu: \n \
    1) Encrypt a custom message. \n \
    2) Encrypt a file. \n \
    3) Decryptor program. \n \
    4) Exit \n")


def create_key():
    # Generate a random encryption key
    char_set = ''
    for i in range(0x00, 0xFF):
        char_set += chr(i)
    encrypted_key = ''
    for i in range(ENCRYPTION_KEY_SIZE):
        encrypted_key += random.choice(char_set)
    return encrypted_key


def encrypt_msg(msg):
    key_index = 0
    max_key_index = ENCRYPTION_KEY_SIZE - 1
    encrypted_message = ''
    encryption_key = create_key()
    # Encrypt each character of the message using XOR operation against the encryption key.
    for char in msg:
        # XOR each char's unicode with encryption key..
        encrypted_char = ord(char) ^ ord(encryption_key[key_index])
        # Convert encrypted unicode to char and append to form result
        encrypted_message += chr(encrypted_char)
        if key_index >= max_key_index:
            key_index = 0
        else:
            key_index += 1
    return encrypted_message, encryption_key


def write_to_file(fname, data):
    try:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(data)
        time.sleep(1.5)
        print(f'\n-> "{fname}" file created!')
    except IOError as err:  # Error handling
        print(f"\nError: Failed to write to file '{fname}': {err}")


def print_message(plain_msg, encryp_msg, key):
    # Print the results.
    if choice == "2":
        print("\n---- Start of plain text ----")
        print(plain_msg)
        print("---- End of plain text ----")
        print("\n-> Encrypting data...")
        time.sleep(3)
        print("\n---- Cipher text starts here ----")
        print(encryp_msg)
        print("---- End of Cipher text ----")
        time.sleep(1)
        print(f"\nDecryption Key: {key}\n\n")

    else:
        print(f'\nDecryption Key = {key}')
        print(f'\nEncrypted Message = {encryp_msg}')


banner = ("Disclaimer: This XOR File Encryptor-Decryptor program is provided for educational purposes only. \n\
Misuse of this program, such as using it to encrypt or decrypt files without proper authorization, or using it on important or irreplaceable files, may result in permanent data loss or file corruption.\n\
Be mindful!")

while True:
    print("\n---| XOR File Encryptor-Decryptor Program |---\n")
    print(f'{banner}\n')
    option_menu()
    choice = input("Enter your choice [1-4]: ")

    if choice == "1":
        custom_msg = input("Enter your message: ")
        encrypted_msg, decryption_key = encrypt_msg(custom_msg)
        print_message(custom_msg, encrypted_msg, decryption_key)
        write_to_file("Encrypted_Message.txt", encrypted_msg)
        write_to_file("Encrypted_Message_Key.txt", decryption_key)
        exit()
    elif choice == "2":
        filename = input(
            "\nEnter the absolute path of the file: \n(example: c:\\download\\TestFile.txt) \n> ")
        try:
            file_data = read_file(filename)
            encrypted_data, encryption_key = encrypt_msg(file_data)
            print_message(file_data, encrypted_data, encryption_key)
            write_to_file(filename + "_Encrypted", encrypted_data)
            write_to_file(filename + "_Key", encryption_key)
        except FileNotFoundError as err:
            print(f"\n{err}")
        exit()
    elif choice == "3":
        Decryptor_file = os.getcwd() + '\Decryptor.py'
        subprocess.call(['python', Decryptor_file])
        exit()
    elif choice == "4":
        print("\nTerminating...")
        time.sleep(1)
        break
    else:
        print("\nInvalid choice!\n\n")

    time.sleep(2)
