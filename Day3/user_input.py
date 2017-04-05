from robot import *


def user():
    url = str(input('Enter the url of the whose information you want to know :'))
    res = get_robots_txt(url)
    return res


print(user())
