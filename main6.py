#If-else Statements
number=int (input("Enter The marks "))
print(number)

if(number>90 and number<100):
    grade="A"
elif(number>80 and number<100):
    grade="B"
else:
    grade="Dont Know"

print('The grade is ',grade)