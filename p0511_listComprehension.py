print('2차원 리스트 만들기')
rows = int(input('몇 행으로 만들건가요?'))
cols = int(input('몇 열로 만들건가요?'))




s = [([0]*cols) for row in range(rows)]

print(s)

