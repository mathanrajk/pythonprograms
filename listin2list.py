list1 =[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5,9]
for i in range(0,len(list2)):
    if list1[i]==list2[i]:
         print(list2[i],"is prestent")
    else:
        print(list2[i],"is not prestent")   
