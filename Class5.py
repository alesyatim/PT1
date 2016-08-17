from pack import *
print(globals())

a = 1
print(a)
def plus():
    # global a
    # a+=1
    globals()['a'] += 1
    globals()['b'] = 100

plus()
print(a)
print(b)

