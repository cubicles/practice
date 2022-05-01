def sum(a: int, b: int) -> int:
    return a + b

#output = sum(4, 5)
#print(output)
#print(type(output))

def typedtest(a: int) -> int:
    return a + "-ting"


typedtest("test")

class masterclass:
    def __init__(self, name: str):
        self.nombre = name

#pruebita = masterclass(4)
#print(pruebita.nombre)
#print(type(pruebita.nombre))

class listcomprehension:
    def __init__(self, lista: list):
        self.identidad = lista

listita = [1, 2, 3]
entero = 4

prueba_lista = listcomprehension(listita)
prueba_lista.identidad

prueba_lista2 = listcomprehension(entero)
prueba_lista2.identidad

print((prueba_lista.identidad))
print((prueba_lista2.identidad))

