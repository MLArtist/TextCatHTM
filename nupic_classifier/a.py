from __future__ import (absolute_import, division,print_function, unicode_literals)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora
from collections import defaultdict
from pprint import pprint  # pretty-printer

from stop_words import get_stop_words

stop_words = get_stop_words('en')

print ("stop_words : ", stop_words)
stoplist = set(str(stop_words[0]))

for i in range(len(stop_words)):
	stoplist.add(str(stop_words[i]))
print (stoplist)
'''
Creates MM corpus
'''
class MyCorpus(object):
    def __iter__(self):
        for line in open('movie_reviews_refined.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())


from six import iteritems

# collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for line in open('movie_reviews_refined.txt'))

# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist 
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]

# remove stop words and words that appear only once
dictionary.filter_tokens(stop_ids + once_ids)

# remove gaps in id sequence after words that were removed
dictionary.compactify()
dictionary.save_as_text('word_ids_dict.txt')  # store the dictionary, for future reference
print(dictionary)

corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
print(corpus_memory_friendly)

corpora.MmCorpus.serialize('corpus_memory_friendly.mm', corpus_memory_friendly)

for vector in corpus_memory_friendly:  # load one vector into memory at a time
    print(vector)

