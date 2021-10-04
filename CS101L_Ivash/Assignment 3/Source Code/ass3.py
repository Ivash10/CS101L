#IvashDangol
#id7d7@umsystem.edu
#cs101L


print("Welcome to the Flarsheim Guesser!")

playAgain = "Y"
while (playAgain == "Y"):
    print("Please think of a number between and including 1 and 100.")
    rem3 = int(input("What is the remainder when your number is divided by 3 ?"))
    while rem3>3 or rem3<0:   
        if rem3>3:
            print("The value entered must be less than 3")
        elif rem3<0:
            print("The value entered must be 0 or greater")
        rem3 = int(input("What is the remainder when your number is divided by 3 ?"))
    rem5 = int(input("What is the remainder when your number is divided by 5 ?"))
    while rem5>5 or rem5<0:
        if rem5>5:
            print("The value entered must be less than 5")
        elif rem5<0:
            print("The value entered must be 0 or greater")
        rem5 = int(input("What is the remainder when your number is divided by 5 ?"))


    rem7 = int(input("What is the remainder when your number is divided by 7 ?"))
    while rem7>7 or rem7<0:
        if rem7>7:
            print("The value entered must be less than 7")
        elif rem7<0:
            print("The value entered must be 0 or greater")
        rem7 = int(input("What is the remainder when your number is divided by 7 ?"))
    
    
    for i in range(1,101):
        if i%3==rem3 and i%5==rem5 and i%7==rem7:
            print("Your number was", i)
            print("How amazing is that?")
        
    playAgain = "a"
    while (playAgain != "Y") and (playAgain != "N"):
        playAgain = input("Do you want to play again? Y to continue, N to quit. ").upper()