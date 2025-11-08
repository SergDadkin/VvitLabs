x =int(input())
print("___")
for i in range(1,x+1):
    print(i)

import re
x1=input('Число1=')
x2=input('Число2=')
n1=re.findall(r'-?\d+',x1)
n2=re.findall(r'-?\d+',x2)
s1=int(n1[0]) if n1 else 0
s2=int(n2[0]) if n2 else 0
if s1>s2:
    print(s1)
elif s1<s2:
    print(s2)
else:
    print(f'{s1}={s2}')
    