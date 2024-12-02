d={'Name':'Flemina','Age':22,'Phone':9061455593}
# print(d)
# print(type(d))
# c=dict(Name='Flemina',Age=22)
# print(c)
print(d['Name'])
print(d.get('Age'))
print(d.keys())
print(d.values())
d['Address']='Thrissur' #add or update values
print(d)
print(d.items())
d.pop('Address') #Remove a pair
print(d)
del d['Phone']
print(d)