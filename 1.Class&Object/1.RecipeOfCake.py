class RecipeOfcake:
    def __init__(self,flour,sugar,egg):
        self.flour = flour
        self.sugar = sugar
        self.egg = egg
    
    def mix(self):
        print("Mixing the ingredients together")
    def bake(self):
        print("Baking the cake in the oven")
    def decorate(self):
        print("Decorating the cake with frosting and toppings")


print("\nWelcome to the cake recipe!")
print("This recipe requires flour, sugar, and eggs.")

print("\nCake 1:")
my_cake = RecipeOfcake(2,1,3)
print("Flour:", my_cake.flour, "cups")
print("Sugar:", my_cake.sugar, "cups")
print("Eggs:", my_cake.egg)
my_cake.mix()
my_cake.bake()
my_cake.decorate()

print("\nCake 2:")
my_cake2 = RecipeOfcake(3,2,4)
print("Flour:", my_cake2.flour, "cups")
print("Sugar:", my_cake2.sugar, "cups")
print("Eggs:", my_cake2.egg)
my_cake2.mix()
my_cake2.bake()
my_cake2.decorate()

print("\nEnjoy your delicious cakes!\n")