import sys

n = int(input())

for _ in range(n):
  m = int(sys.stdin.readline().rstrip())
  list1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
  
  list1.sort()
  maxx = m+1
  cnt = 0
  
  for a,b in list1:
    if maxx>b:
      cnt+=1
      maxx = b
      
  print(cnt)
  cnt=0
  list1=[]
