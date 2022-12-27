
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

    # name=[]
    # index=[index]
    # index_name = [index,name]
    @classmethod
    def add(cls,new_category, name):
        cls.categories = new_category
        if name in new_category:
            raise ValueError('already exist')
        else:
            new_category.append(name)
            return new_category.index(name)

    @classmethod
    def get(cls,new_category,index):
        if index not in new_category:
            raise ValueError
        else:
            return new_category[index]

    @classmethod
    def delete(cls,new_category, index):
        new_category.pop(index)

    @classmethod
    def update(cls,new_category,index_name ):
        cls.categories = new_category
        if index_name not in new_category:
            new_category.insert(index_name)
        else:
            raise ValueError