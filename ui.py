from hash import gen_password, decrypt_rsa, encrypt_rsa, private_key_from_txt
from db_op import store_password, find_password, delete_record, edit_record
import pyperclip


def menu():
    # print('-'*30)
    # print(('-'*13) + 'Menu'+ ('-' *13))


    print('1. Utworz nowe haslo')
    print('2. Znajdz wszystkie strony z haslami dla danego uzytkownika')
    print('3. Otrzymaj haslo dla strony')
    print('4. Redaguj/usuń wpis')
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

def edit(usr):
    print('Wpisz imie strony, pod ktorym jest przechowywana w tej bazie: ')
    appname = input()
    print('Czy chcesz usunąć wpis(del) czy zredagować go?(edit)')
    mode = input()
    while(mode != 'del' and mode != 'edit'):
        print('Niewiadomy tryb działania!')
        print('Czy chcesz usunąć wpis(del) czy zredagować go?(edit)')
        mode = input()
    if mode == 'del':
        delete_record(usr, appname)
    elif mode == 'edit':
        wishes = []
        print('Czy chcesz zmienić hasło? y/n')
        wishes.append(confirm())
        psw = ''
        if(wishes[0]):
            mode = input('Chcesz stworzyc nowe haslo(cre) czy zapisac istniejace(sav)?: ')
            while (mode != 'sav' and mode != 'cre'):
                print('Niewiadomy tryb!')
                mode = input('Chcesz stworzyc nowe haslo(cre) czy zapisac istniejace(sav)?: ')
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
        print('Czy chcesz zmienic email? y/n')
        wishes.append(confirm())
        email = ''
        if(wishes[1]):
            email = input('Podaj nowy mail: ')
        print('Czy chcesz zmienic url? y/n')
        url = ''
        wishes.append(confirm())
        if(wishes[2]):
            url = input('Podaj nowy url(zaczynając od http://): ')
        print('Czy chcesz zmienic imie zapisu? y/n')
        wishes.append(confirm())
        new_name = ''
        if(wishes[3]):
            new_name = input('Podaj nowe imie zapisu: ')
        edit_record(usr, appname, wishes, psw, email, url, new_name)

def confirm():
    conf = input()
    while(conf != 'y' and conf != 'Y' and conf != 'n' and conf != 'N'):
        print('Prosze o "y" lub "n"')
        conf = input()
    if(conf == 'y' or conf == 'Y'):
        return True
    elif(conf == 'n' or conf == 'N'):
        return False

        