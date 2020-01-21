cookbook = {
    "sandwich": {
        "ingredients": [
            "ham",
            "bread",
            "cheese",
            "tomatoes"
        ],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": [
            "flour",
            "sugar",
            "eggs"
        ],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": [
            "avocado",
            "arugula",
            "tomatoes",
            "spinach"
        ],
        "meal": "lunch",
        "prep_time": 16
    }
}


def print_recipe(name=None):
    if name is None:
        print("Please enter the recipe's name to get its details:")
        name = input(">> ")
    print('-' * 10)
    print("Recipe for {}: ".format(name))
    print("Ingredients list: {}".format(cookbook[name]["ingredients"]))
    print("To be eaten for {}.".format(cookbook[name]["meal"]))
    print("Takes {} minutes of cooking.".format(cookbook[name]["prep_time"]))
    print('-' * 10)


def print_cookbook():
    for name in cookbook:
        print_recipe(name)


def add_to_dict():
    to_be_add = ''
    ingredients = []
    print("Enter the name of the receipe :")
    name = input("> ")
    while name in list(cookbook.keys()):
        print("This receipe already exist please give it another name :")
        name = input("> ")
    while to_be_add != "stop":
        print("Enter the ingredients one by one then enter \"stop\"")
        to_be_add = input(">> ")
        ingredients.append(to_be_add)
    print("Enter the type of meal")
    meal_type = input(">>> ")
    print("Enter the preparation time :")
    prep = input(">>>> ")

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal_type,
        "prep_time": prep
    }


def del_entry():
    print("Existing receipe : {}".format(list(cookbook.keys())))
    print("Enter the name of receipe you want to delete :")
    to_del = input(">> ")
    del cookbook[to_del]

n = 0
while n != '5':
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    n = input(">> ")

    if n == '1':
        add_to_dict()
    elif n == '2':
        del_entry()
    elif n == '3':
        print_recipe()
    elif n == '4':
        print_cookbook()
    else:
        print("This option does not exist.")
