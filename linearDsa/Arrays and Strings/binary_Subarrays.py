def noSubarr(nums,goal):
    
    if goal < 0:
        return 0

    left=0
    sum=0
    cnt=0

    for i in range(len(nums)):

        sum += nums[i]

        while sum > goal :
            sum -= nums[left]
            left +=1 

        cnt += i-left +1

    return cnt

def calSubarr():
    nums=[1, 1, 0, 1, 0, 0, 1]
    goal = 3
    
    return noSubarr(nums,goal) -noSubarr(nums,goal-1)

print(calSubarr())

