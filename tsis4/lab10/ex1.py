import psycopg2
from config import params
import csv

a = int(input('1-Add     2-Delete     3-Update     4-Show     5-csv \n'))


def create_table():
    SQL = (
        '''
        CREATE TABLE IF NOT EXISTS book ( 
        Name VARCHAR(255) NOT NULL , 
        Telephone VARCHAR(12) NOT NULL
        ) 
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


create_table()


def add_user(name, telephone):
    SQL = "INSERT INTO book (Name, Telephone) VALUES ('" + name + "','" + telephone + "');"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def drop_by_name(name):
    SQL = "DELETE FROM book where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def drop_by_telephone(telephone):
    SQL = "DELETE FROM book where telephone = '" + telephone + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def update_by_name(name, telephone):
    SQL = "UPDATE book SET telephone = '" + telephone + "' WHERE name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def update_by_telephone(name, telephone):
    SQL = "UPDATE book SET name = '" + name + "' WHERE telephone = '" + telephone + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def show_sort_by_name():
    SQL = "SELECT * FROM book order by name ASC"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        text = "Name                     Telephone"
        print("\033[36m {}".format(text))
        print("\033[0m", end='')

        for row in res:
            l = len(row[0])
            print(str(row[0]), end="")
            for i in range(24 - l):
                print(' ', end="")
            print(' ', end="")
            print(str(row[1]))


    except Exception as Error:
        print(str(Error))


def show_sort_by_telephone():
    SQL = "SELECT * FROM book order by telephone ASC"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        text = "Name                     Telephone"
        print("\033[36m {}".format(text))
        print("\033[0m", end='')

        for row in res:
            l = len(row[0])
            print(str(row[0]), end="")
            for i in range(25 - l):
                print(' ', end="")
            print(str(row[1]))


    except Exception as Error:
        print(str(Error))


def show_sort_by_date():
    SQL = "SELECT * FROM book"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        text = "Name                     Telephone"
        print("\033[36m {}".format(text))
        print("\033[0m", end='')

        for row in res:
            l = len(row[0])
            print(str(row[0]), end="")
            for i in range(25 - l):
                print(' ', end="")
            print(str(row[1]))


    except Exception as Error:
        print(str(Error))


if a == 1:
    name = input('Write your name:   ')
    telephone = input('Write your telephone number:   ')
    add_user(name, telephone)

if a == 2:
    b = int(input('1-Delete by name     2-Delete by telephone \n'))
    if b == 1:
        name = input('Write your name:     ')

        drop_by_name(name)
    if b == 2:
        telephone = input('Write your telephone number:     ')

        drop_by_telephone(telephone)

if a == 3:
    b = int(input('1-Update by name     2-Update by telephone \n'))
    if b == 1:
        name = input('Write your name:     ')
        telephone = input('Write your new telephone number:     ')
        update_by_name(name, telephone)
    if b == 2:
        telephone = input('Write your telephone number: ')
        name = input('Write your new name:     ')
        update_by_telephone(name, telephone)

if a == 4:
    b = int(input('1-Sort by name     2-Sort by telephone     3-Sort by date\n'))
    if b == 1:
        show_sort_by_name()
    if b == 2:
        show_sort_by_telephone()
    if b == 3:
        show_sort_by_date()

if a == 5:
    with open('phones.csv') as f:
        r = csv.reader(f)
        for i in r:
            name = str(i[0])
            telephone = str(i[1])
            add_user(name, telephone)