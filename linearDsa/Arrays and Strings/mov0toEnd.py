# arr = [1,0,2,3,2,0,0,4,5,1]
# temp=[]

# for i in range(len(arr)):
#     if arr[i] != 0:
#         temp.append(arr[i])

# for i in range(len(temp)):
#     arr[i] = temp[i]

# for i in range(len(temp),len(arr)):
#     arr[i] = 0

# print(arr)




arr=[1,0,2,3,2,0,0,4,5,1]

left = 0
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] , arr[left] =arr[left] , arr[i]
        left+=1

print(arr)




    

        





