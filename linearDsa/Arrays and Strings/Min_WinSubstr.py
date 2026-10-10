s= 'ddaaabbca'

t='abc'

left=0
cnt=0
map={}
minlen=float('+inf')
s_idx=0

for i in t:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1


for r in range(len(s)):

    if s[r] in map and map[s[r]] > 0:
        cnt += 1


    if s[r] not in map:
        map[s[r]] = -1

    else:
        map[s[r]] -= 1

    while cnt == len(t):
        if minlen > r -left + 1:
            minlen = r -left + 1
            s_idx = left
        map[s[left]] += 1
        if s[left] in t and map[s[left]] > 0:
            cnt -= 1
        left += 1

print(minlen ,s[s_idx:])
        


      