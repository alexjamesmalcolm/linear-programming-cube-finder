from typing import List
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, LpContinuous, LpStatus, lpSum, value, permutation


def optimal_n_cube(lengths: List[int], n_of_dimensions: int):
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
            in lengths
            if material == int(material)
        )
        else LpContinuous
    )
    dimensions = [
        LpVariable(f"dimension_{i}", lowBound=0, upBound=None, cat=length_cat)
        for i
        in range(n_of_dimensions)
    ]
    material_and_dimension = LpVariable.dicts(
        "material_and_dimension",
        [(i, j) for i in range(len(lengths)) for j in range(n_of_dimensions)],
        lowBound=0,
        upBound=None,
        cat="Binary"
    )
    print("material_and_dimension")
    print(material_and_dimension)

    # Each material must be used once
    for material in range(len(lengths)):
        p += lpSum([material_and_dimension[material, dimension] for dimension in range(n_of_dimensions)]) == 1

    for dimension_index, dimension in enumerate(dimensions):
        p += dimension == lpSum([
            lengths[material] * material_and_dimension[material, dimension_index]
            for material
            in range(len(lengths))
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
    return [
        [
            lengths[material]
            for material
            in range(len(lengths))
            if material_and_dimension[material, dimension].varValue == 1
        ]
        for dimension
        in range(n_of_dimensions)
    ]
