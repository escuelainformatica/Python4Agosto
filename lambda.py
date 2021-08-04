# suma es una funcion lambda que tiene dos argumentos (a y b)
# , y devuelve la suma de ellos


# lambda se puede usar para programacion funcional.
# pero python no es muy bueno para eso.
# =>

suma_lambda = lambda a, b: a + b


def funcion_sumar(a, b):
    return a + b


print(suma_lambda(2, 3))
print(funcion_sumar(2, 3))

peso = int(input("ingrese el valor en peso"))
preguntar = input("quiere convertirlo en euro (e) o en dolar(d)?")
if preguntar == "e":
    convertir_divisa = lambda a: a / 850  # convertir peso en euro.
else:
    convertir_divisa = lambda a: a / 750  # convertir peso el dolar.

print(convertir_divisa(peso))
