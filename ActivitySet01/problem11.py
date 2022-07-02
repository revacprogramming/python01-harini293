# Tuples

fname=input('enter file name :')
fhandle=open(fname,'r')
hours=[]
count=dict()
for line in fhandle:
    if line.startswith('From '):
        lst=line.split()
        time=lst[5]
        time=time.split(':')
        hours.append(time[0])
for num in hours:
    if num not in count:
        count[num]=1
    else :
        count[num]+=1
t=list(count.items())
t.sort()
for key,value in t:
    print(key,value)
 
