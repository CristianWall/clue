from sympy.logic.boolalg import Or, Not
from sympy import symbols

def crear_base_conocimientos():
    kb = []

    jose, maria, juan = symbols('Jose Maria Juan')
    cocina, patio, sala = symbols('Cocina Patio Sala')
    pistola, veneno, martillo = symbols('Pistola Veneno Martillo')

    kb.append(Or(jose, maria, juan))
    kb.append(Or(cocina, patio, sala))
    kb.append(Or(pistola, veneno, martillo))

    kb.append(Not(cocina))
    kb.append(Not(pistola))

    kb.append(Or(juan,maria))
    kb.append(Not(martillo))

    kb.append(Not(maria))
    kb.append(Not(patio))

    return kb, [jose, maria, juan], [cocina, patio, sala], [pistola, veneno, martillo]
