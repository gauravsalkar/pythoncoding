def three_colors(arr):
    i=0
    l=0
    r=len(arr)-1
    while i<=r:
        if arr[i] == 0:
            arr[l],arr[i] = arr[i],arr[l]
            i += 1
            l += 1
        elif arr[i] == 2:
            arr[r],arr[i] = arr[i],arr[r]
            r -= 1
        else:
            i += 1

arr = [2,1,0,1,1,0,2,2,0,1,0,0,2,1]
three_colors(arr)
print(arr)

arr1 = [2,2,2,0,0,0,1,1,1]
three_colors(arr1)
print(arr1)

arr2 = [0,0,2,2,1,1,1,1,1,1,1]
three_colors(arr2)
print(arr2)