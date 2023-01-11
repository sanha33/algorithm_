'''
2차원 리스트 생성과 접근
'''

a = [0]*10   # 1차원 리스트 생성 
print(a)

b = [[0]*3 for _ in range(3)]   # 2차원 리스트 생성 
print(b)

b[0][1] = 1
print(b)
b[1][1] = 2
print(b)

for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=' ')
    print()
