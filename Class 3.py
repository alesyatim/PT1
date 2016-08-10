L = 'Namespaces are one honking great idea -- let\'s do more of those!'
d = {}
for letter in  set(L):
      d[letter] = L.count(letter)


keys = sorted(d, key=lambda x: d[x])
for key in keys:
    print('{}={}'.format(key,d[key]))


def printer(x, y):
    print(x)

printer(y=1, x ='b')
########################
def whisper(word):
    print(word.lower())

def shout(word):
    print(word.upper() + '!!!!')

def say(volume, word='I am talking'):
    volume(word)

time =1
method = shout
for hour in range(10):
    if  hour > 5:
        method = whisper
    say(method)


if time > 9:
    method = whisper



say(shout)
say(whisper, word='HEY!!!!')



#####################################
L = ['one', 'two', 'three']
D = {'1': 2, '3': 4}
def catcher(*args, **kwargs):
    print(args)
    print(type(args[0]))
    print(kwargs)

catcher(L, d=D)
catcher(*L, **D)
#catcher(1,2,3, one=1, two='two')
########################
def hey():
    print('Hey!')

def catcher(*args):
    for _ in args:
        if callable(_):
            print('Cotta function!')
            _()
        else:
            print(_)


catcher(1,2,3, hey)
#####################

#def hey(x):
#    x(x)

#hey(hey)

###################
def f(a, L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)

def f(a, b, L={}):
    L[a] = b
    return L
print f('1', 1)
print f('2', 2)
print f('3', 3)

#########################
def f():
    yield(1)
    yield(2)
    yield(3)
    yield(4)
    yield(0)
    yield(7)

a = f()
l=[]
print(l)
l2=list(f())
print(l2)

l = [_ for _ in f() if _>2 ]
print(l)
l = (_ for _ in f() if _>2 )
print(l)
print(l.next())

# l={k:v for k,v in a}

