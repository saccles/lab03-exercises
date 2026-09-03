def check(l: list):
    unique = set(l)
    
    return len(unique) != len(l)


print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False
