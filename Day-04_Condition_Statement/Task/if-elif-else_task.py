# Practice Task: Electricity Bill Calculator
# | Units Consumed  | Bill Amount |
# | --------------- | ----------- |
# | 0 – 100 units   | ₹2 per unit |
# | 101 – 200 units | ₹3 per unit |
# | 201 – 500 units | ₹5 per unit |
# | Above 500 units | ₹7 per unit |


units = int(input("Enter units consumed: "))
if units> 0 and units <=100:
    bill = units * 2
    print('Bill amount:', bill)
elif units<=200 and units>100:
    print('Bill amount:', units * 3)
elif units<=500 and units>200:
    print('Bill amount:', units * 5)
elif units>500:
    print('Bill amount:', units * 7)
else:
    print('Enter a valid number of units.')
    
    
