# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
fname=input('enter file name')
fhandle=open(fname,'r')
sum=0
count=0
for line in fhandle:
    line=line.rstrip()
    num=re.findall('[0-9]+',line)
    if len(num)>0:
        for value in num:
            count+=1
            sum=int(value)+sum
print(sum)
print(count)
