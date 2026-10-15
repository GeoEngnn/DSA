arr =[6,7,8,4,1]
target =7

for i in range(len(arr)):
    if arr[i] == target:
        print(f'{target} found at index {i}')
        break

else:
    print(f'{target} not in array')