## USE DNF ALGO

arr=[0,2,0,1,1]

n=len(arr)
low=0
mid=0
high=n-1

for i in range(n):

    if mid <= high:

        if arr[mid] < 1:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            low+=1
            mid+=1

        elif arr[mid] == 1:
            mid +=1

        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1



print(arr)

