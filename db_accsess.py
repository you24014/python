import mysql.connector

# conn = mysql.connector.connect(user='root', password='mypassword', host='localhost', database='test1')
config = {
    'user': 'root',
    'password': 'mypassword',
    'host': 'localhost',
    'database' : 'test1',
}

conn = mysql.connector.connect(**config)

cur = conn.cursor()

sql = 'insert into test1 values(%s,%s)'
datas = [
    (3,'sanban'),
    (4,'piyo')
]

cur.executemany(sql,datas)
conn.commit()

sql = 'select * from test1'
cur.execute(sql)
for row in cur.fetchall():
    print(row[0],row[1])

cur.close
conn.close