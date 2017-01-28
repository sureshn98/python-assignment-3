#new list with unique elements of current list

list=['1','1','2','a','s','a','3','d']
def newlist():
    j=[]
    for i in list:
        if i not in j:
            j.append(i)
    return j
print(newlist())
