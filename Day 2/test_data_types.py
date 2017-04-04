def data_type(n):
    if n:
        if type(n) is str:
            return len(n)
        elif type(n) is bool:
            return n
        elif type(n) is int:
            if n < 100:
                return 'less than 100'
            else:
                return 'more than 100'
        elif type(n) is list:
            if True:
                try:
                  return n[4]
                except:
                   return 'None'
    else:
        return 'no value'

a =[1,2,3,5,5]
print(data_type(a))
