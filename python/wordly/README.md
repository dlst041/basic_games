# Wordly

This is a python implementation of the wordly game. This game has a player try to determine the word based on input of letters. 

If the input letter is in the word and in the correct position of the word, the letter will be highlighted in green.

If the input letter is in the word but in the wrong position the letter will be highlighted in yellow.

If the input letter is not in the word, it will be highlighted in red.

## Setup

This game uses NLTK library to import an english language dictionary. 

The script `setup.sh` will generate a list of words of easy, medium, or hard difficulty. The difficulty is defined by the word length.

This script can be modified to extended the number of words used in each group.

The game will use this generated list of words by selecting one from the list randomly.