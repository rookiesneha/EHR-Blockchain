from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_health_record(encrypted_text, secret_key):
    key = secret_key.ljust(32, '\x00')[:32].encode()
    data = base64.b64decode(encrypted_text)
    iv = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode()