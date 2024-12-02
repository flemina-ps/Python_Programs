#reverse a tuple
#Method_1
# t=(1,2,3,4,5,6,7)
# a=t[::-1]
# print("Original Tuple : ",t)
# print("Reversed Tuple : ",a)


#Method_2
t=(1,2,3,4,5,6,7)
a=tuple(reversed(t))
print(a)