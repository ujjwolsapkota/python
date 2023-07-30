line=input('enter a string')
i=0
while i<len(line):
    if line[i]=='a':  #breaks when a is founded
        break
    else:
        print('the character is',line[i])
    i=i+1

print('LOOP ENDED')