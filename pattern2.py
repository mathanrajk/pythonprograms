num= int(input("ener the number of row : "))
for i  in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()   


print("========================================")


for i  in range(num):
    for j in range(num):
        if j==0 or i==num-1 or i==j:
            print("*",end="")

        else:
            print(end=" ")
    print()        