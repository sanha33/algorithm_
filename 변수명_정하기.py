'''
변수명 정하기
1) 영문과 숫자, _로 이루어짐.
2) 대소문자를 구분함.
3) 문자나, _로 시작함.
4) 특수문자를 사용하면 안됨. (&,% 등)
5) 키워드를 사용하면 안됨. (if,for )등
'''
a=1
A=2
A1=3
_b=5
a, b, c = 3, 2, 1
print(a,A,A1,_b)


#값 교환
a, b=10, 20
print(a, b)
a, b = b, a
print(a, b)


#변수 타입
a=12345123456789012345678901234512345678901234567890
print(type(a))
print(a)
a=12.12345123456789012345678901234512345678901234567890
print(type(a))
print(a)
a="student"
print(type(a))
print(a)


#출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number",a ,b , c)
print(a ,b ,c, sep=', ')
print(a ,b ,c, sep=',')
print(a ,b ,c, sep='')
print(a ,b ,c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')
