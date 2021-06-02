import ui
import hash
import db_op
<<<<<<< Updated upstream
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

mode = input('Rejestracja(reg) czy wejscie(log)?:')

username = input('Podaj imie uzytkownika: ')
passw = input('Podaj master-haslo: ')
=======
from Crypto.PublicKey import RSA
import base64

try:
    open("key_file.pem", 'r')
except FileNotFoundError:
    f = open("key_file.pem", 'wb')
    new_key = RSA.generate(2048)
    priv_key = new_key.exportKey("PEM")
    f.write(priv_key)
    f.close()

try:
    log_info = open("login_file.bin", 'rb')
    file = open("key_file.pem", "rb")
    priv_key = private_key_from_txt(file.read())
    log_info_decoded = decrypt_rsa(priv_key, log_info.read()).decode().splitlines()
    username = log_info_decoded[0]
    passw = log_info_decoded[1]
    log_info.close()
    file.close()

except OSError:
    username = input('Podaj imie uzytkownika: ')
    passw = input('Podaj master-haslo: ')

    log_info_uncoded = username+"\n"+passw
    log_info = open("login_file.bin", 'wb')
    file = open("key_file.pem", "rb")
    priv_key = private_key_from_txt(file.read())
    public_key = priv_key.publickey()
    log_info.write(encrypt_rsa(log_info_uncoded, public_key))
    log_info.close()

mode = input('Rejestracja(reg) czy wejscie(log)?:')
>>>>>>> Stashed changes

if mode == 'reg':
    db_op.create_user(username, passw)
elif mode != 'log':
    print('No to do widzenia')
    exit()

attempt = db_op.login_user(username, passw)

if attempt == -1:
    print('Niepowodzenie!')
    exit()
else:
    print('Powodzenie!')

choice = ui.menu()
while choice != 'Q':
    if choice == '1':
        ui.create(username)
    elif choice == '2':
        ui.find_accounts(username)
    elif choice == '3':
        ui.find(username)
    else:
        choice = ui.menu()
    choice = ui.menu()
exit()