def Quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        
        less = []
        for i in lst[1:]:
            if i <= pivot:
                less.append(i)
        
        greater = []
        for i in lst[1:]:
            if i > pivot:
                greater.append(i)
        
        return Quicksort(less) + [pivot] + Quicksort(greater)

print(Quicksort([64, 34, 25, 12, 22, 11, 90]))