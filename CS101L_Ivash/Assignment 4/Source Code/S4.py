import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    playAgain=   input("Do you want to play again? ==>").upper()
    while playAgain != "NO" and playAgain != "N" and playAgain != "Y" and playAgain != "YES":
        print("You must enter Y/YES/N/NO to continue.  Please try again")
        playAgain=   input("Do you want to play again? ==>").upper()
    if playAgain == "NO" or playAgain == "N":
        return False
    else:
        return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager1= int(input("How many chips do you want to wager? ==>"))
    while wager1<=0 or wager1>bank:
        if wager1<=0:
            print("The wager amount must be greater than 0.Please enter again.")
        elif wager1>bank:
            print("The wager amount cannot be greater than how much you have")
        wager1= int(input("How many chips do you want to wager? ==>"))
    return wager1            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    one = random.randint(1,10)
    two = random.randint(1,10)
    three = random.randint(1,10)
    return one, two, three

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    one = random.randint(1,10)
    two = random.randint(1,10)
    three = random.randint(1,10)
    if one == reela and two == reelb and three == reelc:
        return 3
    elif (one == reela and two == reelb) or (one == reela and  three == reelc) or (three == reelc and two == reelb):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    banks= int(input("How many chips do you want to start with? ==> "))
    while banks<=0 or banks>100:
        if banks<0:
            print("Too low a value, you can only choose 1 -100 chips")
        elif banks>100:
            print("Too high a value, you can only choose 1 -100 chips")
        banks= int(input("How many chips do you want to start with? ==> "))

    return banks

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches==3:
        return wager*10
    elif matches==2:
        return wager*3
    else:
      return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank>0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()