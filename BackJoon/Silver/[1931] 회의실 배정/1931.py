import sys

n = int(input())
time_table = []

for _ in range(n):
  s, e = map(int, input().split())
  time_table.append((s,e))

time_table.sort(key =lambda x: (x[1],x[0]))

cnt = 0
ep = 0

for s, e in time_table:
  if ep<=s:
    ep = e
    cnt+=1


print(cnt)
