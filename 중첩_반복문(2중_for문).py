'''
중첩 반복문 (2중 for문)
'''

for i in range(5):
    print('i:', i, sep='',end=' ') # sep='' 띄어쓰기를 없앰. , end=' ' 줄바꿈을 없앰.
    for j in range(5):
        print('j:', j, sep='',end=' ')
    print()


for j in range(5):
    for k in range(j+1):
        print("*", end=' ') 
    print()


for j in range(5, 0 ,-1):
    for k in range(j+1):
        print("*", end=' ') 
    print()

