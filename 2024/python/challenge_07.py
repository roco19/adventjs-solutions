import unittest


# Challenge
def fix_packages(packages):
    main_stack = []

    current_str_stack = []
    for c in packages:
        if c == "(":
            main_stack.append(current_str_stack)
            current_str_stack = []
        elif c == ")":
            previous_str_stack = main_stack.pop()
            while current_str_stack:
                previous_str_stack.append(current_str_stack.pop())
            current_str_stack = previous_str_stack
        else:
            current_str_stack.append(c)

    return "".join(current_str_stack)


# Unit tests
class FixPackages(unittest.TestCase):
    def test1(self):
        self.assertEqual(fix_packages("a(cb)de"), "abcde")

    def test2(self):
        self.assertEqual(fix_packages("a(bc(def)g)h"), "agdefcbh")

    def test3(self):
        self.assertEqual(fix_packages("abc(def(gh)i)jk"), "abcighfedjk")

    def test4(self):
        self.assertEqual(fix_packages("a(b(c))e"), "acbe")


if __name__ == "__main__":
    unittest.main()
