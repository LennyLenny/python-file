#coding=utf-8
import numpy
import scipy

num_moives = 10
num_users = 5

ratings = numpy.random.randint(11, size = (num_moives,num_users))	#建立一个随机矩阵，将用户数量，电影数量和评分放在一起
print(ratings)

did_rate = (ratings !=0) * 1	#评分为0表示没有看过电影
print(did_rate)					#did_rate的目的是建立一个矩阵，用1和0将看过和没看过电影的人标识出来


#normalize操作：可以看得出数据之间的关系，和永远为0


def normalize_ratings(ratings, did_rate):
	num_moives = ratings.shape[0]

	ratings_mean = numpy.zeros(shape = (num_moives, 1))
	ratings_norm = numpy.zeros(shape = ratings.shape)

	for i in range(num_moives):
		#获取所有评分过的数的值

		idx = numpy.where(did_rate[i] == 1)[0]
		#计算平均数
		ratings_mean[i] = numpy.mean(ratings[i, idx])
		ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
		
	return ratings_norm, ratings_mean


ratings, ratings_mean = normalize_ratings(ratings, did_rate)
print(ratings)
print(ratings_mean)

num_users = ratings.shape[1]
num_features = 3





