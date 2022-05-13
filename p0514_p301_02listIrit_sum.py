# 1부터 100 사이의 난수 10개를 생성하여
## 리스트 values룰 채우는 반복 루프 작성하기

import random

list1 = [ ]

for i in range(10) :
    n = random.randint(1, 100)
    list1.append(n)

print('randomList= ', list1)

