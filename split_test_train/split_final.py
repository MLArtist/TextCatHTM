import random
import math
import sys
import operator
import csv

'''inputdata = 'input_data_refined.csv'
datatrain = 'train_set_raw.csv'
datatest = 'test_set.csv'
'''

inputdata = 'movie_reviews_refined.csv'
datatrain = 'train_set_raw_movie.csv'
datatest = 'test_set_movie.csv'

trfraction = 90
tsfraction = 10

data = [l for l in open(inputdata, 'r')]

trfile = open(datatrain, 'w')
tsfile = open(datatest, 'w')

data = data[0:len(data)]

num_of_data = len(data)
nt = int((trfraction/100.0)*num_of_data)
nts = int((tsfraction/100.0)*num_of_data)

data_fractions = [nt, nts]
split = [[],[],[]]

randint = 0

for split_ind, fraction in enumerate(data_fractions):
	for i in range(fraction):
		randint = random.randint(0, len(data)-1)
		split[split_ind].append(data[randint])
		data.pop(randint)

for l in split[0]:
	trfile.write(l)

for l in split[1]:
	tsfile.write(l)

trfile.close()
tsfile.close()


#data = csv.reader(open('train_set_raw.csv'), delimiter=',')
data = csv.reader(open('train_set_raw_movie.csv'), delimiter=',')
sortedlist = sorted(data, key = operator.itemgetter(0))
#with open('train_set_sorted.csv', 'wb') as f:
with open('train_set_sorted_movie.csv', 'w', newline="") as f:
	filewriter = csv.writer(f, delimiter = ',')
	for row in sortedlist:
		filewriter.writerow(row)
#splitting into training and testing set done

import csv
number_of_categories = 2
#with open('dataset_to_split.csv') as to_split_file:
#with open('train_set_sorted.csv') as to_split_file:  good one
with open('train_set_sorted_movie.csv') as to_split_file:
	split_file = csv.reader(to_split_file)
	a = [0] * 1 
	for row in split_file:
		try:
			a[int(row[0]) - 1] += 1
		except:
			for i in range(len(a), int(row[0])):
				a.append(0)
			a[int(row[0]) - 1] += 1
	flag_set_b = 1
	for i in range(0, len(a)):
		if a[i] != 0 and flag_set_b == 1:
			b = a[i]
			flag_set_b = 0
		else:
			if a[i] < b and a[i] != 0:
				b = a[i]		
	#b = min(a)
	#print ("b : ", b)
	#print (a)


#with open('train_set_sorted.csv') as to_split_file:
with open('train_set_sorted_movie.csv') as to_split_file:
	cat_list = []
	split_file = csv.reader(to_split_file)
	to_write = [0] * 2
	cnt = 1
	prev_cat_index = 1
	cat_cnt = 0 
	#with open('train_set.csv', 'wb') as after_splitting_file:
	with open('train_set_movie.csv', 'w', newline="") as after_splitting_file:
		after_splitting = csv.writer(after_splitting_file, delimiter = ',')
		
		for row in split_file:
			if row[0] == prev_cat_index and cnt <= b:
				try:
					cat_list[cat_cnt] = row[0]
				except:
					cat_list.append(row[0])
				to_write[0] = cat_cnt
				to_write[1] = row[1]
				after_splitting.writerow(to_write)
				prev_cat_index = row[0]
				cnt += 1
			elif row[0] != prev_cat_index and cnt <= b:
				cat_cnt += 1
				try:
					cat_list[cat_cnt] = row[0]
				except:
					cat_list.append(row[0])
				to_write[0] = cat_cnt
				to_write[1] = row[1]
				after_splitting.writerow(to_write)
				prev_cat_index = row[0]
				cnt = 1
			elif row[0] == prev_cat_index and cnt > b:
				cat_cnt += 1
				try:
					cat_list[cat_cnt] = row[0]
				except:
					cat_list.append(row[0])
				to_write[0] = cat_cnt
				to_write[1] = row[1]
				after_splitting.writerow(to_write)
				prev_cat_index = row[0]
				cnt = 1
			elif row[0] != prev_cat_index and cnt > b:
				cat_cnt += 1
				try:
					cat_list[cat_cnt] = row[0]
				except:
					cat_list.append(row[0])
				to_write[0] = cat_cnt
				to_write[1] = row[1]
				after_splitting.writerow(to_write)
				cnt = 1
				prev_cat_index = row[0]
				
print (cat_list)


