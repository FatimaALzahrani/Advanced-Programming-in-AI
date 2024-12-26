# XOR encryption and decryption function
def xor_encrypt_decrypt(data, key):
    result = "" 
    for char in data:
        result += chr(ord(char) ^ key)
    return result

message = "Hello, XOR encryption!"
key = 42
encrypted_message = xor_encrypt_decrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
