import random 

name = input('Hello! What is your name?\n')
print('Well, KBTU, I am thinking of a number between 1 and 20.')
counter = 1
number = random.randint(1,20)
print(number)
num1=int(input('Take a guess!\n'))
while num1 != number:
    number = random.randint(1,20)
    num1 = int(input('Take a guess!\n'))
    if num1 < number:
            print ("Your guess is too low.")
            num1 = int(input("Take a guess.\n"))
    elif num1 > number:
            print ("Your guess is too high.")
            num1 = int(input("Take a guess.\n"))
            print('Good job,',name, 'You guessed my number in' ,counter, 'guesses!')
    counter+=1    
print('Good job,',name, 'You guessed my number in' ,counter, 'guesses!')      