def add(a,b):
    return (a+b)
    

def output(a, b):
    print(a,'+',b,'is',sum)

def input_two_numbers():
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    return(a,b)

def main():
    a, b = input_two_numbers()
    sum = add(a, b)
    output(a, b)
    print(sum)

if __name__ == '__main__':
    main()
