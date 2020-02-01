import sqlite3
from datetime import datetime as dt

ntime = dt.now().strftime("%Y-%m-%d %H:%M:%S")


def add_balance(updated):
    with open("balance.txt", "r+") as file:
        bal = file.read()
        bal = float(bal) + float(updated)
        print(bal)
        file.truncate(0)
        file.seek(0)
        file.write(str(bal))

def deduct_balance(updated):
    with open("balance.txt", "r+") as file:
        bal = file.read()
        bal = float(bal) - float(updated)
        print(bal)
        file.truncate(0)
        file.seek(0)
        file.write(str(bal))

def connect():
    conn=sqlite3.connect("transactions")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, money text, date text, msg text)")
    conn.commit()
    conn.close()

def add(money, ntime, msg):
    conn = sqlite3.connect("transactions")
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions(money, date, msg) VALUES (?,?,?)", (money , ntime, msg))
    conn.commit()
    conn.close()


def withdraw(money, ntime, msg):
    conn = sqlite3.connect("transactions")
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions(money, date, msg) VALUES (?,?,?)", (money , ntime, msg))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("transactions")
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete():
    conn = sqlite3.connect("transactions")
    cur = conn.cursor()
    cur.execute("DROP TABLE transactions")
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, money text, date text, msg text)")
    conn.commit()
    conn.close()


connect()
#add(1000,ntime,'hi')
#print(view())





