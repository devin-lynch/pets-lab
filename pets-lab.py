class Pet():
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        
    def walk(self):
        print('Walka walka')

    def __str__(self):
        return f'{self.name} belongs to {self.owner}'

# devins_pet = Pet('Devin', 'Joby')

# print(devins_pet)
# devins_pet.walk()

class Dog(Pet):
    def __init__(self, owner, name, price):
        super().__init__(owner, name)
        self.price = 20

    def __str__(self):
        return f'pet {self.name} belongs to {self.owner} and costs ${self.price}'

    def bark(self):
        print('bark')

    def chase_tail(self):
        print('oh boy oh boy oh boy')

    def get_price(self, price):
        return {price}

devin_dog = Dog('Devin', 'Joby', 30)
print(devin_dog)