import random

vowels = ['a', 'e', 'i', 'o', 'u']
letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w']

num_vowels = 3
num_letters = 5

letter_list = []

def create_list():
    for i in range(num_letters):
        random_index = random.randint(0, len(letters)-1)
        letter_list.append(letters[random_index])
        letters.remove(letters[random_index])
    for j in range(num_vowels):
        random_index = random.randint(0, len(vowels)-1)
        letter_list.append(vowels[random_index])
        vowels.remove(vowels[random_index])

def check_list(user_word):
    for letter in user_word:
        if letter in letter_list:
            continue
        else:
            return False

    return True

def check_list_for_word(user_word):

    possible_words = open('english_words.txt', 'r')

    for line in possible_words:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        if user_word == line:
            return True

    return False

def main():
    create_list()
    print((" ").join(letter_list))

    score = 0

    while True:
        user_word = input("Enter a valid word: ")
        word_follows_rules = check_list(user_word)
        word_follows_rules2 = check_list_for_word(user_word)


        if word_follows_rules and word_follows_rules2:
            score+=len(user_word)
            print("Score: " + str(score))
        else:
            print("Nope. Your final score was " + str(score))
            break

main()