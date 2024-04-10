# print('Now I need some money')
# input()
# input('Give me some money:  ')

# money = input()
# print(money)

# money = input("Give me some money: ")
# print('Here is your money',money)

""" input nie jog and type casting """
first_money = input('Kodomk, Dosto taka de: ')
second_money = input('Laila, Oi taka de: ')
print(type(first_money))

# By default the input from user will be string type

print('Money I got from Kodom', first_money,'and from Laila', second_money)
total = first_money + second_money
print(total)

# Now typecasting
first_money_int = int(first_money)
second_money_int = int(second_money)

print(type(first_money_int))

total2 = first_money_int + second_money_int
print('Total money I got: ',total2)