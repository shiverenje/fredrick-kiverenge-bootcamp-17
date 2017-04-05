def wordcount(n):
    counter = {}
    words = n.split()

    v = [x for x in words]
    for each in v:
        if each in counter:
            counter[each] += 1
        else:
            counter[each] = 1
    return counter


n = 'one fish two fish red fish blue fish'
print(wordcount(n))





