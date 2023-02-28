import time
import random
def get_user_input():
    user_word = input(">")
    return user_word


def game_start():
    file_selected=False
    while file_selected != True:
        diff = input("Select Difficulty (easy, medium, hard):").lower()
        print(diff)
        if diff in ['easy', 'medium', 'hard']:
            file_ = './words/' + diff + '_words.txt'
            with open(file_) as fin:
                words = [word.strip() for word in fin.readlines()]
                word = words[random.randint(0, len(words))]
                print(word)
                return word

    # get user input for difficulty level
    # load words
    # select random word
    

def game(word):
    # loop until exit condition (user exits)
    game_won = False
    while(game_won != True):
        user_word = get_user_input()
        game_won = redraw(word, user_word)
    

def redraw(word, user_word):
    # redraw the terminal view of the word
    # "input field " should have color coding, n letter spaces based on difficulty
    print('word: {}\nuser_word: {}'.format(word, user_word))
    view_str = ""
    if user_word == word:
        print('Correct word chosen: {}'.format(word))
        return True
    else:
        word_list = [x for x in word]
        user_word_list = [x for x in user_word]

        for i in range(0, len(word_list)):
            if user_word_list[i] == word_list[i]:
                view_str+= '\x1b[1;32;40m' + user_word_list[i] + '\x1b[0m'
            elif(user_word[i] in word_list):
                view_str+= '\x1b[1;33;40m' + user_word_list[i] + '\x1b[0m'
            else:
                view_str+= '\x1b[1;31;40m' + user_word_list[i] + '\x1b[0m'

    print(view_str)
    return False

                

if __name__ == "__main__":
    word = game_start()
    game(word)
