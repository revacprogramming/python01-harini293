# Loops & Iterators

largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
        x=num
        if x>largest :
            largest=x
        if x<smallest :
            smallest=x
        

print("Maximum", largest)
