'''
This is flash cards!, 

1. user inputs all the terms and definitions
2. user decides what kind of test they want to try 
3. tells you your score and the words you need to practice more 
'''

import random

cardslist = []
#create new temporary pair
newpair = []
user_cards = input('Please enter a term: ')
while user_cards != 'done':
    newpair.append(user_cards)
    user_def = input('Please enter the definition: ')
    newpair.append(user_def)
    cardslist.append(newpair)
    #clear newpair variable
    newpair = []
    user_cards = input(
        'Please enter a term. If you have no more terms, type done:')


#define function for main play function
def play_cards(user_choice):
    #start a counter for the correct
    correct = 0
    #empty list of wrong cards that we will append to
    wrongcards = []
    random.shuffle(cardslist)
    #check the parameter of function for terms
    if user_choice == 'terms':
        for i in cardslist:
            print('The term is', i[0])
            answer = input('What is the definition? ')
            if answer == i[1]:
                print('Correct')
                correct = correct + 1
            else:
                print('False')
                wrongcards.append(i)
    #check parameter for definitions
    elif user_choice == 'definitions':
        for i in cardslist:
            print('The definition is', i[1])
            answer = input('What is the term? ')
            if answer == i[0]:
                print('Correct!')
                correct = correct + 1
            else:
                print('False.')
                wrongcards.append(i)
    #calculate score
    score = round((100 * correct / len(cardslist)), 2)
    print('Your score is', score,
          'and you need to study the following terms: ', wrongcards)


#ask what kind of test they want to play
test_kind = input(
    'If you would like to practice with given terms, type "terms". If you would like to practice with given definitions, type "definitions".'
)

#call function with the type of test as the parameter hey
play_cards(test_kind)
