nums=[-1,7,2,-3,1,3,-7]

map={}
need=0
high=-1

for i in range(len(nums)):
    need = 0 -nums[i]

    if need in map:
        high =max(high,nums[i],need)

    else:
        map[nums[i]] = i

print(high)
