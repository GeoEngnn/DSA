## BRUTE FORCE SLIDING WINDOW FIXED MASK(WINDOW)

# arr=[-1,2,3,3,4,5,-1]
# k=int(input('Enter the window value:'))

# max_sum = float("-inf")
# if len(arr)>=k:
#     for i in range(len(arr)-k+1):
#         curr_sum = 0
#         for j in range(k):
#             curr_sum+=arr[i+j]
#         max_sum=max(max_sum,curr_sum)

# else:
#     print('Array has insufficient elements')

# print(max_sum)


## OPTIMAL SW (FIXED)

# arr=[-1,2,3,3,4,5,-1]
# k=int(input('Enter the window value:'))

# if len(arr)<k:
#     print("Invalid")

# else:
#     window_sum=sum(arr[:k])
#     max_sum=window_sum

#     for i in range(len(arr)-k):
#         window_sum=window_sum-arr[i]+arr[i+k]
#         max_sum=max(window_sum,max_sum)

# print(max_sum)



1.# Find the maximum sum of any k consecutive elements.
# Given:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# OPTIMAL SOLUTION:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# if len(arr)<k:
#     print('Array contain insufficient elements')

# else:
#     window_sum=sum(arr[:k])
#     max_sum=window_sum

#     for i in range(n-k):
#         window_sum=window_sum-arr[i]+arr[i+k]
#         max_sum=max(max_sum,window_sum)

#     print(max_sum)

# Maximum Average of K Consecutive Elements

# Given:

# arr = [1, 12, -5, -6, 50, 3]
# k = 4

# arr = [1, 12, -5, -6, 50, 3]
# k = 4

# if len(arr)<k:
#     print('Invalid')

# else:
#     window_sum=sum(arr[:k])
#     window_avg=window_sum/k
#     max_avg=window_avg

#     for i in range(len(arr)-k):
#         window_sum=window_sum-arr[i]+arr[i+k]
#         window_avg=window_sum/k
#         max_avg=max(window_avg,max_avg)
#     print(max_avg)
        
# Count Even Numbers in Every Window ⭐⭐

# Given:

# arr = [2, 3, 4, 5, 6, 7, 8]
# k = 3

# arr = [2, 3, 4, 5, 6, 7, 8]
# k = 3

# if len(arr)<k:
#     print('Invalid')

# else:
#     even_window=0
#     max_count=[]
#     for i in arr[:k]:
#         if i%2==0:
#             even_window+=1
#     max_count.append(even_window)

#     for j in range(len(arr)-k):
#         if arr[j]%2==0:
#             even_window-=1
#         if arr[j+k]%2==0:
#             even_window+=1
#         max_count.append(even_window)

#     print(max_count)


# Maximum Number of Vowels in a Substring of Length K ⭐⭐

# Given:

# s = "abciiidef"
# k = 3
        
# s="abciiidef"
# k=3

# if len(s)<k:
#     print('Invalid')

# else:
#     vowels='aeiou'
#     vowel_count=0
#     for i in s[:k]:
#         if i in vowels:
#             vowel_count+=1
#     max_count=vowel_count

#     for j in range(len(s)-k):
#         if s[j] in vowels:
#             vowel_count-=1
#         if s[j+k] in vowels:
#             vowel_count+=1
#         max_count=max(max_count,vowel_count)

# print(max_count)


# First Negative Number in Every Window ⭐⭐⭐

# Given:

# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3


from collections import deque

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

if len(arr) < k:
    print("Invalid")

else:
    negative_arr = []
    q = deque()

    for i in range(len(arr)):

        # Add negative element
        if arr[i] < 0:
            q.append(i)

        # Remove elements outside current window
        while q and q[0] <= i - k:
            q.popleft()

        # Start recording once we have a complete window
        if i >= k - 1:
            if q:
                negative_arr.append(arr[q[0]])
            else:
                negative_arr.append(0)

    print(negative_arr)









