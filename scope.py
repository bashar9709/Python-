# global variable
balance  = 3000

def buy_things(item,price):
    # local scope variable
    # you can acces global variable without using the global keyword
    # local variable shudu fucntion ar modde use hie
    dream_phone = 'X Phone'
    # if you want to modify a global variable , you have to use the global keyword 
    global balance
    print(f'previous balance value', balance)
    balance = balance - price
    print(f'balance after buying {item}', balance)

buy_things('sunglass',100)
print('global balance after buy',balance)

