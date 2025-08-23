import unittest

# Challenge
def prepare_gifts(gifts):
  return sorted(set(gifts))

# Unit tests
class TestPrepareGifts(unittest.TestCase):
  def test_1(self):
    gifts = [3, 1, 2, 3, 4, 2, 5]
    expected =  [1, 2, 3, 4, 5]
    self.assertEqual(prepare_gifts(gifts), expected)
  
  def test_2(self):
    gifts = [6, 5, 5, 5, 5]
    expected = [5, 6]
    self.assertEqual(prepare_gifts(gifts), expected)
  
  def test_3(self):
    gifts = []
    expected = []
    self.assertEqual(prepare_gifts(gifts), expected)

if __name__ == "__main__":
  unittest.main()
