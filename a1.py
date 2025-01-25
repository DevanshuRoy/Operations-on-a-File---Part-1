fo=open("generated.txt")
l=fo.readline()
c=0
while l:
    c+=1
    l=fo.readline()
fo.close()
print("Total number of lines: ",c)

fo=open("generated.txt")
l=fo.readline()
print(l) # extra line under
l=fo.readline()
print(l.rstrip()) #'r' in strip means right side /n will be removed
l=fo.readline()
print(l,end=" ")
fo.close()

fileObj=open("random.txt")
classFo=fileObj.readlines() # reads multiple lines together
print("Total number of lines = ",len(classFo))

# count the lines starting with 'the'
fo=open("generated.txt")
L=fo.readline()
c=0
while L:
    if L.startswith("Lorem"):
        c+=1
    L=fo.readline()

fo.close()
print("Lines starting with the word 'Lorem : '",c)

# count the lines containing "the"
fo=open("generated.txt")
fo2=open("largeLines.txt",'a')
L=fo.readline()
c=0
while L:
    Li=L.strip().split()
    for w in Li:
        if w=="Lorem":
            c+=1
    if len(Li)>5:
        fo2.write(L)
    L=fo.readline()

fo.close()
print("Lines with the word 'Lorem' : ",c)