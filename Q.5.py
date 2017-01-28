#printing the words in backward order

def new():
    input = 'my name is john'
    print('input string is :',input)
    x=input.split()
    x.reverse()
    b=" ".join(x)
    return b
print('reversed string is :',new())
