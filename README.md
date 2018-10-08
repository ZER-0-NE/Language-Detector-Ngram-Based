# Language Detector NGram Based

#### DATASET : *LIGA_BENELEARN11_DATASET* http://www.win.tue.nl/~mpechen/projects/smm/
#### **PAPER REFERENCE** : *N-Gram-Based Text Categorization by William B. Cavnar and John M. Trenkle*

### MODULE REQUIRED:
nltk (natural language toolkit)

### HOW TO RUN:
- TO TRAIN LANGUAGE MODELS :
 ```sh
 python model_generator.py
 ```
- TO DETECT LANGUAGE OF DOCUMENT :
 ```sh
 python lang_detector.py <filename>.txt
 ```
 
#### HOW IT WORKS :
Using the famous dataset **LIGA_BENELEARN11_DATASET** which consists of tweets from six different languages,
the language models are prepared.

> **Language Model** : It consists of 500 most frequent ngrams (n=1 to n=5) in decreasing order of frequency for a particular language.

The document whose language is to be found is also parsed into ngrams and a document model is formed.

> **Document Model** : It consists of 500 most frequent ngrams (n=1 to n=5) in decreasing order of frequency for that document.

Next, the distances between the ngrams present in Document Model and in Language Models is calculated.

> ***Example*** : If **th** is present at index 4 of Document Model and is present at index 1 in English Language Model. Distance is **4-1>=3**. If **th** is not present in language model the distance is any maximum number (in my case i have taken 10000). In this way the cumulative distance is calculated.

The Language with minimum distace is the language of the document.
   
