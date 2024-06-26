class House:
    def __init__(self, numberOfFloors=0):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        setattr(House, 'numberOfFloors', floors)
        print(self.numberOfFloors)

h1 = House
h1.setNewNumberOfFloors(h1, 5)
