# arr=[2,2,3,3,1,2,2]

# n=len(arr)
# half = n//2
# major=-1
# map={}

# for i in range(n):

#     if arr[i] not in map:
#         map[arr[i]] = 1

#     else:
#         map[arr[i]] += 1


# for i in map:
#     if map[i] > half:
#         major=i

# print(major)



arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]

el=0
cnt=0
cnt1=0

for i in range(len(arr)):

    if cnt < 1:
        el=arr[i]
        cnt+=1

    elif cnt > 0:
        if el == arr[i]:
            cnt +=1

        else:
            cnt -=1 

for i in range(len(arr)):
    if el==arr[i]:
        cnt1+=1

if cnt1 > len(arr)/2:
    print(el)
else:
    print('No elements')