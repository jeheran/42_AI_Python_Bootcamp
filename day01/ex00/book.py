import datetime
from recipe import Recipe


class Book:
    def __init__(self, name, recipes_list):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = recipes_list

        if not isinstance(name, str):
            raise TypeError("Name should be a string")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list.keys():
            for rcps in self.recipes_list[key]:
                if rcps.name == name:
                    print(str(rcps))
                    break

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for rcps in self.recipes_list[recipe_type]:
                print(str(rcps))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
