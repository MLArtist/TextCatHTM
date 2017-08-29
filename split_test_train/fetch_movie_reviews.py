import nltk
from nltk.corpus import movie_reviews as reviews

import csv
X = [reviews.raw(fileid) for fileid in reviews.fileids()]   
Y = [reviews.categories(fileid) for fileid in reviews.fileids()]
with open('movie_reviews.csv', 'w', newline="") as moview_reviews:
	filewriter = csv.writer(moview_reviews, delimiter=',')
	a = [0] * 2
	for i in range(len(X)):
		a[0] = Y[i]
		a[1] = X[i]
		filewriter.writerow(a)

