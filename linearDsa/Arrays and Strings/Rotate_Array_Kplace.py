# arr =[1,2,3,4,5,6,7]
# k=3
# n=len(arr)

# temp=arr[:k]

# for i in range(k,n):
#     arr[i-k] =arr[i]

# for i in range(len(arr)-k,n):
#     arr[i] =temp[i-(n-k)]

# print(arr)

# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# n = len(arr)
# k %= n

# def reverse(arr,left,right):


#     while left < right :
#         arr[left],arr[right]=arr[right] ,arr[left]
#         right -=1
#         left+=1

# reverse(arr, 0, k - 1)
# reverse(arr, k, n - 1)
# reverse(arr, 0, n - 1)

# print(arr)



arr=[1, 2, 3, 4, 5, 6, 7]
n=len(arr)
k=3
k=k%n

def reverse(arr,left,right):
    while left < right:
        arr[left],arr[right] = arr[right] ,arr[left]
        right-=1
        left+=1
        

reverse(arr,0,k-1)
reverse(arr,k,n-1)
reverse(arr,0,n-1)

print(arr)


