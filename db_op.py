import psycopg2
import base64
import hash
import pyperclip
from hash import gen_password, decrypt_rsa, encrypt_rsa, private_key_from_txt


def create_user(usr, pwd):
    salt = hash.create_salt()
    password = hash.hash_password(salt, pwd)

    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO logins (password, salt, username) VALUES (%s, %s, %s)"""
        record_to_insert = (password, salt, usr)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except(Exception, psycopg2.Error) as error:
        print(error)
        exit()


def login_user(usr, pwd):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT salt FROM logins WHERE username = '""" + usr + "'"
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        salt = result[0]

        postgres_select_query = """ SELECT password FROM logins WHERE username = '""" + usr + "'"
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        check = result[0]

        password = hash.hash_password(salt, pwd)

        if password == check:
            return 0
        else:
            return -1
    except(Exception, psycopg2.Error) as error:
        print(error)
        exit()


def connect():
    usr = 'postgres'
    pwd = 'admin'
    try:
        connection = psycopg2.connect(user=usr, password=pwd, host='127.0.0.1', database='pass_mgr')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)


def find_password(appname, usr):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """SELECT password FROM accounts WHERE appname = '""" + appname + """' AND username = '""" + usr + "'"
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()

        file = open("key_file.pem", "rb")
        priv_key = private_key_from_txt(file.read())
        print("started decoding")
        decoded_result = decrypt_rsa(priv_key, result[0])
        pyperclip.copy(decoded_result.decode())

        print('')
        print('Haslo skopiowane do schowka')
        print('')

    except (Exception, psycopg2.Error) as error:
        print(error)


def find_users(user_email, usr):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE user_email = '""" + user_email + "'" + """ AND username = '""" + usr + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row) - 1):
                print(data[i] + row[i])
        print('')
        print('-' * 30)
    except (Exception, psycopg2.Error) as error:
        print(error)


def store_password(password, user_email, url, appname, usr):
    try:

        file = open("key_file.pem", "rb")
        priv_key = private_key_from_txt(file.read())
        file.close()
        print("file closed")
        public_key = priv_key.publickey()
        print("public key created of type ", type(public_key))

        encrypted_password = encrypt_rsa(password, public_key)
        print("ENCRYPTED:", encrypted_password)

        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, user_email, username, url, appname) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (encrypted_password, user_email, usr, url, appname)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
