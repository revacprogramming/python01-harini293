# Files

fname = input('enter file name : ')
fhandle = open(fname,'r')
content = fhandle.read()
count,total=0,0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        text=line.split(":")
        y=float(text[1])
        total= total+y
        count+=1
avg = total/count
print('Average spam confidence:',avg)
