#text files overlapping

j=[]
file1=open('text1.txt')
y=file1.readline()
while y:
    j.append(int(y))
    y=file1.readline()

k = []
file2=open('text2.txt')
v = file2.readline()
while v:
    k.append(int(v))
    v = file2.readline()

l=[]
for object in j:
    if object in k:
        l.append(object)
print(l)
file1.close()
file2.close()
