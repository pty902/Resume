def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n

print(sum_n(10))
print(sum_n(100))

def find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))
        
