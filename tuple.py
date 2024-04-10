# Tuple are used to store nultiple items in a single variable.
my_tuple = ("apple", "banana","cherry")
print(my_tuple)

my_tuple2 = ('apple', 'banana','cherry', 'Guava')
print(my_tuple2)

print(type(my_tuple2))
print(my_tuple[0])
print(my_tuple2[-2])
print(my_tuple2[2:4])

if 'banana' in my_tuple2:
    print('exist')

for item in my_tuple2:
    print(item)    