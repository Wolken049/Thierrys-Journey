def BinarySearch(arr, target):
    lower = 0
    higher = len(arr) - 1
    
    while lower <= higher:
        mid = (lower + higher) / 2
        
        if arr == target:
            return mid
        elif arr < target:
            lower = mid + 1
        else:
            lower = mid - 1
    return -1
        