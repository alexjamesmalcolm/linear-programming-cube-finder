import unittest
from optimizer import StructureOptimizer, Material

class TestOptimizer(unittest.TestCase):
    def test_make_cube(self):
        materials = [Material(1), Material(1), Material(1)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(1, structure.volume())
    
    def test_make_rectangle(self):
        materials = [Material(1), Material(1), Material(2)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(2, structure.volume())

def main():
    unittest.main()

if __name__ == '__main__':
    main()