s='cadbzabcd'

lenght=0
char=''
left=0

for right in range(len(s)):
    while s[right] in char:
        char=char[1:]
        left+=1

    char+=s[right]
    lenght=max(lenght,right-left+1)

print(lenght)


    