from hash import gen_password, decrypt_rsa, encrypt_rsa, private_key_from_txt
import subprocess
from db_op import store_password, find_users, find_password
import pyperclip


def menu():
    # print('-'*30)
    # print(('-'*13) + 'Menu'+ ('-' *13))


    print('1. Utworz nowe haslo')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Wyjsc z programu')
    # print('-'*30)
    return input(': ')


def create(usr):
    print('Podaj nazwe strony, dla ktorej zapisujesz haslo: ')
    app_name = input()
    mode = input('Chcesz stworzyc nowe haslo(cre) czy zapisac istniejace(sav)?: ')
    while (mode != 'sav' and mode != 'cre'):
        print('Niewiadomy tryb!')
        mode = input('Chcesz stworzyc nowe haslo(cre) czy zapisac istniejace(sav)?: ')
    psw = ''
    if mode == 'cre':
        psw = gen_password()
        pyperclip.copy(psw)
        print('')
        print('Haslo stworzone i skopiowane do schowka')
        print('')
    elif mode == 'sav':
        psw = input('Wpisz swoje haslo')
        while (psw == ''):
            print('Nie wpisales hasla!')
            psw = input('Wpisz swoje haslo')
    user_email = input('Wpisz maila wykorzystanego do rejestracji: ')
    url = input('Wklej adres strony do ktorej tworzysz haslo: ')


    store_password(psw, user_email, url, app_name, usr=usr)


def find(usr):
    print('Wpisz imie strony, pod ktorym jest przechowywana w tej bazie: ')
    appname = input()
    find_password(appname, usr)


def find_accounts(usr):
    print('Please provide the email that you want to find accounts for')
    user_email = input()
    find_users(user_email, usr)
