arr=[-2,-3,4,-1,-2,1,5,-3]

maxi=float('-inf')
sum=0
st_idx = 0
start = 0
end_idx = 0

for i in range(len(arr)):
    if sum == 0:
        st_idx=i

    sum+=arr[i]

    if maxi < sum:
        maxi=max(sum,maxi)
        start=st_idx
        end_idx=i

    if sum < 0:
        sum=0

print(maxi)
    