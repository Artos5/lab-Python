

import nltk

import string

import numpy as np

import matplotlib.pyplot as plt

from nltk.corpus import stopwords

nltk.download('punkt_tab')

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')


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

from collections import Counter #словник, який дозволяє рахувати кількість незмінюваних об'єктів (напр. рядки)

try:

    File = open('milton-paradise.txt', 'r', encoding='utf-8')
    print("Open ok")

except FileNotFoundError:

    print("Файл не знайдено!")

    exit(0)

text = File.read()
File.close()  # Закриваємо файл після читання
print("Кількість слів у тексті:", count_words(text))
most_used_words(text)

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
words = nltk.word_tokenize(text)
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]

print("Кількість слів після видалення стоп-слів та пунктуації:", len(filtered_words))
most_used_words(' '.join(filtered_words))


