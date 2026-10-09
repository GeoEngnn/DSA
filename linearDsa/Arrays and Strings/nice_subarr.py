def niceSubarr(nums,k):
    if k < 0:
        return 0
    
    left=0
    sum=0
    cnt=0

    for r in range(len(nums)):
        if nums[r] % 2 != 0:
            sum += 1

        while sum > k:
            if nums[left] %2 !=0:
                sum-=1
            left +=1 

        cnt += r -left + 1

    return cnt

def countSubarr():
    nums=[1,1,2,1,1]
    k=3
    return niceSubarr(nums,k) - niceSubarr(nums,k-1)

print(countSubarr())


    