#While Loops
i=int(input("Enter the number "))
while(i<4):
    print("Number is greater then 4")
    i=int(input())
    if(i==9):
        break
    if(i==8):
        continue
        print("Loop ended")