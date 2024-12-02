#if_elif_else

m=int(input("Enter the mark: "))
if m>=90:
    print("A+")
elif m>=80 and m<=89:
    print("A")
elif m>=70 and m<=79:
    print("B+")
elif m>=60 and m<=69:
    print("B")
elif m>=50 and m<=59:
    print("C+")
else:
    print("F")
