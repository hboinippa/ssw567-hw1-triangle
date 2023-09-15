import unittest
def classify_triangle(a, b, c):
  """
  Classify a triangle by its side lengths.
  Args:
    a (float): The length of side a.
    b (float): The length of side b.
    c (float): The length of side c.
  Returns:
    str: The type of triangle.
  """
  # Check if the triangle is valid.
  if a <= 0 or b <= 0 or c <= 0:
    return "Invalid triangle"
  # Check if the triangle is equilateral.
  if a == b and b == c:
    return "Equilateral"
  if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    return "right angled triangle"
  # Check if the triangle is isosceles.
  if a == b or b == c or c == a:
    return "Isosceles"
  # Check if the triangle is scalene.
  if a != b and b != c and c != a:
    return "Scalene"
  # check if the triangle is right angled triangle.
class TestClassifyTriangle(unittest.TestCase):
  def test_equilateral(self):
    self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
  def test_isosceles(self):
    self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
  def test_scalene(self):
    self.assertEqual(classify_triangle(3, 4, 7), "Scalene")
  def test_invalid(self):
    self.assertEqual(classify_triangle(-1, 2, 3), "Invalid triangle")
  def test_invalid(self):
    self.assertEqual(classify_triangle(3,4,5), "right angled triangle")
if __name__ == "__main__":
  unittest.main()