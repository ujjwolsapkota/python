str=input('enter a string')
str=str.lower()
list=['a','e','i','o','u']
c=0
for char in str:
    if char in list:
       c=c+1

print('vowels are',c)