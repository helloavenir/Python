names = []

for i in range(5) :
    nInput = input('학생 이름을 입력하세요: ')
    names.append(nInput)
print(names)


names2 = []
name = ' '
while name !='q' :
    name = input('Name(종료 -q): ')
    if name !='q' :
        names2.append(name)
print(names2)
