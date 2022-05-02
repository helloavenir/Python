weight = float(input('몸무게를 kg 단위로 입력하시오: '))
height = float(input('키를 미터 단위로 입력하시오: '))

BMI = weight / height ** 2

print('당신의 BMI= %f ' %BMI)


if BMI <= 18.5 :
    print('저체중입니다')
elif BMI > 18.5 and BMI < 23 :
    print('정상입니다')
elif BMI >= 23 and BMI < 25 :
    print('과체중입니다')
else :
    print('비만입니다')
    
    
    
