import unittest

# Challenge
def create_frame(names):
  max_length = max([len(name) for name in names])

  lines = []
  border = "*" * (max_length + 4)
  lines.append(border)
  for name in names:
    lines.append(f"* {name.ljust(max_length)} *")
  lines.append(border)
  return "\n".join(lines)

# Unit tests
class CreateFrame(unittest.TestCase):
  def test_1(self):
    names = ['midu', 'madeval', 'educalvolpz']
    expected = """\
***************
* midu        *
* madeval     *
* educalvolpz *
***************"""
    self.assertEqual(create_frame(names), expected)
  
  def test_2(self):
    gifts = ['midu']
    expected = """\
********
* midu *
********"""
    self.assertEqual(create_frame(gifts), expected)
  
  def test_3(self):
    gifts = ['a', 'bb', 'ccc']
    expected =  """\
*******
* a   *
* bb  *
* ccc *
*******"""
    self.assertEqual(create_frame(gifts), expected)

if __name__ == "__main__":
  unittest.main()
