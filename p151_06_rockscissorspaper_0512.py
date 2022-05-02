userRock = int(input('선택하시오(1: 가위 2: 바위 3: 보) '))

import random
computerRock = random.randint(1,3)
print('컴퓨터의 선택(1: 가위 2: 바위 3: 보) ', computerRock)


if userRock == 1 and computerRock == 2 :
    print('컴퓨터가 이겼습니다.')
elif userRock == 1 and computerRock == 3 :
    print('사용자가 이겼습니다.')
elif userRock == 2 and computerRock == 1 :
    print('사용자가 이겼습니다.')
elif userRock == 2 and computerRock == 3 :
    print('컴퓨터가 이겼습니다.')
elif userRock == 3 and computerRock == 1 :
    print('컴퓨터가 이겼습니다.')
elif userRock == 3 and computerRock == 2 :
    print('사용자가 이겼습니다.')
else :
    print('서로 비겼습니다.')

    
