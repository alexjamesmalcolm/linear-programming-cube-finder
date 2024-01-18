import unittest
from optimizer import StructureOptimizer, Material

class TestOptimizer(unittest.TestCase):
    def test_make_cube(self):
        materials = [Material(1), Material(1), Material(1)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(1, structure.volume())

    def test_make_2_volume_rectangle(self):
        materials = [Material(1), Material(1), Material(2)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(2, structure.volume())

    def test_make_4_volume_rectangle(self):
        materials = [Material(1), Material(2), Material(2)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(4, structure.volume())

    def test_make_64_volume_cube(self):
        materials = [Material(2), Material(2), Material(2), Material(2), Material(2), Material(2)]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(64, structure.volume())

    def test_big(self):
        lengths = [
            42,
            37,
            17,
            13,
            99,
            71,
            21,
            51,
            52,
            53,
            93,
            86,
            8,
            92,
            2,
            80,
            85,
            83,
            10,
            47,
            7,
            33,
            3,
            96,
            55,
            97,
            48,
            25,
            94,
            58,
            56,
            6,
            87,
            76,
            49,
            5,
            95,
            24,
            14,
            43,
            63,
            77,
            73,
            30,
            36,
            44,
            34,
            64,
            18,
            82,
            22,
            57,
            26,
            35,
            45,
            66,
            32,
            28,
            90,
            20,
            23,
            81,
            19,
            40,
            72,
            11,
            69,
            75,
            78,
            41,
            46,
            39,
            54,
            74,
            29,
            59,
            4,
            65,
            68,
            1,
            70,
            9,
            50,
            31,
            27,
            16,
            89,
            88,
            67,
            12,
            91,
            100,
            62,
            60,
            84,
            79,
            61,
            15,
            98,
            38,
        ]
        materials = [Material(length) for length in lengths]
        optimizer = StructureOptimizer(materials)
        structure = optimizer.largest_volume_structure()
        self.assertEqual(4769911476, structure.volume())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
