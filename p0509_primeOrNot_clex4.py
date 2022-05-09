number = int(input('소수인지 확인할 숫자를 입력하세요 : '))

for i in range(2, number) :
    if number % i == 0 :
        prime = False
        break
        print('%d는 소수가 아닙니다.' %number)

if prime :
    print('%d는 소수입니다.' %number)
