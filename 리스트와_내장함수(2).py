'''
리스트와 내장함수(2)
'''
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
          
print()
for x in a:
    if x%2==1:
        print(x, end=' ')

print()
for x in enumerate(a):
    print(x)

'''
result
    (0, 23)
    (1, 12)
    (2, 36) 
    (3, 53)
    (4, 19)
'''

b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7 튜플 값은 변경 불가 


for x in enumerate(a):
    print(x[0], x[1])
print()

'''
result
    0 23
    1 12
    2 36
    3 53
    4 19
'''

for index, value in enumerate(a):
    print(index, value)
print()

'''
result
    0 23
    1 12
    2 36
    3 53
    4 19
'''

if all(50>x for x in a):   # a의 값 중 60>x 조건에 '모두' 만족하면 if는 True ! 
    print("Ture !!")
else:
    print("False !!")


if any(15>x for x in a):   # 아무거나 '하나라도' 15>x에 만족하면 if는 True ! 
    print("Ture !!")
else:
    print("False !!")
