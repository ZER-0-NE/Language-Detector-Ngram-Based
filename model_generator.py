#coding:utf-8
import os
import glob
from collections import Counter 

try:
    from nltk.tokenize import RegexpTokenizer
    from nltk.util import ngrams
except ImportError:
    print('[!] nltk module missing. Please install it from http://nltk.org/index.html')
    sys.exit(-1)


Dataset_folder = "./LIGA_Dataset/"
Model_folder = "./Language_Models/"
Languages = {'German':'de_DE','English':'en_UK','Spanish':'es_ES','France':'fr_FR','Italian':'it_IT','Dutch':'nl_NL'}
Tokenizer = RegexpTokenizer("[a-zA-Z'`éèî]+") 

for lang in Languages:
	Fol_loc = Dataset_folder + Languages[lang]
	tweet_files = glob.glob(Fol_loc + '/*.txt')

	# Sentences extracted from the dataset
	sentences = []
	for tweet_file in tweet_files:
		sentences.append(open(tweet_file, mode='r').read())
	######################################

	# Tokens extracted from the sentences
	tokens = []
	for sentence in sentences:
		for token in Tokenizer.tokenize(sentence):
			tokens.append(token)
	###################################

	# Ngrams generated from the tokens from N=1 to 4
	Ngrams = []
	for token in tokens:
		for i in range(1,5):
			ingrams = ngrams(token, i, pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol=' ')
			for ingram in ingrams:
				ngram = ''.join(ingram)
				Ngrams.append(ngram)

	C = Counter(Ngrams)
	most_occur = C.most_common(300)
	# print(most_occur) 
	Save_loc = Model_folder + lang + ".txt"
	file = open(Save_loc, mode='w')
	for key,value in most_occur:
		file.write(key+' '+str(value)+'\n')

	file.close()

