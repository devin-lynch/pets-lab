class Pet():
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def __str__(self):
        return f'{self.name} belongs to {self.owner}'
        
    def walk(self):
        print('Walka walka')


devins_pet = Pet('Devin', 'Joby')

# print(devins_pet)
# devins_pet.walk()

# class Dog(Pet):
#     def __init__(self, owner, name, price):
#         super().__init__(owner, name)
#         price = 20

#     def __str__(self):
#         return f'pet {self.name} belongs to {self.owner} and costs ${self.price}'

#     def bark(self):
#         print('bark')

#     def chase_tail(self):
#         print('oh boy oh boy oh boy')

#     def get_price(self, price):
#         print(price)
#         return price

# devin_dog = Dog('Devin', 'Joby', 34)
# devin_dog.bark()
# devin_dog.chase_tail()
# devin_dog.get_price(10)
# print(devin_dog)

# class Cat(Pet):
#     def __init__(self, owner, name, price = 10):
#         super().__init__(owner, name)

#     def __str__(self):
#         return f'pet {self.name} belongs to {self.owner} and costs $'

#     def purr(self):
#         print('purrrrr')

#     def clean(self):
#         print('cleaning')

#     def get_price(self, price):
#         return price

#     def walk(self):
#         print('Walka walka')

# devins_cat = Cat('Devin', 'Guts', 30)

# # print(devins_cat)
# # devins_cat.purr()
# # devins_cat.clean()
# # # devins_cat.get_price()
# # devins_cat.walk()