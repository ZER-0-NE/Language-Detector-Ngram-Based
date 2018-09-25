#coding:utf-8

try:
    from nltk.tokenize import RegexpTokenizer
    from nltk.util import ngrams
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'
    sys.exit(-1)