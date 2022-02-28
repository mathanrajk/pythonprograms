import string


def largeword(string):
    l=0
    w=""
    words=string.split(" ")
    for word in words:
        if len(word)>l:
            w=word
            l=len(word)
    return(w,l)        


string = input("enter the sentance :")  
w,n=largeword(string)
print("largest word in sentance :",w)
print("lenght of word is : ",n)