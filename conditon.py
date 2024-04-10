# in, not, not in, is , is not
a = 7
if a > 5: 
    print('5 er beshi')
    print('Koto besi ke jane')
else: 
    print('Are nah 5 er kom')


#python ar else if ar jayga te akhon elif condition
# elif condition:

if a>5 :
    print('5 beshi')
elif a>3: 
    print('onek olpo')
else:
     print('Alpo boro') 

boss = True
coin = 'head'
# nested conditions
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do  something')
            if 8%2 == 0 and 5%2==1:
                print('even 8 is an even number')
else:
    print('you are loss not a boss')               