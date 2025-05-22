def division(lista):

  listapositiva = []
  listanegativa = []

  for x in lista:
    if x < 0:
      listanegativa.append(x)
    else:
      listapositiva.append(x)
      
  listapositiva.sort()
  listanegativa.sort()
  
  return listanegativa, listapositiva


lista = [1, 5, 7, 9, 3, -4, -6, -1]
print(division(lista))