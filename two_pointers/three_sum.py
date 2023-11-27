# 3 Sum 
def three_sum(arr, target):
    arr.sort()
    for i in range(len(arr)-1):
        j = i+1
        k = len(arr) - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] == target:
                return True
            elif arr[i] + arr[j] + arr[k] < target:
                j += 1
            else:
                k -= 1
            
    return False

arr = [3,7,1,2,8,4,5]
print("1:" , three_sum(arr, 18))

arr1 = [3,7,2,4]
print("2:" , three_sum(arr1, 21))

arr2 = [3,7,2]
print("3:" , three_sum(arr2, 12))

arr3 = [3,7,2]
print("4:" , three_sum(arr3, 2))

arr3 = [3,2]
print("5:" , three_sum(arr3, 2))