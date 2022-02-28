from array import array


array=[4,6,2,9,7,0,9,10]
print(array)

temp=0
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp

print(array)