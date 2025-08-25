import unittest


# Challenge
def organize_inventory(inventory: list):
    new_inventory = {}
    for gift in inventory:
        cat = gift["category"]
        name = gift["name"]
        qty = gift["quantity"]

        new_inventory.setdefault(cat, {})
        new_inventory[cat][name] = new_inventory[cat].get(name, 0) + qty

    return new_inventory


# Unit tests
class TestOrganizeInventory(unittest.TestCase):
    def test_1(self):
        inventory = [
            {"name": "doll", "quantity": 5, "category": "toys"},
            {"name": "car", "quantity": 3, "category": "toys"},
            {"name": "ball", "quantity": 2, "category": "sports"},
            {"name": "car", "quantity": 2, "category": "toys"},
            {"name": "racket", "quantity": 4, "category": "sports"},
        ]
        expected = {"toys": {"doll": 5, "car": 5}, "sports": {"ball": 2, "racket": 4}}
        self.assertEqual(organize_inventory(inventory), expected)

    def test_2(self):
        inventory = [
            {"name": "book", "quantity": 10, "category": "education"},
            {"name": "book", "quantity": 5, "category": "education"},
            {"name": "paint", "quantity": 3, "category": "art"},
        ]
        expected = {"education": {"book": 15}, "art": {"paint": 3}}
        self.assertEqual(organize_inventory(inventory), expected)


if __name__ == "__main__":
    unittest.main()
