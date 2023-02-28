import time
import random
def get_user_input():
    user_word = input("User word > ")
    return user_word


def game_start():
    file_selected=False
    while file_selected != True:
        diff = input("Select Difficulty (easy, medium, hard): ").lower()
        if diff in ['easy', 'medium', 'hard']:
            file_ = './words/' + diff + '_words.txt'
            with open(file_) as fin:
                words = [word.strip() for word in fin.readlines()]
                word = words[random.randint(0, len(words))]
                return word

    # get user input for difficulty level
    # load words
    # select random word
    

def game():
    # loop until exit condition (user exits)
    game_won = False
    word = game_start()
    while(1):
        if game_won is True:
            word = game_start()
            game_won = False
        else:
            user_word = get_user_input()
            game_won = redraw(word, user_word)
    

def redraw(word, user_word):
    # redraw the terminal view of the word
    # "input field " should have color coding, n letter spaces based on difficulty
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
    game()
