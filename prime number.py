num=int(input("/ enter the number/"))

value=False

if 1>num:
    for i in range(2,num):
        if num%i==0:
            value=True
            break    

if value:
    print("it given value is not prime number")
else:
    print("its given value  is    number")   