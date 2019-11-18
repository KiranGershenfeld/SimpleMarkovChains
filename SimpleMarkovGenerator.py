import numpy as np
import os
# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
storyContent = open('C:/code/markov/sampletextdump.txt', encoding='utf8').read()

corpus = storyContent.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)

while first_word.islower():
    first_word = np.random.choice(corpus) #Just checks first words to get one thats uppercase

chain = [first_word]

n_words = 50

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

' '.join(chain)

finalString = ""
for element in chain:
    finalString += (" " + element)

text_file = open("GeneratedChain.txt", "w")
text_file.write(finalString)
text_file.close()
os.startfile("GeneratedChain.txt")
