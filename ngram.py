# let q be the number of n grams in a sentence containing x words, then
# q = x - (n - 1)

# from nltk.tokenize import word_tokenize

# text = "I am aware that nltk only offers bigrams and trigrams, but is there a way to split my text in four-grams, five-grams or even hundred-grams"
# tokenize = word_tokenize(text)
# print(tokenize[2])

# # ['I', 'am', 'aware', 'that', 'nltk', 'only', 'offers', 'bigrams', 'and', 'trigrams', ',', 'but', 'is', 'there', 'a', 'way', 'to', 'split', 'my', 'text', 'in', 'four-grams', ',', 'five-grams', 'or', 'even', 'hundred-grams']
# # >>> bigrams = ngrams(tokenize,2)
# # >>> bigrams
# # [('I', 'am'), ('am', 'aware'), ('aware', 'that'), ('that', 'nltk'), ('nltk', 'only'), ('only', 'offers'), ('offers', 'bigrams'), ('bigrams', 'and'), ('and', 'trigrams'), ('trigrams', ','), (',', 'but'), ('but', 'is'), ('is', 'there'), ('there', 'a'), ('a', 'way'), ('way', 'to'), ('to', 'split'), ('split', 'my'), ('my', 'text'), ('text', 'in'), ('in', 'four-grams'), ('four-grams', ','), (',', 'five-grams'), ('five-grams', 'or'), ('or', 'even'), ('even', 'hundred-grams')]
# # >>> trigrams=ngrams(tokenize,3)
# # >>> trigrams
# # [('I', 'am', 'aware'), ('am', 'aware', 'that'), ('aware', 'that', 'nltk'), ('that', 'nltk', 'only'), ('nltk', 'only', 'offers'), ('only', 'offers', 'bigrams'), ('offers', 'bigrams', 'and'), ('bigrams', 'and', 'trigrams'), ('and', 'trigrams', ','), ('trigrams', ',', 'but'), (',', 'but', 'is'), ('but', 'is', 'there'), ('is', 'there', 'a'), ('there', 'a', 'way'), ('a', 'way', 'to'), ('way', 'to', 'split'), ('to', 'split', 'my'), ('split', 'my', 'text'), ('my', 'text', 'in'), ('text', 'in', 'four-grams'), ('in', 'four-grams', ','), ('four-grams', ',', 'five-grams'), (',', 'five-grams', 'or'), ('five-grams', 'or', 'even'), ('or', 'even', 'hundred-grams')]
# # >>> fourgrams=ngrams(tokenize,4)
# # >>> fourgrams
# # [('I', 'am', 'aware', 'that'), ('am', 'aware', 'that', 'nltk'), ('aware', 'that', 'nltk', 'only'), ('that', 'nltk', 'only', 'offers'), ('nltk', 'only', 'offers', 'bigrams'), ('only', 'offers', 'bigrams', 'and'), ('offers', 'bigrams', 'and', 'trigrams'), ('bigrams', 'and', 'trigrams', ','), ('and', 'trigrams', ',', 'but'), ('trigrams', ',', 'but', 'is'), (',', 'but', 'is', 'there'), ('but', 'is', 'there', 'a'), ('is', 'there', 'a', 'way'), ('there', 'a', 'way', 'to'), ('a', 'way', 'to', 'split'), ('way', 'to', 'split', 'my'), ('to', 'split', 'my', 'text'), ('split', 'my', 'text', 'in'), ('my', 'text', 'in', 'four-grams'), ('text', 'in', 'four-grams', ','), ('in', 'four-grams', ',', 'five-grams'), ('four-grams', ',', 'five-grams', 'or'), (',', 'five-grams', 'or', 'even'), ('five-grams', 'or', 'even', 'hundred-grams')]
import nltk
