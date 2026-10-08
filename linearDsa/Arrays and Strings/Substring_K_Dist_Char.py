# s='aaabbccd'
# k=2

# left=0
# lenght=0
# map={}

# for right in range(len(s)):
#     if s[right] in map:
#         map[s[right]] += 1
#     else:
#         map[s[right]] = 1

#     if len(map) > k:   ## We use if here as assuming that the next lenght w find should be greater than current one not lesser so we remove one and in the next iteration add one so the window lenght remains the same 
#         map[s[left]] -= 1
#         if map[s[left]] == 0:
#             del map[s[left]]

#         left+=1

#     lenght=max(lenght,right-left+1)
# print(lenght)