class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей изменено на: {self.numberOfFloors}")


# Пример использования:
my_house = House()
print(f"Начальное количество этажей: {my_house.numberOfFloors}")

my_house.setNewNumberOfFloors(5)
