arr=[2,5,3,7,1,2]
target=9

n=len(arr)
need=0
map={}

for i in range(n):
    need =target - arr[i]

    if need in map:
        print(map[need], ',',i)

    else:
        map[arr[i]] = i
