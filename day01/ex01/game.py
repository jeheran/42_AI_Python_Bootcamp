class GotCharacter:

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

        if not isinstance(first_name, str):
            raise TypeError("The first nme should be a string")


class Stark(GotCharacter):
    """A class representing the Stark family.""" 
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
