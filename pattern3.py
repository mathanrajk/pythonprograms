num=input("ener the number of row : ")
l=len(num)
for i  in range(l):
    for j in range(i+1):
        print(num[j],end=" ")
    print()  

