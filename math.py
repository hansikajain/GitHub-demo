# Addition
def add(x,y):
    pass

# Subtraction
def subtract(x,y):
    return x-y       #on master branch

# Mutliplication
def mutiply(x,y):
    return x*y      #On bug456 branch

# Division
def divide(x,y):        #on bug 789
    if(y==0):
        return DIVIDE_BY_ZERO_ERROR

    else:
        return x/y 

#Square
def square(x):
    return x*x
