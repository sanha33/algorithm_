import sys
input = sys.stdin.readline

def DFS(length):
  sum = 0
  for x in tree:
    if x > length:
      sum += x-length  
    
  return sum

n , m = map(int, input().split())
tree = list(map(int, input().split()))

lt = 0
rt = max(tree)

while lt <= rt:
  mid = (lt+rt)//2
  if m > DFS(mid):
    # result = mid
    rt = mid -1
  else:
    result = mid
    lt = mid+1 


print(result)

