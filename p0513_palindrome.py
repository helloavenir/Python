word = input('문자열을 입력하시오 : ')

result = True

for i in range(len(word)//2) :
    if word[i] != word[-1-i] :
        result = False
        break

if result:
    print('회문입니다.')
else :
    print('회문이 아닙니다.')
    

    
