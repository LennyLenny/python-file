Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pymysql
>>> conn = pymysql.connect(host='localhost',user='root',password='root',db='movielist')
>>> a = conn.cursor()
>>> sql ='select * from `movie_rate`;'
>>> a.execute(sql)
3
>>> data_list = a.fetchall()
>>> data_arr = np.array(data_list)
>>> print(data_arr)
[[7 3 4 2 4 4 5 5 3 4 4 4 4 3 3 3 4 2 4 3 5 4 3 5 5 5 4 3 2 1 1 'user1']
 [9 None None None 0 3 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
  'temp']
 [8 2 2 5 4 3 3 2 1 1 4 3 2 2 3 4 3 4 3 3 3 3 2 3 2 2 4 5 5 5 4 'user2']]
>>> 

