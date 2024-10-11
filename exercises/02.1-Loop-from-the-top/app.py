my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

#esto también pasa el test
for i in range(len(my_sample_list) -1, -1, -1): #Funcionamiento de range: 3 argumentos:
 # Argumento 1 = inicio de la lista, con len(my_sample_list) - 1) le digo que empieze en la última posición
 #si no lo pongo len() me usa todos los valores de la lista!!!, si uso len() me dice la cantidad de argumentos.
 #Este primer argumento le digo que empiece en 14 -1, porque las listas se empiezan a contar desde cero, por tanto SIEMPRE le tengo que restar -1 para llamar al último
 #Segundo = por donde quiero que se detenga
 #Tercero = la cantidad de pasos (o cuántos valores debe sunar cada vez que se ejecute)
 #Comenzamos por 
 print(my_sample_list[i])


my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]


reversed_list = []
# Modify the loop below to print from end to start


for a in my_sample_list[::-1]: #Esta es la forma de escribir el último valor de la lista no importa cual sea
   #En detalle: En Python, [::-1] es una forma de usar "slicing" o corte en listas, cadenas y otros tipos de secuencias para invertir su orden.
#Descomposición de [::-1]
#El primer : indica que estamos trabajando con toda la secuencia, desde el inicio hasta el final.
#El segundo : establece el "paso" o la cantidad de elementos que saltamos cada vez.
#El -1 significa que queremos recorrer la secuencia al revés, es decir, desde el último elemento hacia el primero.
  reversed_list.insert(0,a)
  print(a)




#Codigo original:


my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]


# Modify the loop below to print from end to start


for i in range(0, len(my_sample_list)):
  print(my_sample_list[i])


