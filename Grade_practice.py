#What is the score?
score=int(input("What is your test score?"))

#Determine the grade.
if score>=90:
    print('Your grade is an A.')

else:
    if score>=80:
        print('Your grade is a B.')
    else:
        if score>=70:
            print('Your grade is a C.')
        else:
            if score>=60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
counties=['A','B','C']
if 'D' in counties:
    print('D is in thes list of counties')
else:
    print("D is not in the list of counties")
if "A" in counties or "B" in counties:
    print("A and B in the list of counties")
else: 
    print('A or B is not in the list of counties')


                