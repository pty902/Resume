def square(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s

print(square(10)) # O(n)

def square2(n):
    return n * (n + 1) * (n*2 + 1) // 6

print(square2(10)) # O(1)    

    
