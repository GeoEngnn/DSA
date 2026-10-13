# # arr =[2,5,1,10,10]

# # k=14

# # left=0
# # lenght=0
# # sum=0

# # for r in range(len(arr)):

# #     sum +=arr[r]

# #     while sum > k:
# #         sum -= arr[left]
# #         left +=1

# #     lenght =max(lenght ,r -left +1)

# # print(lenght)


# # cards =[6,2,3,4,7,2,1,7,1]

# # k=4

# # lsum ,rsum =0 ,0

# # lsum =sum(cards[:k])
# # win_Sum =lsum

# # ridx=len(cards) -1
# # for r in range(k-1 ,-1 ,-1):
# #     lsum -=cards[r]
# #     rsum +=cards[ridx]
# #     win_Sum =max(win_Sum ,lsum +rsum)
# #     ridx -= 1
    

# # print(win_Sum)


# # arr =[1,1,1,0,0,0,1,1,1,1,0]
# # k=2

# # left =0
# # count=0
# # lenght=0

# # for r in range(len(arr)):
# #     if arr[r] != 1:
# #         count +=1

# #     while count > k:
# #         if arr[left] != 1:
# #             count -=1

# #         left +=1

# #     lenght =max(lenght , r -left +1)

# # print(lenght)

# # arr =[3,3,3,1,2,1,1,2,3,3,4]
# # k=2

# # left =0
# # fruits_count =0
# # basket ={}

# # for r in range (len(arr)):

# #     if arr[r] in basket :
# #         basket[arr[r]] += 1

# #     else:
# #         basket[arr[r]] = 1

# #     while len(basket) > k :
# #         basket[arr[left]] -= 1
# #         if basket[arr[left]] == 0:
# #             del basket[arr[left]]
# #         left += 1

# #     fruits_count =max(fruits_count ,r -left + 1)

# # print(fruits_count)


# # s ='bbacba'

# # left = 0
# # numSub =0
# # cntA ,cntB ,cntC =0 ,0 ,0

# # for r in range(len(s)):

# #     if s[r] == 'b':
# #         cntB += 1
# #     elif s[r] =='a':
# #         cntA += 1
# #     else:
# #         cntC +=1

# #     while (cntA and cntB and cntC) > 0 :
# #         numSub += len(s) - r
# #         if s[left] =='b':
# #             cntB -=1
# #         if s[left] =='a':
# #             cntA -=1
# #         if s[left] =='c':
# #             cntC -=1

# #         left +=1

# # print(numSub)

# # s ='aaababbc'

# # left =0
# # lenght =0
# # max_lenght =0
# # maxfreq=0
# # map={}

# # for r in range(len(s)):
# #     if s[r] in map:
# #         map[s[r]] +=1
# #     else:
# #         map[s[r]] =1

# #     lenght +=1
# #     maxfreq =max(maxfreq ,map[s[r]])

# #     if lenght - maxfreq <=2:
# #         max_lenght =max(max_lenght, r-left +1)

# #     else:
# #         map[s[left]] -= 1
# #         left +=1
# #         lenght -=1

# # print(max_lenght)

# # def noOfBinarySubarr(nums ,goal):

# #     if goal < 0:
# #         return 0

# #     left =0
# #     cnt =0
# #     sum =0

# #     for r in range(len(nums)):
# #         sum += nums[r]

# #         while sum > goal:
# #             if nums[left] !=0:
# #                 sum -= nums[left]
# #             left += 1

# #         cnt += r -left + 1
# #     return cnt

# # def calBinarySubarr():
# #     nums = [1, 0, 1, 0, 1]
# #     goal = 2
# #     return noOfBinarySubarr(nums ,goal) - noOfBinarySubarr(nums ,goal-1)

# # print(calBinarySubarr())


# # def niceSubarr(nums ,goal):
# #     if goal < 0:
# #         return 0

# #     left =0
# #     sum =0
# #     cnt =0

# #     for r in range(len(nums)):
# #         if nums[r] %2 != 0 :
# #             sum+=1

# #         while sum > goal :
# #             if nums[left] %2 != 0 :
# #                 sum -=1

# #             left += 1

# #         cnt += r -left +1

# #     return cnt

# # def calnicSubarr():
# #     nums = [1, 1, 2, 1, 1]
# #     goal = 3
# #     return niceSubarr(nums ,goal) - niceSubarr(nums ,goal-1)

# # print(calnicSubarr())

# s='ddaaabbca'
# t='abc'

# left=0
# cnt=0
# minlenght=float('inf')
# s_idx =-1
# map={}

# for i in t:
#     if i in map:
#         map[i] += 1
#     else:
#         map[i] = 1

# for r in range(len(s)):
#     if s[r] in map and map[s[r]] > 0:
#         cnt +=1

#     if s[r] not in map:
#         map[s[r]] = -1
#     else:
#         map[s[r]] -=1

#     while len(t) == cnt :
#         if minlenght > r -left +1 :
#             minlenght =r -left +1
#             s_idx =left

#         map[s[left]] += 1
#         if s[left] in t and map[s[left]]> 0:
#             cnt -=1

#         left += 1

# print(s[s_idx:])




    

    