import psycopg2

    
conn = psycopg2.connect("host=localhost dbname=Phones user=postgres password=1111")
cur = conn.cursor()


def query_data(value):
    cur.execute(f"SELECT * FROM users WHERE name LIKE '%{value}%' ")
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)
def query_phone(value):
    cur.execute(f"SELECT * FROM users WHERE phone LIKE '%{value}%' ")
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)

def ins_upd(name,phone,adress):
    cur.execute(f"SELECT * FROM users WHERE name = %s",(name,))
    rows = cur.fetchall()
    if len(rows)==0:
        cur.execute(f"INSERT INTO users(name,phone,adress) VALUES(%s,%s,%s) RETURNING user_id",(name,phone,adress))
        print("new row created")
        conn.commit()
    else :
        cur.execute("""UPDATE users SET phone=%s  WHERE name=%s RETURNING user_id""",(phone,name,))
        print("phone updated")
        conn.commit()    
def mult_ins(list):
    for i in list:
        if i[1].isdigit():
            cur.execute(f"INSERT INTO users(name,phone,adress) VALUES(%s,%s,%s) RETURNING user_id",(i[0],i[1],i[2],))
            print("new row created")
            conn.commit()
        else:return i[1]
def delet_name():
    name=input()
    cur.execute(f"DELETE FROM users WHERE name=%s",(name))
    print(" row deleted")
    conn.commit()
def delete_phone():
    phone=input()
    cur.execute(f"DELETE FROM users WHERE name=%s",(phone))
    print(" row deleted")
    conn.commit()
def task4():
    phone="87"
    cur.execute(f"SELECT * FROM users WHERE phone LIKE '{phone}%' LIMIT 4 OFFSET 1")
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)
    conn.commit()


nam=input()
pho=input()
adr=input()
list1=["Dimash","78997654321","asdiq 16"]
list2=["Solomon","79878976549","blanka 73"]
list3=["Erich","97984654132","post1"]
lists=[list1,list2,list3]
query_data(nam)
query_phone(pho)
ins_upd(nam,pho,adr)
mult_ins(lists)
delet_name()
delete_phone()
task4()