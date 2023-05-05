import csv

import psycopg2
import pandas as pd
import re
from io import StringIO

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = ""

conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
        )

cur = conn.cursor()

def is_phone_exists(phone):
    cur.execute("""SELECT EXISTS(SELECT 1 FROM public.phonebook WHERE phone = %s);""", [phone])
    return cur.fetchone()[0]

def main():

    print("Select task:")
    print("1. Design tables for PhoneBook.")
    print("2. Implement two ways of inserting data into the PhoneBook.\n        1) upload data from csv file\n      "
          "2) entering user name, phone from console")
    print("3. Implement updating data in the table (change user first name or phone)")
    print("4. Querying data from the tables (with different filters)")
    print("5. Implement deleting data from tables by username of phone")
    option = input("Option: ")

    if option == "1":
        cur.execute("""CREATE TABLE IF NOT EXISTS
                    public.phonebook(
                                phone bigint,
                                username varchar(50)
                            );
                    """)
        conn.commit()

        print("Table \"Phonebook\" was created")

    elif option == "2":
        print("Please, select way:")
        print("1. Upload data from csv file")
        print("2. Entering user name, phone from console")
        way = input("Way: ")

        if way == "1":
            path = input("Path to csv: ")

            with open(path, "r") as f:
                reader = csv.reader(f)
                next(reader)
                rows_to_insert = []
                existing_phones = set()
                for row in reader:
                    phone, username = row
                    if not is_phone_exists(phone):
                        rows_to_insert.append((phone, username))
                    else:
                        existing_phones.add(phone)

                csv_data = StringIO()
                csv_writer = csv.writer(csv_data)
                csv_writer.writerows(rows_to_insert)
                csv_data.seek(0)

                cur.copy_from(csv_data, 'phonebook', sep=',', columns=('phone', 'username'))

            conn.commit()
        elif way == "2":
            username, phone = input("Username: "), int(input("Phone: "))

            if is_phone_exists(phone):
                cur.execute("""UPDATE public.phonebook SET username=%s WHERE phone=%s;""", [username, phone])
                print("%i number owner is updated" % phone)

            else:
                cur.execute("""INSERT INTO public.phonebook VALUES(%s, %s);""", [phone, username])
                print("%s inserted to table" % username)

            conn.commit()

    elif option == "3":
        cur.execute("""SELECT * FROM public.phonebook;""")
        records = cur.fetchall()
        print("Select phone for update: ")
        for record in records:
            phone = record[0]
            username = record[1]
            print("%s - %i" % (username, phone))

        phone = int(input("Phone: "))
        new_phone = int(input("New phone: "))
        new_username = input("New username: ")

        cur.execute("""UPDATE public.phonebook SET phone = %s, username = %s WHERE phone = %s""", [new_phone, new_username, phone])
        conn.commit()

    elif option == "4":
        t = input("""1 - get all
        2 - get by name
        3 - get by phone number
        4 - sort by name
        5 - sort by phone number\n""")

        if t == "1":
            cur.execute("SELECT * FROM public.phonebook")
        elif t == "2":
            name = input("Name: ")
            cur.execute(f"SELECT * FROM public.phonebook WHERE username='{name}'")
        elif t == "3":
            num = input("Phone number: ")
            cur.execute(f"SELECT * FROM public.phonebook where phone='{num}'")
        elif t == "4":
            cur.execute("SELECT * FROM public.phonebook BY ORDER BY username ASC")
        elif t == "5":
            cur.execute("SELECT * FROM public.phonebook BY ORDER BY phone ASC")
        records = cur.fetchall()
        for record in records:
            phone = record[0]
            username = record[1]
            print("%s - %i" % (username, phone))



    elif option == "5":
        cur.execute("""SELECT * FROM public.phonebook;""")
        records = cur.fetchall()
        for record in records:
            phone = record[0]
            username = record[1]
            print("%s - %i" % (username, phone))
        cin = input("Select the user or phone to delete: ")

        if re.match(r"^\d{11}$", cin):
            cur.execute("""DELETE FROM public.phonebook WHERE phone=%s;""", [int(cin)])
            print("Phone %s is deleted" % cin)
        else:
            cur.execute("""DELETE FROM public.phonebook WHERE username=%s;""", [cin])
            print("User %s is deleted" % cin)

        conn.commit()

    cur.close()
    conn.close()


main()
