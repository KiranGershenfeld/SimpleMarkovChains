# SimpleMarkovChains
This project uses markovs chains to immitate any set of text that it is given

Markov Chains are a type of algorithm that examines each word of a text file and the probability of the words that come after it. Doing this for every word, it is able to predict which words will come after each other and create entirely new strings of text.

# Quick Start
Clone the repository and run MarkovMain.py from the console or an IDE. The output text should be printed to the console. TrainingText.txt is already set up with a large excerpt from Shakespeare, this can be changed to anything but larger amounts of text words better.

# File Overview
In this project there are several implementations of Markov Chains. Here is an overview of files in this project:
1. 'MarkovMain' I have found this version of the generator works best which is why it is labeled main. It puts each word in the text in a dictionary with each 2 word pair that follows that word at any point (one key and two values). Then it uses that dictionary to randomly choose the next 2 words in the sequence.
2. 'MarkovGeneratorTwoWordPairs.py' Uses the same strategy but only makes two word pairs (one key and one value).
3. 'MarkovGeneratorFoudWordPairs.py' Uses the same strategy but makes 4 word pairs (one key and three values).
4. 'TrainingText.txt' is a large sample file of text to test each file and their outputs. It is already filled with an excerpt from Shakespeare but can be changed to anything you want.
