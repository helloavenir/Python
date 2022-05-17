n1=int(input('number1: '))

n2=int(input('number2: '))
try:
    print(n1,'+',n2, ' = ', n1 + n2)
    print(n1,'-',n2, ' = ', n1 - n2)
    print(n1,'*',n2, ' = ', n1 * n2)
    print(n1,'/',n2, ' = ', n1 / n2)   

except ZeroDivisionError:     #try를 실행시 ZeroDivisionError라는 에러가 발생하면
    print('zero')

print('end program')

