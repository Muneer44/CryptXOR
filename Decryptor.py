import time  # Module used for sleep functionality.
import os   # Module used for file operations.


def decrypt_msg(message, key):
    key_index = 0
    max_key_index = len(key) - 1  # Max index.
    decrypted_msg = ''
    for char in message:  # Iterate over each encrypted msg char.
        # XOR each char's unicode with encryption key.
        decrypt_char = ord(char) ^ ord(key[key_index])
        # Convert decrypted unicode to char and append to form result
        decrypted_msg += chr(decrypt_char)
        if key_index >= max_key_index:
            key_index = 0
        else:
            key_index += 1
    return decrypted_msg


def read_file(fname):
    if not os.path.isfile(fname):  # Handle error
        raise FileNotFoundError(f"\nError: file '{fname}' not found")
    with open(fname, "r", encoding="utf-8") as f:
        return f.read()


def write_to_file(fname, data):
    try:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(data)
        time.sleep(1.5)
        print(f'\n-> "{fname}" file created!')
    except IOError as err:  # Error handling
        print(f"\nError: Failed to write to file '{fname}': {err}")


print("\n---| XOR File Decryptor Program |---")
encrypted_filename = input(
    "\nEnter encrypted file's absolute path:\n(example: c:\\download\\TestFile.txt) \n> ")
decryption_key_filename = input("\nLocate decryption key file: \n> ")
if not encrypted_filename or not decryption_key_filename:   # To set default files.
    encrypted_filename = "Encrypted_Message.txt"
    decryption_key_filename = "Encrypted_Message_Key.txt"
try:
    encrypted_data = read_file(encrypted_filename)  # Read encrypted data.
    decryption_key = read_file(decryption_key_filename)  # Read decryption key.
except FileNotFoundError as err:
    print(f'\n{err}')
# Decrypt the encrypted data.
decrypted_data = decrypt_msg(encrypted_data, decryption_key)
print(
    f'\n"----Decrypting "{encrypted_filename}" using "{decryption_key_filename}"----" \n')
time.sleep(1)
print(f'{decrypted_data}\n\n-> Data decrypted successfully!')
write_to_file("_Decrypted.txt", decrypted_data)  # Write decrypted o/p to file.
