def double(n):
    return 2*n



list_a = [ 1, 2, 3, 4, 5 ]
result1 = list(map(double, list_a))     #리스트 항목 각각에 double함수를 적용해
print(result1)                          ## 새로운 리스트를 만들어 출력함

print()

f = lambda x : 2*y                      #람다함수 활
result = map(f, list_a)
print(list(result))
