# Word tokenization is the process of splitting a large sample of text into words.
# This is a requirement in natural language processing tasks where each word needs to be captured and
# subjected to further analysis like classifying and counting them for a particular sentiment etc.

# The Natural Language Tool kit(NLTK) is a library used to achieve this.
import nltk

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)

# We can also tokenize the sentences in a paragraph like we tokenized the words.
# We use the method sent_tokenize to achieve this. Below is an example.

sentence_data = "Sun rises in the east. Sun sets in the west."
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)