# 사용자가 입력하는 정수값을 리스트에 저장하고
## 이 값들의 합계를 계산하는 프로그램

n = int(input(' 입력할 값의 개수: '))
result = [ ]

for i in range(n) :
        value = int(input(''))
        result.append(value)        # 리스트에 값들 저장하기

s = sum(result)                     # 리스트 result의 요소들 합계내기 
print('값의 합계= ', s)



