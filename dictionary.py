# Dictionary
# dictionaries are used to sotre data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# overlap with set
# {key:value, key:value, key:value}
person = {'name':'kala', 'address': 'kalipur', 'age':23, 'job':'facebook'}

print(person)

print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)