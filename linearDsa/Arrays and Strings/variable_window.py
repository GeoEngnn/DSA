# ## SW VARIABLE APPROACH

# arr=[2,1,5,1,3,2]
# target=7

# left=0
# window_sum=0
# lenght=0

# for right in range(len(arr)):
#     window_sum+=arr[right]

#     while window_sum>target:
#         window_sum-=arr[left]
#         left+=1
#     lenght=max(lenght,right-left+1)

# print(lenght)

# Minimum Length Subarray With Sum ≥ Target ⭐⭐
# arr=[2, 3, 1, 2, 4, 3]
# target=7

# left=0
# window_sum=0
# lenght=float('+inf')

# for right in range(len(arr)):
#     window_sum+=arr[right]

#     while window_sum >= target:
#         lenght=min(lenght,right-left+1)
#         window_sum-=arr[left]
#         left+=1

# print(lenght)

# 3. Longest Substring Without Repeating Characters ⭐⭐

# s = "abcabcbb"

# left=0
# char=''
# lenght=0

# for right in range(len(s)):
#     while s[right] in char:
#         char=char[1:]
#         left+=1

#     char+=s[right]
            
#     lenght=max(lenght,right-left+1)

# print(lenght)

## optimized method for finding the lenghot of the subarray problem.

# arr=[2,5,1,10,10]
# target=14

# left=0
# lenght=0
# win_sum=0

# for right in range(len(arr)):
#     win_sum+=arr[right]
#     if win_sum > target:
#         win_sum-=arr[left]
#         left+=1

#     if win_sum<=target :
#         lenght=max(lenght,right-left+1)

# print(lenght)