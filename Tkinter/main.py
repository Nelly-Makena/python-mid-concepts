
#ARGS
def add(*args):
    sum =0
    for n in args:
        sum +=n
    return sum


print(add(5,67,8,9))

#KWARGS

def calculate(n, **kwargs):
    n +=kwargs["add"]
    n +=kwargs["multiply"]
    print(n)

calculate(2, add=5, multiply=9)




class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # Use get with a default value

my_car = Car(make="nissan")
print(my_car.make)  # Output: nissan
print(my_car.model)  # Output: Unknown Model


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="nissan", model="Altima")  # Provide the model argument
print(my_car.make)  # Output: nissan
print(my_car.model)  # Output: Altima
