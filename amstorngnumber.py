import numbers


numbers =int(input("enter the number"))
l=len(str(numbers))
sum=0
temp=numbers
while temp>0:   
    dig=temp%10
    sum+=dig**l
    temp=temp//10

if numbers == sum:
    print("ok")
else:
     print("not")        
