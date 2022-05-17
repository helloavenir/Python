def s(n):
    return n**2



mylist1 = [1,2,3,4,5]
result1 = [ ]

for i in mylist1:               #반복문
    result1.append(i**2)

print(mylist1)
print(result1)

print()

result2 = [ i**3 for i in mylist1]          #리스트함축
print(result2)


print()


result3 = []
for i in mylist1:               #리턴값 수식이 복잡할 때는 함수로 넣는 것도 가능
    result3.append(s(i))        ## 이때는 리턴값들을 한꺼번에 갖고 오는 것이다.

print(result3)

print()

result4 = list(map(s, mylist1))       #mylist1을 가지고 와 적용한 함수 s의 값을 각각
                                      ## 가져와서 리스트 형태로 보여줘




