from datetime import datetime
import time

CACHE = dict()

def timer(arg):
    print(arg)
    def outer(func):
        def inner(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return inner
    return outer


def register(func):
    CACHE[func.__name__] = func
    return func

def time_class(cls):
    class NewCls:
        def __init__(self,*args,**kwargs):
            self.oInstance = cls(*args,**kwargs)
        def __getattribute__(self,s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return timer(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls
#@register
#@timer(datetime.now())
def addID(original_class):
    orig_init = original_class.__init__
    # Make copy of original __init__, so we can call it without recursion

    def __init__(self, id, *args, **kws):
        self.__id = id
        self.getId = getId
        orig_init(self, id *args, **kws) # Call the original __init__


    def getId(self):
        return self.__id

    original_class.__init__ = __init__ # Set the class' __init__ to the new one
    return original_class

@addID
#@time_class
class Car:
    def __init__(self, id):
        self.id = id


    def move(self):
        print('start moving')
        time.sleep(3)
        print('finish')


#c = Car(13)
#c.move()




#print(iterator(range(100)))

#print(CACHE)
#################################################################################

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        self.func(*args, **kwargs)
        print(datetime.now() - start)
        #return res

@Timer
def iterator(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            even += [i]
        else:
            odd += [i]
    return odd, even

print(iterator(range(100000)))
