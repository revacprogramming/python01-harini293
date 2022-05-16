# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
r = 10.50
if h <= 40:
    pay = h*r
else :
    pay = 40*r
    ep = (h-40)*1.5*r
    tot = pay+ep
    
print(tot)
