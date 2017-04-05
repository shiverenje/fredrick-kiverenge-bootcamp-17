
def min_max(n):
    small = min(n)
    big = max(n)
    if small == big:
        return [small]
    else:
        return [small, big]


l = [4, 66, 6, 44, 7, 78, 8, 68, -1,0]
print(min_max(l))
