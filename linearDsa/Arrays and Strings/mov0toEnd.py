arr = [1,0,2,3,2,0,0,4,5,1]
temp=[]

for i in range(len(arr)):
    if arr[i] != 0:
        temp.append(arr[i])

for i in range(len(temp)):
    arr[i] = temp[i]

for i in range(len(temp),len(arr)):
    arr[i] = 0

print(arr)
