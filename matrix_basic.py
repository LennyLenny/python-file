#coding=utf-8
import numpy
import scipy

data = numpy.matrix([[1, 2, 4],[3, 4, 9]])
print(data)
print(data.shape[1])	#获取矩阵格式
print(data.shape)



print("-----")

random_matrix = numpy.random.randint(10 , size = (10,5))		#获取随机矩阵

print(random_matrix)

col = random_matrix[:,0:1]    #获取一列

row = random_matrix[0:1,:]		#获取一行

part_of_col = numpy.array([[1,2,3]])	#获取某一部分
print(random_matrix[[0],part_of_col])

print("-----")

flattened = random_matrix.flatten()		#水平打印



random_matrix_2 = numpy.random.randint(10 , size = (5,2))
random_matrix.dot(random_matrix_2)

a = numpy.array([1,2,3,4,5,6,7,8,9])
print(a.std()) # 结果 1.70782512766



