#! /usr/bin/env python3
import random

#word list to work from
word_list = [
    'book'
]



def main():
    solution = random.choice(word_list)                                     # picking a random word
    word = list(solution)                                                   # making a list because it is easier to wrap my head around
    working_word = ['_' for letter in word]
    lives = 6

    # main game loop
    while lives != 0:
        print(working_word)
        print(f"you have {lives} lives remaining")
        x = input("pick a letter!\n")

        # checking win condition
        if len(x) > 1:
            if x == solution:
                print("you win!")
                break
            print("wrong guess!")
            lives -= 1
            continue

        # checking for letter in word
        if x.lower() in word:
            find_letter(word, x, working_word)
            continue
        print("nice try")
        lives -= 1

    print(f"game over, word was {solution}")


# logic to find letters in word (had a hard time with doubles so I made a list that I can change elements of)
def find_letter(word, x, working_word):
    for i in range(word.count(x)):
        index = word.index(x)
        working_word[index] = x
        word[index] = '_'
        print(f"there is a {x} in position {index + 1}")


if __name__ == '__main__':
    main()    