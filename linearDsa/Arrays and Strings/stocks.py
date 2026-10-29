arr=[7,1,5,3,6,4]

buy=arr[0]
profit=0
sell=0

for i in range(1,len(arr)):
    sell = arr[i] - buy

    profit = max(profit ,sell)

    buy = min(buy ,arr[i])

print(profit)