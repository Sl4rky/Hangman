import random

word_list = [
    'hello',
    'dog',
    'cat',
    'giant',
    'bat',
    'dictionary',
    'book'
]



def main():
    word = random.choice(word_list)
    working_word = ['_' for letter in word]
    lives = 6
    while lives != 0:
        print(working_word)
        print(f"you have {lives} lives remaining")
        x = input("pick a letter!\n")
        if len(x) > 1:
            if x == word:
                print("you win!")
                break
            print("wrong guess!")
            lives -= 1
            continue
        if x.lower() in word:
            location = word.find(x)
            working_word[location] = x.lower()
            print(f"{x} is in position {location + 1}")
            continue
        print("nice try")
        lives -= 1

    print(f"game over, word was {word}")

if __name__ == '__main__':
    main()    