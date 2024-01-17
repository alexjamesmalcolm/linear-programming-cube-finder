from typing import List

class Material:
    def __init__(self, length: int) -> None:
        self.length = length

class Structure:
    def __init__(self, x_materials: List[Material], y_materials: List[Material], z_materials: List[Material]) -> None:
        self.x_materials = x_materials
        self.y_materials = y_materials
        self.z_materials = z_materials
    
    def volume(self) -> int:
        x = sum([m.length for m in self.x_materials])
        y = sum([m.length for m in self.y_materials])
        z = sum([m.length for m in self.z_materials])
        return x * y * z

class StructureOptimizer:
    def __init__(self, materials: List[Material]) -> None:
        self.materials = materials
    
    def largest_volume_structure(self) -> Structure:
        # TODO Perform a real optimization here using PuLP
        return Structure([self.materials[0]], [self.materials[1]], [self.materials[2]])