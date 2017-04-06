class Binary_search:
    def __init__(self, a, b):
        self.length = a
        self.difference = b


    def search(self, n):
        mydict = dict()
        count = 0
        v = [i for i in range(0, self.length, self.difference)]
        print(v)

        first = 0
        last = len(v) - 1
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2
            if v[midpoint] == n:
                found = True
            else:
                if n < v[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        if True:
            count += 1
        ind = v.index(n)
        mydict = count, ind
        return mydict


p = Binary_search(10, 2)
print(p.search(2))
