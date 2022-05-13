# 0부터 100까지의 사이에 2와 3의 공배수들을 리스트로 만들어보기

numbers = [x for x in range(101) if x % 2 == 0 and x % 3 == 0 ]
print(numbers)
