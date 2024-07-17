# import gensim
from gensim.models import KeyedVectors

LOCATION = 'GoogleNews-vectors-negative300.bin'
wv = KeyedVectors.load_word2vec_format(LOCATION, binary=True, limit=1_000_000)
wv.save_word2vec_format('vectors.csv')
