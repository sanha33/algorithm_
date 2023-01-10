'''
변수 입력과 연산자

a=input("숫자를 입력하세요 :")
print(a)
'''

a, b=input("숫자를 입력하세요 : ").split()
a=int(a)
print(type(a))
b=int(b)
print(type(b))
print(a+b)


c,d=map(int, input("숫자를 입력하세요: ").split())
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c//d) #몫
print(c%d)  #나머지


e=4.3
f=5
g=(e+b)  # 형이 다르면, 더 넓은 범위의 형으로 출력된다.
print(type(g))
