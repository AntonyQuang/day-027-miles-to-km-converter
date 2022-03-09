def add(*args):
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    print(sum)

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


add(3, 5, 6, 2, 1)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)