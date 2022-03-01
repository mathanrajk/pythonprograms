num=29
n1=0
n2=1
temp=0
if num<=0:
    print("its negative number")
elif num==1:
    print(n1)  

else:
    while temp<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        temp+=1    

