from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)  # You can choose a different mode if needed
    nonce = cipher.nonce
    ciphertext=cipher.encrypt(msg.encode('ascii'))
    return nonce,ciphertext

def decrypt(nonce,ciphertext):
    cipher=DES3.new(key,DES3.MODE_EAX,nonce=nonce)
    plaintext=cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

# Example usage
nonce,ciphertext=encrypt(input("Enter a message: "))
plaintext=decrypt(nonce,ciphertext)
print(f"Cipher text: {ciphertext}")
print(f"Plain text: {plaintext}")
