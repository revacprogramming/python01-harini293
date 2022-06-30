# Lists

fname = input("Enter file name: ")
fh = open(fname,'r')
string=list()
for line in fh:
    content=line.split()
    for word in content: 
        if not word in string:
           string.append(word)
string.sort()
print(string)
    
