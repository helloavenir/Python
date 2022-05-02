import random

operator = random.randint(1, 4)

x = random.randint(1, 100)

y = random.randint(1, 100)


if operator == 1 :
    answer = int(input(str(x) + '+' + str(y) + '의 값은? '))
    if x + y == answer :
        print('맞았습니다.')
    else :
        print('틀렸습니다.')
elif operator == 2 :
    answer = int(input(str(x) + '-' + str(y) + '의 값은? '))
    if x - y == answer :
        print('맞았습니다.')
    else :
        print('틀렸습니다.')
elif operator == 3 :
     answer = int(input(str(x) + '*' + str(y) + '의 값은? '))
     if x * y == answer :
         print('맞았습니다.')
     else :
         print('틀렸습니다.')
else :
    answer = float(input(str(x) + '/' + str(y) + '의 값은? '))
    if x / y == answer :
        print('맞았습니다.')
    else :
        print('틀렸습니다.')
