import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string

import string

import numpy as np

import matplotlib.pyplot as plt
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def count_words(text):

    sentences = nltk.sent_tokenize(text) #токенізація по реченням
    print("count_words ok")

    k_words = 0

    for sentence in sentences:

        words = nltk.word_tokenize(sentence)

        #words - список зі словами

        k_words += len(words)

    return k_words

def most_used_words(text):

    text1 = text.split() #cписок зі словами
    print("most_used_words ok")

    cnt = Counter(text1) #підрахунок слів

    cort = cnt.most_common(10)

    x = [cort[el][0] for el in range(len(cort))] #слова

    y = [cort[el][1] for el in range(len(cort))] #к-ть повторень у тексті

    plt.bar(x, y)

    plt.title("10 найбільш вживаних слів у тексті")

    plt.xlabel("Слова") #підписи по осям

    plt.ylabel("Зустрічаються разів у тексті")

    plt.show()

# Зберегти текст у файл
original_text = """Here you can insert your text. Make sure it's up to 100 words long."""
with open('original_text.txt', 'w', encoding='utf-8') as file:
    file.write(original_text)

# Завантаження тексту з файлу
with open('original_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
count_words(text)
most_used_words(text)

# Токенізація по словам
words = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in lemmatized_words]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in stemmed_words if word.lower() not in stop_words]

# Видалення пунктуації
filtered_words = [word for word in filtered_words if word.isalpha()]

# Запис обробленого тексту у інший файл
processed_text = ' '.join(filtered_words)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)
    
count_words(processed_text)
most_used_words(processed_text)
print("Оброблений текст збережено у файл 'processed_text.txt'.")
