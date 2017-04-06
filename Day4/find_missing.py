def find_missing(n, m):
    if n == [] and m == []:
        return 0
    elif n == m:
        return 0
    else:
        return set(n) ^ set(m)


a = [5, 4, 7, 6, 11, 66]
b = [5, 4, 1, 7, 6, 11, 66]
print(find_missing(a, b))
