import sys

grade = {'A+': 4.5, 'A0': 4.0, 'B+'	:3.5,'B0':	3.0, 'C+': 2.5,'C0':	2.0,'D+':	1.5,'D0':	1.0, 'F':	0.0}
cnt = 0.0
sum = 0.0

for _ in range(20):
  n, p, g = input().split()
  if g != 'P':
    cnt+=float(p)
    sum += float(p)*grade[g]

print(sum/cnt)
