import string

entrada = input("Introduce el texto: ")

sinpuntuacion = "".join([i for i in entrada if i not in string.punctuation])

minusculas = sinpuntuacion.lower()

palabras = minusculas.split()

diccionario = {}
for palabra in palabras:
    diccionario[palabra] = diccionario.get(palabra, 0) + 1

for palabra, frecuencia in diccionario.items():
    print(f"{palabra}: {frecuencia}")