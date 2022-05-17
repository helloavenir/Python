def fil(n):                                     # 필터 함수
    return n>3


def fil1(n):
    return n%2 == 0


list_a = [1,2,3,4,5,6,7]

result = filter(fil, list_a)
print(list(result))

print()

result1 = []                                    # 반복문으로 처리할 때
for i in list_a:
    if i > 3:
        result1.append(i)
print(result1)

print()

'''
list_a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x : x % 2 == 0, list_a)      #()이 filter의 조건
print(list(result))
'''

result2 = []                                    # 반복문으로 처리할 때
for i in list_a:
    if i%2 == 0 :
        result2.append(i)
print(result2)

print()

result3 = list(filter(fil1, list_a))
print(result3)

result4 = filter(lambda x : x %2 == 0, list_a)  #람다 함수를 사용하니 직관적으로 파악되네
print(list(result4))
