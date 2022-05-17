##
#	이 프로그램은 람다식을 이용하여 온도를 변환한다. 
#

'''def c(t):
    return (5/9)*(t-32)'''

f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(lambda x: (5.0/9.0)*(x-32.0), f_temp) #람다와 맵 함수 사용
print(list(c_temp))
