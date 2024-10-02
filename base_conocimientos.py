from sympy.logic.boolalg import Or, Not
from sympy import symbols

def crear_base_conocimientos():
    kb = []

    jose, maria, juan = symbols(' Jose Maria Juan')
    comedor, cocina, biblioteca = symbols('Comedor Cocina Biblioteca')
    cuchillo, revolver, llave_inglesa = symbols('Cuchillo Revolver Llave_Inglesa')

    kb.append(Or(jose, maria, juan))
    kb.append(Or(comedor, cocina, biblioteca))
    kb.append(Or(cuchillo, revolver, llave_inglesa))

    kb.append(Not(cocina))
    kb.append(Not(revolver))

    kb.append(Not(juan))
    kb.append(Or(Not(biblioteca), Not(llave_inglesa)))

    kb.append(Not(maria))
    kb.append(Not(comedor))

    return kb, [jose, maria, juan], [comedor, cocina, biblioteca], [cuchillo, revolver, llave_inglesa]
 