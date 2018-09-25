#coding:utf-8

import sys,operator,os,glob
from collections import Counter 

try:
    from nltk.tokenize import RegexpTokenizer, sent_tokenize
    from nltk.util import ngrams
except ImportError:
    print('[!] nltk module missing. Please install it from http://nltk.org/index.html')
    sys.exit(-1)


class Language_Detector:
	'''
	Class is used to generate Document Model
	and compare with the Language models to predict the language
	using the 
	'''
	def __init__(self):
		self._Model_folder = "./Language_Models/"
		self._Languages = {'German':'de_DE','English':'en_UK','Spanish':'es_ES','French':'fr_FR','Italian':'it_IT','Dutch':'nl_NL'}
		self._Tokenizer = RegexpTokenizer("[a-zA-Z'`éèî]+") 
		self._Language_models = {}
		self._Language_distances = {}

	def load_models(self):

		for lang in self._Languages:
			model_loc = self._Model_folder + lang + ".txt"
			file = open(model_loc, mode='r')
			Ngrams = file.read().split(',')
			self._Language_models[lang]=Ngrams
			file.close()


	def distance_calculator(self,most_frequent):

		self.load_models()
		for lang in self._Languages:
			dist = 0
			maxi = 10000
			for i,Ngram in enumerate(most_frequent):
				model = self._Language_models[lang]
				if Ngram in model:
					dist = dist + abs(i-model.index(Ngram))
				else:
					dist = dist + maxi
			self._Language_distances[lang] = dist

	def language_detector(self,document):

		sentences = sent_tokenize(document)
		tokens = []
		for sentence in sentences:
			for token in self._Tokenizer.tokenize(sentence):
				tokens.append(token.lower())

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

		most_frequent = []
		for key,value in most_occur:
			most_frequent.append(key)

		self.distance_calculator(most_frequent)
		print(self._Language_distances)
		sorted_distances = sorted(self._Language_distances.items(), key=operator.itemgetter(1))
		print("The Language of the Document is " + str(sorted_distances[0][0]))


if __name__ == '__main__':
	obj = Language_Detector()
	inputfile = sys.argv[1]
	document = open(inputfile,mode='r').read()
	obj.language_detector(document)