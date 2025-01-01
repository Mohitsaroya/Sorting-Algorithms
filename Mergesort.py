def mergesort(lst):
    list_length = len(lst)
    start = lst[0 : list_length//2]
    end = lst[list_length//2 : list_length]
    
    if len(start) == 1:
        return start[0], end[0] 
    start = mergesort(start)
    
    if len(end) == 1:
        return end[0], start[0]
    end = mergesort(end)
    
    return merge(start, end)
    
def merge(start, end):
    result = []
    i = j = 0
    
    while i < len(start) and j < len(end):
        if start[i] < end[j]:
            result.append(start[i])
            i += 1
        else:
            result.append(end[j])
            j += 1
    
    result.extend(start[i:])
    result.extend(end[j:])
    
    return result
    
print(mergesort([1, 3, 2, 4, 5, 7, 6, 8]))