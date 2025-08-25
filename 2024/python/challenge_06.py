import unittest


# Challenge
def in_box(box):
    if len(box) < 3 or len(box[0]) < 3:
        return False

    if not all([c == "#" for c in box[0] + box[-1]]):
        return False

    for i in range(1, len(box) - 1):
        row = box[i]
        if row[0] != "#" or row[-1] != "#":
            return False

    for i in range(1, len(box) - 1):
        inner_row = box[i][1:-1]
        if "*" in inner_row:
            return True

    return False


# Unit tests
class TestInBox(unittest.TestCase):
    def test1(self):
        box = ["###", "#*#", "###"]
        expected = True
        self.assertEqual(in_box(box), expected)

    def test2(self):
        box = ["####", "#* #", "#  #", "####"]
        expected = True
        self.assertEqual(in_box(box), expected)

    def test3(self):
        box = ["#####", "#   #", "#  #*", "#####"]
        expected = False
        self.assertEqual(in_box(box), expected)

    def test4(self):
        box = ["#####", "#   #", "#   #", "#   #", "#####"]
        expected = False
        self.assertEqual(in_box(box), expected)


if __name__ == "__main__":
    unittest.main()
