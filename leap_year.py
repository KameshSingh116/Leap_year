choice='y'
while(choice=='y'):
    year=int(input("Enter the year...:"))
    if(year%4==0 and year%100!=0):
        print("Its a leap year!")
    elif(year%400==0):
        print("Its a leap year!")
    else:
        print("Its not a leap year!")
    choice=input("Do you want to continue:(y/n)...:")
    if(choice=='y'):
        continue
    else:
        break