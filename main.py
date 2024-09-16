lista=[1,2,12,80,90,60,30,70,55,14,12]
vocales=["a","e","i","o","u","A","E","I","O","U"]

def promedio(lista):
 return sum(lista) / len(lista)

def contar_vocales(cadena):
 return print("a=", cadena.count("a"),"e=", cadena.count("e"), "i=", cadena.count("i"),"o=", cadena.count("o"),"u=", cadena.count("u"),"A=", cadena.count("A"),"E=", cadena.count("E"), "I=", cadena.count("I"),"O=", cadena.count("O"),"U=", cadena.count("U"))

 

#def contar_vocales(cadena,vocales):
 #return cadena.count(vocales)
 
numero=int(input("ingrese un número: "))

for a in range (10):
 print((a+1)*numero)

inicio=int(input("ingresa el número inicial: "))
final=int(input("ingresa el número final: "))

for b in range (inicio,final):
 if b%2==0:
  print(b)

print(promedio(lista))
cadena=str(input("ingresa un texto: "))
print(contar_vocales(cadena))



 