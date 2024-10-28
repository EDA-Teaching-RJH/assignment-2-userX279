import random
number = random.randint(1,100)
guess = int(input("Enter an integer: "))
while number!= guess:
    if guess < number:
        print("too low")
        guess = int(input("enter a different integer: "))
    elif guess > number:
        print("too high")
        guess = int(input("enter a different integer: "))
    else:
      break
print("you guessed it right!!")