import random 

print("The value range that is supposed to be with the system ")
high = int(input("Enter the highest number: "))
low = int(input("Enter the lowest number: "))

print("Random pick by the computer has started")
num = random.randint(low,high)
ch = 5 
cout = 0 

while cout <= ch: 
    cout += 1 
    guess = int(input("Enter the number: "))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {cout} attempts.')
        break
    elif cout >= ch and guess != num:
        print(f'Sorry ! Better luck next Time ! The number is {num}')
    
    elif guess > num: 
        print("Too high")
    
    elif guess < num: 
        print("Too low")
