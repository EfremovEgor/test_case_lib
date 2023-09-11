import unittest
import shapes
from math import pi


class TestShapes(unittest.TestCase):
    def test_circle_init(self):
        with self.assertRaises(ValueError):
            shapes.Circle(-1)

        with self.assertRaises(TypeError):
            shapes.Circle("1")
        self.assertTrue(shapes.Circle(1))

    def test_circle_area(self):
        self.assertAlmostEqual(shapes.Circle(2).area(), pi * 2**2, 7)

    def test_triangle_init(self):
        with self.assertRaises(ValueError):
            shapes.Triangle(1, 2, -3)
            shapes.Triangle(-1, 2, -3)
            shapes.Triangle(1, -2, -3)
            shapes.Triangle(1, 2, 4)

        with self.assertRaises(TypeError):
            shapes.Triangle([], "1", "1")
            shapes.Triangle(1, 2, "1")

        self.assertTrue(shapes.Triangle(1, 3, 4))

    def test_triangle_area(self):
        self.assertAlmostEqual(shapes.Triangle(1, 2, 2).area(), 0.968246, 6)

    def test_multiple_shapes_area(self):
        with self.assertRaises(TypeError):
            shapes.multiple_shapes_area([[], "1", "1"])
            shapes.multiple_shapes_area([1, 2, "1"])

        results = shapes.multiple_shapes_area(
            [shapes.Circle(2), shapes.Triangle(1, 2, 2)]
        )
        targets = [pi * 2**2, 0.968246]
        for result, target in zip(results, targets):
            self.assertAlmostEqual(result, target, 6)

        self.assertEqual(shapes.multiple_shapes_area([]), [])


if __name__ == "__main__":
    unittest.main()
