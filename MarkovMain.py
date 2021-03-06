import numpy as np
import random
import os

#PRESS RUN TO GENERATE ORIGINAL TEXT TRAINED ON SHAKESPEARE'S WRITING OR
#PLACE CUSTOM TRAINING TEXT IN TrainingText.txt IT SHOULD BE 500+ WORDS FOR BEST RESULT

number_words = 100 #<-- Number of words in the generated text, feel free to change

#Gets training text from file
fileName = "TrainingText.txt"
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
text = open(os.path.join(__location__, fileName), encoding='utf8').read()

#Splits training text into list
corpus = text.split()

#Makes touple pairs of each word with the 2 words that follow it
def make_pairs(corpus):
    for i in range(len(corpus) - 2):
        yield (corpus[i], corpus[i+1], corpus[i+2])
pairs = make_pairs(corpus)

#Makes a dictionary of each word and each of the 2 words that ever follow that word in the text
word_dict = {}
for word_1, word_2, word_3 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append([word_2, word_3])
    else:
        word_dict[word_1] = [[word_2, word_3]]

#Make sure the first word of the generate text is the start of a sentence (Capitalized)
first_word = np.random.choice(corpus)
while first_word.islower():
    first_word = np.random.choice(corpus)

#Generates orginial text
chain = []
chain.append(first_word)
for i in range(number_words):
    seed = chain[-1]
    #Each word is searched for in the dictionary and a random value entry is chosen, the cycle is then repeated number_words times.
    randomValue = random.randrange(0, len(word_dict[seed]), 1)
    choice = word_dict[seed][randomValue]
    for element in choice:
        chain.append(element)

#Joins together word array and prints to console
finalString = " ".join(chain)
print(finalString)
