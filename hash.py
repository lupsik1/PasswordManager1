from hashlib import sha256
import random
from crypto.Cipher import AES


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

    return ''.join(chars)


def encrypt_aes(msg, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


def decrypt_aes(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
