from typing import List
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, LpContinuous, LpStatus, lpSum, value, permutation

class Material:
    def __init__(self, length: int) -> None:
        self.length = length

class Structure:
    def __init__(self, x_materials: List[Material], y_materials: List[Material], z_materials: List[Material]) -> None:
        self.x_materials = x_materials
        self.y_materials = y_materials
        self.z_materials = z_materials

    def x_length(self) -> int:
        return sum(m.length for m in self.x_materials)

    def y_length(self) -> int:
        return sum(m.length for m in self.y_materials)

    def z_length(self) -> int:
        return sum(m.length for m in self.z_materials)

    def volume(self) -> int:
        return self.x_length() * self.y_length() * self.z_length()

class StructureOptimizer:
    def __init__(self, materials: List[Material]) -> None:
        self.materials = materials

    def largest_volume_structure(self) -> Structure:
        # Declare the problem
        p = LpProblem("Structure", LpMinimize)
        # Objective: Minimize the slack variable
        slack = LpVariable("slack", lowBound=0, upBound=None)
        p += slack

        length_cat = (
            LpInteger
            if any(
                material
                for material
                in self.materials
                if material.length == int(material.length)
            )
            else LpContinuous
        )
        n_of_dimensions = 3
        dimensions = [
            LpVariable(f"dimension_{i}", lowBound=0, upBound=None, cat=length_cat)
            for i
            in range(n_of_dimensions)
        ]
        material_and_dimension = LpVariable.dicts(
            "material_and_dimension",
            [(i, j) for i in range(len(self.materials)) for j in range(3)],
            lowBound=0,
            upBound=None,
            cat="Binary"
        )
        print("material_and_dimension")
        print(material_and_dimension)

        # Each material must be used once
        for material in range(len(self.materials)):
            p += lpSum([material_and_dimension[material, dimension] for dimension in range(3)]) == 1

        for dimension_index, dimension in enumerate(dimensions):
            p += dimension == lpSum([
                self.materials[material].length * material_and_dimension[material, dimension_index]
                for material
                in range(len(self.materials))
            ])

        # Constrain the differences to be less than or equal to the slack variable
        for a, b in permutation(range(n_of_dimensions), 2):
            p += dimensions[a] - dimensions[b] <= slack

        # Solve the problem
        p.solve()

        status = LpStatus[p.status]
        print(f"Status: {status}")
        if status == "Optimal":
            print(f"Objective: {value(p.objective)}")
            print("Solution:")
            for v in p.variables():
                print(f"{v.name} = {v.varValue}")
        x_materials = [
            self.materials[material]
            for material
            in range(len(self.materials))
            if material_and_dimension[material, 0].varValue == 1
        ]
        y_materials = [
            self.materials[material]
            for material
            in range(len(self.materials))
            if material_and_dimension[material, 1].varValue == 1
        ]
        z_materials = [
            self.materials[material]
            for material
            in range(len(self.materials))
            if material_and_dimension[material, 2].varValue == 1
        ]
        return Structure(x_materials, y_materials, z_materials)
