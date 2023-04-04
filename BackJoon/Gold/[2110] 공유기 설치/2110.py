import sys
input = sys.stdin.readline

def DFS(length):
  cnt = 1
  last = x_list[0]
  for i in range(1, n):
    if x_list[i]-last>=length:
      cnt+=1
      last = x_list[i]
  return cnt  

n, c= map(int,input().split())
x_list = []
largest = 0
for _ in range(n):
  temp = int(input())
  x_list.append(temp)
  largest = max(temp, largest)

x_list.sort()
lt = 1
rt = largest

while lt<=rt:
  mid = (lt+rt)//2
  if DFS(mid)>=c:
    result = mid
    lt = mid + 1
  else:
    rt = mid - 1


print(result)
