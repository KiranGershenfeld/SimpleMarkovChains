#text = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c x x x"
import numpy as np
import random
import os
text =  open('C:/code/markov/sampletextdump.txt', encoding='utf8').read()
corpus = text.split()
def make_pairs(corpus):
    for i in range(len(corpus) - 3):
        yield (corpus[i], corpus[i+1], corpus[i+2], corpus[i+3])
pairs = make_pairs(corpus)

word_dict = {}
for word_1, word_2, word_3, word_4 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append([word_2, word_3, word_4])
    else:
        word_dict[word_1] = [[word_2, word_3, word_4]]

first_word = np.random.choice(corpus)
while first_word.islower():
    first_word = np.random.choice(corpus) #Just checks first words to get one thats uppercase


n_words = 100
chain = []
print(first_word)
chain.append(first_word)
for i in range(n_words):
    seed = chain[-1]
    #print(seed)
    #print(word_dict[seed])
    #print(i)
    randomValue = random.randrange(0, len(word_dict[seed]), 1)
    choice = word_dict[seed][randomValue]
    for element in choice:
        chain.append(element)
print(chain)

text_file = open("GeneratedChain3.txt", "w")
text_file.write(' '.join(chain))
text_file.close()
os.startfile("GeneratedChain3.txt")

#print(' '.join(corpus))
