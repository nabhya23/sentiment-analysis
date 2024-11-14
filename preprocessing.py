import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def preprocess_text(filename):
    # Read the text file
    text = open(filename, encoding='utf-8').read()

    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    tokenized_words = word_tokenize(cleaned_text, 'english')
    final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

    
    with open('final_words.txt', 'w') as f:
        for word in final_words:
            f.write(f"{word}\n")



preprocess_text('read.txt')
