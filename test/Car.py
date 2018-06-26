import copy


class Car:
    pass


car = Car()
car.a = 1
print(car.a)
car2 = copy.copy(car)
car2.a = 2
print(car.a)
