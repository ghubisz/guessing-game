import random
import math

#input
lower = int(input("Enter Lower bound: -"))

upper = int(input("Enter Upper bound: -"))

#generating random number between lower and upper
x = random.randint(lower, upper)
print("\n\tYou have only ",
      round(math.log(upper - lower + 1,2)),
      " chances to guess the number! \n")

#the number of guesses
count = 0

#for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1,2):
    count +=1

    #
    guess = int(input("Guess a number: -"))

    #condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        
        #once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

#if passed the number of possible guesses, outputs

if count >= math.log(upper - lower + 1,2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
