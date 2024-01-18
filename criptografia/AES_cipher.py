#!/usr/bin/env python
#
# 2024 Diego L. Pedro <diegolpedro@gmail.com>.
#
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'datos_secretos'

# Generamos encriptador
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

# Encriptado
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce
print(ciphertext)

# Desencriptado
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)
