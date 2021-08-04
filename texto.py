import numpy as np
#        0123456789012345678901234567890
mensaje="maria tenia un corderito"  # str (es un listado)

print(mensaje[2])    # el caracter 2
print(mensaje[6:11]) # el caracter 6 hasta el caracter 11
print(mensaje[6:])   # del caracter 6 hasta el final
print(mensaje[:6])   # desde el comienzo hasta el 6
print(mensaje[:])   # todo
print(mensaje[-9:])  # los ultimos 9 caracteres
print(mensaje[:-9])  # desde el comienzo hasta -5 caracteres "maria tenia un cord"



#         0   ,   1       , 2
lista=["chile","argentina","peru"]

print(lista[1:])  # desde el elemento uno hasta el final

print("La posicion es ", mensaje.index("corderito"))

palabras =mensaje.split(" ") # listado => ndarray

cantidad=[]
for palabra in palabras:
    cantidad.append(len(palabra))


