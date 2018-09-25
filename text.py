from nltk.util import ngrams

text = 'Hello'

ngr = ngrams(text,2)
for n in ngr:
	ngram=''.join(n)
	print(ngram)