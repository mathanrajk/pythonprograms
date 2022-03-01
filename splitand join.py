words = "i am mathanraj and i am 23"
word = ""
resentance=""
list = []
for i in words:
    if i == " ":

        list.append(word)
        word = ""



    else:
        word += i


list.append(word)

print(list)

for i in list:
    resentance=resentance+i+" "

print(resentance)

