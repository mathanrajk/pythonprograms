lists = ["mathan", "raj"]
list2=[]
for i in lists:
    data = i.split(" ")
    if data:
       for j in data:
          for k in j:
              list2.append(k)

    print(list2[1],list2[0],i[2::])
    list2.clear()



