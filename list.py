# Lists are used to store multiple items in a single variable.
# list , array, collection is same (simle terms)

# list indexes can be written in two ways

# index =   0   1   2   3   4   5   6   7   8   9
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 49, 23]
# index = -10 -9   -8  -7  -6  -5  -4  -3  -2 -1

print(numbers[3], numbers[-3])

# list(start:end:step)
print(numbers[2:6])
print(numbers[-5:-1])
print(numbers[1:7:2])
print(numbers[7:1:-1])
print(numbers[4:])
print(numbers[:5])
print(numbers[:]) #short cut to copy a list
print(numbers[::-1]) #shortcut to reverse a list

thislist = ['bashar', 'he', 'she', 'boy']
print(thislist)

#-------------------------------> List methods(built in function) <-------------------------------------------
# append(value)-->Adds an element at the end of the list
numbers.append(88)
print(numbers)
thislist.append('shei')

# insert(index, value) --->Adds an element at the specified position
numbers.insert(2,40)
numbers.insert(0,30)
print(numbers)
thislist.insert(2,'rakib')
print(thislist)

# remove(value)-->Removes the item with the specified value
numbers.remove(12)
print(numbers)
thislist.remove('she')
print(thislist)

if 89 in numbers:
    numbers.remove(89)
else:
    numbers.remove(30)
print(numbers)  

# pop()-->remove the last element of list // Removes the element at the specified position
last = numbers.pop()
print(last, numbers)

last = numbers.pop(5)
print(last, numbers)

# index(value)-->Returns the index of the first element with the specified value
index = numbers.index(45)
print(index)

# sort()-->Sorts the list
numbers.sort()
print(numbers)


# reverse()-->>Reverses the order of the list
numbers.reverse()
print(numbers)

# looping for a index of list

for index, number in enumerate(numbers):
    print(index,number)
