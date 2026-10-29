# arr=[3,1,-2,-5,2,-4]

# pos=[]
# neg=[]

# for i in arr:
#     if i > 0:
#         pos.append(i)

#     else:
#         neg.append(i)

# for i in range(len(pos)):

#     arr[2*i] = pos[i]
#     arr[2*i+1] =neg[i]

# print(arr)


# arr=[3,1,-2,-5,2,-4]

# nums=[0] * len(arr)

# neg=1
# pos=0

# for i in range(len(arr)):
#     if arr[i] > 0:
#         nums[pos] =arr[i]
#         pos+=2

#     else:
#         nums[neg] = arr[i]
#         neg+=2

# print(nums)



arr=[-1,2,3,4,-3,1]

pos=[]
neg=[]

for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

if len(neg) < len(pos):
    for i in range(len(neg)):
        arr[2*i] =pos[i]
        arr[2*i+1]=neg[i]

    idx=2*len(neg)
    for i in range(len(neg),len(pos)):
        arr[idx] =pos[i]
        idx+=1

else:
    for i in range(len(pos)):
        arr[2*i] =pos[i]
        arr[2*i+1]=neg[i]
    
        idx=2*len(pos)
        for i in range(len(pos),len(neg)):
            arr[idx] =neg[i]



print(arr)




