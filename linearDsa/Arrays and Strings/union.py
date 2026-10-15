arr = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

i = 0
j = 0
union = []

while i < len(arr) and j < len(arr2):
    if arr[i] < arr2[j]:
        if not union or union[-1] != arr[i]:
            union.append(arr[i])
        i += 1

    elif arr[i] > arr2[j]:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    else:
        if not union or union[-1] != arr[i]:
            union.append(arr[i])
        i += 1
        j += 1

while i < len(arr):
    if not union or union[-1] != arr[i]:
        union.append(arr[i])
    i += 1

while j < len(arr2):
    if not union or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1

print(union)