import unittest

# Challenge
def create_xmas_tree(height, ornament):
  width = height * 2 - 1
  lines = []
  for i in range(height):
    ornaments = ornament * (i * 2 + 1)
    lines.append(ornaments.center(width, "_"))

  trunk = "#".center(width, "_")
  lines.append(trunk)
  lines.append(trunk)
  return "\n".join(lines)

# Unit tests
class TestCreateXmasTree(unittest.TestCase):
  def test1(self):
    height = 5
    ornament = "*"
    expected =  """\
____*____
___***___
__*****__
_*******_
*********
____#____
____#____"""

    result = create_xmas_tree(height, ornament)
    self.assertEqual(result, expected)

  def test2(self):
    height = 3
    ornament = "+"
    expected =  """\
__+__
_+++_
+++++
__#__
__#__"""

    result = create_xmas_tree(height, ornament)
    self.assertEqual(result, expected)

  def test3(self):
    height = 6
    ornament = "@"
    expected =  """\
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____"""

    result = create_xmas_tree(height, ornament)
    self.assertEqual(result, expected)

if __name__ == "__main__":
  unittest.main()
