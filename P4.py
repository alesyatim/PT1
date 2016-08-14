def sum_integers(*args):
    return reduce(lambda sum, x: sum+x, [arg for arg in args if type(arg) in [int] ], 0)

def spam(number):
    # return ''.join(['egg' for i in range(number+1)]) # 1
    return 'egg'*number # 2

if __name__ == '__main__':
    print(sum_integers(1, 2, 3, 4, 'j', 5))
    print(spam(8))