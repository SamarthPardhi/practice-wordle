import random
from termcolor import colored


def all_alpha(s:str):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s=s.lower()
    for i in s:
        if not i in alphabets:
            return False
    return True


def update_wordle_file(wordle_filename, words_filename_obj):
    file = open(wordle_filename,'w')
    for word in words_filename_obj:
        if len(word.strip()) == 5 and all_alpha(word.strip()) and not word.strip().isupper():
            file.write(word.strip()+str('\n'))
    return True

def ind(my_word, given_word):
    green_ind = []
    yellow_ind = []
    for i in range(len(given_word)):
        if given_word[i] == my_word[i]:
            green_ind.append(i)
        elif given_word[i] in my_word:
            yellow_ind.append(i)
    return green_ind, yellow_ind

def decorated_alpha(l:list):
    yellow_words, green_words, red_words = l
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
    s=''
    for letter in alphabets:
        if letter in yellow_words:
            s+=colored(letter, 'yellow')
        elif letter in green_words:
            s+=colored(letter, 'green')
        elif letter in red_words:
            s+=colored(letter, 'red')
        else:
            s+=letter
    return s


def print_meth(my_word, given_word, yellow_words, green_words, red_words):
    green_ind, yellow_ind = ind(my_word, given_word)
    word_splitted = [i for i in given_word]
    s = ''
    for i in range(len(given_word)):
        if i in green_ind:
            green_words.append(given_word[i])
            s+=colored(word_splitted[i], 'green')
        elif i in yellow_ind:
            if not given_word[i] in green_words:
                yellow_words.append(given_word[i])
            s+=colored(word_splitted[i], 'yellow')
        else:
            red_words.append(given_word[i])
            s+=colored(word_splitted[i], 'white')
    return s, [yellow_words, green_words, red_words]

def filter_master_words_list(words_l):
    return words_l


if __name__ == "__main__":
    words_filename_obj = open('words.txt','r')
    wordle_filename = 'wordle_words.txt'
    update_wordle_file(wordle_filename, words_filename_obj)

    wordle_file_obj = open(wordle_filename, 'r')
    words_list = [i.strip().upper() for i in wordle_file_obj]

    master_words_list = filter_master_words_list(words_list)
    my_word = master_words_list[random.randint(0,len(master_words_list)-1)]

    yellow_words = []
    green_words = []
    red_words = []
    c=0
    while c <= 5:
        guess = input().strip().upper()
        if not guess in words_list:
            if not len(guess)==5:
                print(colored("Word length should be 5. Try again:", 'red'), end=' ')
            else:
                print(colored("Word isn't in wordslist. Try again:", 'red'), end=' ')

        else:
            c+=1
            temp = print_meth(my_word, guess, yellow_words, green_words, red_words)
            yellow_words, green_words, red_words = temp[1]
            print(f"{str(c)}: {temp[0]}  {decorated_alpha(temp[1])}")
            if guess == my_word:
                break

    if c >= 6:
        temp = print_meth(my_word, my_word, yellow_words, green_words, red_words)
        print(f"Correct Answer: {temp[0]}  {decorated_alpha(temp[1])}")