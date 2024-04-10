# set: unique items collection. no douplicate
# Unchangeable, unordered, unindexed

number = [12,37, 24, 56, 63, 20, 64, 66, 85, 23]
print(number)

num_set = set(number)
print(num_set)

num_set.add(55)
num_set.add(13)
print(num_set)

num_set.remove(55)
print(num_set)

for item in num_set:
    print(item)

A = { 1, 2, 3, 4}
B = { 3, 4, 5, 6}
print(A | B) 
print(A & B)   