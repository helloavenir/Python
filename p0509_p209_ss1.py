def get_area(radius) :
    area = 3.14*radius**2
    return area

radius = float(input('면적을 구하고 싶은 원의 반지름을 입력하세요 : '))

result = get_area(radius)
print('반지름이 %.2f인 원의 면적은 %.2f입니다.' %(radius, result))
    
