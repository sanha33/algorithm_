'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))  #인덱스 번호를 return 해줌.
print(tmp.count('T'))  #T가 몇개 있는지
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))  #공백 포함 문자 길이

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')

for x in msg:
    if x.islower ():
        print(x, end=' ')


for x in msg:
    if x.isalpha():  # 알파벳인지 아닌지 
        print(x, end=' ')


tmp='AZ'

for x in tmp:
    print(ord(x))  # 아스키 넘버를 출력 (65~90)


tmp='az'
for x in tmp:
      print(ord(x)) 

tmp=66
print(chr(tmp))
