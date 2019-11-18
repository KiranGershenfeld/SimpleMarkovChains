# SimpleMarkovChains
This project uses markovs chains to immitate any set of text that it is given

Markov Chains are a type of algorithm that examines each word of a text file and the probability of the words that come after it. Doing this for every word, it is able to predict which words will come after each other and create entirely new strings of text. 

In this project there are several implementations of Markov Chains. Here is an overview of files in this project:
1. 'SimpleMarkovGenerator' uses the basic markov implementation of checking the probability of what word should come after any given word and then randomly picking a word based on that probability. It then repeats this process with the new word.
2. 'ThreeWordGenerator' Uses the same strategy but after it picks a word, it also adds on the word that comes after that word in the source text. It then randomly picks a new word based on the last word in the generated string.
3. 'FourWordGenerator' Picks a random word based on probability and then adds the two words that come after that word in the source file. It uses the last word of this new string to randomly select a new word.
4. 'ShakespeareTextDump' is a large sample file of text to test each file and their outputs. Using more words in the generator will make more coherent text but often overfits to the data and can seem repetitive.
