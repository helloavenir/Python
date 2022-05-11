def select_menu() :
    print('-------------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('9. 종료')
    menu = int(input('메뉴를 선택하시오 : '))
    
def output_name() :
    print(friends)
def append_name() :
    name = input('이름을 입력하시오 : ')
        friends.append(name)
def delete_name() :
    del_name = input('삭제하고 싶은 이름을 입력하시오 : ')
        if del_name in friends :
            friends.remove(del_name)
        else :
            print('리스트에 없는 이름입니다.')
def modify_name() :
     old_name = input('변경하고 싶은 이름을 입력하시오 : ')
        if old_name in friends :
            index = friends.index(old_name)
            new_name = input('새로운 이름을 입력하시오 : ')
            friends[index] = new_name
        else :
            print('리스트에 없는 이름입니다.')
    
def main() :
    while menu != 9 :
   
    menu = int(input('메뉴를 선택하시오 : '))
    if menu == 1 :
        output_name()
    elif menu == 2 :
        append_name()
    elif menu == 3 :
        delete_name()
    elif menu == 4 :
        modify_name()
    elif menu == 5 :
        select_menu()



# 함수로 작성해본 것


