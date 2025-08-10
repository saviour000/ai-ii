import random as rd

print("Guessing the number")
print("Range of Numbers")

start = int(input("enter starting point :"))
end = int(input("enter ending point :"))

think = rd.randint(start,end);

while True:
    guess = int(input("Guess the number :"))
    if guess > think:
        print("Guess a lower number :")
    elif guess < think:
        print("Guess a higher number :")
    else:
        print("You have guessed right number")
        break