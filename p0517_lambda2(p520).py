##
#	이 프로그램은 람다식을 이용하여 주문을 처리한다.  
#
orders = [ ["1", "재킷", 5, 120000], 
           ["2", "셔츠", 6, 24000], 
           ["3", "바지", 3, 50000],
           ["4", "코트", 6, 300000] ]

for order in orders:
    print(order)
    


'''
result = list(map(lambda x: (x[0], x[2] * x[3]), orders))
print(result)
'''


for order in orders:
    print(order[0], order[1], order[2], order[3])

print()
results = []
for order in orders:
    p = order[2] * order[3]
    n = order[0]
    t1 = (order[0],order[2] * order[3])
    results.append(t1)
print(results)



