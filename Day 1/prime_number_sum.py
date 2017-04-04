from timeit import time


def list_of_prime_numbers(n: object) -> object:
    y = n
    l =[]
    check = int
    if isinstance(y, check):
        start_time = time.time()
        for i in range(2, n + 1):
            if all(i % x != 0 for x in range(2, i)):
                print(i)
                endtime = time.time()
                elapse_time = endtime - start_time

        print('The running time is::', elapse_time)

    else:
        return 'Invalid Argument'


print(list_of_prime_numbers(5))
