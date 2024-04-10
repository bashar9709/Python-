def sum(num1, num2, num3=0, num4=0, num5=0,):
    result = num1 + num2 + num3 + num4 + num5
    return result
total = sum(10, 20, 5)
print('total:',total)

# args
def all_sum(num1,num2,*number):
    print(number)
    sum = 0
    for num in number:
        print(num)
        sum = sum + num
    return sum 
total = all_sum(10,20,5,15,6,4)
print('all sum:',total)    

def all_sum(*number):
    print(number)
    sum = 0
    for num in number:
        print(num)
        sum = sum + num
    return sum 
total = all_sum(10,20,5,15,6,4)
print('all sum:',total)    

