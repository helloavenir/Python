# 항목이 튜플이고, 리스트 형식인 자료를
## 정렬하고자 하는 키를 람다를 이용해 설정


data = [(3,100), (1, 200), (7, 300), (6, 400)]


print(data)
print()
print(sorted(data))
print()

print(sorted(data, key = lambda item: item[1]))

