from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def encrypt_health_record(plaintext, secret_key):
    key = secret_key.ljust(32, '\x00')[:32]
    iv = get_random_bytes(16)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    encrypted_data = base64.b64encode(iv + ciphertext)
    return encrypted_data.decode()

# Wrapper for web use with fixed key
default_key = "ThisIsASecretKey123"

def encrypt_text(text):
    return encrypt_health_record(text, default_key)