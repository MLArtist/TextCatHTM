import collections
import gensim
import numpy
import operator
import logging
import bz2

from htmresearch.encoders.language_encoder import LanguageEncoder

TARGET_SPARSITY = 1.0
exclusions = ('!', '.', ':', ',', '"', '\'', '\n', '?')

class LSAEncoder(LanguageEncoder):
  """
  A language encoder using LSA model.

  The associated script must be used to generate the tf-idf and LSA models that
  are used by the encoder. The encoder takes arbitrary text, converts it to the
  topic space via the models, and then creates an SDR. The SDR has a bit for
  each topic. The top `w` topics are set to 1.
  """

  def __init__(self):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)
    self.id2word = gensim.corpora.Dictionary.load_from_text('./word_ids_dict.txt')
    mm = gensim.corpora.MmCorpus('./corpus_memory_friendly.mm')
#    print mm   
    self.lsa = gensim.models.lsimodel.LsiModel(corpus = mm, id2word=self.id2word, num_topics = 5000, onepass=False, power_iters=1, extra_samples=100, chunksize=500, decay=1.0)
    self.tfidf = gensim.models.tfidfmodel.TfidfModel(mm)
    self.tfidf.save('tfidf_model')
    self.lsa.save('model')
#    self.tfidf = gensim.models.tfidfmodel.TfidfModel.load('tfidf_model')
#    self.lsa = gensim.models.lsimodel.LsiModel.load('model', mmap='r')
    self.n = self.lsa.num_topics
    print "n : ", self.n
    self.w = int(float(self.n) * 0.1)
    print "w :  ", self.w
    self.description = ("LSA Encoder", 0)
#    print self.lsa.print_topics(num_topics = -1)    

  def _tokenize(self, text):
    """Tokenize the text string into a list of strings."""
    text = "".join([c for c in text if c not in exclusions])
    return text.split(" ")


  def encode(self, text):
    """
    Encodes the input text into an SDR.

    @param  text    (str, list)       If the input is type str, the encoder
                                      assumes it has not yet been tokenized. A
                                      list input will skip the tokenization
                                      step.
    @return         (list)            SDR.

    TODO: test tokenization logic for str and list inputs
    """
    if isinstance(text, str):
      text = self._tokenize(text)

    for i in range(len(text)):
	text[i] = text[i].lower()

    bow = self.id2word.doc2bow(text)
    tfidf = self.tfidf[bow]
    weights = self.lsa[tfidf]
    #print "weights : ", weights
    topWeights = sorted(weights, key=operator.itemgetter(1))[-self.w:]
    activeIndices = [pair[0] for pair in topWeights]
    print len(activeIndices)
    encoded = numpy.zeros([self.n], dtype=numpy.bool)
    encoded[activeIndices] = 1
    print 
    return encoded


  def encodeIntoArray(self, inputText, output):
    """See method description in language_encoder.py."""
    if not isinstance(inputText, str):
      raise TypeError("Expected a string input but got input of type {}."
                      .format(type(inputText)))

    ## TODO
    pass


  def decode(self, encoding, numTerms=None):
    """Converts an SDR back into the most likely word or words.

    By default, the most likely term will be returned. If numTerms is
    specified then it determines how many terms will be returned and the
    return value will be a sequence of (term, weight) tuples where the
    higher the weight, the more the term matches the encoding.
    """
    potentialTerms = collections.defaultdict(float)
    for topicNum in xrange(self.lsa.num_topics):
      if encoding[topicNum] == 1:
        for weight, term in self.lsa.show_topic(topicNum):
	  #print "weight : ", weight
	  #print "term : ", term
          #potentialTerms[term] += float(weight.replace(u'\N{MINUS SIGN}', '-'))
          potentialTerms[weight] += term 

    # Temporary variable for how many terms to get
    n = numTerms if numTerms is not None else 1
    topTerms = sorted(potentialTerms.items(),
                      key=operator.itemgetter(1),
                      reverse=True)[:n]
    # If numTerms is not specified, return just the most likely term, otherwise
    # return the top numTerms terms with weights.
    if numTerms is None:
      return topTerms[0][0]
    else:
      return topTerms


  def getWidth(self):
    return self.n


  def getDescription(self):
    return self.description
