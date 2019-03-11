Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> conn = pymysql.connect(host='localhost',user='root',password='root',db='movielist')
>>> a = conn.cursor()
>>> sql = 'SELECT * from `movie_rate`;'
>>> a.execute(sql)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.execute(sql)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\cursors.py", line 166, in execute
    result = self._query(query)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 856, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1057, in _read_query_result
    result.read()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1340, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1014, in _read_packet
    packet.check_error()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 393, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1146, "Table 'movielist.movie_rate' doesn't exist")
>>> print(sql)
SELECT * from `movie_rate`;
>>> a.execute(sql)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.execute(sql)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\cursors.py", line 166, in execute
    result = self._query(query)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 856, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1057, in _read_query_result
    result.read()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1340, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 1014, in _read_packet
    packet.check_error()
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\connections.py", line 393, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pymysql\err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1146, "Table 'movielist.movie_rate' doesn't exist")
>>> sql = 'SELECT * from `user_info`;'
>>> a.execute(sql)
3
>>> 
