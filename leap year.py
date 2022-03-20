# Leap Year
while True:
    year = int(input("Enter the Year: "))
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year.")
        else: 
            print(year, "is a leap year.")
    else:
        print(year, "not a leap year.")
    year = input("Check again for leap year? (y/n) ")
    if year.lower() == 'n':
        year = False
        break
        
    
        


