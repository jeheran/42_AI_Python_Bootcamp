from book import Book
from recipe import Recipe
import datetime

#tourte = Recipe("jean", 5, 10, ["sel"], "", "lunch")
#to_print = str(tourte)
#print(to_print)

a = Book("Livrederecettes", {"starter": [
    Recipe("cereal", 5, 10, ["sel"], "", "starter"),
    Recipe("jean", 5, 10, ["sel"], "", "starter")],
    "lunch": [
    Recipe("tom", 5, 10, ["sel"], "", "lunch")],
    "dessert": [
    Recipe("timmy", 5, 10, ["sel"], "", "dessert")],
})

#a.get_recipe_by_name("timmy")
a.add_recipe(Recipe("sammy", 5, 10, ["sel"], "", "dessert"))

a.get_recipes_by_types("dessert")
