'''
반복문을 이용한 문제풀이
  1) 1부터 N까지 홀수 출력하기
  2) 1부터 N까지의 합 구하기
  3) N의 약수 출력하기
'''

n = int(input("숫자를 입력하세요"))
for i in range(1,n+1):
    if i%2==1:
        print(i)


m = int(input("숫자를 입력하세요"))
sum = 0
for j in range(1, m+1):
    sum=sum+j

print(sum)



a = int(input("숫자를 입력하세요"))
for k in range(1,a+1):
    if a%k==0:
        print(k, end=' ')
        
