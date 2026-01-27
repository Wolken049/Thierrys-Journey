def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    
    return i + 1

def Quick(a, low = 0, high = None):
    if high is None:
        high = len(a) - 1
    
    if low < high:
        pivot_index = partition(a, low, high)
        Quick(a, low, pivot_index - 1)
        Quick(a, pivot_index + 1, high)
    return a