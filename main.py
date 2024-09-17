lista=[1,2,12,80,90,60,30,70,55,14,12]
vocales=["a","e","i","o","u","A","E","I","O","U"]
ventas=[100,400,20,30,60,70,150,90,60,45,44,30,11,12,320,40,15,20]
playing=True
mayor=0
menor=0
contador_ventas=0
ordenes = [
    {"cliente": "Juan", "productos": ["manzana", "pera"], "total": 15.50},
    {"cliente": "María", "productos": ["plátano", "manzana", "pera"], "total": 20.75},
    {"cliente": "Pedro", "productos": ["naranja"], "total": 5.00}
]


notas={
  "Juan": "5.0",
  "Pedro": "4.5",
  "Luis": "3.0",
  "Maria": "2.0",
  "Sofia": "1.0",
  "Jose": "1.5",
  "Lucia": "2.0",
  "Carlos": "3.5",
  "Marta": "2.0",
  "Miguel": "1.8",
  "Laura": "3.0"}

def promedio(lista):
 return sum(lista) / len(lista)

def contar_vocales(cadena):
  contador=0
  for i in cadena:
   if i in vocales:
    contador+=1
  return contador

while playing:
  print("oprime 1 para tablas de multiplicar")
  print("oprime 2 para números pares en un rango")
  print("oprime 3 para promedio de una lista")
  print("oprime 4 para contar  vocales en un texto")
  print("oprime 5 para opciones de dicionario")
  print("oprime 6 para análisis de ventas")
  print("oprime 7 para orden de compras")
  print("oprime 8 para salir")

  opcion = int(input("ingrese la opcion que desea realizar: "))
  if opcion == 1:
   numero=int(input("ingrese un número: "))
   for a in range (10):
    print((a+1)*numero)
  elif  opcion == 2:
   inicio=int(input("ingresa el número inicial: "))
   final=int(input("ingresa el número final: "))
   for b in range (inicio,final):
    if b%2==0:
     print(b)
  elif  opcion == 3:
   print(promedio(lista))
  elif  opcion == 4:
   cadena=str(input("ingresa un texto: "))
   print(contar_vocales(cadena))
  elif  opcion == 5:
    print("oprime 1 para mostrar la lista")
    print("oprime 2 para agregar un nuevo usuario")
    print("oprime 3 para eliminar un estudiante")
   
    opcion2 = int(input("ingrese la opcion que desea realizar: "))
    if opcion2 == 1:
     print(notas)
    elif  opcion2 == 2:
     nombre = input("ingrese el nombre del estudiante: ")
     nota = input("ingrese la nota del estudiante: ")
     if notas.get(nombre)== nombre:
            print("estudiante ya existente")
     else:
      notas[nombre]=nota
    elif opcion2 == 3:
      nombre2 = input("ingrese el nombre del estudiante: ")
      if notas.get(nombre2)== "none":
            print("usuario no encontrado")
      else:
       notas.pop(nombre2)
  elif  opcion == 6:
      print("la suma de las ventas es: ",sum(ventas))
      for d in  ventas:
        if  d>mayor:
          mayor=d
      print ("el precio más alto es: ",mayor)
      for e in  ventas:
        if  e<menor:
          menor=e
      print("el precio más bajo es: ",menor)
      for  f in  ventas:
        if f>= 100:
          contador_ventas+=1
      print(contador_ventas)
  elif opcion == 7:
    print(ordenes.items())











  elif opcion == 8:
     break
