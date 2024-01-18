from typing import List
from n_cube_optimizer import optimal_n_cube

class Structure:
    def __init__(self, x_materials: List[int], y_materials: List[int], z_materials: List[int]) -> None:
        self.x_materials = x_materials
        self.y_materials = y_materials
        self.z_materials = z_materials

    def x_length(self) -> int:
        return sum(m for m in self.x_materials)

    def y_length(self) -> int:
        return sum(m for m in self.y_materials)

    def z_length(self) -> int:
        return sum(m for m in self.z_materials)

    def volume(self) -> int:
        return self.x_length() * self.y_length() * self.z_length()

class StructureOptimizer:
    def __init__(self, materials: List[int]) -> None:
        self.materials = materials

    def largest_volume_structure(self) -> Structure:
        result = optimal_n_cube(lengths=[m for m in self.materials], n_of_dimensions=3)
        print(result)
        x_materials = [length for length in result[0]]
        y_materials = [length for length in result[1]]
        z_materials = [length for length in result[2]]

        return Structure(x_materials, y_materials, z_materials)
