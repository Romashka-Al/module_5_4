class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, numb):
        self.name = name
        self.numbers_of_floors = numb


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        return


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.numbers_of_floors}"


    def __eq__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors == other
        return self.numbers_of_floors == other.numbers_of_floors


    def __lt__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors < other
        return self.numbers_of_floors < other.numbers_of_floors


    def __le__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors <= other
        return self.numbers_of_floors <= other.numbers_of_floors


    def __gt__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors > other
        return self.numbers_of_floors > other.numbers_of_floors


    def __ge__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors >= other
        return self.numbers_of_floors >= other.numbers_of_floors


    def __ne__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors != other
        return self.numbers_of_floors != other.numbers_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


house1 = House("ЖК Новая Жизнь", 20)
print(House.houses_history)
house2 = House("ЖК Берёзки", 17)
print(House.houses_history)
house3 = House("ЖК Горы", 30)
print(House.houses_history)

del house2
del house3

print(House.houses_history)