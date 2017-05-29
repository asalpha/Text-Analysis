


# write_file = open('test' + '.csv', 'w', newline='')
# 	csv_write = csv.writer(write_file)
import nltk
import csv
import numpy
from itertools import zip_longest

l = [[1,2,3,4,5],[6,7,8,9],[11,23,34]]

def transposed2(lists, defval=0):
   return list(zip_longest(*lists))


def a():
	write_file = open('twqest' + '.csv', 'w', newline='')
	csv_write = csv.writer(write_file)
	for r in l:
		csv_write.writerow(r)

# for x in transposed2(l):
# 	print (x)
# print(np.matrix(l))

# print(l[2][1])
# print('---------')
# k = list(transposed2(l))
# print(k[0])
# print(k[1])
# print(k[2])
# print(k[3])
# print(k[4])

# print(np.matrix(k))