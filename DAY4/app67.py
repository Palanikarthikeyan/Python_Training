import sqlite3 
sqlite3.connect("prod.db")
'''
>>> import sqlite3
>>> sqlite3.connect("prod.db")
<sqlite3.Connection object at 0x00000174AE4DEC50>
>>>
>>> conn = sqlite3.connect("prod.db")
>>>
>>> conn.cursor()
<sqlite3.Cursor object at 0x00000174B057CD40>
>>>
>>> sth = conn.cursor()
>>>
>>>
>>> import sqlite3
>>> conn = sqlite3.connect("prod.db")
>>> sth = conn.cursor()
>>> sth.execute("create table products(pid INT,pname TEXT,pcost INT)")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> sth.execute("insert into products(pid,pname,pcost) values(101,'pA',1000)")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> sth.execute("insert into products(pid,pname,pcost) values(102,'pB',2000)")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> va = 103
>>> vb = 'pC'
>>> vc = 3000
>>>
>>> sth.execute("insert into products(pid,pname,pcost) values(?,?,?)",(va,vb,vc))
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> sth.execute("select *from products")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> sth.fetchone()
(101, 'pA', 1000)
>>>
>>> sth.fetchone()
(102, 'pB', 2000)
>>> sth.fetchone()
(103, 'pC', 3000)
>>> sth.fetchone()
>>>
>>> sth.execute("select *from products")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> sth.fetchall()
[(101, 'pA', 1000), (102, 'pB', 2000), (103, 'pC', 3000)]
>>>
>>> sth.fetchall()
[]
>>> sth.execute("select *from products")
<sqlite3.Cursor object at 0x00000174B057D140>
>>>
>>> list(sth) # generator
[(101, 'pA', 1000), (102, 'pB', 2000), (103, 'pC', 3000)]
>>> conn.commit()
>>>
>>> conn.close()
>>>
'''
