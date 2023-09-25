def zero(op = lambda x: x):
    return op(0)
def one(op = lambda x: x):
    return op(1)
def two(op = lambda x: x):
    return op(2)
def three(op = lambda x: x):
    return op(3)
def four(op = lambda x: x):
    return op(4)
def five(op = lambda x: x):
    return op(5)
def six(op = lambda x: x):
    return op(6)
def seven(op = lambda x: x):
    return op(7)
def eight(op = lambda x: x):
    return op(8)
def nine(op = lambda x: x):
    return op(9)

def plus(num1):
    return lambda num2: num2 + num1
def minus(num1):
    return lambda num2: num2 - num1
def times(num1):
    return lambda num2: num2 * num1
def divided_by(num1):
    return lambda num2: num2 // num1
