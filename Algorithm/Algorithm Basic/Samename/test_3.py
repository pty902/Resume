def two_name(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i + 1, n):
            print(a[i], "-", a[j])

name = ["Tome", "Jerry", "Mike"]
two_name(name)
print()
name2 = ["Tome", "Jerry", "Mike", "John"]
two_name(name2)      
            
