from MenuItem import MenuItem

class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem('latte', 200, 150, 24,2.5),
            MenuItem('espresso', 50, 0, 18,1.5),
            MenuItem('cappuccino', 250, 50, 24,3.0),
        ]

    def get_item(self):
        """Returns all the names of the available menu items"""
        options= ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")