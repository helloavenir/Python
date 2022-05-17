n1=int(input('number1: '))

n2=int(input('number2: '))

print(n1,'+',n2, ' = ', n1 + n2)
print(n1,'-',n2, ' = ', n1 - n2)
print(n1,'*',n2, ' = ', n1 * n2)


if not n2:
    print('zero')
else:
    print(n1, '/' , n2, ' = ', n1/n2)

print('program end')
