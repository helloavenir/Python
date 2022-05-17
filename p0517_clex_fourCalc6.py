n1=int(input('number1: '))

n2=int(input('number2: '))
a = []

while True:
    try:
        a.append(n1)
        a.append(n2)
        print(a)
        i=int(input('숫자:'))
        print(a[i])
        print(n1/n2)
              
        

    except ZeroDivisionError as e:     #try를 실행시 ZeroDivisionError라는 에러가 발생하면 
        print(e)


        
    except IndexError as e1:     #try를 실행시 ZeroDivisionError라는 에러가 발생하면 
        print(e1)                 #e라는 변수를 출력해줘

print('end program')        #먼저 만나는 에러를 먼저 표시하게 된다
                            ##그리고 나눗셈은 하지 않고 반복문 처음으로 돌아간다


