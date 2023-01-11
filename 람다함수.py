'''
람다 함수 (익명의 함수)
'''

def plus_one(x):
    return x+1

print(plus_one(1))


plus_two = lambda x: x+2
print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_one, a)))   # map 함수는 map(내장함수, 데이터) : 데이터가 내장함수의 영항을 받음


print(list(map(lambda x: x+1, a)))   # 람다함수는 이와 같이 내장함수의 인자로 사용할 때 좋음 ! 
 
