# PF-Tryout
import random
def guess_number(number_in_mind):
    number = random.randrange(1, 10)
    if (number < number_in_mind):
        print('Number is low')
    elif (number > number_in_mind):
        print('Number is high')
    else:
        print('You have got it right!!!')
# use the print statements given below wherever applicable
# Provide different values for number_in_mind and test your program
guess_number(4)