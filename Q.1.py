#checking for a word in text file

i='the'   #word to be checked
file=open('1.txt','w+')
file.write('lets make the whole world green')
file.seek(0)
y=file.read()
print ('text in file:',y)
print('word to find :',i)
if i in y:
    print('found in file')
else:
    print('not found')
file.close






