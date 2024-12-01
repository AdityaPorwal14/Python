import random
secret_number=random.randint(1,10)
print(secret_number)
attempts=0
print("welcome to the number guessing game")
#ask user to guess the number
user_guess=int(input("guess the number between 0 to 10\n"))
attempts=attempts+1
#cheak if the guess is true
if(user_guess==secret_number):
    print("congratulation you guess right number in",attempts,"attempts")
    print("the number is ",secret_number)
elif(user_guess<=secret_number):
    print("you guess higher number")
else:
    print("you guess lower number")        