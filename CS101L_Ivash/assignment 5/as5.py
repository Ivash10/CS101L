import string

def verify_check_digit(card):
    
    
    
    if len(card)!= 10:
        return(False, "The length of the number given must be 10")
    a = isLetter(card)
    if isLetter(card)!=-1:
        return (False, "The first 5 characters must be A-Z, the invalid character is at " + str(a) +" is " + card[a])
    b= isNum(card)
    if isNum(card) !=-1:
        return (False, "The last 3 characters must be 0-9, the invalid character is at " + str(b) + " is " +card[b])
    elif card[5]!= "1" and card[5]!="2" and card[5]!="3":
        return (False, "The sixth character must be 1 2 or 3")
    elif card[6]!= "1" and card[6]!="2" and card[6]!="3" and card[6]!="4":
        return (False, "The seventh character must be 1 2 3 or 4")
    c = get_check_digit(card)
    if int(card[9])!=c:
        return (False, "Check Digit "+card[9]+" does not match calculated value "+ str(c) +".")
    else:
        return (True,"")
    
def get_check_digit(card):
    sum = 0
    for i in range(0,9):
        
        if i<5:
            sum=sum + (i + 1)*character_value(card[i])
        else:
            sum=sum + (i + 1)*int(card[i])
    return sum%10

def character_value(y):
   
    return string.ascii_uppercase.index(y)

def isLetter(card):    
    for x in range(0,5):
        card[x].upper()
        if ord(card[x])<65 or ord(card[x])>90:
            
            return x
        
    return -1
 
def isNum(card):    
    for x in range(7,10):

        if card[x].isnumeric() == False:
            return x
    return -1

def get_school(s):
    if s == "1":
        return "School of Computing and Engineering SCE"
    elif s=="2":
        return "School of Law"
    elif s=="3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
def get_grade(g):
    if g == "1":
        return "Freshman"
    elif g=="2":
        return "Sophomore"
    elif g=="3":
        return "Junior"
    elif g == "4":
        return "Senior"
    else:
        return "Invalid grade"    
if __name__ == "__main__":
    valid = 1
    print("          LINDA HALL             ")
    print("        Library Card Check   ")
    print("==================================================")
    while valid == 1:

        card=input("Enter library Card. Hit Enter to Exit ==>")
        result=verify_check_digit(card)
        if result[0]==False:
            print("Library Card is invalid.")
            print(result[1])
            
            
        else:
            print("Library Card is Valid.")
            print("The Card belongs to a student in",get_school(card[5]),".")
            print("The Card belongs to a",get_grade(card[6]),".")
            
            
            
        
