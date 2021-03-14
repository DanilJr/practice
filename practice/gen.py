
def courutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


#@courutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:               # here we could use 'throw' method
            print('Loop is over!!!\n'*5)    # to raise Exception!!!!!!
        else:
            count += 1
            summ += x
            average = summ / count

#################################################################################
#################################################################################


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value

    def __iter__(self):
        return self

f = Fib()
for i in range(60):
    print(next(f))
