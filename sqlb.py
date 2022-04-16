import sqlite3
import aiogram
import parsing

conn= sqlite3.connect('val.db',check_same_thread=False)
cursor =conn.cursor()


def create():
 name = parsing.lang()
 for i in range(len(name)):
  cursor.execute(f"ALTER TABLE info ADD '{name[i]}' INTEGER ")
  conn.commit()

def chest(message):
    user_id=message.from_user.id
    cursor.execute(f'SELECT id FROM info WHERE id={user_id}')
    react=cursor.fetchone()
    return react

def add_id(message):
    user_id = message.from_user.id
    cursor.execute(f"INSERT INTO info (id) VALUES ({user_id})")
    conn.commit()

def value(n,k,message):
 for i in range(len(n)):
       cursor.execute(f"UPDATE info SET '{n[i]}'={int(k[i])} WHERE id ={message}")
       conn.commit()

def inf(message):
    cursor.execute(f"SELECT * FROM info WHERE id={message}")
    react=cursor.fetchone()
    i=[]
    for n in range(1,len(react)):
        i.append(react[n])
    return i

def check(message):
    i=inf(message)
    while "NONE" in i:
        i.remove("NONE")
    print(i)
    return i





