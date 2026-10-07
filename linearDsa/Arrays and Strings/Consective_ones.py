arr=[1,1,1,0,0,0,1,1,1,1,0]
k=2

left=0
lenght=0
count=0

for right in range(len(arr)):

    if arr[right] != 1:
        count+=1

    while count > k:
        if arr[left] != 1:
            count -=1
        left+=1

    lenght=max(lenght,right-left+1)

print(lenght)