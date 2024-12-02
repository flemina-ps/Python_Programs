#Access value 20 from the tuple which should be the 5th item
# a=(1,5,10,12,13,20,24,49)

# print(a[5])


#Tuple with a single item 50
# a=50,
# print(type(a))

#Swap two tuples
# a=(1,2,3,5,6,7,9)
# b=(10,20,30,50,90,100)
# print("Original Tuples ")
# print("First Tuple : ",a)
# print("Second Tuple : ",b)
# #swapped
# a,b=b,a
# print("\n Swapped Tuples")
# print("First Tuple : ",a)
# print("Second Tuple : ",b)


#Copy specific elements from one tuple to another tuple

# a=(1,2,3,5,6,7,9)
# b=(10,20,30,50,90,100)
# b=b+a[2:5]
# print(b)


#Modify the tuple
# a=(1,2,3,5)
# b=(10,20,30)
# a=list(a)
# # b=list(b)
# a.append(b)
# a=tuple(a)
# b=tuple(b)
# print(a)
# print(b)
# # print(type(a))


#Sort a tuple
a=(9,3,78,1,12,10)
b=tuple(sorted(a))
print("Sorted Tuple : ",b)

