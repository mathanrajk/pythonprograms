def replaceword(a,b,c):
    list=a.split()
    
    for i in list:
        if b==i:
            print(c,end=" ")
            break
        else:
            print(i,end=" ")    




words="hello i am mathan , i am 23 , i am from trichy "
now="i"
then="e"
print(replaceword(words,now,then))

