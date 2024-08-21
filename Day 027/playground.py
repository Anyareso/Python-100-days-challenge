# def add(*args):
#     som = 0
#     for n in args:
#         som += n
#     return som
#
#
# print(add(3, 5, 6))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
