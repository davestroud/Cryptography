# https://stackoverflow.com/questions/
# 36834580/iv-must-be-16-bytes-long-error-in-aes-encryption
# -------------------------
# Uses the pycrypto library

from Crypto.Cipher import AES
# import binascii
import os


def aes_encrypt(plaintext):
    key = "00112233445566778899aabbccddeeff"
    iv = os.urandom(16)
    aes_mode = AES.MODE_CBC
    obj = AES.new(key, aes_mode, iv)
    ciphertext = obj.encrypt(plaintext)
    return ciphertext


# print(aes_encrypt("TestTestTestTest"))

# iv = binascii.hexlify(os.urandom(16))
# print(iv)

# print(len(iv))

iv = os.urandom(16)

print(iv)
