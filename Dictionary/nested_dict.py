#Nested Dictionary Operation
people = {1: {'name': 'Flemina', 'age': '22', 'sex': 'Female'},
          2: {'name': 'Sisira', 'age': '21', 'sex': 'Female'}}
people[3]={}
people[3]['name']='Nadeera'
people[3]['age']=30
people[3]['sex']='Female'

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])