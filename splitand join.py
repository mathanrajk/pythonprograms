
def splits(string):
    word = ""
    list = []
    for i in string:
        if i == " ":
            list.append(word)
            word = ""

        else:
            word += i
    list.append(word)
    return list

def joins(lists):
    joinwords=""
    for i  in lists:
        joinwords=joinwords+i+" "
    return joinwords


string="i mathan raj and i am 24"
a = splits(string)
print(a)
b = joins(a)
print(b)




