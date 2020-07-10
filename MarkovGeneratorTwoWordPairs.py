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
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
pairs = make_pairs(corpus)

#Makes a dictionary of each word and each of the 2 words that ever follow that word in the text
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

#Make sure the first word of the generate text is the start of a sentence (Capitalized)
first_word = np.random.choice(corpus)
while first_word.islower():
    first_word = np.random.choice(corpus) #Just checks first words to get one thats uppercase

#Generates orginial text
chain = [first_word]
for i in range(number_words):
    #Each word is searched for in the dictionary and a random value entry is chosen, the cycle is then repeated number_words times.
    chain.append(np.random.choice(word_dict[chain[-1]]))

#Joins together word array and prints to console
finalString = " ".join(chain)
print(finalString)
