name = input("Who are we calculating grade for?==>")
labs = int(input("Enter your lab score.1-100==>"))
if labs>100:
    print("The lab value should have been 100 or less.It has been changed to 100.")
    labs=100
elif labs<0 :
    print("The lab value should have been 0 or more. It has been changed to 0.")
    labs=0
labExam = int(input("Enter your lab exam score.1-100==>"))
if labExam>100:
    print("The labExam value should have been 100 or less.It has been changed to 100.")
    labExam=100
elif labExam<0 :
    print("The labExam value should have been 0 or more. It has been changed to 0.")
    labExam=0
attendance=int(input("Enter" + " your attendance.1-100==>"))
if attendance>100:
    print("The attendance value should have been 100 or less.It has been changed to 100.")
    attendance=100
elif attendance<0 :
    print("The attendace value should have been 0 or more. It has been changed to 0.")
    attendance=0
sum= labs *0.7+ labExam *0.2+ attendance*0.1
print ("The weighted grade for", name,"is", sum)
if sum >= 90:
    grade = "A"
elif sum >=80:
    grade="B"
elif sum>=70:
    grade="C"
elif sum>=60:
    grade="D"
else :
    grade="F"

print(name,"has a letter grade of",grade)


                  