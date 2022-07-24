def inp():
    a = float(input('enter a number: '))
    return a


def add(a, b):
    return (a+b)


def main():
    a = inp()
    b = inp()
    c = add(a, b)
    print(c)
