#check if a year is leap year

year=int(input("Enter the year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is not a Leap Year")
