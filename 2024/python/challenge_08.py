import unittest


# Challenge
def draw_race(indexes, length):
    lines = []
    num_lanes = len(indexes)
    for i, index in enumerate(indexes):
        line_start = " " * (num_lanes - i - 1)
        line_end = f" /{i + 1}"

        if index == 0:
            line_mid = "~" * length
        elif index > 0:
            line_mid = f"{'~' * index}r{'~' * (length - index - 1)}"
        else:
            line_mid = f"{'~' * (length + index)}r{'~' * (-index - 1)}"

        lines.append(f"{line_start}{line_mid}{line_end}")

    return "\n".join(lines)


# Unit tests
class DrawRace(unittest.TestCase):
    def test_1(self):
        expected = """\
  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3"""
        self.assertEqual(draw_race([0, 5, -3], 10), expected)

    def test_2(self):
        expected = """\
   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4"""
        self.assertEqual(draw_race([2, -1, 0, 5], 8), expected)

    def test_3(self):
        expected = """\
  ~~~r~~~~~~~~ /1
 ~~~~~~~r~~~~ /2
~~~~~~~~~~r~ /3"""
        self.assertEqual(draw_race([3, 7, -2], 12), expected)


if __name__ == "__main__":
    unittest.main()
