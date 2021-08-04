def ejemplo(**kwargs):
    print("ejecutando ejemplo")
    print(kwargs)


def ejemplo2(a1, a2, a3, a4, a5, a6, a7):
    print(a1 + a2 + a3 + a4 + a5 - a6 + a7)


# control + q
def elevar_numero(**kwargs) -> int:
    r"""
    eleva un numero
    :param kwargs: numero indica el numero a elevar, y exponente indica el exponente
    :return: regresa la operacion
    """
    if kwargs.get('exponente') is None: kwargs['exponente'] = 2
    print(kwargs['numero'] ** kwargs['exponente'])
    return kwargs['numero'] ** kwargs['exponente']


def elevar_numero2(numero=1, exponente=2):
    print(numero ** exponente)


dic = {"argumento1": "hola", "argumento2": "mundo"}

ejemplo(**dic)

ejemplo(argumento1="hola", argumento2="mundo")

elevar_numero(numero=10, exponente=2)

elevar_numero(numero=5, exponente=3)

elevar_numero(numero=5)

elevar_numero2(10)
