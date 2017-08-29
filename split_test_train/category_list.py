from __future__ import absolute_import, division, print_function, unicode_literals
import csv
from string import punctuation
from stop_words import get_stop_words


stop_words = get_stop_words('en')
#print(str(stop_words[1]))
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

#with open('category_list', 'wb') as category_list_file:
with open('category_list_movie', 'w', newline="") as category_list_file:
	category_list_file_to_write = csv.writer(category_list_file, delimiter = ',')
	list_category = [0] * 2
	#with open('input_data.csv') as test_data_csv_file:
	with open('movie_reviews.csv') as test_data_csv_file:
		#with open('input_data_refined.csv', 'wb') as test_data_refined_csv_file:
		with open('movie_reviews_refined.csv', 'w', newline="") as test_data_refined_csv_file:
			category_file = csv.reader(test_data_csv_file)
			count_category = 1
			a = dict()
			b = dict()
			write_file = csv.writer(test_data_refined_csv_file, delimiter=',')
			list_to_write = [0] * 2
			flag = 1
			for row in category_file:
				if flag == 1:
					flag = 0
					continue	
				if row[1] == 'NULL':
					continue
				if row[1].lower() == 'techm' or row[1].lower() == 'na' or row[1].lower() == 'as above' or row[1].lower() == 'test' or row[1].lower() == 'https' or row[1].lower() == 'main problem' or row[1] == 'N/A' or row[1] == '' or row[1].lower() == 'urgent' or row[1].lower() == 'attached' or row[1] == 'Address 1' or row[1] == 'attached error':
					continue
				if row[0] not in a.keys():
					b[row[0]] = 0
					a[row[0]] = count_category
					count_category += 1
					list_category[0] = row[0]
					list_category[1] = count_category - 1
					category_list_file_to_write.writerow(list_category)		
				b[row[0]] += 1
				list_to_write[0] = a[row[0]]
				str1 = ''
				after_punctuation = strip_punctuation(row[1])
				for something in after_punctuation.split():
					#print (something)
					flag_not_found = 1
					for stopword in stop_words:
						if something == str(stopword):
							flag_not_found = 0
							break
					if flag_not_found == 1:
						str1 += something + ' '

				list_to_write[1] = str1
								
				write_file.writerow(list_to_write)
				

#with open('category_count', 'wb') as category_count_file:
with open('category_counti_movie', 'w', newline="") as category_count_file:
	category_count_to_write = csv.writer(category_count_file, delimiter = ',')
	
	for keys in b.keys():
		list_category[0] = a[keys]
		list_category[1] = b[keys]
		category_count_to_write.writerow(list_category)



