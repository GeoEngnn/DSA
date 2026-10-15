arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]

inter=[]
j=0
i=0

while i<len(arr1) and j < len(arr2):
    if arr1[i] ==arr2[j] : 
            inter.append(arr2[j])
            j+=1
            i+=1
    elif arr1[i] < arr2[j]:
        i+=1
    else:
        j+=1
print(inter)