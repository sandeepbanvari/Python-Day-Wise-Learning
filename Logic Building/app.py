# Right angled triangle
# for i in range (1, 6):
#     for j in range (1, i+1):
#         print('*', end=" ")
#     print()
    
# Reverse right angled triangle
i = 1
# count = 0
while i<6:
    j = 1
    while j<6:
        if j<=i:
            print('* ', end='')
        j+=1
        print()
    i+=1
