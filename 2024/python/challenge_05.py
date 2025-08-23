import unittest
from collections import defaultdict

# Challenge
def organize_shoes(shoes):
  shoe_dict = {}
  for shoe in shoes:
    type = shoe["type"]
    size = shoe["size"]
    shoe_dict.setdefault(size, {})
    shoe_dict[size][type] = shoe_dict[size].get(type, 0) + 1

  pairs = []
  for size, type in shoe_dict.items():
    pair_count = min(type.get("I", 0), type.get("R", 0))
    pairs.extend([size] * pair_count)

  return pairs

def organize_shoes_2(shoes):
  shoe_dict = defaultdict(lambda: {"I": 0, "R": 0})
  for shoe in shoes:
    shoe_dict[shoe["size"]][shoe["type"]] += 1

  pairs = []
  for size, type in shoe_dict.items():
    pair_count = min(type["I"], type["R"])
    pairs.extend([size] * pair_count)

  return pairs

# Unit tests
class TestOrganizeShoes(unittest.TestCase):
  def test_1(self):
    shoes = [
      { "type": 'I', "size": 38 },
      { "type": 'R', "size": 38 },
      { "type": 'R', "size": 42 },
      { "type": 'I', "size": 41 },
      { "type": 'I', "size": 42 }
    ]
    expected = [38, 42]
    self.assertEqual(organize_shoes(shoes), expected)

  def test_2(self):
    shoes = [
      { "type": 'I', "size": 38 },
      { "type": 'R', "size": 38 },
      { "type": 'I', "size": 38 },
      { "type": 'I', "size": 38 },
      { "type": 'R', "size": 38 }
    ]
    expected = [38, 38]
    self.assertEqual(organize_shoes(shoes), expected)

  def test_3(self):
    shoes = [
      { "type": 'I', "size": 38 },
      { "type": 'R', "size": 36 },
      { "type": 'R', "size": 42 },
      { "type": 'I', "size": 41 },
      { "type": 'I', "size": 43 }
    ]
    expected = []
    self.assertEqual(organize_shoes(shoes), expected)

if __name__ == "__main__":
  unittest.main()
