class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "patty"]
        return Burger(ingredients)
    def createDoubleCheeseBurger(self):
        ingredients = ["bun", "cheese", "cheese", "patty"]
        return Burger(ingredients)
    def createBunlessCheeseBurger(self):
        ingredients = ["cheese", "patty"]
        return Burger(ingredients)
