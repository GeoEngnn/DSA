# arr=[2,5,1,10,10]
# k=14

# left=0
# max_sum=0
# lenght=0

# for r in range(len(arr)):
#     max_sum +=arr[r]

#     while max_sum > k:
#         max_sum -= arr[left]
#         left +=1

#     lenght =max(lenght,r-left+1)

# print(lenght)

    
# cards =[6,2,3,4,7,2,1,7,1]
# k=4

# left=0
# l_sum ,r_sum =0,0

# l_sum =sum(cards[:k])
# max_sum=l_sum

# r_idx=len(cards) -1
# for r in range(k):
#     l_sum -=cards[left]
#     r_sum +=cards[r_idx]

#     max_sum=max(max_sum,l_sum+r_sum)
#     r_idx -=1
#     left+=1

# print(max_sum)

# arr=[1,1,1,0,0,0,1,1,1,1,0]
# k=2

# count=0
# left=0
# lenght=0

# for r in range(len(arr)):
#     if arr[r] < 1:
#         count+=1

#     while count > k:
#         if arr[left] < 1:
#             count-=1
#         left+=1

#     lenght=max(lenght,r-left+1)

# print(lenght)

# arr=[3,3,3,1,2,1,1,2,3,3,4]
# k=2

# map={}
# count=0
# left=0

# for r in range(len(arr)):
#     if arr[r] in map:
#         map[arr[r]] += 1
#     else:
#         map[arr[r]] =1

#     while len(map) > k:
#         map[arr[left]] -=1
#         if map[arr[left]] ==0:
#             del map[arr[left]]

#         left+=1

#     count=max(count,r-left+1)

# print(count)



# s='bbacba'

# left=0
# count=0
# cntA,cntB,cntC=0,0,0
# n=len(s)


# for r in range(len(s)):
#     if s[r] =='a':
#         cntA+=1
#     elif s[r] =='b':
#         cntB+=1

#     else:
#         cntC +=1

#     while cntA > 0 and cntB > 0 and cntC > 0:
#         count +=n-r
#         if s[left] =='a':
#             cntA -=1
#         elif s[left] =='b':
#             cntB -=1
#         else:
#             cntC -=1

#         left+=1

# print(count)


# s='aaababbc'
# k=2

# left=0
# maxfreq=0
# lenght=0
# maxlen=0
# map={}

# for r in range(len(s)):
#     if s[r] not in map:
#         map[s[r]] =1
#     else:
#         map[s[r]] += 1

#     maxfreq=max(maxfreq,map[s[r]])
#     lenght+=1

#     if lenght -maxfreq <=k:
#         maxlen=max(maxlen,r-left+1)

#     else:
#         map[s[left]] -=1
#         lenght -=1
#         left+=1

# print(maxlen)


# def noSubarr(nums,goal):

#     if goal < 0:
#         return 0

#     left=0
#     sum=0
#     cnt=0

#     for r in range(len(nums)):
#         if nums[r] !=0:
#             sum+=1

#         while sum > goal :
#             if nums[left] !=0:
#                 sum-=1
#             left+=1

#         cnt +=r -left +1

#     return cnt

# def calSub():
#     nums = [1,0,1,0,1] 
#     goal = 2

#     return noSubarr(nums,goal) - noSubarr(nums,goal-1)

# print(calSub())




# def nycSub(arr,k):
#     left=0
#     sum=0
#     cnt=0

#     for r in range(len(arr)):
#         if arr[r] %2 == 1:
#             sum+=1

#         while sum > k :
#             if arr[left] %2 ==1:
#                 sum -=1
#             left+=1

#         cnt +=(r-left+1)

#     return cnt

# def calnyc():
#     arr=[1,1,2,1,1]
#     k=3
#     return nycSub(arr,k) - nycSub(arr,k-1)

# print(calnyc())



    







# s='ddaaabbca'
# t='abc'

# map={}
# minlen=float('-inf')
# left=0
# sidx=-1
# cnt =0

# for i in t:
#     if i not in map:
#         map[i] =1
#     else:
#         map[i] +=1

# for r in range(len(s)):
#     if s[r] in map and map[s[r]] > 0:
#         cnt+=1
#     if s[r] not in map:
#         map[s[r]] =-1
#     else:
#         map[s[r]] -=1

#     while cnt ==len(t):
#         if minlen > r-left+1:
#             minlen =r-left+1
#             sidx=left

#         map[s[left]] +=1
#         if map[s[left]] in map and map[s[left]] > 0:
#             cnt-=1
#         left+=1


# s=[1,2,3,4,4,5,4,5]

# largest=s[0]
# s_large=-1

# for i in range(1,len(s)):
#     if s[i] > largest:
#         s_large=largest
#         largest=s[i]

# print(s_large)


# arr=[1,2,3,2,4,4,6]

# for i in range(len(arr)-1):
#     if arr[i] <= arr[i+1]:
#         sorted='True'

#     else:
#         sorted ='False'
#         break

# print('Sorted:',sorted)

# arr=[1,1,2,2,2,3,3,3]

# left=0

# for r in range(1,len(arr)):

#     if arr[r] !=arr[left]:
#         left+=1
#         arr[left] ,arr[r] =arr[r] ,arr[left]
#     k=left+1

# print(arr,k)

# arr=[1,0,2,3,2,0,0,4,5,1]

# left=0

# for r in range(len(arr)):
#     if arr[r] !=0:
#         arr[left] ,arr[r] =arr[r] ,arr[left]
#         left+=1

# print(arr)


# arr=[0,1,2,3,5]
# sums=sum(range(arr[0],arr[-1]+1))
# print(sums)
# arr_sum=0

# for i in arr:
#     arr_sum += i

# print(sums-arr_sum)

# arr=[0,1,2,3,5]
# xor1 , xor2 = 0 , 0

# for i in range(len(arr)):
#     xor1 ^= arr[i]
#     xor2 ^=i

# xor2^=arr[-1]

# print(xor2^xor1)


# arr1=[1,1,2,3,4,5]
# arr2=[2,3,4,4,5,6]

# union=[]

# i ,j =0 ,0

# while i<len(arr1) and j<len(arr2):
#     if arr1[i] < arr2[j]:
#         if not union or union[-1] != arr1[i]:
#             union.append(arr1[i])
#         i+=1

#     elif arr1[i] > arr2[j]:
#         if not union or union[-1] != arr2[j]:
#             union.append(arr2[j])
#         j+=1
#     else:
#         if not union or union[-1] != arr1[i]:
#             union.append(arr1[i])
#         i+=1
#         j+=1

# while i<len(arr1):
#     if not union or union[-1] != arr1[i]:
#         union.append(arr1[i])
#     i+=1
# while j<len(arr2):
#     if not union or union[-1] != arr1[j]:
#         union.append(arr2[j])
#     j+=1 

# print(union)

# def leftRot():
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     k = 3

#     if len(arr)==0:
#         return 0
    
#     k=k%len(arr)
    

#     def reverse(left,right):
#         while left < right:
#             arr[left] ,arr[right] = arr[right] , arr[left]
#             left+=1
#             right-=1

#     reverse(0,k-1)
#     reverse(k,len(arr)-1)
#     reverse(0,len(arr)-1)
#     return arr

# print(leftRot())


    







    

    

        










