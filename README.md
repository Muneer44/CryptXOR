# CryptXOR 

This 'CryptXOR - Encryptor-Decryptor' program is designed to encrypt custom messages or files, while the Decryptor program enables decryption using the corresponding encryption key. 
The program utilizes manual XOR operations to perform encryption and decryption, instead of using advanced cryptography encryption algorithm modules, to understand and analyze the weaknesses and mechanism of basic cryptography.   


### Disclaimer:
Misuse of this program, such as using it to encrypt or decrypt files without proper authorization, or using it on important or irreplaceable files, may result in permanent data loss or file corruption. 
Use this program responsibly and at your own risk.

## Analysis
![XOR weak 2](https://github.com/Muneer44/CryptXOR/assets/117259069/e8a61725-e4c1-4bdb-a430-58a6d1b38e3a)  

![XOR weak](https://github.com/Muneer44/CryptXOR/assets/117259069/a15c8d78-51ef-4b38-89e3-e649e661bc01)
> Demonstrates XOR key repeatition: Exhibiting predictable pattern when the message is longer than the encryption key.

- **Limited key space:** XOR encryption uses relatively short and fixed-length encryption keys, making it vulnerable to brute force attacks.
- **Key distribution challenges:** Securely distributing and managing encryption keys in XOR encryption can be difficult, especially in large-scale systems or when communicating over untrusted channels.
- **Lack of diffusion and confusion:** XOR encryption does not provide strong mixing and confusion of data, making it susceptible to frequency analysis attacks.
- **Known plaintext vulnerability:** XOR encryption is vulnerable to known plaintext attacks, where having access to both the plaintext and ciphertext can reveal the encryption key.
- **Bit flipping susceptibility:** XOR encryption is prone to bit flipping attacks, allowing attackers to manipulate specific bits in the ciphertext and affect the corresponding bits in the decrypted plaintext.


## Demonstration
https://github.com/Muneer44/CryptXOR/assets/117259069/8c31a355-a38f-4f5d-8eb1-486190216efd

## Usage
![A-1](https://github.com/Muneer44/CryptXOR/assets/117259069/2c233e61-875f-422b-bbb3-aa9670ec0615)
-> _Choose the desired operation from the menu: encrypt a custom message, encrypt a file, or use the decryptor program._  

---  

![A-2](https://github.com/Muneer44/CryptXOR/assets/117259069/0d06dc43-0936-42b4-9833-28b7411a8a14)    
-> _Provide the necessary inputs such as the message to encrypt or the file path._    

---  

![A-3](https://github.com/Muneer44/CryptXOR/assets/117259069/352f69e0-9265-40e4-bb5d-308023984f2d)  
![A-4](https://github.com/Muneer44/CryptXOR/assets/117259069/6c98b066-5fb4-4e89-aef1-ea2dd6cb3365)  
-> _The program will perform the encryption or decryption and display the results._  

---  

![B-1](https://github.com/Muneer44/CryptXOR/assets/117259069/7695f4a3-c159-43ae-a8ab-15fee95848e5)  
![B-2](https://github.com/Muneer44/CryptXOR/assets/117259069/e26183bd-846a-45a9-a13b-de0292678822)  

-> _Encrypted data will be written to a file for further use._  

![B-3](https://github.com/Muneer44/CryptXOR/assets/117259069/2f187edc-d02a-4368-aca1-93553430b07a)  

![B-4](https://github.com/Muneer44/CryptXOR/assets/117259069/5254e898-ed4a-4916-b565-2b35d69e1ab9)  

---  

![C-1](https://github.com/Muneer44/CryptXOR/assets/117259069/7ce84b3e-aa05-45ee-b91e-0521820c40b9)  

![image](https://github.com/Muneer44/CryptXOR/assets/117259069/dc336536-9553-4719-b60b-2f89720aaa8e)  
-> _Even the Decrypted data will be written to a file for further use._  

## Note
This program uses a simple XOR encryption algorithm, which has limitations and is not considered secure for real-world encryption needs. It is designed for educational purposes to understand encryption mechanism and analyze its weaknesses.
