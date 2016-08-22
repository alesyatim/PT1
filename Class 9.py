import time

class Logger(object):
    __instance = None
    def __new__(self):
        if self.__instance == None:
            self.__instance = self
            return self
        else:
            self = self.__instance
            return self

    def __init__(self, path='/'):
        self.path = path

log1 = Logger()
log1.path = '/tmp'
log2 = Logger()
log2.path = '/s'
log3 = Logger()
print(id(log1), id(log2), id(log3))
print(log1.path, log2.path, log3.path)


def whisper(x):
    def wrapper_function(word):
        x(word.lower() + '!')
    return wrapper_function

@whisper
def say_smth(word):
    print(word)

say_smth('Hey')