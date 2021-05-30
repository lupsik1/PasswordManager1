from hashlib import sha256
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def create_salt():
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

    chars = []

    while len(chars) < 5:
        n = random.randint(0, len(ALPHABET) - 1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha) - 1)
        chars.append(alpha[n])

    return ''.join(chars)


def hash_password(salt, plaintext):
    return sha256((salt + plaintext).encode('utf-8')).hexdigest()


def gen_password():
    length = random.randint(9, 18)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

    chars = []

    while len(chars) < length:
        n = random.randint(0, len(ALPHABET) - 1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha) - 1)
        chars.append(alpha[n])
    return "KUPADUPA"
    # return ''.join(chars)


def encrypt_rsa(msg: str, public_key):
    print("encrypt got msg of type", type(msg))
    cipher_rsa = PKCS1_OAEP.new(public_key)

    ret = cipher_rsa.encrypt(msg.encode('utf-8'))
    print("encryption succeeded!")
    return ret


def decrypt_rsa(private_key, enc_msg):
    enc_msg = enc_msg
    print(enc_msg)
    print(enc_msg[0])
    cipher_rsa = PKCS1_OAEP.new(private_key)
    print("cipher rsa sie zrobilo")
    ret = cipher_rsa.decrypt(enc_msg)
    print("decrypted :)")
    return ret


def private_key_from_txt(text):
    return RSA.importKey(text)
