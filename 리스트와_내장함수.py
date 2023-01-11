'''
리스트와 내장함수(1)
'''

import random as r
a = []  # 빈 리스트
print(a)
b = list()
print(b)

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])


b = list(range(1, 11))
print(b)


c = a + b
print(c)


print(a)
a.append(6)
print(a)


a.insert(3, 7)  # 인덱스 3번 지점에 7을 insert 
print(a)


a.pop()
print(a)
a.pop(3)   # 인덱스 3번의 값을 pop 
print(a)


a.remove(4)   # 4라는 값을 제거
print(a) 


print(a.index(5))   # 5라는 값의 인덱스 번호를 출력 



x = list(range(1, 11))
print(x)
print(sum(x))   # 리스트 안의 값들을 모두 더함 
print(max(x))
print(min(x))
print(min(7, 5))   # 7과 5 중에서 작은 값을 출력해줌
print(min(7, 5, 3))
print(x)
r.shuffle(x)   # 리스트 x의 원소들을 다 섞음
print(x)
x.sort(reverse=True)   # 내림차순 
print(x)
x.sort()   # 오름차순 
print(x)
x.clear()   # 빈리스트로 만듦 
print(x)
