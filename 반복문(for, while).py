'''
반복문(for, while)
'''
a=range(1, 10)
print(list(a))


for i in range(10):
    print("hello",i)
    


for j in range(1, 10): # 1~9
    print("hello",j)


for k in range(10 , 0, -1): # 10~1
    print(k)


a = 1
while a<=10: # 1~10
    print(a)
    a=a+1


b = 10
while b>=1: # 10~1
    print(b)
    b=b-1


c = 1
while True:
    print(c)
    if c==10:
        break
    c+=1
    

for d in range(1,11): # 홀수만 출력 
    if d%2==0:
        continue
    print(d)


for e in range(1,11): # for-else 구문 , for문이 모두 정상 종료가 되면 else 문 실행.
    print(e)
    if e>5:
        break
else:
    print(11)
    
