import sys
input = sys.stdin.readline

def DFS(length):
  cnt = 0
  for x in list1:
    cnt += x//length

  return cnt


k, n = map(int, input().split())
list1 = []
largest = 0
for _ in range(k):
  temp = int(input())
  list1.append(temp)
  largest = max(largest, temp)

lt = 1
rt = largest

while lt<=rt:
  mid = (lt+rt)//2
  
  if DFS(mid)>=n:
    result = mid
    lt = mid + 1
  else:
    rt = mid - 1
  
print(result)
