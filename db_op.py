import psycopg2
import hash
import pyperclip

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
        pyperclip.copy(result[0])
        print('')
        print('Haslo skopiowane do schowka')
        print('')
    
    except (Exception, psycopg2.Error) as error:
        print(error)

<<<<<<< Updated upstream
def find_users(user_email, usr):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ') 
=======

def find_users(usr):
    data = ('Password: ', 'Email: ', 'url: ', 'App/Site name: ')
>>>>>>> Stashed changes
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT user_email, url, appname FROM accounts WHERE username = '""" + usr + "'"
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        print('-'*30)
        for row in result:
<<<<<<< Updated upstream
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('')
        print('-'*30)
=======
            print(data[0] + '************')
            for i in range(0, len(row)):
                print(data[i+1] + row[i])
            print('-'*30)
>>>>>>> Stashed changes
    except (Exception, psycopg2.Error) as error:
        print(error)

def store_password(password, user_email, url, appname, usr):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, user_email, username, url, appname) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, usr, url, appname)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)