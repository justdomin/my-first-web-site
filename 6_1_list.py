person = {'name':'chaeuimin', 'address':'Gwangju', 'interest' : 'coding'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name':'chaeuimin', 'address':'Gwangju', 'interest' : 'coding'},
    {'name':'park ha eun', 'address':'incheon', 'interest' : 'cosdac'},
    {'name':'im sun a', 'address':'seoul', 'interest' : 'kid'},
]
print('=====persons=====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-------------')