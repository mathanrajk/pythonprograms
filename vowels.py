from itertools import count


vowels=["a","e","i","o","u"]
count=0
word="mathan"

for i  in word:
    if(i in vowels):
        count=count+1
      
print(count)

