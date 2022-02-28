def check(a,b):
    if len(a)==len(b):
        
        for i in range(0,len(a)):
            if a[i]!=b[i]:
                return False


    else:
        return False
    return True            






list=[1,2,3,4,6]
list2=[1,2,3,4,5]
if check(list,list2):
    print("equal")
else:
    print("not equal")    

           
         


        