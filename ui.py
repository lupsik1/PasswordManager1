from hash import gen_password
import subprocess 
from db_op import store_password, find_users, find_password
import pyperclip

def menu():
    #print('-'*30)
    #print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Utworz nowe haslo')
    print('2. Znajdz wszystkie strony z haslami dla danego uzytkownika')
    print('3. Otrzymaj haslo dla strony')
    print('Q. Wyjsc z programu')
    #print('-'*30)
    return input(': ')

def create(usr):
    app_name = input('Podaj nazwe strony, dla ktorej zapisujesz haslo: ')
    mode = input('Chcesz stworzyc nowe haslo(cre) czy zapisac istniejace(sav)?: ')
    while(mode != 'sav' and mode != 'cre'):
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
<<<<<<< Updated upstream
        psw = input('Wpisz swoje haslo')
        while(psw == ''):
=======
        psw = input('Wpisz swoje haslo: ')
        while (psw == ''):
>>>>>>> Stashed changes
            print('Nie wpisales hasla!')
            psw = input('Wpisz swoje haslo: ')
    user_email = input('Wpisz maila wykorzystanego do rejestracji: ')
    url = input('Wklej adres strony do ktorej tworzysz haslo: ')
    store_password(psw, user_email, url, app_name, usr=usr)

def find(usr):
    print('Wpisz imie strony, pod ktorym jest przechowywana w tej bazie: ')
    appname = input()
    find_password(appname, usr)

def find_accounts(usr):
<<<<<<< Updated upstream
    print('Please provide the email that you want to find accounts for')
    user_email = input() 
    find_users(user_email, usr)
=======
    find_users(usr)
>>>>>>> Stashed changes
