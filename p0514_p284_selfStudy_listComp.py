# 0부터 100까지의 사이에 2와 3의 공배수들을 리스트로 만들어보기

numbers = [x for x in range(101) if x % 2 == 0 and x % 3 == 0 ]
print(numbers)



# 0부터 10까지의 정수 중에서 짝수이면 '짝수'를, 홀수이면 '홀수'를
## 리스트에 추가하는 리스트 함축 만들어보기
print()

evenOdd = ['짝수' if x % 2 == 0 else '홀수' for x in range(11) ]
print(evenOdd)


# 누적 합계 리스트 만들기
print()

list1 = [10, 20, 30, 40, 50]
list2 = [sum(list1[0:x+1]) for x in range(len(list1))]

print('원래 리스트: ', list1)
print('새로운 리스트: ', list2)


