#coding:utf-8


import os,glob
from collections import Counter 

try:
    from nltk.tokenize import RegexpTokenizer
    from nltk.util import ngrams
except ImportError:
    print('[!] nltk module missing. Please install it from http://nltk.org/index.html')
    sys.exit(-1)


class Model_Generator:
	'''
	Class is used to generate Languages Models 
	by extracting the Ngrams
	'''
	def __init__(self):
		self._Dataset_folder = "./LIGA_Dataset/"
		self._Model_folder = "./Language_Models/"
		self._Languages = {'German':'de_DE','English':'en_UK','Spanish':'es_ES','French':'fr_FR','Italian':'it_IT','Dutch':'nl_NL'}
		self._Tokenizer = RegexpTokenizer("[a-zA-Z'`éèî]+") 

	def generator(self):
		for lang in self._Languages:
			Fol_loc = self._Dataset_folder + self._Languages[lang]
			tweet_files = glob.glob(Fol_loc + '/*.txt')

			# Sentences extracted from the dataset
			sentences = []
			for tweet_file in tweet_files:
				sentences.append(open(tweet_file, mode='r').read())
			######################################

			# Tokens extracted from the sentences
			tokens = []
			for sentence in sentences:
				for token in self._Tokenizer.tokenize(sentence):
					tokens.append(token)
			###################################

			# Ngrams generated from the tokens from N=1 to 5
			Ngrams = []
			for token in tokens:
				for i in range(1,6):
					ingrams = ngrams(token, i, pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol=' ')
					for ingram in ingrams:
						ngram = ''.join(ingram)
						Ngrams.append(ngram)

			C = Counter(Ngrams)
			most_occur = C.most_common(1000)
			# print(most_occur) 
			Save_loc = self._Model_folder + lang + ".txt"
			file = open(Save_loc, mode='w')
			for key,value in most_occur:
				file.write(key+',')

			file.close()


if __name__ == '__main__':
	obj=Model_Generator()
	obj.generator()