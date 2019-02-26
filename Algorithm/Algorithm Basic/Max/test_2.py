def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if a[i] < a[0]:
            min_v = a[i]
    return min_v

v = [11,22,33,44,55,66,77]
print(find_min(v))
        
