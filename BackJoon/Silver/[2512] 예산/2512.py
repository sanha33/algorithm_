import sys
input = sys.stdin.readline

def func(money):
  sum = 0
  for x in con:
    if x >= money:
      sum += money
    else:
      sum += x
  return sum
  
n = int(input())
con = list(map(int, input().split()))
m = int(input())

lt = 1
rt = max(con)

while lt<=rt:
  mid = (lt+rt)//2
  if func(mid)<=m:
    result = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(result)
