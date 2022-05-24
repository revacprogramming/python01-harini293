# Functions



def computepay(h, r):
    if h<=40 :
        pay=h*r
        return pay
    else :
        ext_pay = (h-40)*1.5*r
        pay = ext_pay + (40*r)
        return pay
    
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("enter rate :")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)

