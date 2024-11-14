import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def preprocess_text(filename):
    # Read the text file
    text = open(filename, encoding='utf-8').read()

    # Convert text to lowercase and remove punctuation
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # Tokenize text and filter out stop words
    tokenized_words = word_tokenize(cleaned_text, 'english')
    final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

    # Save the final words to a file for the next script to use
    with open('final_words.txt', 'w') as f:
        for word in final_words:
            f.write(f"{word}\n")


# Run preprocessing when this file is executed
preprocess_text('read.txt')
