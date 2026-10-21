arr=[1,1,0,1,1,1,0,1,1]

max_sum,sum=0 ,0
left=0

for i in range(len(arr)):
    sum+=arr[i]
    if arr[i] < 1:
        sum=0
    max_sum =max(max_sum,sum)

print(max_sum)
