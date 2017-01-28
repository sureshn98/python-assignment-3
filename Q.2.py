#returning max of three variables without using max()

def maximum():
    x=1732
    y=400
    z=560
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print('maximum value of three variables is:', maximum())
