# a={1,'hello','python','hello',1,12}
# print(a)
# print(type(a))
# for i in a:
#     print(i)
# print('hello' in a)


#add, update, union
# a={1,'hello','python','hello',1,12}
# a.add('hi')
# print(a)
# b=[1,2,3,4,5,6]
# a.update(b)
# print(a)
# c=a.union(b)
# print(c)

#remove ,discard , pop(remove randomly an item from the set)
# a.remove('hi')
# print(a)
# a.discard(1)
# print(a)
# a.pop()
# print(a)

#intersection_update,intersection
# a={1,'hello','python','hello',1,12}
# b=[1,2,3,4,5,6]
# a.intersection_update(b)
# print(a) #the common element between the two will get printed
# c=a.intersection(b)
# print(c) #Here the common element will get into a new variable set and gets printed

#symmetric_difference_update,symmetric_difference
a={1,'hello','python','hello',1,12}
b=[1,2,3,4,5,6]
# a.symmetric_difference_update(b)
# print(a)#Here the common elements will be removed and the rest will get printed
c=a.symmetric_difference(b)
print(c)#The common elements will get removed and the rests gets into a new set and gets printed