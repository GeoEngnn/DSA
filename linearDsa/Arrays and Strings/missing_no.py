# arr=[1,2,4,5]

# for i in range(1,len(arr)+1):
#     flag=0
#     for j in range(len(arr)):
#         if arr[j] == i:
#             flag=1
#             break
        
#     if flag ==0:
#         print(i) 

    
# arr=[1,2,3,4,6]
# n=6

# sum_of = (n * (n+1))//2

# arr_sum=0
# for i in arr:
#     arr_sum += i

# missing_no =sum_of -arr_sum

# print(missing_no)

# arr=[21,22,23,25,26]

# sum_of =sum(range(arr[0],arr[-1]+1))

# arr_sum=0
# for i in arr:
#     arr_sum+=i

# missing_no =sum_of -arr_sum

# print(missing_no)

arr=[1,2,3,4,6]
n=6
xor1 ,xor2 = 0, 0


for i in range(n-1):
    xor2^=arr[i]
    xor1^=(i+1)

xor1 ^=n


print(xor1^xor2)


arr=[1,2,3,4,6]





