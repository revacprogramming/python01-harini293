# Conditional Execution 1

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


# Conditional Execution 2

score = input("Enter Score: ")
score = float(score)

if score >= 0.9 and score <= 1.0 :
    print('A')
elif score >= 0.8 and score < 0.9 : 
    print('B')
elif score >= 0.7 and score < 0.8 :
    print('C')
elif score >= 0.6 and score < 0.7 :
    print('D')
elif score < 0.6 and score >= 0.0 :
    print('F')
else :
    print('enter valid message')

