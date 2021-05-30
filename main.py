import ui
import os
from hash import private_key_from_txt
import db_op
from Crypto.PublicKey import RSA
import base64
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

mode = input('Rejestracja(reg) czy wejscie(log)?:')

username = input('Podaj imie uzytkownika: ')
passw = input('Podaj master-haslo: ')

try:
    open("key_file.pem", 'r')
except FileNotFoundError:
    f = open("key_file.pem", 'wb')
    new_key = RSA.generate(2048)
    priv_key = new_key.exportKey("PEM")
    f.write(priv_key)
    f.close()

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
