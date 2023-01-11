'''
함수 만들기
'''

def add(a, b):
    c = a+b
    print(c)

add(3, 2)
add(5, 7)

def add2(a, b):
    c = a+b
    return c

print(add2(10, 11))
result = add2(1, 10)
print(result)


def add3(a, b):
    c = a+b
    d = a-b
    return c, d  # 튜플 형태로 return 

print(add3(6, 7))



def isPrime(x):   # 소수 인지 아닌지 
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

x = [12, 13, 7, 9, 19]
for k in x:
    if isPrime(k):
        print(k, end = ' ')
