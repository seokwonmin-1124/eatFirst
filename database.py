import sqlite3
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

conn = sqlite3.connect('wsdb.db')

cur = conn.cursor()

# 테이블 생성
cur.execute("""CREATE TABLE IF NOT EXISTS woosun(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    schNum TEXT,
    name TEXT,
    reason TEXT,
    Tel TEXT,
    date TEXT
    )""")

dataList = list(tuple())
dataList.append(('20612', '이름', '교내 스포츠클럽', '01038132720', str(nowDate)))

cur.executemany('INSERT INTO woosun (schNum, name, reason, Tel, date) VALUES (?, ?, ?, ?, ?)', dataList)
conn.commit()

conn.close()