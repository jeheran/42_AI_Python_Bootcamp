class Recipe:

    VLD = ["starter", "lunch", "dessert"]

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        if not isinstance(name, str) or name == "":
            raise TypeError("The name should be a string")
        if not isinstance(cooking_lvl, int) or (1 > cooking_lvl > 5):
            raise TypeError("The Coocking_lvl should be an int in range(1, 5)")
        if not isinstance(cooking_time, int) or cooking_time <= 0:
            raise TypeError("The Coocking_time should be a positive int")
        if isinstance(ingredients, list):
            for ele in ingredients:
                if not isinstance(ele, str):
                    raise TypeError("The ingredients should be str")
        else:
            raise TypeError("The ingredients should be a list")
        if not isinstance(description, str):
            raise TypeError("The description should be a str")
        if not isinstance(recipe_type, str) or recipe_type not in Recipe.VLD:
            raise TypeError("Type should be a string in {}".format(Recipe.VLD))
        if recipe_type == "":
            raise TypeError("Receipe_Type can't by empty")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name: {}\n".format(self.name)
        txt += "cooking_lvl: {}\n".format(self.cooking_lvl)
        txt += "cooking_time: {}\n".format(self.cooking_time)
        txt += "ingredients: {}\n".format(self.ingredients)
        txt += "description: {}\n".format(self.description)
        txt += "recipe_type: {}".format(self.recipe_type)
        return txt
