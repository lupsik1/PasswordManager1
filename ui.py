from hash import gen_password, decrypt_rsa, encrypt_rsa, private_key_from_txt
import subprocess
from db_op import store_password, find_users, find_password
import pyperclip


def menu():
    # print('-'*30)
    # print(('-'*13) + 'Menu'+ ('-' *13))


    print('1. Utworz nowe haslo')
    print('2. Znajdz wszystkie strony z haslami dla danego uzytkownika')
    print('3. Otrzymaj haslo dla strony')
    print('Q. Wyjsc z programu')
    # print('-'*30)
    return input(': ')


def create(usr):
    app_name = input('Podaj nazwe strony, dla ktorej zapisujesz haslo: ')
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
        psw = input('Wpisz swoje haslo: ')
        while (psw == ''):
            print('Nie wpisales hasla!')
            psw = input('Wpisz swoje haslo: ')
    user_email = input('Wpisz maila wykorzystanego do rejestracji: ')
    url = input('Wklej adres strony do ktorej tworzysz haslo(z http:// na początku): ')


    store_password(psw, user_email, url, app_name, usr=usr)


def find(usr):
    print('Wpisz imie strony, pod ktorym jest przechowywana w tej bazie: ')
    appname = input()
    find_password(appname, usr)