import nltk
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--difficulty", help="Specify difficulty level: (easy, medium, hard)", type=str)
parser.add_argument("-c", "--count", help="Specify number of words to save", type=int)

args = parser.parse_args()

difficulty = 'easy'
word_count = 30

#print(args.difficulty)

difficulties = {
    'easy': 4,
    'medium': 5,
    'hard': 6
}

if args.difficulty:
    difficulty = args.difficulty
    if difficulty not in ['easy', 'medium', 'hard']:
        print('difficulty value not accepted; options are (easy, medium, hard)')
        exit(0)

if args.count:
    word_count = args.count

#print("diff: {}\ncount: {}".format(difficulty, word_count))
difficulty_val = difficulties[difficulty]

nltk.download('english-words')
from nltk.corpus import words
wordslist = words.words()

shortlist = []

while len(shortlist) < word_count:
    randint = random.randint(0, len(wordslist)-1)
    word = wordslist[randint]
    uppers = [l for l in word if l.isupper()]
    # if len(uppers) > 0:
    #     print('Proper noun? : {}'.format(word))
    if word not in shortlist and len(word) == difficulty_val and len(uppers) == 0:
        shortlist.append(word)

#print(shortlist)

new_file = './words/' + difficulty + '_words.txt'
with open(new_file, 'w') as fout:
    for word in shortlist:
        fout.write(word)
        fout.write('\n')

