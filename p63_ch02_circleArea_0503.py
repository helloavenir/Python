radius = float(input('원의 반지름은? '))
area = 3.14 * radius ** 2
print('반지름 %.2f인 원의 면적 = %.2f' %(radius, area))
print()


radiusRound = '{:0,.2f}'.format(radius)
areaRound = '{:0,.2f}'.format(area)

print('반지름', radius, '인 원의 면적= ', area)
print()


print('반지름', radiusRound, '인 원의 면적= ', areaRound)
