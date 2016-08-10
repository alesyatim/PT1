import mymodule
import sys
from mymodule import other  as mo

print('Local module {}'.format(__name__))
#print(sys.path)
# sys.path.append('/tmp')
# sys.path.append(1, '/tmp')

# print(dir(mymodule))
# print(mymodule.__doc__)
# print(help(mymodule))

a = mymodule.l
print(a)
mymodule.other()
print(mymodule.l.append('123'))
print(mymodule.l)
# print(mymodule.__dict__)

