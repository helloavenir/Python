
#pi사용하기 위해

import math

def calc_circle () :
    area = math.pi * radius ** 2
    around = math.pi * radius * 2
    return(area, around)


r = int(input('원의 반지름을 입력하시오 : '))

(a, d) = calc_circle(r)

print('반지름이 %d인 원의 면적은 %10.2f이고, 둘레는 %10.2f이다.' %(r, a, d))
