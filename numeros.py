entrada = input("Introduce los numeros del primer vector separados por comas: ")
vector1 = entrada.split(",")

entrada = input("Introduce los numeros del segundo vector separados por comas: ")
vector2 = entrada.split(",")

interseccion = set(set(vector1) & set(vector2))
print (f"Interseccion: {interseccion}")

union = set(vector1 + vector2)
print (f"Union: {union}")

diferencia = set(set(vector1) ^ set(vector2))
print (f"Diferencia simetrica: {diferencia}")
