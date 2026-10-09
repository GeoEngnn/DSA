def subArr(nums ,k):

    left = 0
    cnt =0
    map={}

    for r in range(len(nums)):

        if nums[r] in map:
            map[nums[r]] += 1

        else:
            map[nums[r]] = 1

        while len(map) > k:
            map[nums[left]] -= 1
            if map[nums[left]] == 0:
                del map[nums[left]]
            left += 1

        cnt += r - left +1

    return cnt 

def calSubarr():
    nums=[1,2,1,3,4]
    k=3

    return subArr(nums ,k) - subArr(nums ,k-1)

print(calSubarr())