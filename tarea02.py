#Tupla 
tupla = (4, "Hola", 7.15)
print(len(tupla))
#Teniendo en cuenta que una tupla no se puede modificar una vez ya este creada, podemos hacer que una tupla pueda ser una lista 
lista = list(tupla)
print(lista)
#la tupla no se esta modificando en ningun momento, simplemente la converti en lista para un ejemplo 

#Segundo ejercicio 
#Dada una lista de las edades de una población que ha ido a vacunarse,

vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
#elimino de la lista el numero 10
#muestro en pantalla la lista con un ciclo for

for vNumEdad in vEdades: 

    if vNumEdad == 10: vEdades.remove(10)
    else:
        print("edad", vNumEdad, "años")

Total = len(vEdades)
print("Total:", Total + 1)
print(vEdades)

  