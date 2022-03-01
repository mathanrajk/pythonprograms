def sumofnum(num):
    s=str(num)
    sum=0
    for i in s:
        sum+=int(i)
    return sum        


num=int(input("enter  the number :"))
print(sumofnum(num))