#find the the largest item in list with for

l1=[700,312,4,124,5,56,64,54,5,500]
max=l1[0]
for x in l1:
    if x>max:
        max=x
print("the max element equal :",max)