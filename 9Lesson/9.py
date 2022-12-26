
# 1

class Car(object):

    def __init__(self, color:str, count_passenger_seat:int, is_baby_seat:bool, is_busy:bool):

        self.is_busy = False
        self.is_baby_seat = is_baby_seat
        self.color = color
        self.count_passenger_seat = count_passenger_seat

    def __str__(self)-> str:
        return f'Car {self.count_passenger_seat=} {self.is_baby_seat=} {self.is_busy=} {self.color=}'


# 2

class Taxi(object):

    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passenger: int, is_baby: bool) -> Car | None:
        if is_baby:
            cars = list(filter(lambda x: not x.is_busy and x.is_baby_seat, self.cars))
        else:
            cars = list(filter(lambda x: not x.is_busy, self.cars))
        for car in cars:
            if car.count_passenger_seat >= count_passenger:
                car.is_busy = True
                return car

# 3

class Category(object):
    categories = []
    # name = None

    @classmethod
    def add(cls, new_categories:str) -> int:
        cls.categories = new_categories
        for name in new_categories:
            if name not in new_categories:
                new_categories = new_categories.append(name)
            else:
                raise ValueError ('данная категория уже существует')
            return new_categories.index(name)

    # @classmethod
    # def get(cls):
    #     return
    #


# 4








