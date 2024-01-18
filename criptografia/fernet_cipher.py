#!/usr/bin/env python
#
# 2024 Diego L. Pedro <diegolpedro@gmail.com>.
#
from cryptography.fernet import Fernet

# Generar una nueva clave Fernet
clave_secreta = Fernet.generate_key()

# Crear un objeto Fernet
cipher_suite = Fernet(clave_secreta)

# Encriptar la contraseña
password = "tu_contraseña"
print(password)

# Encriptamos
encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
print(encrypted_password)

# Desencriptamos
# Guardar la contraseña en un archivo o en algún lugar seguro
password = cipher_suite.decrypt(encrypted_password).decode('utf-8')

print(password)
