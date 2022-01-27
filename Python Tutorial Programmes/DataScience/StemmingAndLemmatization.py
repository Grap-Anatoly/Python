# In the areas of Natural Language Processing we come across situation where two or more words have a common root.
# For example, the three words - agreed, agreeing and agreeable have the same root word agree.
# A search involving any of these words should treat them as the same word which is the root word.
# So it becomes essential to link all the words into their root word.
# The NLTK library has methods to do this linking and give the output showing the root word.

import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#Next find the roots of the word
for w in nltk_tokens:
       print("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))